#!/usr/bin/env python3
"""Hitung rasio kontras WCAG 2.x antara dua warna hex.

Pemakaian:
    python3 contrast-check.py "#FFFFFF" "#1F2937"
    python3 contrast-check.py --selftest

Output: rasio dan verdict untuk teks normal (4.5), teks besar dan elemen
non-teks (3.0). Hanya pustaka standar Python 3.
"""
import re
import sys


def parse_hex(value):
    v = value.strip().lstrip("#")
    if not re.fullmatch(r"[0-9a-fA-F]{3}|[0-9a-fA-F]{6}", v):
        raise ValueError("bukan warna hex: %r" % value)
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    return tuple(int(v[i:i + 2], 16) / 255 for i in (0, 2, 4))


def luminance(rgb):
    def lin(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = luminance(parse_hex(a)), luminance(parse_hex(b))
    hi, lo = max(la, lb), min(la, lb)
    return round((hi + 0.05) / (lo + 0.05), 2)


def selftest():
    assert ratio("#000000", "#FFFFFF") == 21.0
    assert ratio("#FFFFFF", "#777777") == 4.48
    assert ratio("#123", "#112233") == 1.0
    print("selftest OK")


def main(argv):
    if argv == ["--selftest"]:
        selftest()
        return 0
    if len(argv) != 2:
        print(__doc__)
        return 1
    try:
        r = ratio(argv[0], argv[1])
    except ValueError as e:
        print("ERROR: %s" % e)
        return 1
    print("ratio: %.2f:1" % r)
    print("normal text (4.5:1): %s" % ("PASS" if r >= 4.5 else "FAIL"))
    print("large text / non-text (3.0:1): %s" % ("PASS" if r >= 3.0 else "FAIL"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
