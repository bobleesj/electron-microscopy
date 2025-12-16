#!/usr/bin/env python3
"""
Convert HEIC images to JPG and compress them.

Usage:
    python scripts/convert_heic_to_jpg.py [folder] [--quality 85] [--max-width 1200] [--delete-originals]

Options:
    folder            Folder to process (default: images/ in repo root)
    --quality         JPEG quality (1-100, default: 85)
    --max-width       Max width in pixels (default: None, keeps original size)
    --delete-originals  Delete original HEIC files after conversion
    --dry-run         Show what would be done without making changes

Requirements:
    pip install Pillow pillow-heif
"""

import argparse
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow not installed. Run: pip install Pillow")
    exit(1)

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    print("pillow-heif not installed. Run: pip install pillow-heif")
    exit(1)


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
    """
    Convert a single HEIC file to JPG.

    Returns:
        Tuple of (original_size_mb, new_size_mb)
    """
    original_size = get_file_size_mb(input_path)
    output_path = input_path.with_suffix(".jpg")

    if dry_run:
        print(f"  [DRY RUN] Would convert: {input_path.name} → {output_path.name}")
        return original_size, original_size

    with Image.open(input_path) as img:
        # Convert to RGB (HEIC can have alpha channel)
        if img.mode in ("RGBA", "P", "LA"):
            img = img.convert("RGB")

        # Resize if max_width specified and image is larger
        if max_width and img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        # Save as optimized JPEG
        img.save(
            output_path,
            "JPEG",
            quality=quality,
            optimize=True,
            progressive=True,
        )

    new_size = get_file_size_mb(output_path)

    # Delete original if requested
    if delete_original:
        input_path.unlink()

    return original_size, new_size


def convert_all_heic(
    target_dir: Path,
    quality: int = 85,
    max_width: int | None = None,
    delete_originals: bool = False,
    dry_run: bool = False,
) -> None:
    """Convert all HEIC images in directory tree to JPG."""
    if not target_dir.exists():
        print(f"Error: {target_dir} does not exist")
        return

    # Find all HEIC files (case-insensitive)
    heic_files = list(target_dir.rglob("*.HEIC")) + list(target_dir.rglob("*.heic"))

    if not heic_files:
        print("No HEIC files found.")
        return

    print(f"Found {len(heic_files)} HEIC files")
    print(f"Quality: {quality}, Max width: {max_width or 'unchanged'}")
    if delete_originals:
        print("Will delete original HEIC files after conversion")
    print("-" * 50)

    total_original = 0.0
    total_new = 0.0

    for heic_path in sorted(heic_files):
        rel_path = heic_path.relative_to(target_dir)
        try:
            original, new = convert_heic_to_jpg(
                heic_path, quality, max_width, delete_originals, dry_run
            )
            total_original += original
            total_new += new

            reduction = ((original - new) / original * 100) if original > 0 else 0
            status = "converted" if not dry_run else "would convert"
            print(f"  {rel_path}: {original:.2f} MB → {new:.2f} MB ({reduction:.1f}% saved) [{status}]")
        except Exception as e:
            print(f"  {rel_path}: ERROR - {e}")

    print("-" * 50)
    total_reduction = (
        (total_original - total_new) / total_original * 100
    ) if total_original > 0 else 0
    print(f"Total: {total_original:.2f} MB → {total_new:.2f} MB ({total_reduction:.1f}% saved)")

    if not dry_run and delete_originals:
        print(f"\nDeleted {len(heic_files)} original HEIC files")


def main():
    parser = argparse.ArgumentParser(
        description="Convert HEIC images to JPG and compress them"
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=None,
        help="Folder to process (default: images/ in repo root)",
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=85,
        help="JPEG quality 1-100 (default: 85)",
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=None,
        help="Max width in pixels (default: keep original)",
    )
    parser.add_argument(
        "--delete-originals",
        action="store_true",
        help="Delete original HEIC files after successful conversion",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )

    args = parser.parse_args()

    # Determine folder to process
    if args.folder:
        target_dir = Path(args.folder).resolve()
    else:
        # Default to images/ folder in repo root
        script_dir = Path(__file__).parent
        target_dir = script_dir.parent / "images"

    print(f"Processing HEIC files in: {target_dir}")
    convert_all_heic(
        target_dir,
        args.quality,
        args.max_width,
        args.delete_originals,
        args.dry_run,
    )


if __name__ == "__main__":
    main()
