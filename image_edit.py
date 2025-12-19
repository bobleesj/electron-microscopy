#!/usr/bin/env python3
"""
Process only NEW (untracked) image files detected by git.

This script automatically detects new files using git and processes them:
  - Converts HEIC/HEIF → JPG
  - Converts PNG → JPG (with white background for transparency)
  - Compresses existing JPG/JPEG files
  - Normalizes extensions to lowercase .jpg

Usage Examples:
    # Dry run - see what would be done without making changes
    python scripts/process_new_images.py --dry-run

    # Process with default settings (quality=85, no resize)
    python scripts/process_new_images.py

    # Resize to max 1200px width and delete original HEIC/PNG files
    python scripts/process_new_images.py --max-width 1200 --delete-originals

    # Process a specific folder
    python scripts/process_new_images.py src/img/STEM --quality 90

    # Include already staged files (not just untracked)
    python scripts/process_new_images.py --include-staged

Options:
    folder              Folder to process (default: src/img/)
    --quality N         JPEG quality 1-100 (default: 85, higher = better quality)
    --max-width N       Resize images to max width in pixels (default: no resize)
    --delete-originals  Delete original HEIC/PNG files after successful conversion
    --dry-run           Preview changes without modifying any files
    --include-staged    Also process staged (git add) files, not just untracked
    --all               Process ALL images, including already committed files

Requirements:
    Python 3.10+ (uses modern type hints)
    pip install Pillow pillow-heif

Note:
    This script only processes files that are NEW to git (untracked files).
    Already committed files are not touched. This makes it perfect for
    processing freshly added images before committing.
"""

import argparse
import subprocess
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow not installed. Run: pip install Pillow")
    exit(1)

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
    HEIC_SUPPORT = True
except ImportError:
    print("Warning: pillow-heif not installed. HEIC conversion disabled.")
    print("Run: pip install pillow-heif")
    HEIC_SUPPORT = False


def get_repo_root() -> Path:
    """Get the git repository root directory."""
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=True,
    )
    return Path(result.stdout.strip())


def get_all_image_files(target_dir: Path) -> list[Path]:
    """
    Get all image files in the target directory (recursive).
    
    Args:
        target_dir: Directory to scan for images
    
    Returns:
        List of Path objects for all image files
    """
    extensions = (".heic", ".heif", ".png", ".jpg", ".jpeg")
    files = []
    for ext in extensions:
        files.extend(target_dir.rglob(f"*{ext}"))
        files.extend(target_dir.rglob(f"*{ext.upper()}"))
    return [f for f in files if f.is_file()]


def get_new_files(target_dir: Path, include_staged: bool = False) -> list[Path]:
    """
    Get list of new (untracked) files in the target directory.
    
    Args:
        target_dir: Directory to check for new files
        include_staged: If True, also include staged files
    
    Returns:
        List of Path objects for new files
    """
    repo_root = get_repo_root()
    rel_target = target_dir.relative_to(repo_root)
    
    # Get untracked files
    result = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", str(rel_target)],
        capture_output=True,
        text=True,
        cwd=repo_root,
    )
    files = [repo_root / f for f in result.stdout.strip().split("\n") if f]
    
    # Optionally include staged (new) files
    if include_staged:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=A", str(rel_target)],
            capture_output=True,
            text=True,
            cwd=repo_root,
        )
        staged = [repo_root / f for f in result.stdout.strip().split("\n") if f]
        files.extend(staged)
    
    return [f for f in files if f.exists()]


def get_file_size_mb(path: Path) -> float:
    """Get file size in MB."""
    return path.stat().st_size / (1024 * 1024)


def convert_heic_to_jpg(
    input_path: Path,
    quality: int = 85,
    max_width: int | None = None,
    delete_original: bool = False,
    dry_run: bool = False,
) -> tuple[float, float]:
    """Convert a single HEIC file to JPG."""
    original_size = get_file_size_mb(input_path)
    output_path = input_path.with_suffix(".jpg")

    if dry_run:
        print(f"  [DRY RUN] Would convert: {input_path.name} → {output_path.name}")
        return original_size, original_size

    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "P", "LA"):
            img = img.convert("RGB")

        if max_width and img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        img.save(
            output_path,
            "JPEG",
            quality=quality,
            optimize=True,
            progressive=True,
        )

    new_size = get_file_size_mb(output_path)

    if delete_original:
        input_path.unlink()

    return original_size, new_size


def convert_png_to_jpg(
    input_path: Path,
    quality: int = 85,
    max_width: int | None = None,
    delete_original: bool = False,
    dry_run: bool = False,
) -> tuple[float, float]:
    """Convert a single PNG file to JPG."""
    original_size = get_file_size_mb(input_path)
    output_path = input_path.with_suffix(".jpg")

    if dry_run:
        print(f"  [DRY RUN] Would convert: {input_path.name} → {output_path.name}")
        return original_size, original_size

    with Image.open(input_path) as img:
        # Handle transparency by compositing on white background
        if img.mode in ("RGBA", "LA", "P"):
            if img.mode == "P":
                img = img.convert("RGBA")
            background = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "RGBA":
                background.paste(img, mask=img.split()[3])  # Use alpha as mask
            else:
                background.paste(img)
            img = background
        elif img.mode != "RGB":
            img = img.convert("RGB")

        if max_width and img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        img.save(
            output_path,
            "JPEG",
            quality=quality,
            optimize=True,
            progressive=True,
        )

    new_size = get_file_size_mb(output_path)

    if delete_original:
        input_path.unlink()

    return original_size, new_size


def compress_jpg(
    input_path: Path,
    quality: int = 85,
    max_width: int | None = None,
    dry_run: bool = False,
) -> tuple[float, float, Path]:
    """Compress a single JPG file and normalize extension to lowercase .jpg."""
    original_size = get_file_size_mb(input_path)
    
    # Check if we need to rename (case-sensitive check on extension string)
    needs_rename = input_path.suffix != ".jpg"
    
    if needs_rename:
        output_path = input_path.with_suffix(".jpg")
    else:
        output_path = input_path

    if dry_run:
        if needs_rename:
            print(f"  [DRY RUN] Would compress and rename: {input_path.name} → {output_path.name}")
        else:
            print(f"  [DRY RUN] Would compress: {input_path.name}")
        return original_size, original_size, output_path

    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        if max_width and img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        # On case-insensitive filesystems (macOS), .JPG and .jpg are the same file
        # So we need to use a temp file when renaming
        if needs_rename:
            temp_path = input_path.with_suffix(".jpg.tmp")
            img.save(
                temp_path,
                "JPEG",
                quality=quality,
                optimize=True,
                progressive=True,
            )
            input_path.unlink()
            temp_path.rename(output_path)
        else:
            img.save(
                input_path,
                "JPEG",
                quality=quality,
                optimize=True,
                progressive=True,
            )

    new_size = get_file_size_mb(output_path)
    return original_size, new_size, output_path


def process_new_images(
    target_dir: Path,
    quality: int = 85,
    max_width: int | None = None,
    delete_originals: bool = False,
    dry_run: bool = False,
    include_staged: bool = False,
    process_all: bool = False,
) -> None:
    """Process images in the target directory."""
    
    if not target_dir.exists():
        print(f"Error: {target_dir} does not exist")
        return

    if process_all:
        print(f"🔍 Scanning for ALL image files in: {target_dir}")
    else:
        print(f"🔍 Scanning for new files in: {target_dir}")
    print(f"   Quality: {quality}, Max width: {max_width or 'unchanged'}")
    print("-" * 60)

    if process_all:
        new_files = get_all_image_files(target_dir)
    else:
        new_files = get_new_files(target_dir, include_staged)
    
    if not new_files:
        if process_all:
            print("✅ No image files found in the directory.")
        else:
            print("✅ No new files found. Everything is already tracked by git.")
        return

    # Categorize files
    heic_files = [f for f in new_files if f.suffix.lower() in (".heic", ".heif")]
    png_files = [f for f in new_files if f.suffix.lower() == ".png"]
    jpg_files = [f for f in new_files if f.suffix.lower() in (".jpg", ".jpeg")]

    total_original = 0.0
    total_new = 0.0

    # Process HEIC files
    if heic_files:
        if not HEIC_SUPPORT:
            print(f"\n⚠️  Skipping {len(heic_files)} HEIC files (pillow-heif not installed)")
        else:
            print(f"\n📸 Converting {len(heic_files)} HEIC files to JPG...")
            for heic_path in sorted(heic_files):
                original, new = convert_heic_to_jpg(
                    heic_path, quality, max_width, delete_originals, dry_run
                )
                total_original += original
                total_new += new
                reduction = ((original - new) / original * 100) if original > 0 else 0
                action = "converted" if not dry_run else "would convert"
                print(f"  ✓ {heic_path.name}: {original:.2f}MB → {new:.2f}MB ({reduction:.1f}% reduction)")

    # Process PNG files
    if png_files:
        print(f"\n🖼️  Converting {len(png_files)} PNG files to JPG...")
        for png_path in sorted(png_files):
            original, new = convert_png_to_jpg(
                png_path, quality, max_width, delete_originals, dry_run
            )
            total_original += original
            total_new += new
            reduction = ((original - new) / original * 100) if original > 0 else 0
            print(f"  ✓ {png_path.name}: {original:.2f}MB → {new:.2f}MB ({reduction:.1f}% reduction)")

    # Process JPG files
    if jpg_files:
        print(f"\n🗜️  Compressing {len(jpg_files)} JPG files...")
        for jpg_path in sorted(jpg_files):
            original, new, output_path = compress_jpg(jpg_path, quality, max_width, dry_run)
            total_original += original
            total_new += new
            reduction = ((original - new) / original * 100) if original > 0 else 0
            if output_path.name != jpg_path.name:
                print(f"  ✓ {jpg_path.name} → {output_path.name}: {original:.2f}MB → {new:.2f}MB ({reduction:.1f}% reduction)")
            else:
                print(f"  ✓ {jpg_path.name}: {original:.2f}MB → {new:.2f}MB ({reduction:.1f}% reduction)")

    # Summary
    print("\n" + "=" * 60)
    total_reduction = ((total_original - total_new) / total_original * 100) if total_original > 0 else 0
    saved = total_original - total_new
    
    print(f"📊 Summary:")
    print(f"   Files processed: {len(heic_files) + len(png_files) + len(jpg_files)}")
    print(f"   Original size:   {total_original:.2f} MB")
    print(f"   New size:        {total_new:.2f} MB")
    print(f"   Space saved:     {saved:.2f} MB ({total_reduction:.1f}%)")
    
    if dry_run:
        print("\n⚠️  This was a dry run. No files were modified.")
    else:
        if delete_originals and (heic_files or png_files):
            print("\n🗑️  Original HEIC/PNG files have been deleted.")
        print("\n✅ Done! You can now stage the converted files with: git add .")


def main():
    parser = argparse.ArgumentParser(
        description="Process new (untracked) images: convert HEIC/PNG to JPG and compress"
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default="src/img",
        help="Folder to process (default: src/img/)",
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=85,
        help="JPEG quality (1-100, default: 85)",
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=1200,
        help="Max width in pixels (default: 1200)",
    )
    parser.add_argument(
        "--delete-originals",
        action="store_true",
        default=True,
        help="Delete original HEIC/PNG files after conversion (default: True)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )
    parser.add_argument(
        "--include-staged",
        action="store_true",
        help="Also process staged (git add) files, not just untracked",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        dest="process_all",
        help="Process ALL images, including already committed files",
    )

    args = parser.parse_args()

    # Resolve folder path relative to repo root
    repo_root = get_repo_root()
    target_dir = repo_root / args.folder

    process_new_images(
        target_dir=target_dir,
        quality=args.quality,
        max_width=args.max_width,
        delete_originals=args.delete_originals,
        dry_run=args.dry_run,
        include_staged=args.include_staged,
        process_all=args.process_all,
    )


if __name__ == "__main__":
    main()
