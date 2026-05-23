#!/usr/bin/env python3
"""Shuffle gallery images in index.html. Pin _1032793.jpg to position 4 (second row)."""
import re, random

HTML = "/Users/ishaan.yadav/photography-portfolio/index.html"
PINNED = "_1032793.jpg"
PIN_POS = 3  # 0-indexed = 4th item = second row col 1 in 3-col grid

with open(HTML, encoding="utf-8") as f:
    content = f.read()

# Extract all image blocks between masonry open and close tags
start_tag = '<div class="masonry-grid"'
end_tag   = "</div><!-- end masonry -->"

start_idx = content.index(start_tag)
# find end of opening div tag
open_end = content.index(">", start_idx) + 1
close_idx = content.index(end_tag)

header = content[:open_end]          # everything up to and including opening masonry div >
blocks_str = content[open_end:close_idx]
footer = content[close_idx:]         # from </div><!-- end masonry --> onwards

# Split into individual image blocks
blocks = re.split(r'(?=<div class="break-inside-avoid)', blocks_str)
blocks = [b for b in blocks if b.strip()]

print(f"Total image blocks: {len(blocks)}")

# Find pinned block
pinned_block = None
others = []
for b in blocks:
    if PINNED in b:
        pinned_block = b
        print(f"Pinned: {PINNED} found")
    else:
        others.append(b)

if pinned_block is None:
    print(f"WARNING: {PINNED} not found — shuffling all")
    random.shuffle(blocks)
    final_blocks = blocks
else:
    random.shuffle(others)
    # Insert pinned at PIN_POS
    others.insert(PIN_POS, pinned_block)
    final_blocks = others

# Rebuild
new_content = header + "\n".join(final_blocks) + "\n" + footer
with open(HTML, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Shuffled {len(final_blocks)} images. {PINNED} at position {PIN_POS + 1}.")
