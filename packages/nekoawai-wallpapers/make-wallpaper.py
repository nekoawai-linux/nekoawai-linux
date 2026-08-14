#!/usr/bin/python3
"""Draw the NekoAwai wallpaper.

The picture is arithmetic rather than artwork: NekoAwai has none of its own and
borrows none, so the default background is drawn from the palette the rest of
the system already uses. A near-black room lit from below the bottom edge, and
the project's mark set into the light at about a tenth of the contrast the
desktop icons have -- there on the second day, not on the first.

Deterministic: the same bytes come out of every build.
"""

import math
import struct
import sys
import zlib

WIDTH = 2560
HEIGHT = 1440

GROUND = (0x0d, 0x0b, 0x12)   # recess, the unlit part of the room
GLOW = (0x24, 0x1c, 0x30)     # one step above panel, where the light falls
ACCENT = (0xe0, 0x5a, 0x95)   # the NekoAwai pink, at a few percent
MARK = (0x9a, 0x92, 0xad)     # muted, the colour of text nobody has to read

# The lamp sits below the bottom edge, a little wider than the screen is tall.
CENTRE_X = 0.5
CENTRE_Y = 1.06
RADIUS = 0.95

# =^..^= across the middle of the light, six cells wide.
MARK_Y = 0.66
MARK_CELL = 1 / 22.0
MARK_ALPHA = 0.20

# An 8x8 ordered dither. The gradient spans eight values of red over 1440
# rows; without dithering that is eight visible bands.
BAYER = [
    [0, 32, 8, 40, 2, 34, 10, 42],
    [48, 16, 56, 24, 50, 18, 58, 26],
    [12, 44, 4, 36, 14, 46, 6, 38],
    [60, 28, 52, 20, 62, 30, 54, 22],
    [3, 35, 11, 43, 1, 33, 9, 41],
    [51, 19, 59, 27, 49, 17, 57, 25],
    [15, 47, 7, 39, 13, 45, 5, 37],
    [63, 31, 55, 23, 61, 29, 53, 21],
]


def chunk(tag, data):
    return (struct.pack('>I', len(data)) + tag + data
            + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff))


def room():
    """The lit room, one scanline at a time, ready for a PNG."""
    cx = CENTRE_X * WIDTH
    cy = CENTRE_Y * HEIGHT
    r = RADIUS * HEIGHT

    # The light is symmetrical about the vertical axis, so half of each row is
    # enough to work out and the other half is that half backwards.
    half = WIDTH // 2
    dx2 = [((x - cx) / r) ** 2 for x in range(half)]

    raw = bytearray()
    for y in range(HEIGHT):
        dy2 = ((y - cy) / r) ** 2
        bayer = BAYER[y % 8]
        row = bytearray()
        for x in range(half):
            light = math.exp(-(dx2[x] + dy2) * 1.6)
            warm = light ** 4 * 0.06
            d = (bayer[x % 8] + 0.5) / 64.0 - 0.5
            for i in range(3):
                v = (GROUND[i]
                     + (GLOW[i] - GROUND[i]) * light
                     + (ACCENT[i] - GROUND[i]) * warm) + d
                row.append(0 if v < 0 else 255 if v > 255 else int(v + 0.5))
        mirror = bytearray()
        for x in range(half - 1, -1, -1):
            mirror += row[x * 3:x * 3 + 3]
        raw += b'\x00' + row + mirror
    return raw


# How much room each glyph takes, in cells. The dots are the eyes of the
# thing and belong close together, so they are set tighter than a console
# would set them.
ADVANCE = {'=': 1.00, '^': 0.80, '.': 0.42}


def segments(cell):
    """=^..^= as line segments and dots, in pixels, around the origin.

    A bar is a segment, a caret is two of them, and a dot is a segment with no
    length -- one shape covers the whole mark.
    """
    glyphs = '=^..^='
    width = sum(ADVANCE[g] for g in glyphs) * cell

    out = []
    pen = -width / 2.0
    for glyph in glyphs:
        step = ADVANCE[glyph] * cell
        cx = pen + step / 2.0
        pen += step
        if glyph == '=':
            for dy in (-0.16 * cell, 0.16 * cell):
                out.append((cx - 0.30 * cell, dy, cx + 0.30 * cell, dy, 0.06, 0.0))
        elif glyph == '^':
            out.append((cx - 0.26 * cell, 0.20 * cell, cx, -0.20 * cell, 0.06, 0.0))
            out.append((cx, -0.20 * cell, cx + 0.26 * cell, 0.20 * cell, 0.06, 0.0))
        else:
            # The eyes carry the only warmth in the picture, and barely.
            out.append((cx, 0.16 * cell, cx, 0.16 * cell, 0.085, 0.5))
    return [(x0, y0, x1, y1, t * cell, warm) for x0, y0, x1, y1, t, warm in out]


def draw_mark(raw):
    cell = MARK_CELL * HEIGHT
    ox = WIDTH / 2.0
    oy = MARK_Y * HEIGHT
    shapes = segments(cell)

    pad = 0.3 * cell + 2
    x0 = int(min(min(s[0], s[2]) for s in shapes) + ox - pad)
    x1 = int(max(max(s[0], s[2]) for s in shapes) + ox + pad)
    y0 = int(min(min(s[1], s[3]) for s in shapes) + oy - pad)
    y1 = int(max(max(s[1], s[3]) for s in shapes) + oy + pad)

    stride = 1 + WIDTH * 3
    for y in range(y0, y1 + 1):
        py = y + 0.5 - oy
        for x in range(x0, x1 + 1):
            px = x + 0.5 - ox
            cover = 0.0
            warmth = 0.0
            for sx0, sy0, sx1, sy1, half, warm in shapes:
                dx, dy = sx1 - sx0, sy1 - sy0
                length = dx * dx + dy * dy
                if length:
                    t = ((px - sx0) * dx + (py - sy0) * dy) / length
                    t = 0.0 if t < 0 else 1.0 if t > 1 else t
                else:
                    t = 0.0
                ex, ey = px - (sx0 + t * dx), py - (sy0 + t * dy)
                # One pixel of feathering, which is all a mark this quiet needs.
                a = half + 0.5 - math.hypot(ex, ey)
                a = 0.0 if a < 0 else 1.0 if a > 1 else a
                if a > cover:
                    cover, warmth = a, warm
            if cover <= 0:
                continue
            i = y * stride + 1 + x * 3
            for c in range(3):
                base = raw[i + c]
                tint = MARK[c] + (ACCENT[c] - MARK[c]) * warmth
                v = base + (tint - base) * MARK_ALPHA * cover
                raw[i + c] = 0 if v < 0 else 255 if v > 255 else int(v + 0.5)


def main(path):
    raw = room()
    draw_mark(raw)
    png = (b'\x89PNG\r\n\x1a\n'
           + chunk(b'IHDR', struct.pack('>IIBBBBB', WIDTH, HEIGHT, 8, 2, 0, 0, 0))
           + chunk(b'IDAT', zlib.compress(bytes(raw), 9))
           + chunk(b'IEND', b''))
    with open(path, 'wb') as f:
        f.write(png)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'wallpaper.png')
