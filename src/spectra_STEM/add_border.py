"""
Add 1px black border to all images in img/ directory.

Creates a backup in img_backup/ before modifying.

Usage:
    python add_border.py --dry-run   # Preview changes
    python add_border.py             # Apply borders
"""

import argparse
import shutil
from pathlib import Path
from PIL import Image, ImageOps


IMG_DIR = Path(__file__).parent / "img"
BACKUP_DIR = Path(__file__).parent / "img_backup"
BORDER_WIDTH = 1
BORDER_COLOR = (0, 0, 0)  # Black


def backup_images():
    """Backup all images to img_backup/ directory."""
    if BACKUP_DIR.exists():
        print(f"Backup directory already exists: {BACKUP_DIR}")
        return False
    print(f"Creating backup at {BACKUP_DIR}")
    shutil.copytree(IMG_DIR, BACKUP_DIR)
    print(f"Backed up {len(list(BACKUP_DIR.rglob('*.jpg')))} images")
    return True


def add_border_to_image(img_path: Path, dry_run: bool = False):
    """Add black border to a single image."""
    try:
        img = Image.open(img_path)
        # Add border using ImageOps.expand
        bordered = ImageOps.expand(img, border=BORDER_WIDTH, fill=BORDER_COLOR)
        if dry_run:
            print(f"  [DRY RUN] Would add border: {img_path.name} ({img.size} -> {bordered.size})")
        else:
            bordered.save(img_path, quality=95)
            print(f"  Added border: {img_path.name}")
        return True
    except Exception as e:
        print(f"  ERROR: {img_path.name}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Add 1px black border to images")
    parser.add_argument("--dry-run", action="store_true", help="Preview without making changes")
    args = parser.parse_args()
    if not IMG_DIR.exists():
        print(f"Image directory not found: {IMG_DIR}")
        return
    # Find all jpg images
    images = sorted(IMG_DIR.rglob("*.jpg"))
    print(f"Found {len(images)} images in {IMG_DIR}")
    if not images:
        return
    # Backup first (unless dry run)
    if not args.dry_run:
        if not BACKUP_DIR.exists():
            backup_images()
        else:
            print(f"Backup already exists at {BACKUP_DIR}")
    # Process images
    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Adding {BORDER_WIDTH}px black border to images:")
    success = 0
    for img_path in images:
        if add_border_to_image(img_path, dry_run=args.dry_run):
            success += 1
    print(f"\n{'Would process' if args.dry_run else 'Processed'} {success}/{len(images)} images")
    if not args.dry_run:
        print(f"Original images backed up to: {BACKUP_DIR}")


if __name__ == "__main__":
    main()
