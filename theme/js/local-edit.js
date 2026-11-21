// This toolbar is active only in the local, writable mdBook preview.
(async () => {
    if (location.origin !== "http://127.0.0.1:8765") return;
    const address = new URL(location.href);
    if (address.searchParams.has("editRevision")) {
        address.searchParams.delete("editRevision");
        history.replaceState(history.state, "", address);
    }
    const remote = document.querySelector('a[rel="edit"]');
    if (!remote) return;
    const source = new URL(remote.href).pathname.split("/src/")[1];
    if (!source) return;
    const editor = "http://127.0.0.1:8766";
    const query = new URLSearchParams({chapter: decodeURIComponent(source)});
    const endpoint = editor + "/source?" + query;
    try {
        if (!(await fetch(editor + "/status")).ok) return;
    } catch {
        return;
    }

    const toolbar = document.createElement("span");
    toolbar.className = "local-edit-toolbar";
    const edit = document.createElement("button");
    edit.textContent = "Edit page";
    const markdown = document.createElement("a");
    markdown.textContent = "Markdown";
    markdown.href = editor + "/edit?" + query;
    const status = document.createElement("span");
    status.setAttribute("role", "status");
    toolbar.append(status, edit, markdown);
    remote.before(toolbar);

    // Render chapter excerpts without adding active HTML or new editing targets.
    function reviewExcerpt(markup, chapterURL) {
        const cell = document.createElement("div");
        cell.className = "review-excerpt";
        if (!markup) {
            cell.textContent = "—";
            return cell;
        }
        const template = document.createElement("template");
        template.innerHTML = markup;
        const allowed = new Set("p strong em code pre ol ul li blockquote br h1 h2 h3 h4 h5 h6 table thead tbody tr th td img del s details summary".split(" "));
        function append(parent, node) {
            if (node.nodeType === Node.TEXT_NODE) {
                parent.append(node.textContent);
                return;
            }
            if (node.nodeType !== Node.ELEMENT_NODE || ["SCRIPT", "STYLE"].includes(node.tagName)) return;
            const tag = node.localName;
            const target = allowed.has(tag) ? document.createElement(tag) : parent;
            if (tag === "img") {
                const src = node.getAttribute("src");
                if (!src) return;
                let url;
                try { url = new URL(src, chapterURL); } catch { return; }
                if (url.origin !== location.origin) {
                    parent.append(node.getAttribute("alt") || "Image");
                    return;
                }
                target.src = url.href;
                target.alt = node.getAttribute("alt") || "";
                target.loading = "lazy";
            }
            if (tag === "ol" && node.hasAttribute("start")) target.start = node.start;
            if (target !== parent) parent.append(target);
            for (const child of node.childNodes) append(target, child);
        }
        for (const node of template.content.childNodes) append(cell, node);
        return cell;
    }

    const reviewButton = document.createElement("button");
    reviewButton.hidden = true;
    toolbar.insertBefore(reviewButton, markdown);
    const review = document.createElement("details");
    review.id = "local-chapter-changes";
    review.className = "local-chapter-review";
    review.hidden = true;
    let showAll = address.hash === "#book-changes" || address.hash.startsWith("#review-page-");
    let reviewData;
    const preference = "chapter-review-collapsed:" + source;
    review.open = showAll || address.hash === "#" + review.id || sessionStorage.getItem(preference) !== "yes";
    const summary = document.createElement("summary");
    const comparison = document.createElement("div");
    comparison.className = "review-body";
    const pages = document.createElement("nav");
    pages.className = "review-pages";
    pages.setAttribute("aria-label", "Changed pages");
    review.append(summary, pages, comparison);
    document.querySelector("main").before(review);
    review.addEventListener("toggle", () => {
        sessionStorage.setItem(preference, review.open ? "no" : "yes");
    });
    reviewButton.addEventListener("click", () => {
        showAll = true;
        history.replaceState(history.state, "", "#book-changes");
        if (reviewData) drawReview(reviewData);
        review.hidden = false;
        review.open = true;
        review.scrollIntoView({block: "start"});
        summary.focus({preventScroll: true});
    });

    function drawReview(data) {
        const sections = document.createDocumentFragment();
        const links = document.createDocumentFragment();
        let hasCurrent = false;
        for (const page of data.pages) {
            const current = page.path === query.get("chapter");
            if (current) hasCurrent = true;
            if (!showAll && !current) continue;
            const section = document.createElement("section");
            section.id = "review-page-" + page.path;
            const chapterURL = new URL("/" + page.path.split("/").map(encodeURIComponent).join("/").replace(/\.md$/, ".html"), location.origin);
            if (showAll) {
                const heading = document.createElement("h2");
                heading.textContent = page.title;
                section.append(heading);
                const jump = document.createElement("a");
                jump.href = "#" + encodeURIComponent(section.id);
                jump.textContent = page.title;
                links.append(jump);
            }
            const grid = document.createElement("div");
            grid.className = "review-comparison";
            for (const label of ["Before", "After"]) {
                const header = document.createElement("strong");
                header.className = "review-column-heading";
                header.textContent = label;
                grid.append(header);
            }
            for (const change of page.changes) {
                grid.append(reviewExcerpt(change.before, chapterURL), reviewExcerpt(change.after, chapterURL));
            }
            if (page.changes.length) section.append(grid);
            else section.append("Only whitespace changed.");
            sections.append(section);
        }
        comparison.replaceChildren(sections);
        pages.replaceChildren(links);
        review.classList.toggle("all-page-changes", showAll);
        const total = data.pages.length;
        summary.textContent = total + (total === 1 ? " changed page" : " changed pages") + " since " + data.baseline;
        reviewButton.textContent = "Changes (" + total + ")";
        reviewButton.hidden = !total;
        review.hidden = !total || (!showAll && !hasCurrent);
    }

    let seen = "", checking = false;
    async function refreshReview() {
        if (checking || document.hidden) return;
        checking = true;
        try {
            const params = new URLSearchParams(query);
            if (seen) params.set("seen", seen);
            const response = await fetch(editor + "/review?" + params);
            if (response.status === 204) return;
            if (!response.ok) throw new Error("Review unavailable");
            const data = await response.json();
            const firstLoad = !reviewData;
            reviewData = data;
            drawReview(data);
            if (firstLoad && showAll) {
                const destination = location.hash.startsWith("#review-page-")
                    ? [...comparison.children].find(section => "#" + encodeURIComponent(section.id) === location.hash)
                    : review;
                destination?.scrollIntoView({block: "start"});
            }
            seen = data.tag;
        } catch {
            // Keep a failed refresh distinct from a successfully loaded comparison.
            seen = "";
            reviewData = null;
            reviewButton.hidden = false;
            reviewButton.textContent = "Changes";
            summary.textContent = "Changes unavailable. Check the local editor server.";
            review.hidden = false;
            pages.replaceChildren();
            comparison.replaceChildren();
        } finally {
            checking = false;
        }
    }
    refreshReview();
    document.addEventListener("visibilitychange", refreshReview);
    window.setInterval(refreshReview, 5000);

    // Match complete source lines, including inline markup. Leave unfamiliar
    // constructs in the Markdown editor so an edit cannot rewrite nearby HTML.
    function inlineMarkdown(node) {
        if (node.nodeType === Node.TEXT_NODE) return node.data;
        if (node.nodeType !== Node.ELEMENT_NODE) return "";
        const children = [...node.childNodes].map(inlineMarkdown).join("");
        if (node.hasAttribute("data-after-code")) return children.replace(/^\u200b/, "");
        switch (node.tagName) {
            case "CODE": {
                if (!children) return "";
                const runs = children.match(/`+/g) || [];
                const fence = "`".repeat(1 + Math.max(0, ...runs.map(run => run.length)));
                const pad = /^[` ]|[` ]$/.test(children) && children.trim() ? " " : "";
                return fence + pad + children + pad + fence;
            }
            case "EM": return "*" + children + "*";
            case "STRONG": return "**" + children + "**";
            case "A": {
                if (node.classList.contains("header")) return children;
                let href = node.getAttribute("href");
                if (!/^\w+:/.test(href)) href = href.replace(/\.html(?=#|$)/, ".md");
                return "[" + children + "](" + href + ")";
            }
            default: return children;
        }
    }

    // Apply a single-backtick code span at the caret using the browser's
    // editing command so the replacement participates in native undo.
    function formatCodeAtCaret(field) {
        const selection = window.getSelection();
        const node = selection.anchorNode;
        if (!selection.isCollapsed || node?.nodeType !== Node.TEXT_NODE ||
            !field.contains(node) || node.parentElement.closest("code")) return;
        const end = selection.anchorOffset;
        const prefix = node.data.slice(0, end);
        const match = /(?<![\\`])`([^`\n]+)`$/.exec(prefix);
        if (!match || node.data[end] === "`") return;

        const range = document.createRange();
        range.setStart(node, match.index);
        range.setEnd(node, end);
        selection.removeAllRanges();
        selection.addRange(range);
        const code = document.createElement("code");
        code.className = "hljs";
        code.textContent = match[1];
        // A separate text run keeps WebKit/Chromium from moving the caret
        // back inside the code span when ordinary typing resumes.
        const tail = document.createElement("span");
        tail.dataset.afterCode = "new";
        tail.textContent = "\u200b";
        document.execCommand("insertHTML", false, code.outerHTML + tail.outerHTML);
        const inserted = field.querySelector('[data-after-code="new"]');
        if (inserted) {
            inserted.dataset.afterCode = "";
            selection.collapse(inserted.firstChild, 1);
        }
    }

    function toggleSelectedCode(field, event) {
        const selection = window.getSelection();
        if (selection.isCollapsed || !selection.rangeCount) return;
        const range = selection.getRangeAt(0);
        if (!field.contains(range.commonAncestorContainer)) return;
        const word = range.toString();
        if (!word.trim() || /[`\n]/.test(word)) return;

        // Expand a selection inside a code label to the whole label. This
        // also handles double-clicks that select only one word of a label.
        const codes = [...field.querySelectorAll("code")].filter(code => range.intersectsNode(code));
        const code = codes.length === 1 ? codes[0] : null;
        const unwrap = code && (code.contains(range.commonAncestorContainer) || code.textContent === word);
        if (!unwrap && (codes.length || range.cloneContents().querySelector("*"))) return;

        event.preventDefault();
        if (unwrap) {
            range.selectNode(code);
            selection.removeAllRanges();
            selection.addRange(range);
        }
        const replacement = document.createElement(unwrap ? "span" : "code");
        if (!unwrap) replacement.className = "hljs";
        replacement.dataset.selectedWord = "";
        replacement.textContent = unwrap ? code.textContent : word;
        document.execCommand("insertHTML", false, replacement.outerHTML);
        const inserted = field.querySelector("[data-selected-word]");
        if (inserted) {
            delete inserted.dataset.selectedWord;
            range.selectNodeContents(inserted);
            selection.removeAllRanges();
            selection.addRange(range);
        }
    }

    function findFields(text) {
        const candidates = new Map();
        function add(start, value, kind) {
            if (!value) return;
            const key = kind + "\n" + value;
            // An ambiguous source location must never receive a write.
            candidates.set(key, candidates.has(key) ? null : start);
        }
        let offset = 0;
        let fence = "";
        for (const raw of text.split("\n")) {
            const line = raw.trimEnd();
            const marker = line.match(/^\s*(`{3,}|~{3,})/);
            if (marker && (!fence || marker[1].startsWith(fence))) {
                fence = fence ? "" : marker[1];
            } else if (!fence && line.trimStart().startsWith("|")) {
                const cells = [...line.matchAll(/\|([^|]*)/g)];
                cells.forEach((cell, column) => {
                    const value = cell[1].trim();
                    const row = line.trim().replace(/^\||\|$/g, "").split("|").map(s => s.trim()).join("\t");
                    add(offset + cell.index + 1 + cell[1].indexOf(value), value, row + ":" + column);
                });
            } else if (!fence) {
                const prefix = line.match(/^\s*(?:>\s*)*(?:(?:#{1,6}|\d+\.|[-+*])\s+)?/)[0];
                add(offset + prefix.length, line.slice(prefix.length), "block");
            }
            offset += raw.length + 1;
        }
        const fields = [];
        for (const el of document.querySelectorAll("main p,main li,main :is(h1,h2,h3,h4,h5,h6),main th,main td")) {
            if (el.querySelector("img,ul,ol,p,table,pre,input,br,details,figure,div,video")) continue;
            const original = inlineMarkdown(el);
            const cell = el.matches("th,td");
            const kind = cell ? [...el.parentElement.cells].map(inlineMarkdown).join("\t") + ":" + el.cellIndex : "block";
            const key = kind + "\n" + original;
            const start = candidates.get(key);
            if (start == null) continue;
            candidates.delete(key);
            fields.push({el, original, start, cell});
        }
        return fields.sort((a, b) => b.start - a.start);
    }

    // Bind an ordered list as a sequence. Matching the whole list disambiguates
    // repeated instructions and empty items after a save and reload.
    function findOrderedSteps(text) {
        const lines = [...text.matchAll(/^[^\n]+/gm)];
        const rows = lines.map(line => {
            const match = /^( *)(\d+)\.(?:([ \t]+)(.*)|$)/.exec(line[0]);
            return match && {start: line.index, stop: line.index + line[0].length,
                indent: match[1], number: match[2], gap: match[3] || "", body: match[4] || ""};
        });
        const steps = new Map();
        for (const list of document.querySelectorAll("main ol")) {
            const elements = [...list.children].map(item => item.querySelector(":scope > p:first-child") || item);
            const bodies = elements.map(inlineMarkdown);
            if (!bodies.length) continue;
            const matches = [];
            for (let i = 0; i < rows.length; i++) {
                if (rows[i]?.body !== bodies[0] || Number(rows[i].number) !== list.start) continue;
                const group = [];
                let j = i;
                for (const body of bodies) {
                    const row = rows[j];
                    if (!row || row.indent !== rows[i].indent || row.body !== body) break;
                    let end = row.stop;
                    j++;
                    // Keep indented continuations (photos, captions, sublists)
                    // with their source step when inserting its next sibling.
                    while (j < lines.length && (lines[j][0].trim() === "" ||
                            lines[j][0].startsWith(row.indent + " "))) {
                        if (lines[j][0].trim()) end = lines[j].index + lines[j][0].length;
                        j++;
                    }
                    group.push({...row, end});
                }
                if (group.length === elements.length && rows[j]?.indent !== rows[i].indent) matches.push(group);
            }
            if (matches.length !== 1) continue;
            elements.forEach((el, i) => steps.set(el, matches[0][i]));
        }
        return steps;
    }

    const itemFields = new Map();
    const listSources = new Map();
    const photos = new WeakMap();
    let uploading = 0;

    function createStep(el, fragment) {
        const item = document.createElement("li");
        const next = item.appendChild(document.createElement("p"));
        if (fragment) next.append(fragment);
        el.closest("li").after(item);
        registerStep(next, null);
        enableField(next, true);
        next.focus();
        window.getSelection().collapse(next, 0);
        queueSave();
    }

    function splitStep(el) {
        const selection = window.getSelection();
        if (!selection.rangeCount) return;
        const range = selection.getRangeAt(0);
        if (!el.contains(range.commonAncestorContainer)) return;
        range.deleteContents();
        range.setEnd(el, el.childNodes.length);
        createStep(el, range.extractContents());
    }

    function deleteEmptyStep(el, event) {
        const item = el.closest("li");
        const source = steps.get(el);
        if (!item || inlineMarkdown(el).trim() || uploading ||
            (source && source.end > source.stop) ||
            [...item.children].some(child => child !== el && !child.classList.contains("step-tools"))) return;
        event.preventDefault();
        const previous = itemFields.get(item.previousElementSibling);
        const next = previous || itemFields.get(item.nextElementSibling);
        const list = item.parentElement;
        item.remove();
        itemFields.delete(item);
        if (next) {
            next.focus();
            const caret = document.createRange();
            caret.selectNodeContents(next);
            caret.collapse(!previous);
            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(caret);
        } else {
            list.hidden = true;
            edit.focus();
        }
        queueSave();
    }

    function registerStep(el, source) {
        const item = el.closest("li");
        steps.set(el, source);
        itemFields.set(item, el);
        item.classList.add("local-edit-step");
        const controls = document.createElement("span");
        controls.className = "step-tools";
        const button = (label, symbol) => {
            const b = document.createElement("button");
            b.type = "button";
            b.title = label;
            b.setAttribute("aria-label", label);
            b.textContent = symbol;
            controls.append(b);
            return b;
        };
        button("Add step below", "+").onclick = () => createStep(el);
        const grip = button("Move step (drag or use arrow keys)", "⠿");
        grip.className = "step-grip";
        grip.addEventListener("pointerdown", e => dragStep(e, item, grip));
        grip.onkeydown = event => {
            if (event.key !== "ArrowUp" && event.key !== "ArrowDown") return;
            event.preventDefault();
            event.stopPropagation();
            const up = event.key === "ArrowUp";
            const other = up ? item.previousElementSibling : item.nextElementSibling;
            if (itemFields.has(other)) moveStep(item, other, !up);
            grip.focus();
        };
        const input = document.createElement("input");
        input.type = "file";
        input.hidden = true;
        input.accept = "image/jpeg,image/png,image/webp";
        input.multiple = true;
        button("Add photo", "▧").onclick = () => input.click();
        input.onchange = () => { attachPhotos(item, Array.from(input.files)); input.value = ""; };
        controls.append(input);
        item.prepend(controls);
    }

    function canMove(item, target) {
        return target && item !== target && !item.contains(target) &&
            item.parentElement.parentElement === target.parentElement.parentElement;
    }

    function moveStep(item, target, after) {
        if (!canMove(item, target)) return;
        if (after) target.after(item);
        else target.before(item);
        queueSave();
    }

    function dragStep(event, item, grip) {
        if (event.button !== 0) return;
        event.preventDefault();
        grip.setPointerCapture(event.pointerId);
        item.classList.add("moving");
        let x = event.clientX, y = event.clientY, target, after, frame;
        function clearTarget() { target?.classList.remove("drop-before", "drop-after"); }
        function locate() {
            clearTarget();
            target = document.elementFromPoint(x, y)?.closest(".local-edit-step");
            if (!canMove(item, target)) target = null;
            if (!target) return;
            const rect = target.getBoundingClientRect();
            after = y > rect.top + rect.height / 2;
            target.classList.add(after ? "drop-after" : "drop-before");
        }
        function tick() {
            const dy = y < 64 ? -12 : y > innerHeight - 64 ? 12 : 0;
            if (dy) { window.scrollBy(0, dy); locate(); }
            frame = requestAnimationFrame(tick);
        }
        grip.onpointermove = e => { x = e.clientX; y = e.clientY; locate(); };
        frame = requestAnimationFrame(tick);
        function finish(e) {
            cancelAnimationFrame(frame);
            if (e.type === "pointerup") {
                x = e.clientX; y = e.clientY; locate();
                moveStep(item, target, after);
            }
            clearTarget();
            item.classList.remove("moving");
            grip.onpointermove = grip.onpointerup = grip.onpointercancel = grip.onlostpointercapture = null;
            if (grip.hasPointerCapture(e.pointerId)) grip.releasePointerCapture(e.pointerId);
        }
        grip.onpointerup = grip.onpointercancel = grip.onlostpointercapture = finish;
    }

    async function attachPhotos(item, files) {
        uploading++;
        edit.disabled = true;
        try {
            for (const file of files) {
                status.textContent = "Adding photo…";
                const params = new URLSearchParams(query);
                params.set("name", file.name);
                const response = await fetch(editor + "/photo?" + params, {
                    method:"POST", body:file, headers:{"Content-Type":"text/plain"}
                });
                if (!response.ok) throw new Error(await response.text());
                const src = await response.text();
                const img = document.createElement("img");
                img.alt = file.name.replace(/\.[^.]+$/, "");
                img.width = 500;
                img.src = src;
                const markup = img.outerHTML;
                // Show the original bytes immediately while mdBook copies the asset.
                const preview = URL.createObjectURL(file);
                img.src = preview;
                window.addEventListener("pagehide", () => URL.revokeObjectURL(preview), {once:true});
                item.append(img);
                const list = photos.get(item) || [];
                list.push(markup);
                photos.set(item, list);
                await flush();
            }
        } catch (error) { report(error); }
        finally { uploading--; edit.disabled = uploading > 0; }
    }

    function installPhotoDrops() {
        const main = document.querySelector("main");
        let hover;
        function clear() { hover?.classList.remove("drop-photo"); hover = null; }
        main.addEventListener("dragover", event => {
            if (!event.dataTransfer.types.includes("Files")) return;
            event.preventDefault(); clear();
            hover = event.target.closest(".local-edit-step");
            event.dataTransfer.dropEffect = hover ? "copy" : "none";
            hover?.classList.add("drop-photo");
        });
        main.addEventListener("dragleave", event => {
            if (!main.contains(event.relatedTarget)) clear();
        });
        main.addEventListener("drop", event => {
            if (!event.dataTransfer.types.includes("Files")) return;
            event.preventDefault(); clear();
            const item = event.target.closest(".local-edit-step");
            if (item) attachPhotos(item, [...event.dataTransfer.files]);
        });
    }

    // Work from the Markdown captured at the start of editing. Text edits in a
    // caption or nested list are applied before its containing step is moved.
    function renderRange(start, end, changes) {
        let text = "", cursor = start;
        const inside = changes.filter(c => c.start >= start && c.stop <= end);
        // An outer list already incorporates its inner edits.
        inside.sort((a, b) => a.start - b.start || b.stop - a.stop);
        for (const c of inside) {
            if (c.start < cursor) continue;
            text += base.slice(cursor, c.start) + c.value;
            cursor = c.stop;
        }
        return text + base.slice(cursor, end);
    }

    function updatedText() {
        const edits = [];
        for (const {el, original, start, cell} of fields) {
            if (steps.has(el)) continue;
            let value = inlineMarkdown(el);
            if (value === original) continue;
            if (!original.includes("\u00a0")) value = value.replace(/\u00a0/g, " ");
            if (cell) value = value.replace(/\|/g, "\\|");
            edits.push({start, stop:start + original.length, value});
        }
        // Lists were registered in document order, with parents before children.
        for (const [list, rows] of [...listSources].reverse()) {
            const start = rows[0].start, stop = rows.at(-1).end;
            const items = [...list.children];
            const reordered = items.length !== rows.length ||
                items.some((item, i) => steps.get(itemFields.get(item)) !== rows[i]);
            let value = "";
            items.forEach((item, i) => {
                const el = itemFields.get(item), row = steps.get(el);
                const number = reordered ? String(list.start + i) : row.number;
                const indent = rows[0].indent;
                const raw = inlineMarkdown(el);
                if (row && !reordered && raw === row.body) value += base.slice(row.start, row.stop);
                else {
                    const body = raw.replace(/\u00a0/g, " ").trim();
                    value += indent + number + "." + (body ? (row?.gap || " ") + body : "");
                }
                const padding = indent + " ".repeat(number.length + 2);
                if (row) {
                    let tail = renderRange(row.stop, row.end, edits);
                    const oldPad = indent + " ".repeat(row.number.length + 1 + (row.gap.length || 1));
                    if (reordered && oldPad !== padding) tail = tail.split("\n").map(line =>
                        line.startsWith(oldPad) ? padding + line.slice(oldPad.length) : line).join("\n");
                    value += tail;
                }
                for (const img of photos.get(item) || []) value += "\n\n" + padding + img;
                if (i < items.length - 1) {
                    const gap = rows[i+1] && base.slice(rows[i].end, rows[i+1].start);
                    value += gap || "\n";
                }
            });
            edits.push({start, stop, value});
        }
        return renderRange(0, base.length, edits);
    }

    let fields, steps, base, revision, saved, timer, pending;
    async function save() {
        let text;
        while ((text = updatedText()) !== saved) {
            // A text/plain request permits a same-machine cross-origin save.
            // The server checks both the preview origin and the source revision.
            const response = await fetch(endpoint, {method:"POST", body:JSON.stringify({text, revision})});
            if (!response.ok) throw new Error(await response.text());
            revision = await response.text();
            saved = text;
        }
        status.textContent = "Saved locally";
        refreshReview();
    }
    function flush() {
        if (!pending) pending = save().finally(() => { pending = null; });
        return pending;
    }
    const report = error => { status.textContent = error.message; };
    function queueSave() {
        status.textContent = "Saving…";
        clearTimeout(timer);
        timer = setTimeout(() => flush().catch(report), 400);
    }
    function enableField(el, step) {
        el.contentEditable = "true";
        el.classList.add("local-edit-field");
        el.addEventListener("click", event => {
            if (event.target.closest("a")) event.preventDefault();
        });
        el.addEventListener("keydown", event => {
            event.stopPropagation();
            if (step && !event.isComposing && (event.key === "Backspace" || event.key === "Delete"))
                deleteEmptyStep(el, event);
            if (event.key === "`" && !event.isComposing && !event.ctrlKey && !event.metaKey)
                toggleSelectedCode(el, event);
        });
        el.addEventListener("keyup", event => event.stopPropagation());
        el.addEventListener("beforeinput", event => {
            if (step && !event.isComposing && ["deleteContentBackward", "deleteContentForward"].includes(event.inputType))
                deleteEmptyStep(el, event);
            if (event.inputType === "insertText" && event.data === "`" && !event.isComposing)
                toggleSelectedCode(el, event);
            if (event.inputType === "insertParagraph" && !event.isComposing && step) splitStep(el);
            if (/^(insertParagraph|insertLineBreak|insertFromDrop|format)/.test(event.inputType)) event.preventDefault();
        });
        el.addEventListener("paste", event => {
            event.preventDefault();
            const plain = event.clipboardData.getData("text/plain").replace(/[\r\n]+/g, " ");
            document.execCommand("insertText", false, plain);
        });
        el.addEventListener("input", event => {
            if (!event.isComposing && event.data?.endsWith("`")) formatCodeAtCaret(el);
            queueSave();
        });
    }
    async function start() {
        const response = await fetch(endpoint);
        if (!response.ok) throw new Error(await response.text());
        const data = await response.json();
        saved = base = data.text;
        revision = data.revision;
        if (typeof socket !== "undefined" && socket instanceof WebSocket) socket.close();
        const mapped = findOrderedSteps(base);
        steps = new Map();
        for (const [field, row] of mapped) {
            let el = field;
            if (el.tagName === "LI") {
                const p = document.createElement("p");
                p.append(...el.childNodes);
                el.append(p);
                el = p;
            }
            const list = el.closest("ol");
            if (!listSources.has(list)) listSources.set(list, []);
            listSources.get(list).push(row);
            registerStep(el, row);
        }
        fields = findFields(base);
        for (const el of new Set([...fields.map(field => field.el), ...steps.keys()])) {
            enableField(el, steps.has(el));
        }
        installPhotoDrops();
        window.addEventListener("beforeunload", event => {
            if (uploading || updatedText() !== saved) { event.preventDefault(); event.returnValue = ""; }
        });
        status.textContent = "Click text to edit";
        edit.textContent = "Done";
    }
    edit.addEventListener("click", async () => {
        edit.disabled = true;
        try {
            if (!fields) await start();
            else {
                clearTimeout(timer);
                await flush();
                status.textContent = "Building preview…";
                const deadline = Date.now() + 15000;
                while (true) {
                    const state = await fetch(editor + "/built?" + query);
                    if (!state.ok) throw new Error(await state.text());
                    if (await state.text() === "ready") break;
                    if (Date.now() >= deadline) throw new Error("Preview is still building. Try Done again.");
                    await new Promise(resolve => setTimeout(resolve, 150));
                }
                // mdBook's HTTP Last-Modified header has one-second resolution.
                // Use the saved revision so fast consecutive builds cannot serve a stale 304.
                const target = new URL(location.href);
                target.searchParams.set("editRevision", revision);
                location.replace(target);
            }
        } catch (error) { report(error); }
        finally { edit.disabled = false; }
    });
})();
