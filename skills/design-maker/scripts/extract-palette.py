#!/usr/bin/env python3
"""Ambil warna dominan dari gambar referensi (logo, screenshot, foto).

Pemakaian:
    python3 extract-palette.py <gambar> [<gambar> ...] [--colors N]

Output per gambar: daftar warna (hex), porsi piksel, dan label kasar
(netral / gelap / terang / berwarna). Piksel transparan diabaikan.
Format: PNG, JPG, WebP, GIF, HEIC/HEIF (dikonversi lewat `sips` di macOS),
dan SVG (hex dibaca dari kode SVG, porsi = jumlah kemunculan).
Butuh Pillow untuk gambar raster; kalau tidak ada, script memberi tahu cara memasangnya.
"""
import colorsys
import os
import re
import subprocess
import sys
import tempfile

try:
    from PIL import Image
except ImportError:
    sys.exit(
        "Pillow belum terpasang. Pasang dengan: python3 -m pip install --user pillow\n"
        "Atau perkirakan warna dari gambar secara visual dan tandai sebagai 'perkiraan' di DESIGN.md."
    )


def label(rgb):
    r, g, b = (c / 255 for c in rgb)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    if s < 0.12 or l < 0.06 or l > 0.96:
        if l > 0.9:
            return "netral terang"
        if l < 0.15:
            return "netral gelap"
        return "netral"
    return "berwarna gelap" if l < 0.35 else ("berwarna terang" if l > 0.75 else "berwarna")


MERGE_DISTANCE = 12  # jarak RGB; warna lebih dekat dari ini dianggap satu warna (krem vs putih tetap terpisah)
MAX_BUCKETS = 4000  # hanya ember terbanyak yang dikelompokkan, supaya foto besar tetap cepat
MIN_ACCENT_SHARE = 0.002  # warna berwarna sekecil 0.2% tetap dilaporkan sebagai aksen
CHROMA_DEDUPE_DISTANCE = 36  # di hasil akhir, varian warna berwarna yang mirip (umum di foto) digabung


def open_image(path):
    ext = os.path.splitext(path)[1].lower()
    if ext in (".heic", ".heif"):
        # Pillow tidak membaca HEIC tanpa plugin; di macOS konversi dulu dengan sips
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "converted.png")
            subprocess.run(["sips", "-s", "format", "png", path, "--out", out],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            img = Image.open(out)
            img.load()  # baca ke memori sebelum folder sementara dihapus
            return img
    return Image.open(path)


def svg_palette(path, n):
    text = open(path, encoding="utf-8", errors="ignore").read()
    counts = {}
    for m in re.finditer(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", text):
        h = m.group(1)
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
        counts[rgb] = counts.get(rgb, 0) + 1
    for m in re.finditer(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", text):
        rgb = tuple(min(255, int(v)) for v in m.groups())
        counts[rgb] = counts.get(rgb, 0) + 1
    total = sum(counts.values())
    ranked = sorted(counts.items(), key=lambda kv: -kv[1])[:n]
    return [("#%02X%02X%02X" % rgb, c / total, label(rgb)) for rgb, c in ranked]


def palette(path, n):
    if path.lower().endswith(".svg"):
        return svg_palette(path, n)
    img = open_image(path).convert("RGBA")
    # NEAREST supaya warna tidak tercampur saat diperkecil; hex yang dilaporkan tetap warna asli
    img.thumbnail((400, 400), Image.NEAREST)
    # Ember 6-bit per kanal supaya foto dengan ratusan ribu warna unik tetap cepat;
    # tiap ember diwakili warna persis yang paling sering muncul di dalamnya.
    buckets = {}
    for p in img.getdata():
        if p[3] >= 128:
            rgb = p[:3]
            b = buckets.setdefault((rgb[0] >> 2, rgb[1] >> 2, rgb[2] >> 2), {})
            b[rgb] = b.get(rgb, 0) + 1
    counts = {}
    for b in buckets.values():
        rep = max(b, key=b.get)
        counts[rep] = sum(b.values())
    total = sum(counts.values())
    if not total:
        return []
    # Kelompokkan warna mirip (anti-aliasing, kompresi JPEG); wakil = warna paling sering di kelompok
    clusters = []  # [wakil_rgb, jumlah]
    for rgb, c in sorted(counts.items(), key=lambda kv: -kv[1])[:MAX_BUCKETS]:
        for cl in clusters:
            if sum((a - b) ** 2 for a, b in zip(rgb, cl[0])) <= MERGE_DISTANCE ** 2:
                cl[1] += c
                break
        else:
            clusters.append([rgb, c])
    clusters.sort(key=lambda cl: -cl[1])
    # Gabungkan varian warna berwarna yang mirip (gradasi di foto); netral tidak disentuh
    # supaya beda tipis seperti krem vs putih tetap terlihat.
    deduped = []
    for rgb, c in clusters:
        if label(rgb).startswith("berwarna"):
            for cl in deduped:
                if label(cl[0]).startswith("berwarna") and \
                        sum((a - b) ** 2 for a, b in zip(rgb, cl[0])) <= CHROMA_DEDUPE_DISTANCE ** 2:
                    cl[1] += c
                    break
            else:
                deduped.append([rgb, c])
        else:
            deduped.append([rgb, c])
    clusters = sorted(deduped, key=lambda cl: -cl[1])
    main = clusters[:n]
    accents = [cl for cl in clusters[n:]
               if cl[1] / total >= MIN_ACCENT_SHARE and label(cl[0]).startswith("berwarna")][:4]
    out = []
    for rgb, c in main + accents:
        out.append(("#%02X%02X%02X" % rgb, c / total, label(rgb)))
    return out


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    n = 8
    paths = []
    i = 0
    while i < len(argv):
        if argv[i] == "--colors":
            if i + 1 >= len(argv) or not argv[i + 1].isdigit() or int(argv[i + 1]) < 1:
                sys.exit("--colors butuh angka bulat positif, mis. --colors 6")
            n = int(argv[i + 1])
            i += 2
            continue
        paths.append(argv[i])
        i += 1
    if not paths:
        sys.exit(__doc__)
    failed = 0
    for path in paths:
        try:
            colors = palette(path, n)
        except Exception as e:  # file rusak / format tidak didukung
            print("%s: gagal dibaca (%s)" % (path, e))
            failed += 1
            continue
        print("== %s" % path)
        if not colors:
            print("  (semua piksel transparan)")
        for hex_, share, lab in colors:
            print("  %s  %5.1f%%  %s" % (hex_, share * 100, lab))
    if failed == len(paths):
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
