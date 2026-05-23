#!/usr/bin/env python3
"""Compress all gallery images to JPEG, max 300KB"""
import os
from pathlib import Path
from PIL import Image

GALLERY = Path(__file__).parent.parent / "dist/assets/gallery"
MAX_BYTES = 300 * 1024  # 300KB

def compress(path):
    img = Image.open(path).convert("RGB")
    quality = 85
    while quality >= 20:
        img.save(path, "JPEG", quality=quality, optimize=True)
        if os.path.getsize(path) <= MAX_BYTES:
            break
        quality -= 5
    return os.path.getsize(path)

total = skipped = compressed = 0
for f in sorted(GALLERY.glob("*")):
    if f.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
        continue
    orig = os.path.getsize(f)
    if orig <= MAX_BYTES:
        skipped += 1
        continue
    # rename non-jpg to jpg
    if f.suffix.lower() != ".jpg":
        new = f.with_suffix(".jpg")
        f.rename(new); f = new
    size = compress(f)
    compressed += 1
    print(f"  {f.name}: {orig//1024}KB → {size//1024}KB")
    total += orig - size

print(f"\nDone: {compressed} compressed, {skipped} already small, saved {total//1024//1024}MB")
