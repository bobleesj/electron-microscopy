#!/usr/bin/env python3
"""
Compress JPG images without losing quality.

Usage:
    python scripts/compress_images.py [--quality 85] [--resize 1200]

Options:
    --quality   JPEG quality (1-100, default: 85, higher = better quality)
    --resize    Max width in pixels (default: None, keeps original size)
    --dry-run   Show what would be done without making changes
"""

import argparse
import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow not installed. Run: pip install Pillow")
    exit(1)


def get_file_size_mb(path: Path) -> float:
    """Get file size in MB."""
    return path.stat().st_size / (1024 * 1024)


def compress_image(
    input_path: Path,
    quality: int = 85,
    max_width: int | None = None,
    dry_run: bool = False,
) -> tuple[float, float]:
    """
    Compress a single image.
    
    Returns:
        Tuple of (original_size_mb, new_size_mb)
    """
    original_size = get_file_size_mb(input_path)
    
    if dry_run:
        print(f"  [DRY RUN] Would compress: {input_path}")
        return original_size, original_size
    
    with Image.open(input_path) as img:
        # Convert to RGB if necessary (handles RGBA, etc.)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        # Resize if max_width specified and image is larger
        if max_width and img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
        # Save with optimization
        img.save(
            input_path,
            "JPEG",
            quality=quality,
            optimize=True,
            progressive=True,
        )
    
    new_size = get_file_size_mb(input_path)
    return original_size, new_size


def compress_all_images(
    root_dir: Path,
    quality: int = 85,
    max_width: int | None = None,
    dry_run: bool = False,
) -> None:
    """Compress all JPG images in directory tree."""
    img_dir = root_dir / "img"
    
    if not img_dir.exists():
        print(f"Error: {img_dir} does not exist")
        return
    
    jpg_files = list(img_dir.rglob("*.jpg")) + list(img_dir.rglob("*.jpeg"))
    
    if not jpg_files:
        print("No JPG files found.")
        return
    
    print(f"Found {len(jpg_files)} JPG files")
    print(f"Quality: {quality}, Max width: {max_width or 'unchanged'}")
    print("-" * 50)
    
    total_original = 0.0
    total_new = 0.0
    
    for jpg_path in sorted(jpg_files):
        rel_path = jpg_path.relative_to(root_dir)
        original, new = compress_image(jpg_path, quality, max_width, dry_run)
        total_original += original
        total_new += new
        
        reduction = ((original - new) / original * 100) if original > 0 else 0
        print(f"  {rel_path}: {original:.2f} MB → {new:.2f} MB ({reduction:.1f}% saved)")
    
    print("-" * 50)
    total_reduction = ((total_original - total_new) / total_original * 100) if total_original > 0 else 0
    print(f"Total: {total_original:.2f} MB → {total_new:.2f} MB ({total_reduction:.1f}% saved)")


def main():
    parser = argparse.ArgumentParser(description="Compress JPG images")
    parser.add_argument(
        "--quality",
        type=int,
        default=85,
        help="JPEG quality 1-100 (default: 85)",
    )
    parser.add_argument(
        "--resize",
        type=int,
        default=None,
        help="Max width in pixels (default: keep original)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )
    
    args = parser.parse_args()
    
    # Find repo root (where this script is in scripts/)
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    
    print(f"Compressing images in: {root_dir}")
    compress_all_images(root_dir, args.quality, args.resize, args.dry_run)


if __name__ == "__main__":
    main()
