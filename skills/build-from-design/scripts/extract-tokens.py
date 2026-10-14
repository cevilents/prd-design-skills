#!/usr/bin/env python3
"""Ekstrak design tokens dari DESIGN.md (format skill design-maker) ke JSON.

Pemakaian:
    python3 extract-tokens.py DESIGN.md [--out tokens.json]

Yang dibaca:
    2.1 Warna      tabel dengan kolom Token + Light (+ Dark). Sel token boleh pasangan
                   "`card` / `card-foreground`" dengan nilai "#FFF / #000". Nilai boleh
                   hex, rgb(), hsl(), atau oklch(). Kalau 2.1 kosong, dicoba dari
                   blok CSS di 2.8 (--nama: #hex, blok .dark = mode gelap).
    2.4 Tipografi  tabel Token + "Ukuran / line-height" + Weight; baris "**Font ...:**"
                   untuk nama font.
    2.6 Bentuk     token radius-* dan shadow-* (jika berupa tabel).

Keluaran:
    {"colors": {nama: {"light": "#RRGGBB", "dark": "#RRGGBB" | null}},
     "typography": {nama: {size, lineHeight, weight, sizePx, sizeMaxPx,
                           lineHeightPx, lineHeightRatio}},
     "fonts": [...], "fallbackFonts": [...],
     "radius": {nama: {raw, px}}, "shadow": {nama: raw},
     "warnings": [...]}
Bagian yang tidak terbaca memberi peringatan di stderr dan diabaikan; script lanjut.
Hanya pustaka standar, kompatibel dengan Python 3.9.
"""
import argparse
import colorsys
import json
import math
import re
import sys

WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)
    sys.stderr.write("WARN: %s\n" % msg)


# ---------------------------------------------------------------------------
# Markdown: heading, kode, tabel
# ---------------------------------------------------------------------------

def scan(lines):
    """Kembalikan (headings, in_code). headings: (lineno, level, text); lineno 1-based."""
    headings, in_code, fence = [], [False] * (len(lines) + 2), None
    for i, line in enumerate(lines, 1):
        m = re.match(r"^\s*(```+|~~~+)", line)
        if fence is None:
            if m:
                fence = m.group(1)[0]
                in_code[i] = True
                continue
            hm = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
            if hm:
                headings.append((i, len(hm.group(1)), hm.group(2)))
        else:
            in_code[i] = True
            if m and m.group(1)[0] == fence:
                fence = None
    return headings, in_code


def section(headings, n_lines, num):
    """Rentang (start, end) baris untuk heading '### num' atau '## num'; end eksklusif."""
    for ln, lvl, txt in headings:
        if lvl in (2, 3) and re.match(r"^%s(\s|\.|:|$)" % re.escape(num), txt):
            end = n_lines + 1
            for ln2, lvl2, _ in headings:
                if ln2 > ln and lvl2 <= lvl:
                    end = ln2
                    break
            return (ln, end)
    return None


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    cells, cur, tick, i = [], [], False, 0
    while i < len(s):
        c = s[i]
        if c == "`":
            tick = not tick
            cur.append(c)
        elif c == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur.append("|")
            i += 1
        elif c == "|" and not tick:
            cells.append("".join(cur).strip())
            cur = []
        else:
            cur.append(c)
        i += 1
    cells.append("".join(cur).strip())
    return cells


SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")


def tables_in(lines, in_code, rng):
    """Semua tabel dalam rentang: [{header:[...], rows:[(lineno, cells)]}]."""
    out = []
    if not rng:
        return out
    i = rng[0]
    while i < rng[1] - 1:
        if (not in_code[i] and "|" in lines[i - 1] and not in_code[i + 1]
                and SEP_RE.match(lines[i])):
            header, rows, j = split_row(lines[i - 1]), [], i + 2
            while j < rng[1] and not in_code[j] and lines[j - 1].strip().startswith("|"):
                rows.append((j, split_row(lines[j - 1])))
                j += 1
            out.append({"header": header, "rows": rows})
            i = j
        else:
            i += 1
    return out


def find_col(header, *keys):
    for idx, h in enumerate(header):
        hl = h.lower()
        if any(k in hl for k in keys):
            return idx
    return None


def strip_md(s):
    return re.sub(r"[`*]", "", s).strip()


# ---------------------------------------------------------------------------
# Warna
# ---------------------------------------------------------------------------

COLOR_RE = re.compile(
    r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3})(?![0-9a-zA-Z_])"
    r"|oklch\([^)]*\)|rgba?\([^)]*\)|hsla?\([^)]*\)", re.I)


def to_hex(rgb):
    return "#%02X%02X%02X" % tuple(max(0, min(255, int(round(v)))) for v in rgb)


def oklch_to_rgb(L, C, h):
    a, b = C * math.cos(math.radians(h)), C * math.sin(math.radians(h))
    l_ = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m_ = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s_ = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    lin = (4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
           -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
           -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_)

    def gam(x):
        x = max(0.0, min(1.0, x))
        return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055
    return tuple(gam(v) * 255 for v in lin)


def parse_color(tok):
    """String warna -> '#RRGGBB' atau None."""
    t = tok.strip()
    if t.startswith("#"):
        h = t[1:]
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return "#" + h[:6].upper()
    nums = re.findall(r"-?\d*\.?\d+%?", t.split("(", 1)[1].split("/")[0])
    fn = t.split("(", 1)[0].lower()

    def num(s, pct_scale=1.0):
        return float(s[:-1]) / 100 * pct_scale if s.endswith("%") else float(s)
    try:
        if fn.startswith("oklch") and len(nums) >= 3:
            return to_hex(oklch_to_rgb(num(nums[0]), num(nums[1], 0.4), float(nums[2].rstrip("%"))))
        if fn.startswith("rgb") and len(nums) >= 3:
            return to_hex([num(n, 255) if n.endswith("%") else float(n) for n in nums[:3]])
        if fn.startswith("hsl") and len(nums) >= 3:
            r, g, b = colorsys.hls_to_rgb(float(nums[0].rstrip("%")) / 360, num(nums[2]), num(nums[1]))
            return to_hex((r * 255, g * 255, b * 255))
    except (ValueError, IndexError):
        pass
    return None


def cell_tokens(cell):
    toks = re.findall(r"`([^`]+)`", cell)
    if not toks:
        m = re.match(r"^\s*([A-Za-z][\w.\-]*)\s*$", cell)
        toks = [m.group(1)] if m else []
    return toks


def cell_colors(cell):
    return [parse_color(m.group(0)) for m in COLOR_RE.finditer(cell)]


TOKEN_NAME_RE = re.compile(r"^[A-Za-z][\w.\-]*$")


def parse_colors(lines, in_code, rng):
    colors = {}
    for tbl in tables_in(lines, in_code, rng):
        h = tbl["header"]
        tcol = find_col(h, "token", "nama") if find_col(h, "token", "nama") is not None else 0
        lcol = find_col(h, "light", "terang")
        dcol = find_col(h, "dark", "gelap")
        if lcol is None:
            # tanpa kolom Light: pakai kolom pertama (selain token) yang berisi warna
            for idx in range(len(h)):
                if idx != tcol and idx != dcol and any(
                        idx < len(c) and COLOR_RE.search(c[idx]) for _, c in tbl["rows"]):
                    lcol = idx
                    break
        if lcol is None:
            continue
        for ln, cells in tbl["rows"]:
            if len(cells) <= max(tcol, lcol):
                continue
            names = cell_tokens(cells[tcol])
            bad = [n for n in names if not TOKEN_NAME_RE.match(n)]
            if not names or bad:
                if bad:
                    warn("baris %d: token '%s' bukan nama token valid (placeholder?), dilewati" % (ln, bad[0]))
                continue
            light = cell_colors(cells[lcol])
            dark = cell_colors(cells[dcol]) if dcol is not None and dcol < len(cells) else []
            if len(light) != len(names):
                if light:
                    warn("baris %d: %d token tapi %d warna Light (%s), dilewati"
                         % (ln, len(names), len(light), ", ".join(names)))
                continue
            if dark and len(dark) != len(names):
                warn("baris %d: jumlah warna Dark (%d) tidak cocok dengan token (%d), Dark diabaikan"
                     % (ln, len(dark), len(names)))
                dark = []
            for i, n in enumerate(names):
                colors[n] = {"light": light[i], "dark": dark[i] if dark else None}
    return colors


def colors_from_css(lines, in_code, rng):
    """Cadangan: --nama: warna; dari blok kode 2.8. Blok yang diawali .dark = mode gelap."""
    colors, mode = {}, None
    if not rng:
        return colors
    for i in range(rng[0], rng[1]):
        if not in_code[i]:
            continue
        line = lines[i - 1]
        if re.search(r"\.dark\b|\[data-theme=.?dark|prefers-color-scheme:\s*dark", line) and "{" in line:
            mode = "dark"
        elif re.search(r":root|^\s*html\s*\{", line) and "{" in line:
            mode = "light"
        m = re.match(r"^\s*--([\w-]+)\s*:\s*(.+?)\s*;", line)
        if m and mode:
            found = COLOR_RE.search(m.group(2))
            val = parse_color(found.group(0)) if found else None
            if val:
                ent = colors.setdefault(m.group(1), {"light": None, "dark": None})
                ent[mode] = val
    for ent in colors.values():
        if ent["light"] is None:
            ent["light"] = ent["dark"]
    return colors


# ---------------------------------------------------------------------------
# Tipografi
# ---------------------------------------------------------------------------

def to_px(s):
    """'28px' '1.5rem' '44' '8dp' -> float px; selain itu None."""
    m = re.match(r"^\s*(-?\d*[.,]?\d+)\s*(px|rem|em|pt|dp|sp)?\s*$", s.strip(), re.I)
    if not m:
        return None
    v = float(m.group(1).replace(",", "."))
    u = (m.group(2) or "px").lower()
    return v * 16 if u in ("rem", "em") else v * 4 / 3 if u == "pt" else v


def split_top(s, sep):
    out, depth, cur = [], 0, []
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == sep and depth == 0:
            out.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    out.append("".join(cur).strip())
    return out


def parse_size(raw):
    """-> (min_px, max_px). Non-fluid: min == max. clamp(a, b, c): (a, c)."""
    raw = strip_md(raw)
    m = re.match(r"^clamp\((.*)\)$", raw, re.I)
    if m:
        parts = split_top(m.group(1), ",")
        if len(parts) == 3:
            lo, hi = to_px(parts[0]), to_px(parts[2])
            if lo is not None and hi is not None:
                return lo, hi
        return None, None
    px = to_px(raw)
    return px, px


def parse_lh(raw, size_px):
    """-> (px, ratio)."""
    raw = strip_md(raw)
    if raw.endswith("%"):
        try:
            return None, float(raw[:-1]) / 100
        except ValueError:
            return None, None
    if re.match(r"^\d*[.,]?\d+$", raw):
        v = float(raw.replace(",", "."))
        return (None, v) if v <= 4 else (v, None)
    return to_px(raw), None


def parse_typography(lines, in_code, rng):
    typo = {}
    for tbl in tables_in(lines, in_code, rng):
        h = tbl["header"]
        scol, wcol = find_col(h, "ukuran", "size"), find_col(h, "weight", "bobot")
        if scol is None:
            continue
        tcol = find_col(h, "token") if find_col(h, "token") is not None else 0
        for ln, cells in tbl["rows"]:
            if len(cells) <= scol:
                continue
            names = cell_tokens(cells[tcol])
            if len(names) != 1:
                continue
            parts = split_top(cells[scol], "/")
            size_raw = strip_md(parts[0])
            lh_raw = strip_md(parts[1]) if len(parts) > 1 else ""
            lo, hi = parse_size(size_raw)
            if lo is None:
                warn("baris %d: ukuran '%s' untuk %s tidak terbaca" % (ln, size_raw, names[0]))
            lh_px, lh_ratio = parse_lh(lh_raw, lo) if lh_raw else (None, None)
            if lh_raw and lh_px is None and lh_ratio is None:
                warn("baris %d: line-height '%s' untuk %s tidak terbaca" % (ln, lh_raw, names[0]))
            weight = None
            if wcol is not None and wcol < len(cells):
                wm = re.search(r"\b([1-9]00)\b", cells[wcol])
                weight = int(wm.group(1)) if wm else None
            typo[names[0]] = {
                "size": size_raw, "lineHeight": lh_raw, "weight": weight,
                "sizePx": lo, "sizeMaxPx": hi if hi != lo else None,
                "lineHeightPx": lh_px, "lineHeightRatio": lh_ratio,
            }
    return typo


GENERIC_FONTS = {"serif", "sans-serif", "monospace", "system-ui", "ui-sans-serif", "ui-serif",
                 "ui-monospace", "ui-rounded", "cursive", "fantasy", "-apple-system",
                 "blinkmacsystemfont", "sans", "arial narrow"}

FAMILY_RE = re.compile(r"^((?:[A-Z][\w]*)(?:\s+[A-Z][\w]*)*)")
FAMILY_WEIGHT_RE = re.compile(r"\b([A-Z][\w]*(?:\s+[A-Z][\w]*)+)\s+[1-9]00\b")


def parse_fonts(lines, in_code, rng):
    fonts, fallbacks = [], []
    if not rng:
        return fonts, fallbacks

    def add(name):
        name = name.strip()
        if name and name.lower() not in [f.lower() for f in fonts]:
            fonts.append(name)

    for i in range(rng[0], rng[1]):
        if in_code[i]:
            continue
        line = lines[i - 1]
        m = re.match(r"^\s*[-*]\s*\*\*Font[^*]*:\*\*\s*(.+)$", line)
        if not m:
            continue
        body = m.group(1)
        fm = FAMILY_RE.match(body)
        if fm:
            add(fm.group(1))
        else:
            warn("baris %d: nama font tidak terbaca dari '%s'" % (i, body[:40]))
        for wm in FAMILY_WEIGHT_RE.finditer(body):
            add(wm.group(1))
        for stack in re.findall(r"fallback\s+`([^`]+)`", body):
            for fam in stack.split(","):
                fam = fam.strip().strip("\"'")
                if fam and fam.lower() not in [f.lower() for f in fallbacks]:
                    fallbacks.append(fam)
    return fonts, fallbacks


# ---------------------------------------------------------------------------
# Radius & shadow
# ---------------------------------------------------------------------------

def parse_shape(lines, in_code, rng):
    radius, shadow = {}, {}
    for tbl in tables_in(lines, in_code, rng):
        h = tbl["header"]
        tcol = find_col(h, "token") if find_col(h, "token") is not None else 0
        vcol = find_col(h, "nilai", "value")
        if vcol is None:
            continue
        for ln, cells in tbl["rows"]:
            if len(cells) <= max(tcol, vcol):
                continue
            names = cell_tokens(cells[tcol])
            if len(names) != 1:
                continue
            n, raw = names[0], strip_md(cells[vcol])
            if n.startswith("radius"):
                m = re.match(r"^(\d*[.,]?\d+)\s*(px|rem|dp|sp)?", raw)
                px = to_px(m.group(0)) if m else None
                if px is None:
                    warn("baris %d: nilai radius '%s' untuk %s tidak terbaca" % (ln, raw, n))
                radius[n] = {"raw": raw, "px": px}
            elif n.startswith("shadow"):
                shadow[n] = raw
    return radius, shadow


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Ekstrak design tokens dari DESIGN.md ke JSON.")
    ap.add_argument("design", help="path DESIGN.md")
    ap.add_argument("--out", help="file JSON keluaran (default: stdout)")
    args = ap.parse_args()
    try:
        text = open(args.design, encoding="utf-8").read()
    except OSError as e:
        sys.exit("Tidak bisa membuka %s: %s" % (args.design, e))
    lines = text.split("\n")
    headings, in_code = scan(lines)
    n = len(lines)

    sec21, sec24, sec26, sec28 = (section(headings, n, k) for k in ("2.1", "2.4", "2.6", "2.8"))
    for name, s in (("2.1 Warna", sec21), ("2.4 Tipografi", sec24)):
        if not s:
            warn("bagian %s tidak ditemukan" % name)

    colors = parse_colors(lines, in_code, sec21)
    if not colors:
        colors = colors_from_css(lines, in_code, sec28)
        if colors:
            warn("tabel warna 2.1 kosong, token diambil dari blok kode 2.8")
        else:
            warn("tidak ada token warna yang terbaca")
    typography = parse_typography(lines, in_code, sec24)
    if not typography:
        warn("tidak ada token tipografi yang terbaca")
    fonts, fallbacks = parse_fonts(lines, in_code, sec24)
    if not fonts:
        warn("tidak ada nama font yang terbaca dari 2.4")
    radius, shadow = parse_shape(lines, in_code, sec26)

    out = {"colors": colors, "typography": typography, "fonts": fonts,
           "fallbackFonts": fallbacks, "radius": radius, "shadow": shadow,
           "warnings": WARNINGS}
    payload = json.dumps(out, ensure_ascii=False, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(payload + "\n")
    else:
        print(payload)
    has_dark = sum(1 for c in colors.values() if c["dark"])
    sys.stderr.write("OK: colors=%d (dark=%d) typography=%d fonts=%d radius=%d shadow=%d warnings=%d%s\n" % (
        len(colors), has_dark, len(typography), len(fonts), len(radius), len(shadow), len(WARNINGS),
        " -> " + args.out if args.out else ""))
    if not colors and not typography:
        sys.exit(1)


if __name__ == "__main__":
    main()
