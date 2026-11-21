"""Local Markdown editor for the mdBook preview on port 8765."""

import argparse
import difflib
import hashlib
import html
import io
import json
import os
import re
import subprocess
import tempfile
import textwrap
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src"
PREVIEW = "http://127.0.0.1:8765"
EDITOR = "http://127.0.0.1:8766"


def book_chapters():
    summary = (SOURCE / "SUMMARY.md").read_text()
    return {path: title for title, path in re.findall(r"\[([^]\n]+)\]\(([^)]+\.md)\)", summary)}


def changed_chapters(head):
    tracked = subprocess.check_output(
        ["git", "diff", "--no-renames", "--name-only", "-z", head, "--", "src"], cwd=ROOT
    )
    untracked = subprocess.check_output(
        ["git", "ls-files", "--others", "--exclude-standard", "-z", "--", "src"], cwd=ROOT
    )
    changed = set(os.fsdecode(tracked + untracked).split("\0"))
    return [
        {"path": path, "title": title}
        for path, title in book_chapters().items()
        if f"src/{path}" in changed and (SOURCE / path).is_file()
    ]


def chapter_path(query):
    name = parse_qs(query).get("chapter", [""])[0]
    if name not in book_chapters():
        return None
    path = (SOURCE / name).resolve()
    return path if SOURCE in path.parents and path.is_file() else None


def revision(data):
    return hashlib.sha256(data).hexdigest()


def review_changes(before, data):
    old = before.decode().splitlines()
    new = data.decode().splitlines()
    try:
        from markdown import markdown
    except ImportError:
        markdown = None

    def render(excerpt):
        if not excerpt.strip():
            return ""
        if markdown is None:
            return "<pre>" + html.escape(excerpt) + "</pre>"
        return markdown(textwrap.dedent(excerpt), extensions=["extra", "sane_lists"])

    parts = []
    for kind, i, j, k, l in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
        if kind == "equal":
            continue
        left, right = "\n".join(old[i:j]), "\n".join(new[k:l])
        if left.strip() or right.strip():
            parts.append({"before": render(left), "after": render(right)})
    return parts


class Editor(BaseHTTPRequestHandler):
    def respond(self, status, body, media="text/plain"):
        self.send_response(status)
        self.send_header("Content-Type", media + "; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", PREVIEW)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def review(self, path, query):
        try:
            head = subprocess.check_output(
                ["git", "rev-parse", "--verify", "HEAD"], cwd=ROOT, text=True
            ).strip()
            pages = changed_chapters(head)
            current = path.relative_to(SOURCE).as_posix()
            contents = {}
            for page in pages:
                chapter = (SOURCE / page["path"]).resolve()
                if SOURCE not in chapter.parents:
                    return self.respond(403, b"Unexpected chapter path")
                contents[page["path"]] = chapter.read_bytes()
            fingerprints = {name: revision(data) for name, data in contents.items()}
            tag = revision(json.dumps([head, pages, fingerprints]).encode())
            if parse_qs(query).get("seen") == [tag]:
                return self.respond(204, b"")
            for page in pages:
                name = "src/" + page["path"]
                tracked = subprocess.check_output(["git", "ls-tree", head, "--", name], cwd=ROOT)
                before = subprocess.check_output(["git", "show", f"{head}:{name}"], cwd=ROOT) if tracked else b""
                page["changes"] = review_changes(before, contents[page["path"]])
        except (OSError, subprocess.CalledProcessError):
            return self.respond(503, b"Review needs a readable Git commit and chapters.")

        changes = next((p["changes"] for p in pages if p["path"] == current), [])
        body = {"baseline": head[:8], "tag": tag, "changes": changes, "pages": pages}
        self.respond(200, json.dumps(body).encode(), "application/json")

    def do_GET(self):
        if self.headers.get("Host") != urlsplit(EDITOR).netloc:
            return self.respond(403, b"Unexpected host")
        route = urlsplit(self.path)
        if route.path == "/status":
            return self.respond(200, b"ready")
        path = chapter_path(route.query)
        if path is None:
            return self.respond(404, b"Unknown chapter")
        if route.path == "/review":
            return self.review(path, route.query)
        if route.path == "/built":
            page = ROOT / "book" / path.relative_to(SOURCE).with_suffix(".html")
            ready = page.exists() and page.stat().st_mtime_ns >= path.stat().st_mtime_ns
            return self.respond(200, b"ready" if ready else b"building")
        if route.path == "/edit":
            return self.respond(200, Path(__file__).with_name("editor.html").read_bytes(), "text/html")
        if route.path == "/source":
            data = path.read_bytes()
            body = {"text": data.decode(), "revision": revision(data)}
            return self.respond(200, json.dumps(body).encode(), "application/json")
        self.respond(404, b"Unknown route")

    def save_photo(self, path, query):
        try:
            from PIL import Image
        except ImportError:
            return self.respond(503, b"Install Pillow in the editor's Python environment to add photos.")
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 < size <= 32 * 1024 * 1024:
                return self.respond(413, b"Choose a photo smaller than 32 MB.")
            data = self.rfile.read(size)
            with Image.open(io.BytesIO(data)) as image:
                ext = {"JPEG": "jpg", "PNG": "png", "WEBP": "webp"}[image.format]
                image.verify()
        except (OSError, KeyError, ValueError, SyntaxError, Image.DecompressionBombError):
            return self.respond(400, b"Choose a JPEG, PNG or WebP image.")
        folder = (path.parent / "img").resolve()
        if folder.parent != path.parent:
            return self.respond(403, b"Unexpected image directory")
        folder.mkdir(exist_ok=True)
        name = Path(parse_qs(query).get("name", ["photo"])[0]).stem
        stem = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:64] or "photo"
        target = folder / f"{stem}-{revision(data)[:12]}.{ext}"
        if not target.exists():
            with tempfile.NamedTemporaryFile(dir=folder, delete=False) as tmp:
                tmp.write(data)
            os.replace(tmp.name, target)
        self.respond(200, ("img/" + target.name).encode())

    def do_POST(self):
        route = urlsplit(self.path)
        if self.headers.get("Host") != urlsplit(EDITOR).netloc or self.headers.get("Origin") not in (EDITOR, PREVIEW):
            return self.respond(403, b"Unexpected origin")
        path = chapter_path(route.query)
        if route.path == "/photo" and path is not None:
            return self.save_photo(path, route.query)
        if route.path != "/source" or path is None:
            return self.respond(404, b"Unknown chapter")
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 4_000_000:
                return self.respond(413, b"Invalid chapter size")
            body = json.loads(self.rfile.read(length))
            data = body["text"].encode()
            if body["revision"] != revision(path.read_bytes()):
                return self.respond(409, b"File changed on disk. Copy your edits before reloading.")
        except (ValueError, KeyError, TypeError, AttributeError):
            return self.respond(400, b"Invalid edit")
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as temp:
            temp.write(data)
        try:
            os.chmod(temp.name, path.stat().st_mode)
            os.replace(temp.name, path)
        finally:
            Path(temp.name).unlink(missing_ok=True)
        self.respond(200, revision(data).encode())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--serve", action="store_true", help="also start the live mdBook preview")
    args = parser.parse_args()
    with HTTPServer(("127.0.0.1", 8766), Editor) as server:
        if args.serve:
            with subprocess.Popen(
                ["mdbook", "serve", "--hostname", "127.0.0.1", "--port", "8765"], cwd=ROOT
            ) as preview:
                try:
                    server.timeout = 0.5
                    while preview.poll() is None:
                        server.handle_request()
                except KeyboardInterrupt:
                    pass
                finally:
                    if preview.poll() is None:
                        preview.terminate()
                raise SystemExit(preview.wait() if preview.returncode is not None else 0)
        else:
            server.serve_forever()
