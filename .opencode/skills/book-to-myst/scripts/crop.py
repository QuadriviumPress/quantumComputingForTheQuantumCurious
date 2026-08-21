#!/usr/bin/env python3
"""Crop a sub-image from a page image using normalized 0-999 coordinates.

Usage:
    python crop.py --path page_012.png --box X1 Y1 X2 Y2 --name fig_2_6 \
        --out-dir book/images/ch-02

Box coordinates are thousandths (0 = left/top edge, 999 = right/bottom edge).
Outputs JSON to stdout: {"path": "/abs/<name>_crop.png"}
"""
import argparse
import json
import os

from PIL import Image


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True)
    ap.add_argument("--box", nargs=4, type=int, required=True,
                    help="X1 Y1 X2 Y2 in 0-999 normalized coordinates")
    ap.add_argument("--name", required=True)
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args()

    x1, y1, x2, y2 = args.box
    img = Image.open(args.path)
    w, h = img.size
    box_px = (round(x1 / 999 * w), round(y1 / 999 * h),
              round(x2 / 999 * w), round(y2 / 999 * h))
    os.makedirs(args.out_dir, exist_ok=True)
    out = os.path.abspath(
        os.path.join(args.out_dir, f"{args.name}_crop.png"))
    img.crop(box_px).save(out)
    print(json.dumps({"path": out, "box": [x1, y1, x2, y2]}))


if __name__ == "__main__":
    main()
