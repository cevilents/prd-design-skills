#!/usr/bin/env python3
"""Lint mekanis untuk DESIGN.md hasil skill design-maker.

Pemakaian:
    python3 lint-design.py DESIGN.md [--prd PRD.md]

Keluaran: temuan dikelompokkan per tingkat (ERROR / WARN / INFO), tiap temuan
membawa nomor baris dan pesan singkat. Exit code 1 bila ada ERROR, selain itu 0.
Hanya memakai pustaka standar, kompatibel dengan Python 3.9.
"""

import argparse
import re
import sys

ERROR, WARN, INFO = "ERROR", "WARN", "INFO"

findings = []  # (severity, check_no, line, message)


def add(sev, check, line, msg):
    findings.append((sev, check, line, msg))


# ---------------------------------------------------------------------------
# Parsing dasar markdown
# ---------------------------------------------------------------------------

HEX_RE = re.compile(r"(?<![\w&#])#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})(?![0-9a-zA-Z_])")


def norm_hex(h):
    h = h.lstrip("#").upper()
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return "#" + h


def find_hexes(text):
    out = []
    for m in HEX_RE.finditer(text):
        g = m.group(1)
        if len(g) == 3 and not re.search(r"[a-fA-F]", g):
            continue  # "#123" lebih mungkin nomor, bukan warna
        out.append((m.start(), norm_hex(g)))
    return out


class Doc(object):
    def __init__(self, text):
        self.lines = text.split("\n")
        self.n = len(self.lines)
        self.in_code = [False] * (self.n + 2)  # indeks 1-based
        self.blocks = []  # dict(start, end, lang, lines)
        self.headings = []  # (lineno, level, text)
        self._scan()
        self.tables = self._find_tables()

    def _scan(self):
        fence = None
        cur = None
        for i, line in enumerate(self.lines, 1):
            m = re.match(r"^\s*(```+|~~~+)\s*(.*)$", line)
            if fence is None:
                if m:
                    fence = m.group(1)[0] * 3
                    cur = {"start": i, "lang": m.group(2).strip(), "lines": [], "end": None}
                    self.in_code[i] = True
                    continue
                hm = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
                if hm:
                    self.headings.append((i, len(hm.group(1)), hm.group(2)))
            else:
                self.in_code[i] = True
                if m and m.group(1)[0] * 3 == fence and not m.group(2).strip():
                    cur["end"] = i
                    self.blocks.append(cur)
                    fence = None
                    cur = None
                else:
                    cur["lines"].append(line)
        if cur is not None:
            cur["end"] = self.n
            self.blocks.append(cur)

    # -- seksi -------------------------------------------------------------
    def main_section(self, num):
        """(start, end) baris untuk '## num.' (end eksklusif)."""
        start = None
        for ln, lvl, txt in self.headings:
            if lvl == 2 and re.match(r"^%s\.(\s|$)" % re.escape(str(num)), txt):
                start = ln
                break
        if start is None:
            return None
        end = self.n + 1
        for ln, lvl, txt in self.headings:
            if ln > start and lvl <= 2:
                end = ln
                break
        return (start, end)

    def sub_section(self, num):
        """(start, end) untuk '### num' (mis. '2.1'); berakhir di heading level <= 3."""
        start = None
        for ln, lvl, txt in self.headings:
            if lvl == 3 and re.match(r"^%s(\s|\.|:|$)" % re.escape(num), txt):
                start = ln
                break
        if start is None:
            return None
        end = self.n + 1
        for ln, lvl, txt in self.headings:
            if ln > start and lvl <= 3:
                end = ln
                break
        return (start, end)

    def text_of(self, rng, skip_code=False):
        if not rng:
            return ""
        out = []
        for i in range(rng[0], rng[1]):
            if skip_code and self.in_code[i]:
                continue
            out.append(self.lines[i - 1])
        return "\n".join(out)

    # -- tabel -------------------------------------------------------------
    @staticmethod
    def split_row(line):
        s = line.strip()
        if s.startswith("|"):
            s = s[1:]
        if s.endswith("|") and not s.endswith("\\|"):
            s = s[:-1]
        cells, cur, in_tick = [], [], False
        i = 0
        while i < len(s):
            c = s[i]
            if c == "`":
                in_tick = not in_tick
                cur.append(c)
            elif c == "\\" and i + 1 < len(s) and s[i + 1] == "|":
                cur.append("|")
                i += 1
            elif c == "|" and not in_tick:
                cells.append("".join(cur).strip())
                cur = []
            else:
                cur.append(c)
            i += 1
        cells.append("".join(cur).strip())
        return cells

    def _find_tables(self):
        tables = []
        i = 1
        while i < self.n:
            if (not self.in_code[i] and "|" in self.lines[i - 1]
                    and not self.in_code[i + 1]
                    and re.match(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$", self.lines[i])):
                header = self.split_row(self.lines[i - 1])
                rows = []
                j = i + 2
                while j <= self.n and not self.in_code[j] and self.lines[j - 1].strip().startswith("|"):
                    rows.append((j, self.split_row(self.lines[j - 1])))
                    j += 1
                tables.append({"hline": i, "header": header, "rows": rows, "end": j})
                i = j
            else:
                i += 1
        return tables

    def tables_in(self, rng):
        if not rng:
            return []
        return [t for t in self.tables if rng[0] <= t["hline"] < rng[1]]


def col_index(header, *keys):
    for idx, h in enumerate(header):
        hl = h.lower()
        for k in keys:
            if k in hl:
                return idx
    return None


def ticks(cell):
    return re.findall(r"`([^`]+)`", cell)


def first_token(cell):
    m = re.search(r"`([a-z][a-z0-9-]*)`", cell)
    if m:
        return m.group(1)
    m = re.match(r"^\s*([a-z][a-z0-9-]*)\b", cell)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Parsing CSS
# ---------------------------------------------------------------------------

def strip_css_comments(text):
    def repl(m):
        return "\n" * m.group(0).count("\n")
    return re.sub(r"/\*.*?\*/", repl, text, flags=re.S)


def css_blocks(text, selector_re):
    """Kembalikan list (body, offset_body) untuk blok yang selector-nya cocok."""
    out = []
    for m in re.finditer(r"(^|[}\s;])(%s)\s*\{" % selector_re, text):
        start = m.end()
        depth, i = 1, start
        while i < len(text) and depth:
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
            i += 1
        out.append((text[start:i - 1], start))
    return out


def css_decls(body, offset, text, base_line):
    """Hasilkan dict nama -> (nilai, nomor_baris) untuk deklarasi --x: v;"""
    res = {}
    for m in re.finditer(r"--([\w-]+)\s*:\s*([^;{}]+);", body):
        pos = offset + m.start()
        line = base_line + text.count("\n", 0, pos)
        res[m.group(1)] = (m.group(2).strip(), line)
    return res


class CssInfo(object):
    def __init__(self):
        self.found = False
        self.root = {}
        self.dark = {}
        self.theme = {}  # --nama (tanpa --) di @theme
        self.has_dark_block = False
        self.has_custom_variant_dark = False
        self.has_color_scheme_light = False
        self.first_line = None
        self.full_text = ""


def parse_css(doc, rng):
    info = CssInfo()
    if not rng:
        return info
    for b in doc.blocks:
        if not (rng[0] <= b["start"] < rng[1]):
            continue
        body = "\n".join(b["lines"])
        looks_css = b["lang"].lower() in ("css", "scss", "pcss") or ":root" in body or "@theme" in body
        if not looks_css:
            continue
        info.found = True
        if info.first_line is None:
            info.first_line = b["start"]
        text = strip_css_comments(body)
        info.full_text += "\n" + text
        base = b["start"] + 1
        for blk, off in css_blocks(text, r":root"):
            info.root.update(css_decls(blk, off, text, base))
            if re.search(r"color-scheme\s*:\s*light", blk):
                info.has_color_scheme_light = True
        for blk, off in css_blocks(text, r"\.dark"):
            info.has_dark_block = True
            info.dark.update(css_decls(blk, off, text, base))
        for blk, off in css_blocks(text, r"@theme(?:\s+inline)?"):
            info.theme.update(css_decls(blk, off, text, base))
    if re.search(r"@custom-variant\s+dark\b", info.full_text):
        info.has_custom_variant_dark = True
    if re.search(r"color-scheme\s*:\s*light", info.full_text):
        info.has_color_scheme_light = True
    return info


# ---------------------------------------------------------------------------
# Kontras WCAG
# ---------------------------------------------------------------------------

def luminance(h):
    h = h.lstrip("#")
    chans = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255.0
        chans.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * chans[0] + 0.7152 * chans[1] + 0.0722 * chans[2]


def contrast(h1, h2):
    l1, l2 = luminance(h1), luminance(h2)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


# ---------------------------------------------------------------------------
# Konteks bersama
# ---------------------------------------------------------------------------

class Ctx(object):
    pass


def parse_tokens_table(doc, ctx):
    """Isi ctx.light, ctx.dark (token -> (hex, baris)), ctx.has_dark_col."""
    ctx.light, ctx.dark = {}, {}
    ctx.has_dark_col = False
    rng = doc.sub_section("2.1")
    ctx.rng_21 = rng
    if not rng:
        add(WARN, 1, 0, "tidak bisa membaca bagian 2.1 (heading '### 2.1' tidak ditemukan)")
        return
    tabs = doc.tables_in(rng)
    if not tabs:
        add(WARN, 1, rng[0], "tidak bisa membaca bagian 2.1 (tabel warna tidak ditemukan)")
        return
    t = tabs[0]
    h = t["header"]
    lc = col_index(h, "light", "nilai", "value")
    dc = col_index(h, "dark")
    if lc is None:
        # cari kolom pertama yang berisi hex
        for ci in range(1, len(h)):
            if any(find_hexes(r[1][ci]) for r in t["rows"] if len(r[1]) > ci):
                lc = ci
                break
    if lc is None:
        add(WARN, 1, t["hline"], "tidak bisa membaca bagian 2.1 (kolom nilai warna tidak ditemukan)")
        return
    ctx.has_dark_col = dc is not None
    for ln, cells in t["rows"]:
        if len(cells) <= lc:
            continue
        names = re.findall(r"`([a-z][a-z0-9-]*)`", cells[0])
        for col, store in ((lc, ctx.light), (dc, ctx.dark)):
            if col is None or col >= len(cells):
                continue
            hx = [x[1] for x in find_hexes(cells[col])]
            if not hx or not names:
                continue
            if len(hx) != len(names):
                add(WARN, 1, ln, "tidak bisa memasangkan token dan hex di baris ini (%d token, %d hex)" % (len(names), len(hx)))
                continue
            for nm, v in zip(names, hx):
                store[nm] = (v, ln)


# ---------------------------------------------------------------------------
# Pemeriksaan
# ---------------------------------------------------------------------------

def detect_stack(doc, ctx):
    """Tebak stack dari blok kode bagian 2.8: tailwind / css / other."""
    if ctx.stack != "auto":
        return ctx.stack
    css = ctx.css
    if css.found:
        if css.theme or re.search(r'@import\s+["\']tailwindcss["\']|@tailwind\b', css.full_text):
            return "tailwind"
        return "css"
    rng = doc.sub_section("2.8")
    if rng:
        for b in doc.blocks:
            if rng[0] <= b["start"] < rng[1]:
                return "other"
    return "unknown"


def check_tokens(doc, ctx):
    """1. Token tabel 2.1 vs blok CSS 2.8."""
    css = ctx.css
    if not ctx.light:
        return
    if not css.found:
        if ctx.stack == "other":
            rng = doc.sub_section("2.8")
            code = "\n".join("\n".join(b["lines"]) for b in doc.blocks if rng and rng[0] <= b["start"] < rng[1])
            found = set()
            for m in re.finditer(r"0x[fF]{2}([0-9a-fA-F]{6})\b", code):     # Flutter/Dart 0xFFRRGGBB (alpha penuh saja)
                found.add("#" + m.group(1).upper())
            for m in re.finditer(r"0x([0-9a-fA-F]{6})\b", code):          # Swift Color(hex: 0xRRGGBB)
                found.add("#" + m.group(1).upper())
            for h in find_hexes(code):                                    # '#RRGGBB' di TS/JSON
                found.add(h[1])
            missing = 0
            for nm, (hv, ln) in sorted(ctx.light.items(), key=lambda x: x[1][1]):
                if norm_hex(hv) not in found:
                    missing += 1
                    add(ERROR, 1, ln, "warna token `%s` (%s) dari tabel 2.1 tidak ditemukan di kode 2.8 (dicari sebagai #RRGGBB, 0xRRGGBB, atau 0xFFRRGGBB)" % (nm, hv))
            add(INFO, 1, 0, "stack non-web: %d warna tabel 2.1 dicocokkan dengan kode 2.8, %d tidak ditemukan; nama token dan nilai non-warna dicek manual" % (len(ctx.light), missing))
        else:
            add(WARN, 1, 0, "tidak bisa membaca bagian 2.8 (blok CSS tidak ditemukan)")
        return

    def hexval(v):
        found = find_hexes(v)
        if found and re.fullmatch(r"\s*#[0-9a-fA-F]{3,6}\s*", v):
            return found[0][1]
        return None

    root_hex = {}
    for k, (v, ln) in css.root.items():
        hv = hexval(v)
        if hv:
            root_hex[k] = (hv, ln)
    for k, (v, ln) in css.theme.items():
        if k.startswith("color-"):
            hv = hexval(v)
            nm = k[len("color-"):]
            if hv and nm not in root_hex:
                root_hex[nm] = (hv, ln)

    for nm, (hv, ln) in sorted(ctx.light.items(), key=lambda x: x[1][1]):
        if nm not in root_hex:
            add(ERROR, 1, ln, "token `%s` ada di tabel 2.1 tapi tidak ada di blok CSS 2.8: tambahkan `--%s: %s;`" % (nm, nm, hv))
        elif root_hex[nm][0] != hv:
            add(ERROR, 1, ln, "token `%s`: tabel 2.1 %s, CSS 2.8 %s (baris %d): samakan keduanya" % (nm, hv, root_hex[nm][0], root_hex[nm][1]))
    for nm, (hv, ln) in sorted(root_hex.items(), key=lambda x: x[1][1]):
        if nm not in ctx.light:
            add(ERROR, 1, ln, "token `%s` (%s) ada di CSS 2.8 tapi tidak ada di tabel 2.1: tambahkan ke tabel atau hapus dari CSS" % (nm, hv))

    # dark
    if ctx.has_dark_col:
        if not css.has_dark_block:
            add(ERROR, 1, ctx.dark and min(v[1] for v in ctx.dark.values()) or 0,
                "tabel 2.1 punya kolom Dark tapi CSS 2.8 tidak punya blok `.dark`")
        else:
            dk = {}
            for k, (v, ln) in css.dark.items():
                hv = hexval(v)
                if hv:
                    dk[k] = (hv, ln)
            for nm, (hv, ln) in ctx.dark.items():
                if nm not in dk:
                    add(ERROR, 1, ln, "token dark `%s` ada di tabel 2.1 tapi tidak ada di `.dark` CSS 2.8" % nm)
                elif dk[nm][0] != hv:
                    add(ERROR, 1, ln, "token dark `%s`: tabel %s, CSS %s (baris %d): samakan keduanya" % (nm, hv, dk[nm][0], dk[nm][1]))
            for nm, (hv, ln) in dk.items():
                if nm not in ctx.dark:
                    add(ERROR, 1, ln, "token dark `%s` ada di `.dark` CSS tapi tidak ada di kolom Dark tabel 2.1" % nm)
    elif css.has_dark_block:
        add(ERROR, 1, css.first_line or 0, "CSS 2.8 punya blok `.dark` tapi tabel 2.1 tidak punya kolom Dark")

    # pemetaan @theme (khusus Tailwind)
    if ctx.stack == "tailwind" and (css.theme or any(True for _ in root_hex)):
        mapped = set(k[len("color-"):] for k in css.theme if k.startswith("color-"))
        for nm, (hv, ln) in root_hex.items():
            if nm in css.root and nm not in mapped:
                add(WARN, 1, ln, "token `%s` ada di :root tapi tidak dipetakan sebagai `--color-%s` di @theme: utility Tailwind-nya tidak akan ada" % (nm, nm))


def check_hex_outside(doc, ctx):
    """2. Hex di luar bagian 2."""
    s2 = doc.main_section(2)
    s15 = doc.sub_section("1.5")
    for i in range(1, doc.n + 1):
        if s2 and s2[0] <= i < s2[1]:
            continue
        if s15 and s15[0] <= i < s15[1]:
            continue
        for pos, hv in find_hexes(doc.lines[i - 1]):
            add(ERROR, 2, i, "hex %s di luar bagian 2: pakai nama token, bukan nilai hex" % hv)


def check_contrast(doc, ctx):
    """3. Tabel kontras 2.3."""
    rng = doc.sub_section("2.3")
    if not rng:
        add(WARN, 3, 0, "tidak bisa membaca bagian 2.3 (heading '### 2.3' tidak ditemukan)")
        return
    tabs = doc.tables_in(rng)
    if not tabs:
        add(WARN, 3, rng[0], "tidak bisa membaca bagian 2.3 (tabel kontras tidak ditemukan)")
        return
    prev_end = rng[0]
    for t in tabs:
        h = t["header"]
        ratio_c = col_index(h, "rasio")
        norm_c = col_index(h, "normal")
        large_c = col_index(h, "besar", "non-teks")
        if ratio_c is None:
            add(WARN, 3, t["hline"], "tidak bisa membaca bagian 2.3 (kolom Rasio tidak ditemukan)")
            continue
        pre = " ".join(doc.lines[prev_end - 1:t["hline"] - 1]).lower()
        prev_end = t["end"]
        is_dark = "dark" in pre
        palette = ctx.dark if is_dark else ctx.light
        mode = "dark" if is_dark else "light"
        if not palette:
            add(WARN, 3, t["hline"], "tidak bisa membaca bagian 2.3 (palet %s dari 2.1 kosong)" % mode)
            continue
        for ln, cells in t["rows"]:
            if len(cells) <= ratio_c or len(cells) < 2:
                continue
            if any("dekoratif" in c.lower() for c in cells):
                continue

            def resolve(cell):
                hx = find_hexes(cell)
                if hx:
                    return hx[0][1], hx[0][1]
                tk = first_token(cell)
                if tk and tk in palette:
                    return palette[tk][0], tk
                return None, tk

            fg, fgn = resolve(cells[0])
            bg, bgn = resolve(cells[1])
            if fg is None or bg is None:
                miss = [n for n, v in ((fgn, fg), (bgn, bg)) if v is None]
                add(WARN, 3, ln, "token tidak bisa di-resolve ke hex (%s, mode %s): ratio tidak diperiksa" % (", ".join(str(x) for x in miss), mode))
                continue
            m = re.search(r"\d+(?:[.,]\d+)?", cells[ratio_c])
            if not m:
                add(WARN, 3, ln, "rasio tidak terbaca di baris `%s` / `%s`" % (fgn, bgn))
                continue
            stated = float(m.group(0).replace(",", "."))
            real = contrast(fg, bg)
            real2 = float("%.2f" % real)
            if abs(stated - real2) > 0.02:
                add(ERROR, 3, ln, "rasio `%s` di atas `%s` tertulis %.2f, hitungan WCAG %.2f: perbaiki angkanya" % (fgn, bgn, stated, real2))

            def verdict(ci):
                if ci is None or ci >= len(cells):
                    return None
                c = cells[ci].upper()
                if "PASS" in c:
                    return True
                if "FAIL" in c:
                    return False
                return None

            vn, vl = verdict(norm_c), verdict(large_c)
            if vn is not None and (real >= 4.5) != vn:
                add(ERROR, 3, ln, "`%s` di atas `%s` rasio %.2f: kolom Normal (4.5) tertulis %s, seharusnya %s" % (fgn, bgn, real2, "PASS" if vn else "FAIL", "PASS" if real >= 4.5 else "FAIL"))
            if vl is not None and (real >= 3.0) != vl:
                add(ERROR, 3, ln, "`%s` di atas `%s` rasio %.2f: kolom Besar/non-teks (3.0) tertulis %s, seharusnya %s" % (fgn, bgn, real2, "PASS" if vl else "FAIL", "PASS" if real >= 3.0 else "FAIL"))


def check_typography(doc, ctx):
    """4. Token tipografi 2.4 ada di @theme."""
    rng = doc.sub_section("2.4")
    if not rng:
        add(WARN, 4, 0, "tidak bisa membaca bagian 2.4 (heading '### 2.4' tidak ditemukan)")
        return
    names = []
    for t in doc.tables_in(rng):
        for ln, cells in t["rows"]:
            m = re.match(r"^`(text-[a-z0-9-]+)`$", cells[0].strip())
            if m:
                names.append((m.group(1), ln))
    if not names:
        add(WARN, 4, rng[0], "tidak bisa membaca bagian 2.4 (tidak ada token `text-*` di tabel)")
        return
    if ctx.stack != "tailwind":
        add(INFO, 4, rng[0], "stack bukan Tailwind: pemeriksaan token tipografi di @theme dilewati")
        return
    if not ctx.css.found:
        add(WARN, 4, rng[0], "tidak bisa membaca bagian 2.8 (blok CSS tidak ditemukan), token tipografi tidak diperiksa")
        return
    for nm, ln in names:
        if nm not in ctx.css.theme:
            add(ERROR, 4, ln, "`%s` ada di tabel 2.4 tapi tidak ada di blok @theme 2.8: tambahkan `--%s: <ukuran>;` dan `--%s--line-height`" % (nm, nm, nm))


def check_dark_safety(doc, ctx):
    """5. Light saja harus mengunci varian dark."""
    s13 = doc.sub_section("1.3")
    t13 = doc.text_of(s13).lower()
    says_light = bool(re.search(r"light saja|hanya light|light only|light-only", t13))
    light_only = says_light or (not ctx.has_dark_col and not ctx.css.has_dark_block)
    if not light_only:
        return
    if ctx.stack == "other":
        add(INFO, 5, 0, "stack non-web: pastikan tema terang dikunci di platform (mis. Flutter `themeMode: ThemeMode.light`, iOS `UIUserInterfaceStyle`), cek manual")
        return
    if not ctx.css.found:
        add(WARN, 5, 0, "dokumen light saja tapi blok CSS 2.8 tidak terbaca: `@custom-variant dark` dan `color-scheme: light` tidak bisa dicek")
        return
    ln = ctx.css.first_line or 0
    if ctx.stack == "css":
        if not ctx.css.has_color_scheme_light:
            add(WARN, 5, ln, "dokumen light saja: tambahkan `color-scheme: light` di `:root` supaya kontrol bawaan browser tidak tampil gelap")
        return
    if not ctx.css.has_custom_variant_dark:
        add(ERROR, 5, ln, "dokumen light saja tapi CSS 2.8 tidak punya `@custom-variant dark (&:is(.dark *));`: kelas `dark:` bawaan shadcn akan aktif saat HP user mode gelap")
    if not ctx.css.has_color_scheme_light:
        add(ERROR, 5, ln, "dokumen light saja tapi CSS 2.8 tidak punya `color-scheme: light` di `:root`: kontrol bawaan browser bisa tampil gelap")


def check_ring(doc, ctx):
    """6. Ring transparan."""
    pat = re.compile(r"(?<![\w-])(?:outline-ring|ring-ring|ring)/\d+")
    cur_table = None
    for i in range(1, doc.n + 1):
        line = doc.lines[i - 1]
        if not pat.search(line):
            continue
        # apakah baris ini bagian tabel dengan kolom 'Default'?
        for t in doc.tables:
            if any(r[0] == i for r in t["rows"]):
                cur_table = t
                break
        else:
            cur_table = None
        for m in pat.finditer(line):
            exempt = False
            if cur_table is not None:
                # tentukan kolom tempat match berada
                col, pos_acc, in_tick = 0, 0, False
                s = line.strip()
                offset = line.index(s)
                p = m.start() - offset
                c = 0
                tick = False
                k = 1 if s.startswith("|") else 0
                idx = k
                while idx < p:
                    ch = s[idx]
                    if ch == "`":
                        tick = not tick
                    elif ch == "|" and not tick:
                        c += 1
                    idx += 1
                col = c
                hdr = cur_table["header"]
                if col < len(hdr) and "default" in hdr[col].lower():
                    exempt = True
            if exempt:
                add(INFO, 6, i, "`%s` disebut sebagai default library (kolom Default), dilewati" % m.group(0))
            else:
                add(ERROR, 6, i, "`%s` adalah ring/outline transparan: rasio di tabel 2.3 dihitung untuk warna penuh, pakai `ring` solid" % m.group(0))


def check_dashes(doc, ctx):
    """7. Em dash / en dash di luar code block."""
    for i in range(1, doc.n + 1):
        if doc.in_code[i]:
            continue
        line = doc.lines[i - 1]
        for ch, nm in (("—", "em dash"), ("–", "en dash")):
            if ch in line:
                add(ERROR, 7, i, "ada %s (%s) di luar code block: ganti dengan titik dua, koma, titik tengah (·), atau kata 'sampai'" % (nm, ch))


HTML_TAGS = set("html head body main nav header footer section article aside div span p a ul ol li br hr img input button label form table tr td th thead tbody h1 h2 h3 h4 h5 h6 meta link script style title svg path select option textarea strong em b i code pre".split())


def check_placeholders(doc, ctx):
    """8. Placeholder template tersisa."""
    for i in range(1, doc.n + 1):
        if doc.in_code[i]:
            continue
        line = doc.lines[i - 1]
        s = re.sub(r"`[^`]*`", "", line)
        hits = []
        for m in re.finditer(r"(?<![\w`])<(?!\s)([^<>\n]*)(>|$)", s):
            inner = m.group(1)
            if not inner or not re.match(r"[A-Za-z./À-ɏ]", inner):
                continue
            hits.append((m.group(0), inner, m.group(2) == ">"))
        for whole, inner, closed in hits:
            tag = re.match(r"/?([A-Za-z0-9]+)", inner)
            if closed and tag and tag.group(1).lower() in HTML_TAGS and not re.search(r"\s[^=]+\s", " " + inner.split(" ", 1)[-1] if " " in inner else ""):
                add(WARN, 8, i, "tag HTML %s di luar backtick: bungkus dengan backtick supaya tidak terbaca sebagai placeholder" % whole)
            else:
                add(ERROR, 8, i, "placeholder template tersisa: %s : ganti dengan isi nyata" % (whole if len(whole) < 60 else whole[:57] + "..."))


def check_structure(doc, ctx):
    """9. Sembilan bagian utama berurutan."""
    found = {}
    for ln, lvl, txt in doc.headings:
        if lvl == 2:
            m = re.match(r"^(\d+)\.", txt)
            if m:
                n = int(m.group(1))
                found.setdefault(n, ln)
    for n in range(1, 10):
        if n not in found:
            add(ERROR, 9, 0, "bagian utama '## %d.' tidak ada: tambahkan sesuai template" % n)
    present = [(found[n], n) for n in sorted(found) if 1 <= n <= 9]
    prev = 0
    for ln, n in sorted(present):
        if n < prev:
            add(ERROR, 9, ln, "bagian '## %d.' muncul setelah bagian %d: urutan harus 1 sampai 9" % (n, prev))
        prev = max(prev, n)


def check_breakpoints(doc, ctx):
    """10. Breakpoint konsisten dengan 2.5."""
    if ctx.stack == "other":
        add(INFO, 10, 0, "stack non-web: pemeriksaan breakpoint web dilewati (pastikan ukuran perangkat dan safe area di 2.5/4.3 konsisten)")
        return
    rng = doc.sub_section("2.5")
    if not rng:
        add(WARN, 10, 0, "tidak bisa membaca bagian 2.5 (heading '### 2.5' tidak ditemukan)")
        return
    declared = {}
    txt = doc.text_of(rng, skip_code=True)
    for m in re.finditer(r"`(?:sm|md|lg|xl|2xl)`\s*(\d{3,4})", txt):
        declared[int(m.group(1))] = True
    if not declared:
        add(WARN, 10, rng[0], "tidak bisa membaca breakpoint di bagian 2.5 (pola '`sm` 640' tidak ditemukan)")
        return
    ok = set()
    for v in declared:
        ok.update((v, v - 1))
    ignore = set([320, 360, 375, 390, 412, 414, 428, 430])
    kw = re.compile(r"breakpoint|min-width|max-width|ke atas|tablet|desktop|laptop|di bawah", re.I)
    ops = [
        re.compile(r"[≥<>]=?\s*(\d{3,4})\s*px"),
        re.compile(r"di bawah\s+(\d{3,4})\s*px", re.I),
        re.compile(r"(\d{3,4})\s*px\s+ke atas", re.I),
        re.compile(r"(?:min|max)-width\s*:\s*(\d{3,4})\s*px"),
    ]
    rngre = re.compile(r"(\d{3,4})\s*[-–]\s*(\d{3,4})\s*px")
    extra = {}
    for i in range(1, doc.n + 1):
        line = doc.lines[i - 1]
        vals = []
        for o in ops:
            for m in o.finditer(line):
                vals.append(int(m.group(1)))
        if kw.search(line):
            for m in rngre.finditer(line):
                vals.extend((int(m.group(1)), int(m.group(2))))
        for v in vals:
            if v in ok or v in ignore or v < 480:
                continue
            extra.setdefault(v, []).append(i)
    for v in sorted(extra):
        ls = extra[v]
        add(WARN, 10, ls[0], "nilai %dpx dipakai sebagai batas lebar (baris %s) tapi bukan breakpoint di 2.5 (%s): samakan atau tambahkan ke 2.5" % (v, ", ".join(str(x) for x in ls[:6]), ", ".join(str(x) for x in sorted(declared))))


def check_primary(doc, ctx):
    """11. Tombol primary di wireframe: [[ ]] = primary, [ ] = secondary, ( ) = ghost."""
    rng = doc.main_section(5)
    if not rng:
        add(WARN, 11, 0, "tidak bisa membaca bagian 5 (heading '## 5.' tidak ditemukan)")
        return
    wires = [b for b in doc.blocks if rng[0] <= b["start"] < rng[1] and not b["lang"]]
    if not wires:
        add(WARN, 11, rng[0], "tidak ada wireframe (code block tanpa bahasa) di bagian 5")
        return
    total_primary = 0
    any_single = False
    for b in wires:
        body = "\n".join(b["lines"])
        prim = re.findall(r"\[\[[^\[\]\n]+\]\]", body)
        total_primary += len(prim)
        stripped = re.sub(r"\[\[[^\[\]\n]+\]\]", "", body)
        if re.search(r"\[\s*[^\[\]\s][^\[\]\n]*\]", stripped):
            any_single = True
        if len(prim) > 1:
            add(ERROR, 11, b["start"], "wireframe ini punya %d tombol primary `[[ ]]`: aturan komponen 'satu primary per layar', turunkan sisanya jadi `[ ]` atau `( )`" % len(prim))
    if total_primary == 0 and any_single:
        add(WARN, 11, rng[0], "wireframe tidak menandai tombol primary dengan [[ ]]: tandai satu tombol primary per layar dengan `[[ Label ]]`, secondary `[ Label ]`, ghost `( Label )`")
    elif total_primary == 0:
        add(INFO, 11, rng[0], "tidak ada penanda tombol di wireframe; tandai primary `[[ ]]`, secondary `[ ]`, ghost `( )` secara konsisten")
    t = doc.text_of((1, doc.n + 1), skip_code=True)
    if not re.search(r"satu\s+(?:tombol\s+)?(?:primary|aksi utama)", t, re.I):
        add(INFO, 11, 0, "aturan 'satu primary per layar' tidak ditemukan di dokumen; tambahkan di 3.2 Button")


def check_length(doc, ctx):
    """12. Panjang dokumen."""
    n = len(doc.lines)
    if doc.lines and doc.lines[-1] == "":
        n -= 1
    add(INFO, 12, 0, "panjang dokumen %d baris" % n)
    limit = 1000 if ctx.stack == "other" else 900
    if n > limit:
        add(WARN, 12, n, "dokumen %d baris (> %d): pangkas duplikasi lebih dulu (spesifikasi komponen hanya di bagian 3, token hanya di bagian 2, halaman serupa cukup 'sama dengan 5.x')" % (n, limit))


def check_prd(doc, ctx, prd):
    """13. Silang PRD."""
    # (a) route
    s5 = doc.main_section(5)
    heads5 = " \n".join(txt for ln, lvl, txt in doc.headings if s5 and s5[0] < ln < s5[1])
    routes = []
    for t in prd.tables:
        rc = col_index(t["header"], "route")
        if rc is None:
            continue
        for ln, cells in t["rows"]:
            if rc < len(cells):
                for tk in ticks(cells[rc]):
                    if tk.startswith("/"):
                        routes.append((tk, ln))
        break
    if not routes:
        add(WARN, 13, 0, "tidak bisa membaca daftar halaman PRD (kolom Route dengan nilai `/...` tidak ditemukan)")
    for rt, ln in routes:
        if not re.search(r"(?<![\w/\[\]-])%s(?![\w/\[\]-])" % re.escape(rt), heads5):
            add(ERROR, 13, 0, "route PRD `%s` (PRD baris %d) tidak ada di heading bagian 5 DESIGN.md: tambahkan spesifikasi halamannya" % (rt, ln))

    # (b) kode error
    env_names = set()
    for t in prd.tables:
        h0 = t["header"][0].lower() if t["header"] else ""
        if re.search(r"variab|env", h0):
            for ln, cells in t["rows"]:
                for tk in ticks(cells[0]):
                    env_names.add(tk)
    codes = {}
    for i, line in enumerate(prd.lines, 1):
        if prd.in_code[i]:
            continue
        for tk in ticks(line):
            if re.fullmatch(r"[A-Z][A-Z0-9_]{5,}", tk) and tk not in env_names:
                if re.match(r"^(NEXT_PUBLIC_|SUPABASE_|SEND_SMS_|FONNTE_|SHOP_)", tk):
                    continue
                codes.setdefault(tk, i)
    s62 = doc.sub_section("6.2")
    if not s62:
        add(WARN, 13, 0, "tidak bisa membaca bagian 6.2 (heading '### 6.2' tidak ditemukan), kode error PRD tidak dicocokkan")
    else:
        t62 = doc.text_of(s62)
        for code, ln in sorted(codes.items(), key=lambda x: x[1]):
            if not re.search(r"(?<![A-Z0-9_])%s(?![A-Z0-9_])" % re.escape(code), t62):
                add(ERROR, 13, s62[0], "kode error PRD `%s` (PRD baris %d) tidak ada di 6.2: tambahkan pesan untuk user" % (code, ln))

    # (c) status dari stateDiagram-v2
    states = {}
    for b in prd.blocks:
        if b["lang"].lower() != "mermaid":
            continue
        if not any("stateDiagram" in l for l in b["lines"]):
            continue
        for k, l in enumerate(b["lines"]):
            if "-->" not in l:
                continue
            left, right = l.split("-->", 1)
            right = right.split(":", 1)[0]
            for part in (left, right):
                nm = part.strip()
                if nm and nm != "[*]" and re.fullmatch(r"[A-Za-z_][\w]*", nm):
                    states.setdefault(nm, b["start"] + 1 + k)
    s22 = doc.sub_section("2.2")
    if not states:
        add(WARN, 13, 0, "tidak bisa membaca status PRD (blok stateDiagram-v2 tidak ditemukan)")
    elif not s22:
        add(WARN, 13, 0, "tidak bisa membaca bagian 2.2 (heading '### 2.2' tidak ditemukan), status PRD tidak dicocokkan")
    else:
        t22 = doc.text_of(s22)
        for st, ln in sorted(states.items(), key=lambda x: x[1]):
            if not re.search(r"(?<![\w])%s(?![\w])" % re.escape(st), t22):
                add(ERROR, 13, s22[0], "status PRD `%s` (PRD baris %d) tidak ada di 2.2: tambahkan badge-nya" % (st, ln))


def check_components(doc, ctx):
    """14. Komponen 3.1 dipakai di bagian 5."""
    rng = doc.sub_section("3.1")
    s5 = doc.main_section(5)
    if not rng or not s5:
        add(WARN, 14, 0, "tidak bisa membaca bagian 3.1 atau 5 untuk pemeriksaan cakupan komponen")
        return
    tabs = doc.tables_in(rng)
    if not tabs:
        add(WARN, 14, rng[0], "tidak bisa membaca bagian 3.1 (tabel komponen tidak ditemukan)")
        return
    t5 = doc.text_of(s5)
    for ln, cells in tabs[0]["rows"]:
        raw = re.sub(r"\([^)]*\)", "", cells[0])
        for nm in re.split(r"[,/]", raw):
            nm = nm.strip().strip("`").strip()
            if not nm or not re.match(r"^[A-Za-z][A-Za-z0-9]*$", nm):
                continue
            if not re.search(r"(?<![A-Za-z0-9])%s(?![A-Za-z0-9])" % re.escape(nm), t5):
                add(WARN, 14, ln, "komponen `%s` ada di daftar 3.1 tapi tidak disebut di bagian 5: pakai di halaman atau hapus dari daftar" % nm)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

CHECKS = [
    (1, "Token tabel vs CSS", check_tokens),
    (2, "Hex di luar bagian 2", check_hex_outside),
    (3, "Kontras 2.3", check_contrast),
    (4, "Token tipografi", check_typography),
    (5, "Keamanan dark mode", check_dark_safety),
    (6, "Focus ring transparan", check_ring),
    (7, "Tanda baca (dash)", check_dashes),
    (8, "Placeholder", check_placeholders),
    (9, "Struktur bagian", check_structure),
    (10, "Breakpoint", check_breakpoints),
    (11, "Tombol primary", check_primary),
    (12, "Panjang dokumen", check_length),
    (14, "Cakupan komponen", check_components),
]

CHECK_NAMES = dict((n, nm) for n, nm, _ in CHECKS)
CHECK_NAMES[13] = "Silang PRD"
CHECK_NAMES[0] = "Stack"


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main(argv=None):
    ap = argparse.ArgumentParser(description="Lint DESIGN.md hasil design-maker")
    ap.add_argument("design", help="path DESIGN.md")
    ap.add_argument("--prd", help="path PRD.md untuk pemeriksaan silang")
    ap.add_argument("--stack", default="auto", choices=["auto", "tailwind", "css", "other"],
                    help="stack implementasi token (default: tebak dari blok kode 2.8)")
    args = ap.parse_args(argv)

    try:
        doc = Doc(read(args.design))
    except Exception as e:  # noqa
        print("ERROR: tidak bisa membuka %s: %s" % (args.design, e))
        return 1

    ctx = Ctx()
    ctx.css = CssInfo()
    ctx.light, ctx.dark, ctx.has_dark_col = {}, {}, False
    ctx.stack = args.stack
    try:
        parse_tokens_table(doc, ctx)
    except Exception as e:  # noqa
        add(WARN, 1, 0, "tidak bisa membaca bagian 2.1 (%s)" % e)
    try:
        ctx.css = parse_css(doc, doc.sub_section("2.8"))
    except Exception as e:  # noqa
        add(WARN, 1, 0, "tidak bisa membaca bagian 2.8 (%s)" % e)

    ctx.stack = detect_stack(doc, ctx)
    add(INFO, 0, 0, "stack terdeteksi: %s" % ctx.stack)
    ctx.quick = bool(re.search(r"draf cepat", "\n".join(doc.lines[:40]), re.I))
    if ctx.quick:
        add(INFO, 0, 0, "dokumen bertanda Draf cepat: pemeriksaan bagian 4 sampai 9 (breakpoint, komponen dipakai di halaman) diturunkan jadi INFO")
    for num, nm, fn in CHECKS:
        try:
            fn(doc, ctx)
        except Exception as e:  # noqa
            add(WARN, num, 0, "tidak bisa membaca bagian untuk pemeriksaan '%s' (%s: %s)" % (nm, type(e).__name__, e))

    if args.prd:
        try:
            prd = Doc(read(args.prd))
            check_prd(doc, ctx, prd)
        except Exception as e:  # noqa
            add(WARN, 13, 0, "tidak bisa membaca PRD atau bagian terkait (%s: %s)" % (type(e).__name__, e))
    else:
        add(INFO, 13, 0, "pemeriksaan silang PRD dilewati (jalankan dengan --prd PRD.md untuk route, kode error, dan status)")

    if getattr(ctx, "quick", False):
        for i, (sev, chk, ln, msg) in enumerate(findings):
            if chk in (10, 13, 14) and sev in (WARN, ERROR):
                findings[i] = (INFO, chk, ln, "[draf cepat] " + msg)

    counts = {ERROR: 0, WARN: 0, INFO: 0}
    print("Lint %s%s" % (args.design, " (PRD: %s)" % args.prd if args.prd else ""))
    for sev in (ERROR, WARN, INFO):
        items = sorted([f for f in findings if f[0] == sev], key=lambda f: (f[1], f[2]))
        counts[sev] = len(items)
        if not items:
            continue
        print("\n== %s (%d) ==" % (sev, len(items)))
        for _, chk, ln, msg in items:
            loc = "baris %d" % ln if ln else "-"
            print("  [C%d %s] %s: %s" % (chk, CHECK_NAMES.get(chk, ""), loc, msg))
    print("\nRingkasan: %d ERROR, %d WARN, %d INFO" % (counts[ERROR], counts[WARN], counts[INFO]))
    return 1 if counts[ERROR] else 0


if __name__ == "__main__":
    sys.exit(main())
