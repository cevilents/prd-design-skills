#!/usr/bin/env python3
"""Bandingkan screenshot hasil build dengan screenshot layar yang sama di design-preview.html.

Pemakaian:
    python3 compare-screens.py built.png reference.png --out diff.png [--threshold 0.15]

Langkah: gambar referensi diubah lebarnya ke lebar built (rasio dijaga), kedua gambar
dipotong ke tinggi terpendek, lalu dibuat komposit "built | reference | diff" (diff =
built keabu-abuan dengan lapisan panas merah di piksel yang berbeda).

Metrik yang dicetak:
  - selisih absolut rata-rata per piksel (0 sampai 1)
  - persentase piksel yang berbeda lebih dari 10%
  - 6 warna dominan tiap gambar (kuantisasi ember + pengelompokan seperti extract-palette.py
    di design-maker) dan kecocokan warna dominan referensi di build
  - cek regional: kedua gambar dibagi grid (kolom dan baris menyesuaikan ukuran, sekitar 150px per
    petak); tiap petak dihitung kepadatan konten (porsi piksel bertepi tajam). Petak yang berisi konten
    di satu gambar tapi hampir polos di gambar lain ditandai "blok konten hilang/berlebih"; selisih
    kepadatan >= 35% ditandai "konten berkurang/bertambah"; petak
    dengan selisih besar ditandai "beda besar". Petak bertanda dicetak (baris/kolom + kotak piksel)
    dan diberi garis merah (konten) atau oranye (selisih) di komposit
  - verdict: "mirip", "berbeda sedang", atau "berbeda jauh" = yang terburuk antara global dan regional

Verdict global: persentase piksel berbeda <= threshold dan selisih rata-rata <= 0.06 -> mirip;
sampai 2x threshold -> berbeda sedang; selebihnya berbeda jauh. Bila jarak rata-rata (berbobot porsi) warna
dominan referensi ke warna terdekat di build > 48 (skala RGB 0 sampai 441), verdict turun satu tingkat.
Verdict regional: ada petak konten hilang/berlebih -> minimal berbeda sedang; petak konten
>= 15% dari semua petak, atau petak bertanda > 2x threshold -> berbeda jauh; petak bertanda > threshold
-> berbeda sedang.

CATATAN: selisih piksel hanyalah sinyal kasar. Data sungguhan vs data contoh, panjang teks,
font yang belum termuat, animasi di tengah jalan, dan pergeseran layout beberapa piksel semuanya
menaikkan selisih. Penilaian utama tetap tinjauan visual atas komposit (lihat gambarnya,
cari beda komposisi, ukuran, spasi, warna, dan hierarki), bukan angkanya.

Butuh Pillow. Python 3.9, pustaka standar + Pillow.
"""
import argparse
import colorsys
import sys

try:
    from PIL import Image, ImageChops, ImageDraw, ImageFilter
except ImportError:
    sys.exit("Pillow belum terpasang. Pasang dengan: python3 -m pip install --user pillow")

DIFF_PIXEL = 0.10  # piksel dianggap berbeda bila selisih kanal terbesar > 10%
MEAN_OK = 0.06
PALETTE_BAD = 48
MAX_COMPOSITE_W = 4200
TILE_PX = 150  # ukuran petak target untuk cek regional
EDGE_LEVEL = 8  # selisih luminans tetangga yang dihitung sebagai tepi
CONTENT_MIN = 0.02  # kepadatan tepi minimal untuk dianggap "berisi konten"
FLAT_MAX = 0.004  # kepadatan tepi maksimal untuk dianggap "hampir polos"
DENSE_MIN = 0.05  # kepadatan minimal agar aturan "konten berkurang/bertambah" berlaku (hindari noise anti-aliasing teks kecil)
DENSITY_DROP = 0.35  # selisih kepadatan tepi >= 35% dari yang lebih padat = konten sebagian hilang/bertambah
TILE_DIFF_PCT = 0.5  # petak dengan > 50% piksel berbeda > 10% ditandai "beda besar"


def load(path):
    try:
        img = Image.open(path)
        img.load()
    except Exception as e:
        sys.exit("Gagal membuka %s: %s" % (path, e))
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(bg, img)
    return img.convert("RGB")


# --- palet (disarikan dari extract-palette.py) -------------------------------

MERGE_DISTANCE = 12
CHROMA_DEDUPE_DISTANCE = 36


def label(rgb):
    r, g, b = (c / 255 for c in rgb)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    if s < 0.12 or l < 0.06 or l > 0.96:
        return "netral"
    return "berwarna"


def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5


def palette(img, n=6):
    im = img.copy()
    im.thumbnail((400, 400), Image.NEAREST)
    buckets = {}
    for p in im.getdata():
        b = buckets.setdefault((p[0] >> 2, p[1] >> 2, p[2] >> 2), {})
        b[p] = b.get(p, 0) + 1
    counts = {max(b, key=b.get): sum(b.values()) for b in buckets.values()}
    total = sum(counts.values())
    clusters = []
    for rgb, c in sorted(counts.items(), key=lambda kv: -kv[1])[:4000]:
        for cl in clusters:
            if dist(rgb, cl[0]) <= MERGE_DISTANCE:
                cl[1] += c
                break
        else:
            clusters.append([rgb, c])
    clusters.sort(key=lambda cl: -cl[1])
    deduped = []
    for rgb, c in clusters:
        if label(rgb) == "berwarna":
            for cl in deduped:
                if label(cl[0]) == "berwarna" and dist(rgb, cl[0]) <= CHROMA_DEDUPE_DISTANCE:
                    cl[1] += c
                    break
            else:
                deduped.append([rgb, c])
        else:
            deduped.append([rgb, c])
    deduped.sort(key=lambda cl: -cl[1])
    return [(rgb, c / total) for rgb, c in deduped[:n]]


def hx(rgb):
    return "#%02X%02X%02X" % tuple(rgb)


# --- cek regional ------------------------------------------------------------

def edge_map(img):
    """Gambar biner: 255 di piksel yang luminansnya beda tajam dari tetangga kanan atau bawah."""
    g = img.convert("L").filter(ImageFilter.GaussianBlur(1))  # samakan ketajaman (referensi hasil skala lebih lembut)
    gx = ImageChops.difference(g, ImageChops.offset(g, 1, 0))
    gy = ImageChops.difference(g, ImageChops.offset(g, 0, 1))
    return ImageChops.lighter(gx, gy).point(lambda v: 255 if v > EDGE_LEVEL else 0)


def density(edges, box):
    t = edges.crop(box)
    return t.histogram()[255] / float(max(1, t.width * t.height))


def regional(built, ref, diff_max):
    w, h = built.size
    cols = max(2, min(10, round(w / TILE_PX)))
    rows = max(2, min(14, round(h / TILE_PX)))
    eb, er = edge_map(built), edge_map(ref)
    flags = []
    for r in range(rows):
        for c in range(cols):
            box = (c * w // cols, r * h // rows, (c + 1) * w // cols, (r + 1) * h // rows)
            if box[2] - box[0] < 16 or box[3] - box[1] < 16:
                continue
            db, dr = density(eb, box), density(er, box)
            hi, lo = max(db, dr), min(db, dr)
            kind = None
            if hi >= CONTENT_MIN and lo <= max(FLAT_MAX, hi * 0.15):
                kind = "blok konten hilang di build" if db < dr else "blok konten berlebih di build"
            elif hi >= DENSE_MIN and hi - lo >= hi * DENSITY_DROP:
                kind = "konten berkurang di build" if db < dr else "konten bertambah di build"
            else:
                t = diff_max.crop(box)
                over = sum(t.histogram()[int(DIFF_PIXEL * 255) + 1:]) / float((box[2] - box[0]) * (box[3] - box[1]))
                if over > TILE_DIFF_PCT:
                    kind = "beda besar (%.0f%% piksel)" % (over * 100)
            if kind:
                flags.append({"row": r + 1, "col": c + 1, "box": box, "kind": kind,
                              "content": kind.startswith(("blok", "konten")), "db": db, "dr": dr})
    return flags, rows, cols


# --- komposit ----------------------------------------------------------------

def make_composite(built, ref, diff_max, flags=()):
    w, h = built.size
    gray = built.convert("L").convert("RGB")
    base = Image.blend(gray, Image.new("RGB", (w, h), (255, 255, 255)), 0.55)
    mask = diff_max.point(lambda v: 0 if v < 26 else min(255, 90 + v))
    heat = Image.composite(Image.new("RGB", (w, h), (255, 40, 40)), base, mask)
    gap, head = 12, 28
    canvas = Image.new("RGB", (w * 3 + gap * 2, h + head), (30, 30, 34))
    d = ImageDraw.Draw(canvas)
    for i, (name, im) in enumerate((("built", built), ("reference", ref), ("diff (merah = beda)", heat))):
        x = i * (w + gap)
        canvas.paste(im, (x, head))
        d.text((x + 8, 8), name, fill=(240, 240, 240))
        for f in flags:
            x0, y0, x1, y1 = f["box"]
            color = (255, 0, 0) if f["content"] else (255, 140, 0)
            d.rectangle((x + x0, head + y0, x + x1 - 1, head + y1 - 1), outline=color, width=3)
            d.text((x + x0 + 6, head + y0 + 5), "%d,%d" % (f["row"], f["col"]), fill=color)
    if canvas.width > MAX_COMPOSITE_W:
        k = MAX_COMPOSITE_W / canvas.width
        canvas = canvas.resize((MAX_COMPOSITE_W, max(1, int(canvas.height * k))), Image.LANCZOS)
    return canvas


def main():
    ap = argparse.ArgumentParser(description="Bandingkan screenshot build dengan referensi.")
    ap.add_argument("built")
    ap.add_argument("reference")
    ap.add_argument("--out", required=True, help="file PNG komposit")
    ap.add_argument("--threshold", type=float, default=0.15,
                    help="porsi piksel berbeda yang masih dianggap 'mirip' (default 0.15)")
    a = ap.parse_args()

    built, ref = load(a.built), load(a.reference)
    w = built.width
    new_h = max(1, round(ref.height * w / ref.width))
    ref_r = ref.resize((w, new_h), Image.LANCZOS)
    h = min(built.height, new_h)
    notes = []
    if abs(built.height - new_h) / max(built.height, new_h) > 0.25:
        notes.append("tinggi berbeda jauh (built %dpx, referensi %dpx setelah diskala): dibandingkan hanya %dpx teratas; "
                     "kemungkinan beda panjang halaman atau screenshot bukan layar yang sama" % (built.height, new_h, h))
    built_c, ref_c = built.crop((0, 0, w, h)), ref_r.crop((0, 0, w, h))

    diff = ImageChops.difference(built_c, ref_c)
    r, g, b = diff.split()
    diff_max = ImageChops.lighter(ImageChops.lighter(r, g), b)
    npx = w * h
    hist = diff_max.histogram()
    over = sum(hist[int(DIFF_PIXEL * 255) + 1:])
    mean = sum(sum(i * c for i, c in enumerate(ch.histogram())) for ch in (r, g, b)) / (3 * npx * 255.0)
    pct = over / npx

    flags, rows, cols = regional(built_c, ref_c, diff_max)
    comp = make_composite(built_c, ref_c, diff_max, flags)
    comp.save(a.out)

    pb, pr = palette(built_c), palette(ref_c)
    print("Ukuran dibandingkan : %d x %d px (built %dx%d, referensi %dx%d -> %dx%d)" % (
        w, h, built.width, built.height, ref.width, ref.height, w, new_h))
    print("Selisih rata-rata   : %.4f (0 sampai 1)" % mean)
    print("Piksel beda > 10%%   : %.1f%%" % (pct * 100))
    for title, pal in (("Warna dominan built    ", pb), ("Warna dominan referensi", pr)):
        print("%s: %s" % (title, "  ".join("%s %.0f%%" % (hx(c), s * 100) for c, s in pal)))
    wsum, dsum, missing = 0.0, 0.0, []
    for c, s in pr:
        dn = min(dist(c, c2) for c2, _ in pb)
        wsum += s
        dsum += s * dn
        if dn > 24 and s >= 0.01:
            missing.append("%s (%.0f%%, terdekat di build jarak %.0f)" % (hx(c), s * 100, dn))
    avg = dsum / wsum if wsum else 0
    print("Jarak palet (berbobot porsi): %.1f (warna referensi ke warna terdekat di build; >%d = palet bergeser)" % (avg, PALETTE_BAD))
    if missing:
        print("Warna referensi tanpa padanan di build: " + "; ".join(missing))
    for n in notes:
        print("CATATAN: " + n)

    levels = ["mirip", "berbeda sedang", "berbeda jauh"]
    lv = 0 if (pct <= a.threshold and mean <= MEAN_OK) else 1 if pct <= 2 * a.threshold else 2
    if avg > PALETTE_BAD:
        lv = min(2, lv + 1)
    n_tiles = rows * cols
    n_content = sum(1 for f in flags if f["content"])
    frac = len(flags) / float(n_tiles)
    lv_reg = 2 if (n_content / float(n_tiles) >= 0.15 or frac > 2 * a.threshold) else \
        1 if (n_content or frac > a.threshold) else 0
    print("Grid regional       : %d baris x %d kolom, %d petak bertanda (%d konten hilang/berlebih)" % (
        rows, cols, len(flags), n_content))
    for f in flags:
        print("  petak baris %d kolom %d  kotak x %d-%d y %d-%d : %s" % (
            f["row"], f["col"], f["box"][0], f["box"][2], f["box"][1], f["box"][3], f["kind"]))
    print("Verdict global      : %s | regional: %s" % (levels[lv], levels[lv_reg]))
    lv = max(lv, lv_reg)
    print("Komposit            : %s" % a.out)
    print("VERDICT: %s" % levels[lv])
    print("(sinyal kasar; nilai komposit dengan mata sebelum memutuskan)")


if __name__ == "__main__":
    main()
