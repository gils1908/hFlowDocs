#!/usr/bin/env python3
"""Export help-site brand PNGs from Assets/hFlow Logos/.

Run from the Gilat workspace root:

  pip install Pillow   # once per machine
  python3 hFlowDocs/scripts/export-brand-assets.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "Assets" / "hFlow Logos"
OUT = ROOT / "hFlowDocs" / "images" / "brand"

LOCKUP_CANVAS = (1548, 512)


def fit_on_canvas(src: Path, dest: Path, canvas_size: tuple[int, int]) -> None:
    im = Image.open(src).convert("RGBA")
    cw, ch = canvas_size
    scale = min(cw / im.width, ch / im.height)
    nw = max(1, int(im.width * scale))
    nh = max(1, int(im.height * scale))
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    canvas.paste(im, ((cw - nw) // 2, (ch - nh) // 2), im)
    dest.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dest, optimize=True)


def resize_square(src: Path, dest: Path, size: int) -> None:
    im = Image.open(src).convert("RGBA")
    im = im.resize((size, size), Image.Resampling.LANCZOS)
    dest.parent.mkdir(parents=True, exist_ok=True)
    im.save(dest, optimize=True)


def strip_dark_lockup_navy(src: Path, dest: Path, canvas_size: tuple[int, int]) -> None:
    """Crop to non-navy opaque content, then fit on transparent canvas."""
    im = Image.open(src).convert("RGBA")
    pixels = im.load()
    w, h = im.size

    def is_content(r: int, g: int, b: int, a: int) -> bool:
        if a < 8:
            return False
        # Full-width navy card in Dark exports (~#0f172a / similar)
        if r < 45 and g < 55 and b < 75:
            return False
        return True

    xs: list[int] = []
    ys: list[int] = []
    for y in range(h):
        for x in range(w):
            if is_content(*pixels[x, y]):
                xs.append(x)
                ys.append(y)

    if not xs:
        fit_on_canvas(src, dest, canvas_size)
        return

    pad = 4
    left = max(0, min(xs) - pad)
    right = min(w - 1, max(xs) + pad)
    top = max(0, min(ys) - pad)
    bottom = min(h - 1, max(ys) + pad)
    cropped = im.crop((left, top, right + 1, bottom + 1))
    tmp = dest.with_suffix(".crop-tmp.png")
    cropped.save(tmp)
    fit_on_canvas(tmp, dest, canvas_size)
    tmp.unlink(missing_ok=True)


def main() -> int:
    if not ASSETS.is_dir():
        print(f"Missing assets dir: {ASSETS}", file=sys.stderr)
        return 1

    # Flat lockup for light UI: dark wordmark on transparent bg (D_lockup_flat).
    # Do not use Light/lockup-flat-* — those have a white wordmark for dark surfaces.
    fit_on_canvas(
        ASSETS / "D_lockup_flat" / "hFlow-lockup-512.png",
        OUT / "hflow-lockup.png",
        LOCKUP_CANVAS,
    )
    strip_dark_lockup_navy(
        ASSETS / "Dark" / "lockup-framed-flat-h512.png",
        OUT / "hflow-lockup-dark.png",
        LOCKUP_CANVAS,
    )
    fit_on_canvas(
        ASSETS / "D_lockup_flat" / "hFlow-lockup-256.png",
        OUT / "hflow-lockup-sm.png",
        (774, 256),
    )

    resize_square(
        ASSETS / "Light" / "chart-only-flat-256.png",
        OUT / "hflow-mark-sm.png",
        64,
    )
    resize_square(
        ASSETS / "Dark" / "chart-only-framed-flat-256.png",
        OUT / "hflow-mark-dark-sm.png",
        64,
    )
    resize_square(
        ASSETS / "Light" / "chart-only-flat-256.png",
        OUT / "hflow-mark.png",
        128,
    )
    resize_square(
        ASSETS / "Dark" / "chart-only-framed-flat-256.png",
        OUT / "hflow-mark-dark.png",
        128,
    )
    resize_square(
        ASSETS / "Light" / "chart-only-flat-256.png",
        OUT / "hflow-favicon.png",
        32,
    )

    print("Wrote brand assets to", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
