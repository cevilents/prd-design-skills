# Visual Craft Playbook: Ekspresif Tanpa Generik

Baca file ini saat merumuskan konsep art direction (langkah 2), menulis token dan motion (template bagian 2.1 sampai 2.8), momen signature (1.6), wireframe layar signature (bagian 5), serta saat membuat `design-concepts.html` dan `design-preview.html`. Tujuannya: DESIGN.md yang membuat orang bilang "wow, keren banget" pada pandangan pertama, tanpa jatuh ke slop yang dilarang `antislop-ui` dan tanpa mengorbankan kecepatan kerja atau aksesibilitas.

Hubungan dengan antislop: antislop melarang **default tanpa alasan**, bukan energi. Setiap resep di bawah punya bagian "Beda dari versi generik". Kalau kamu tidak bisa menulis alasan dari dunia user untuk sebuah efek, buang efeknya. Dial yang disarankan (skala 1 sampai 3; ENERGY = seberapa ramai/berani visualnya, MOTION = seberapa banyak gerak): layar signature ENERGY 3 / MOTION 2 sampai 3; layar kerja ENERGY 1 sampai 2 / MOTION 1 sampai 2. Tulis keputusannya sebagai nilai konkret di DESIGN.md (jangan menulis istilah dial).

**Konvensi CSS:** kelas custom di bawah (`.field-brand`, `.duotone`, `.btn-tactile`, `.glass`, `.ticket`, `.torn`, `.stage`) ditaruh di `@layer components { ... }` supaya utilitas Tailwind bisa menimpanya (mis. responsif); helper murni ditulis `@utility`; aturan elemen (`h1`, `h2`) di `@layer base`. Nilai warna dasar ditulis hex (dibaca `contrast-check.py`); `oklch()` dipakai di dalam gradien, bayangan, dan turunan.

Semua kode: Tailwind v4 (CSS-first, `@theme`), `motion` (`motion/react`), browser modern. API eksperimental ditandai **[EKSPERIMENTAL]** beserta fallback-nya.

---

## 1. Prinsip "wow"

### 1.1 Enam sumber impact pandangan pertama

| Sumber | Artinya | Tes cepat |
|---|---|---|
| Satu konsep | Semua keputusan turun dari satu ide dunia user (mis. "uap setrika", "kertas nota", "papan jadwal stasiun"), bukan daftar efek | Bisa dijelaskan dalam satu kalimat; motif muncul di 3 tempat berbeda |
| Kontras skala | Satu elemen 5 sampai 10 kali lebih besar dari yang lain | Blur mata: masih ada satu bentuk dominan? |
| Komitmen warna | Warna brand menguasai area besar (latar penuh, blok), bukan hanya tombol | Screenshot kecil 120px: warna identitas masih terbaca? |
| Kedalaman & material | Permukaan terasa punya bahan (kertas, kaca, enamel) lewat bayangan berlapis, highlight, grain | Tidak terlihat datar seperti wireframe |
| Koreografi motion | Satu urutan masuk yang terarah, bukan semua elemen bergerak | Mata dituntun ke satu titik, berurutan |
| Detail kerajinan | Angka tabular, kerning, radius konsisten, state hover/press yang dipikirkan | Zoom 200%: tidak ada yang patah atau canggung |

Jangan menumpuk keenamnya di semua layar. Pilih 3 sampai 4 yang paling cocok dengan konsep, jalankan sampai tuntas.

### 1.2 Aturan: wow di momen signature, tenang dan cepat di layar kerja

Intensitas visual berbanding terbalik dengan **frekuensi pakai**.

| Tingkat | Contoh | Boleh | Tidak boleh |
|---|---|---|---|
| Showcase (jarang, emosional) | Layar status untuk pelanggan, login/onboarding, sukses bayar, empty state pertama, pencapaian | Latar penuh warna, display raksasa, grain, motion 600 sampai 1200ms, ilustrasi custom | Menghalangi tombol aksi, memutar ulang animasi tiap buka |
| Kerja harian (puluhan kali/hari) | Daftar order, dashboard owner, form input | Satu motif identitas, tipografi karakter, warna status tegas, motion masuk ≤ 250ms total, hanya saat pertama muat; stagger maks 8 baris pertama | Latar ber-gradien di belakang daftar, shadow tebal per baris, stagger saat refetch/filter/kembali ke daftar |
| Kerja berulang (ratusan kali/hari) | Ketik nominal, toggle, scan, ubah status | Feedback press 80 sampai 120ms, perubahan state instan | Animasi masuk apa pun, delay, spring memantul |

Aturan hitung: **jumlah momen signature mengikuti level ambisi** (aturan isi 14): Spektakuler ≥ 4, Ekspresif 2 sampai 3, Tenang 1 sampai 2 (mis. layar status pelanggan, sukses bayar, login, empty state pertama). Layar kerja membawa **satu motif identitas** (pola, bentuk, atau suara tipografi) dan warna aksen. Tulis di 1.6 di mana tepatnya tiap momen dan di layar mana motif identitas tampil, supaya layar utama role utama tetap punya ciri (aturan isi 12) tanpa jadi lambat. Momen lebih banyak tidak berarti layar kerja lebih ramai: tambahan momen datang dari layar jarang.

### 1.3 Tes ekspresif vs generik (jalankan per efek)

1. **Alasan dunia user:** apa di pekerjaan user yang membenarkan efek ini? ("stempel LUNAS" ya; "glow di kartu" tidak.)
2. **Fungsi:** efek ini memandu mata, memberi kepastian, atau menandai status? Kalau hanya "biar bagus", buang.
3. **Dosis:** dipakai di berapa tempat? Efek yang muncul di lebih dari 2 sampai 3 tempat sudah jadi default.
4. **Biaya:** menghalangi tugas, menurunkan kontras, atau memperlambat perangkat Android kelas menengah? Kalau ya, ada versi lebih murah atau tidak jadi.

---

## 2. Resep teknik

### 2.1 Tipografi display

**Kapan:** judul layar signature, angka utama, nama status, kode order. **Bukan** untuk teks isi, label form, atau tombol kecil.

**Pasangan font** (semua tersedia di Google Fonts, sudah dicek; weight/axis menurut metadata Google Fonts):

| Mood | Display | UI/Body | Catatan |
|---|---|---|---|
| Hangat, ramah, UMKM, makanan, laundry | Bricolage Grotesque (opsz, wdth, 200 sampai 800) | Instrument Sans | Pakai opsz tinggi + 700 sampai 800 untuk karakter; wdth sempit untuk angka besar |
| Hospitality, heritage, editorial | Fraunces (axis SOFT, WONK, opsz) | Hanken Grotesk | Ini selera bawaan model; pilih hanya kalau konsepnya memang editorial/hangat dan tulis alasannya |
| Elegan, fashion, ritual, studio | Instrument Serif (satu weight, regular + italic) | Instrument Sans | Hanya ≥ 32px; italic untuk satu kata penekanan, bukan seluruh judul |
| Futuristik, fintech playful, event | Unbounded (200 sampai 900, lebar) | Onest | Display saja, ≥ 28px; sangat lebar, judul harus pendek |
| Seni, budaya, komunitas, berani | Syne (400 sampai 800) | DM Sans | 700 sampai 800 untuk judul; weight 400 sampai 500 berkarakter sempit, jangan dicampur |
| Logistik, otomotif, olahraga, tegas | Archivo (wdth 62 sampai 125, 100 sampai 900) | Archivo (wdth 100) | Satu keluarga, kontras lewat lebar: judul 62 sampai 75 + 800, isi 100 + 400 |
| Kesehatan, wellness, edukasi modern | Sora (100 sampai 800) | Figtree | 600 untuk judul; jaga rasio agar tidak terlihat generik, kuatkan lewat warna dan bentuk |
| Anak, belajar, ceria | Bagel Fat One atau Gabarito (400 sampai 900) | Rethink Sans | Bagel Fat One hanya angka/judul pendek ≥ 32px |
| Terpercaya, berita, klasik | DM Serif Display (satu weight) | Familjen Grotesk | Serif hanya ≥ 28px; Familjen Grotesk memberi nada manusiawi pada isi |
| Komunitas, koperasi, religi, hangat-buku | Young Serif (satu weight) | Instrument Sans | Berat dan akrab; hindari untuk angka tabel |
| Angka/kode/operasional | Space Grotesk (300 sampai 700) atau JetBrains Mono (100 sampai 800) | (ikut body) | Dua font ini ada di daftar default antislop: pakai hanya untuk angka/kode dengan alasan tertulis ("angka tabular industri") |

Pilih satu baris, jangan campur lintas baris. Maksimal 2 keluarga + 1 mono opsional.

**Loading (Next.js):**
```tsx
// app/layout.tsx
import { Bricolage_Grotesque, Instrument_Sans } from "next/font/google";
const display = Bricolage_Grotesque({
  subsets: ["latin"], variable: "--font-bricolage",
  axes: ["opsz", "wdth"], display: "swap",
});
const sans = Instrument_Sans({ subsets: ["latin"], variable: "--font-instrument", display: "swap" });
// <html className={`${display.variable} ${sans.variable}`}>
```

```css
/* globals.css */
@theme inline {
  --font-display: var(--font-bricolage), "Arial Narrow", sans-serif;
  --font-sans: var(--font-instrument), system-ui, sans-serif;

  /* token fluid: rem + vw agar tetap membesar saat zoom 200% */
  --text-hero: clamp(3.25rem, 1.4rem + 9vw, 8rem);   /* maks ≤ 2.5 x min, lihat guardrail */
  --text-hero--line-height: 0.9;
  --text-hero--letter-spacing: -0.045em;
  --text-hero--font-weight: 800;
  --text-title: clamp(1.75rem, 1.1rem + 3vw, 3rem);
  --text-title--line-height: 1;
  --text-title--letter-spacing: -0.03em;
}
@utility num-xl {
  font-family: var(--font-display); font-size: clamp(3rem, 2rem + 10vw, 7.5rem);
  line-height: 0.8; letter-spacing: -0.06em; font-variant-numeric: tabular-nums lining-nums;
  font-optical-sizing: auto; font-variation-settings: "wdth" 80;
}
@utility balance { text-wrap: balance; }
@layer base { h1, h2 { text-wrap: balance; } }
```
Pakai: `<h1 class="font-display text-hero">`. Angka besar: kecilkan tracking sampai −0.04 sampai −0.06em dan `line-height: 0.8 sampai 0.9`; luruskan tepi optik dengan `-ml-[0.05em]`. **[EKSPERIMENTAL]** `text-box: trim-both cap alphabetic` merapatkan kotak teks ke tinggi huruf (Chrome 133+, Safari 18.2+); bungkus dengan `@supports (text-box: trim-both cap alphabetic)`, fallback `line-height` di atas.

**Guardrail:** display font hanya di ukuran yang dirancang (lihat catatan tabel); isi dan label tetap font body ≥ 16px; `clamp()` harus punya lantai dan langit-langit `rem` dengan **maks ≤ 2.5 x min** dan komponen `rem` yang dominan (vw yang dominan tidak ikut membesar saat zoom, karena zoom browser mengecilkan lebar viewport; WCAG 1.4.4); **angka besar harus muat di 328px**: lebar angka tabular ≈ jumlah karakter x 0.5em x (1 − tracking), jadi "Rp86.000" (8 karakter) ≈ 4em dan font ≤ 82px di 360px; `num-xl` di atas jatuh ke ±68px di 360px; ukur di preview (`scrollWidth`), jangan dikira-kira, dan sesuaikan clamp per jumlah digit terpanjang; panjang judul diuji di 360px tanpa overflow (`overflow-wrap: anywhere` sebagai jaring pengaman); preload hanya weight yang dipakai; `font-display: swap`.
**Beda dari generik:** judul besar dengan font bawaan di tengah halaman. Di sini: skala 5 sampai 10 kali, tracking dan line-height diatur, angka punya perlakuan sendiri, dan pasangan font dipilih dari mood user, bukan roster default.

### 2.2 Komitmen warna

**Kapan:** layar signature dan satu blok warna di layar kerja (header, kartu ringkasan utama). Aturan palet SKILL.md (aturan isi 1): 1 primary + netral bertinta + 1 sampai 2 warna hero/aksen dari konsep. "Komitmen" artinya **luas area dan kejenuhan**, bukan menambah hue di luar keluarga konsep.

**Ramp OKLCH di Tailwind v4:**
```css
@theme {
  /* ramp primary: hue bergeser hangat di bagian terang, lebih merah di gelap.
     Hex = hasil konversi dari oklch(L C H) di komentar, supaya bisa dicek script kontras. */
  --color-brand-100: #FBEDD1;  /* oklch(0.95 0.04 85) */
  --color-brand-300: #FDB862;  /* oklch(0.83 0.13 70) */
  --color-brand-500: #F3680F;  /* oklch(0.68 0.19 45) */
  --color-brand-700: #A03317;  /* oklch(0.48 0.15 35) */
  --color-brand-900: #451913;  /* oklch(0.28 0.07 30) */
  --color-ink:       #22110B;  /* netral bertinta rona brand, bukan abu murni */
  --color-paper:     #F9F5EC;
}
```
Kontras yang dipakai di resep (diukur dengan `python3 <SKILL_DIR>/scripts/contrast-check.py "#F9F5EC" "#A03317"` dan seterusnya): paper di atas brand-700 6.48 · ink di atas brand-500 5.90 · ink di atas brand-300 10.59 · paper di atas brand-900 13.77 · **paper di atas brand-500 hanya 2.84 (gagal)**. Ulangi pengukuran untuk setiap ramp baru. Chroma > ~0.2 melampaui sRGB di banyak hue dan akan terpotong saat dikonversi ke hex. Mau lebih menyala di layar P3: `@media (color-gamut: p3) { :root { --color-brand-500: oklch(0.7 0.22 45); } }` (kontras diukur dari hex dasar, pastikan versi P3 tidak lebih rendah). Turunan cepat: `bg-brand-500/20` (Tailwind memakai `color-mix`), atau relative color `oklch(from var(--color-brand-500) calc(l - 0.1) c h)`.

**a) Latar penuh:** `<main class="min-h-dvh bg-brand-700 text-paper">` (6.48) atau latar terang `bg-brand-500 text-ink` (5.90). Tombol utama di atas `brand-700` dibalik (`bg-paper text-brand-900`, 13.77). Sinkronkan UI browser: `<meta name="theme-color" content="#...">` per status.

**b) Gradient mesh dari ramp brand** (bukan biru ke ungu): beberapa `radial-gradient` bertitik asal berbeda, semua dari ramp token.
```css
.field-brand {
  background:
    radial-gradient(60% 50% at 10% 5%,  var(--color-brand-300) 0%, transparent 70%),
    radial-gradient(55% 45% at 95% 20%, var(--color-brand-500) 0%, transparent 72%),
    radial-gradient(80% 60% at 60% 105%, var(--color-brand-900) 0%, transparent 75%),
    var(--color-brand-700);
}
```
Aturan: hue tetap dalam ±40° dari brand; lightness tersebar ≥ 0.3 antar titik; statis (jangan dianimasikan; gradien beranimasi repaint terus); beri grain (2.3) agar tidak terlihat plastik; teks besar di atasnya diperiksa di titik **terburuk** (stop paling terang di belakang teks), atau letakkan teks di atas pelat solid. Beda dari generik: bukan "orb blur di belakang hero"; titik terang diletakkan menjauh dari teks utama dan mengikuti komposisi layar, bukan dekorasi acak.

**c) Duotone untuk foto/ilustrasi:** dua warna dari token, foto jadi bagian identitas.
```css
.duotone { position: relative; isolation: isolate; background: var(--color-paper); }
.duotone img { display: block; width: 100%; filter: grayscale(1) contrast(1.1); mix-blend-mode: multiply; }
.duotone::after { content: ""; position: absolute; inset: 0; background: var(--color-brand-700);
  mix-blend-mode: lighten; pointer-events: none; }
```
Guardrail: foto bermakna (bukti nyata) jangan di-duotone; pakai untuk dekorasi hero.

**d) Warna per status sebagai latar imersif** (layar pelanggan):
```css
.stage { background: var(--stage-bg); color: var(--stage-fg);
  transition: background-color .6s var(--ease-out-expo), color .6s var(--ease-out-expo); }
.stage[data-status="diterima"] { --stage-bg: #EBBD57; --stage-fg: #281606; }  /* 9.89 */
.stage[data-status="dicuci"]   { --stage-bg: #007083; --stage-fg: #F1FAFD; }  /* 5.44 */
.stage[data-status="siap"]     { --stage-bg: #246E3A; --stage-fg: #F4FAF5; }  /* 5.89 */
```
Status **tidak boleh** dibedakan hanya lewat warna: kata status raksasa + ikon/ilustrasi + posisi stepper tetap ada. Rasio di komentar sudah diukur dengan `contrast-check.py`; ukur ulang untuk status dan warna milik aplikasimu. Transisi warna latar penuh hanya terjadi sekali per perubahan status (aman); jangan dipakai untuk hover. Di DESIGN.md nilai-nilai ini menjadi token bernama (mis. `--surface-ready`) di tabel 2.1 DESIGN.md, lalu dirujuk dari tabel status 2.2, bukan hex lepas.

### 2.3 Kedalaman & material

**Kapan:** kartu hero, sheet, tombol primary di layar signature, satu "objek" utama (nota, kartu member). Layar kerja: sebagian besar datar, satu level `raised` untuk elemen yang memang melayang.

**Skala elevasi (bayangan berlapis, bertinta rona ink, bukan hitam):**
```css
:root { --ink-h: 40; }  /* sama dengan hue --color-ink */
@theme {
  --shadow-rest:   0 1px 0 oklch(0.25 0.03 var(--ink-h) / 0.08);
  --shadow-raised: 0 1px 1px oklch(0.25 0.03 var(--ink-h) / 0.10),
                   0 2px 4px oklch(0.25 0.03 var(--ink-h) / 0.08),
                   0 8px 16px -4px oklch(0.25 0.03 var(--ink-h) / 0.10);
  --shadow-float:  0 2px 2px oklch(0.25 0.03 var(--ink-h) / 0.08),
                   0 6px 8px oklch(0.25 0.03 var(--ink-h) / 0.08),
                   0 16px 24px -6px oklch(0.25 0.03 var(--ink-h) / 0.14),
                   0 32px 48px -12px oklch(0.25 0.03 var(--ink-h) / 0.18);
  --shadow-edge:   inset 0 1px 0 oklch(1 0 0 / 0.55), inset 0 -1px 0 oklch(0.2 0.03 var(--ink-h) / 0.10);
}
```
Pakai: `shadow-raised`, `shadow-float`; highlight tepi atas lewat `shadow-edge` (gabung lewat kelas `[box-shadow:var(--shadow-raised),var(--shadow-edge)]`). Aturan: tiap lapis menggandakan offset-y dan blur; maksimal 3 tingkat dipakai aplikasi; tulis alasan tiap tingkat di DESIGN.md (R-12).

**Tombol taktil (satu per layar, layar signature):**
```css
.btn-tactile { background: linear-gradient(180deg, var(--color-brand-300), var(--color-brand-500));
  color: var(--color-ink);
  box-shadow: var(--shadow-raised), inset 0 1px 0 oklch(1 0 0 / .45), inset 0 -2px 0 oklch(0.3 0.1 35 / .35);
  transition: transform .1s var(--ease-out-expo), box-shadow .1s; }
.btn-tactile:active { transform: translateY(1px) scale(.985); box-shadow: var(--shadow-rest), inset 0 2px 3px oklch(0.3 0.1 35 / .35); }
```
Teks tombol memakai `text-ink` (5.90 di brand-500, 10.59 di brand-300); selalu ukur di stop terburuk gradien.

**Grain (tekstur noise) lewat SVG inline**, dosis rendah, statis:
```css
:root {
  /* butir gelap (latar terang) dan butir terang (latar gelap): beda hanya di baris RGB feColorMatrix */
  --grain-dark:  url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .6 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  --grain-light: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .6 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
@utility grain {
  position: relative; isolation: isolate;
  &::after { content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
    opacity: 0.07; mix-blend-mode: multiply; background-image: var(--grain-dark); }
}
@utility grain-light {   /* latar gelap: butir putih, blend screen */
  position: relative; isolation: isolate;
  &::after { content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
    opacity: 0.06; mix-blend-mode: screen; background-image: var(--grain-light); }
}
```
Opacity 0.04 sampai 0.1 (di atas itu mengotori teks); pasang di blok warna besar, bukan di seluruh `body` dan bukan di setiap kartu. Butir gelap + `multiply` untuk latar terang; di latar gelap pakai `grain-light` (butir gelap + `screen` di atas latar gelap tidak terlihat). Teks tetap dicek kontrasnya dengan grain aktif.
**Tekstur berbasis konsep (hanya jika konsepnya cocok):** kertas = grain + `--color-paper` hangat + pinggir sobek (2.4); kain/linen (laundry) = dua `repeating-linear-gradient` tegak lurus 1px per 3px, opacity ≤ 0.04. Itu bukan "background grid" generik karena ada alasan material yang tertulis.

**Kaca (glass), hanya di atas latar kaya:**
```css
@layer components {
  .glass { background: oklch(1 0 0 / 0.14); border: 1px solid oklch(1 0 0 / 0.28);
    -webkit-backdrop-filter: blur(14px) saturate(1.4); backdrop-filter: blur(14px) saturate(1.4);
    box-shadow: var(--shadow-float); }
  @supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
    .glass { background: oklch(0.2 0.03 40 / 0.9); }
  }
}
```
Maksimal 1 sampai 2 elemen (R-10); wajib di atas mesh/foto yang berwarna, jangan di atas putih polos; ukur kontras teks pada **piksel latar terang terburuk** di belakangnya (cek dengan tangkapan layar), kalau gagal tambah overlay solid. Di mobile blur ≤ 14px dan jangan di elemen yang ikut scroll (mahal). `design-preview.html` tidak punya build/autoprefixer, jadi tulis `-webkit-backdrop-filter` seperti di atas agar Safari menampilkannya.
**Beda dari generik:** shadow satu lapis `shadow-lg` abu-abu di semua kartu; glass di navbar+kartu+modal sekaligus. Di sini elevasi punya skala bertinta dengan alasan, material berasal dari konsep.

### 2.4 Bahasa bentuk (shape)

**Kapan:** satu motif identitas yang berulang (tiket, stempel, label, gelembung) + radius yang punya sistem.
```css
@layer components {
/* tiket/nota dengan takik samping */
.ticket { --r: 12px;
  mask: radial-gradient(var(--r) at 0 50%, #0000 98%, #000) left / 51% 100% no-repeat,
        radial-gradient(var(--r) at 100% 50%, #0000 98%, #000) right / 51% 100% no-repeat; }
/* tepi sobek */
.torn { clip-path: polygon(0 0,100% 0,100% calc(100% - 8px),94% 100%,88% calc(100% - 6px),80% 100%,
  71% calc(100% - 7px),62% 100%,54% calc(100% - 5px),45% 100%,36% calc(100% - 8px),27% 100%,
  18% calc(100% - 5px),9% 100%,0 calc(100% - 6px)); }
/* sudut kapsul bertingkat: besar hanya di elemen konsep */
.shape-lead { border-radius: 28px 28px 28px 6px; }
}
```
**[EKSPERIMENTAL]** `corner-shape: squircle` (Chrome 139+; belum di Safari/Firefox): `@supports (corner-shape: squircle) { .card { corner-shape: squircle; border-radius: 28px; } }`, fallback `border-radius` biasa.
Aturan: `mask`/`clip-path` memotong bayangan dan focus ring di pinggirnya, jadi bungkus dengan `filter: drop-shadow(...)` pada parent dan beri `outline-offset` positif; konten interaktif jangan diletakkan di zona takik; uji di 360px dan zoom 200%. Radius: tetapkan 3 nilai (kecil kontrol, sedang kartu, besar elemen konsep) dan beri alasan (R-11); radius oversize hanya di elemen yang membawa konsep.

### 2.5 Ilustrasi & ikonografi

**Aturan gaya satu set ilustrasi (tulis di DESIGN.md sebagai spesifikasi):**
- Stroke seragam 2px pada viewBox 96, `stroke-linecap: round; stroke-linejoin: round`, `vector-effect: non-scaling-stroke` agar tidak menipis saat diperbesar.
- Palet hanya dari token (`currentColor`, `var(--color-brand-300)`, `var(--color-ink)`): maksimal 3 warna per ilustrasi.
- Satu ciri khas: **fill bergeser** 3 sampai 4px dari garis (efek cetak meleset) atau garis putus-putus pada satu bagian. Konsisten di semua ilustrasi.
- Subjeknya objek domain user (keranjang cucian, nota, hanger), bukan orang blob atau bentuk abstrak (R-22).
- Dipakai di empty state, sukses, onboarding, 404; tidak di layar kerja padat.
```tsx
<svg viewBox="0 0 96 96" role="img" aria-label="Keranjang cucian kosong" className="size-24">
  <path d="M20 40h56l-6 38H26z" fill="var(--color-brand-300)" transform="translate(3 3)" />
  <path d="M20 40h56l-6 38H26zM16 40h64M36 40c0-10 6-16 12-16s12 6 12 16"
        fill="none" stroke="var(--color-ink)" strokeWidth="2" strokeLinecap="round"
        strokeLinejoin="round" vectorEffect="non-scaling-stroke" />
</svg>
```
Ilustrasi dekoratif: `aria-hidden="true"` dan kosongkan teks alternatifnya; kalau membawa makna, beri `role="img"` + `aria-label`.

**Ikon (lucide-react) kustom tanpa ganti library:** `strokeWidth` 1.5 untuk tampilan ringan, 2.25 untuk kuat; satu nilai di seluruh app (lewat CSS: `svg.lucide { stroke-width: 1.75; }`, CSS menimpa atribut). **Duotone:** `<PackageCheck className="stroke-brand-900 fill-brand-300/40" />` (isi hanya terlihat di bentuk tertutup). Ikon aksi utama boleh ditaruh dalam wadah bentuk konsep. Ikon tetap hanya di tempat yang membantu memindai (aturan SKILL.md).

### 2.6 Koreografi motion

**Token (taruh di `@theme`, rujuk dari komponen):**
```css
@theme {
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out-soft: cubic-bezier(0.65, 0, 0.35, 1);
  /* pegas lewat linear() (Chrome 113+, Safari 17.2+, Firefox 112+) */
  --ease-spring: linear(0, 0.2 6%, 0.62 13%, 0.98 22%, 1.08 28%, 1.05 34%, 1.01 44%, 0.995 56%, 1);
  --animate-stamp: stamp 460ms var(--ease-out-expo) both;
  @keyframes stamp { 0% { opacity: 0; transform: scale(1.7) rotate(-14deg); }
    60% { opacity: 1; transform: scale(0.96) rotate(-8deg); } 100% { opacity: 1; transform: scale(1) rotate(-8deg); } }
}
```
**Anggaran durasi:** feedback press 80 sampai 120ms · hover/focus 120 sampai 180ms · masuk/keluar komponen 180 sampai 300ms (maks 400) · perpindahan layar 300 sampai 450ms · momen celebration ≤ 1200ms total dan bisa dilewati · stagger total ≤ 250ms. Hanya animasikan `transform` dan `opacity` (kecuali satu transisi warna latar saat status berubah). Jangan `width/height/top/left`. Semua di bawah `prefers-reduced-motion`.

**Setup `motion` (satu kali di layout client):**
```tsx
"use client";
import { MotionConfig } from "motion/react";
export const spring = {
  snappy: { type: "spring", stiffness: 520, damping: 38, mass: 0.7 },
  smooth: { type: "spring", stiffness: 260, damping: 30 },
  bouncy: { type: "spring", stiffness: 380, damping: 16, mass: 0.9 }, // celebration saja
} as const;
export const Motion = ({ children }: { children: React.ReactNode }) => (
  <MotionConfig reducedMotion="user" transition={spring.smooth}>{children}</MotionConfig>
);
```
`reducedMotion="user"` mematikan animasi transform/layout saat user memilih kurangi gerak (opacity tetap). Tambahkan CSS: `@media (prefers-reduced-motion: reduce) { *, ::before, ::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; animation-iteration-count: 1 !important; scroll-behavior: auto !important; } }`.

**Daftar masuk bertahap (stagger), hanya saat pertama muat:**
```tsx
const list = { show: { transition: { staggerChildren: 0.04, delayChildren: 0.05 } } };
const item = { hidden: { opacity: 0, y: 12 }, show: { opacity: 1, y: 0, transition: spring.smooth } };
<motion.ul variants={list} initial="hidden" animate="show">
  {rows.map((r, i) => i < 8
    ? <motion.li key={r.id} variants={item}>{/* ... */}</motion.li>
    : <li key={r.id}>{/* ... */}</li>)}
</motion.ul>
```
Aturan tunggal untuk semua daftar: stagger hanya saat daftar pertama kali muncul di sesi itu, 8 baris pertama, total ≤ 250ms; refetch, filter, polling, dan kembali ke daftar tidak memutar ulang (gunakan state `hasAnimated`). Di layar kerja berulang (bagian 1.2, tingkat ketiga) tanpa stagger sama sekali.

**Number ticker (angka utama):**
```tsx
"use client";
import { animate, motion, useMotionValue, useReducedMotion, useTransform } from "motion/react";
import { useEffect } from "react";
const fmt = new Intl.NumberFormat("id-ID");
export function Ticker({ value }: { value: number }) {
  const reduce = useReducedMotion();
  const mv = useMotionValue(reduce ? value : 0);
  const text = useTransform(mv, (v) => fmt.format(Math.round(v)));
  useEffect(() => {
    if (reduce) { mv.set(value); return; }
    const c = animate(mv, value, { duration: 0.9, ease: [0.16, 1, 0.3, 1] });
    return () => c.stop();
  }, [value, reduce, mv]);
  return (<><motion.span aria-hidden className="tabular-nums">{text}</motion.span>
    <span className="sr-only">{fmt.format(value)}</span></>);
}
```
Pakai di momen: pertama muat dashboard, total setelah bayar. Bukan untuk angka yang berubah tiap detik.

**Stepper/progress:** isi garis lewat `transform: scaleX()` dengan `transform-origin: left`, bukan `width`.
```tsx
<motion.div className="h-1 origin-left bg-brand-500" initial={{ scaleX: 0 }}
  animate={{ scaleX: step / (total - 1) }} transition={spring.smooth} />
```
Posisi tahap saat ini juga ditandai teks dan `aria-current="step"`, bukan animasinya.

**Momen sukses (≤ 1200ms):** (1) centang tergambar, (2) stempel menghantam, (3) letusan partikel dari objek domain. Pilih satu atau dua, bukan ketiganya.
```tsx
<svg viewBox="0 0 52 52" className="size-16 text-brand-500" aria-hidden>
  <circle cx="26" cy="26" r="24" fill="none" stroke="currentColor" strokeWidth="3" opacity=".25" />
  <motion.path d="M14 27l8 8 16-17" fill="none" stroke="currentColor" strokeWidth="4"
    strokeLinecap="round" strokeLinejoin="round" initial={{ pathLength: 0 }}
    animate={{ pathLength: 1 }} transition={{ duration: 0.4, delay: 0.1, ease: [0.16, 1, 0.3, 1] }} />
</svg>
```
Stempel (CSS): `<div class="animate-stamp border-4 border-brand-700 px-4 py-1 font-display text-title uppercase tracking-tight text-brand-700">LUNAS</div>`; tekstur tinta opsional: tumpuk utilitas `grain` di wadah stempel; teksnya nyata di DOM (bukan gambar) dan diumumkan lewat `role="status"` di wilayah live.
```tsx
// letusan partikel: render HANYA setelah aksi sukses (client), bukan di SSR
import { useEffect, useMemo } from "react";
export function Burst({ shape, n = 18, onDone }: { shape: React.ReactNode; n?: number; onDone: () => void }) {
  const reduce = useReducedMotion();
  useEffect(() => {
    const t = setTimeout(onDone, 1100);                       // selesai sendiri
    const esc = (e: KeyboardEvent) => e.key === "Escape" && onDone();
    window.addEventListener("keydown", esc);
    return () => { clearTimeout(t); window.removeEventListener("keydown", esc); };
  }, [onDone]);
  const parts = useMemo(() => Array.from({ length: n }, (_, i) => {
    const a = (i / n) * Math.PI * 2 + Math.random() * 0.4, d = 70 + Math.random() * 90;
    return { x: Math.cos(a) * d, y: Math.sin(a) * d, r: (Math.random() - 0.5) * 240 };
  }), [n]);
  if (reduce) return null;
  return (<div aria-hidden onPointerDown={onDone} className="absolute inset-0 z-0 grid place-items-center">
    {parts.map((p, i) => (<motion.span key={i} className="absolute"
      initial={{ x: 0, y: 0, scale: 0.4, opacity: 1, rotate: 0 }}
      animate={{ x: p.x, y: p.y + 60, scale: 1, opacity: 0, rotate: p.r }}
      transition={{ duration: 0.9, ease: [0.16, 1, 0.3, 1], opacity: { delay: 0.5, duration: 0.4 } }}>{shape}</motion.span>))}
  </div>);
}
```
`shape` adalah SVG kecil dari objek domain (gelembung sabun, butir kopi, kancing, koin), 12 sampai 20 piksel. Maksimal 24 partikel. Jangan pakai emoji. Putar hanya sekali per aksi; hapus dari DOM setelah selesai (`onDone` mengosongkan state). **Setiap perayaan bisa dilewati** (ketuk lapisan, tombol Esc) dan tombol aksi (`relative z-10`) aktif sejak detik 0, tidak pernah tertutup lapisan perayaan; pengguna reduced-motion mendapat hasil akhir statis (centang/stempel tanpa gerak).

**Shared element / View Transitions** (daftar ke detail):
```css
/* nama HANYA untuk kartu yang diketuk (data-vt="active") dan elemen tujuannya di halaman detail, bukan semua item daftar */
[data-vt="active"], .detail-hero { view-transition-name: order-hero; }
::view-transition-group(*) { animation-duration: 350ms; animation-timing-function: var(--ease-out-expo); }
@media (prefers-reduced-motion: reduce) { ::view-transition-group(*), ::view-transition-old(*), ::view-transition-new(*) { animation: none; } }
```
```tsx
import { flushSync } from "react-dom";
const go = (fn: () => void) => {
  const d = document as Document & { startViewTransition?: (cb: () => void) => unknown };
  if (d.startViewTransition) d.startViewTransition(() => flushSync(fn)); // flushSync: DOM baru harus sudah ada saat callback selesai
  else fn();
};
// pemakaian: tandai kartu dulu (el.dataset.vt = "active"), lalu go(() => setSelected(id)); hapus penanda setelah selesai
```
**[EKSPERIMENTAL]** Integrasi Next.js (`experimental.viewTransition: true` di `next.config` + komponen `ViewTransition` yang diimpor dari `react`, di Next 16 bukan lagi `unstable_ViewTransition`; tetap butuh build React yang mendukung) masih berubah antar versi: cek dokumentasi versi yang dipakai sebelum menuliskannya di DESIGN.md; fallback yang stabil adalah `startViewTransition` untuk perubahan state di satu halaman client, dan `layoutId` dari `motion` untuk elemen bersama. `view-transition-name` yang duplikat di satu halaman membatalkan transisi.

**Efek terkait scroll (CSS scroll-driven animations) [EKSPERIMENTAL: Chrome 115+, Safari 26+, Firefox di balik flag]:**
```css
@keyframes reveal { from { opacity: 0; transform: translateY(24px); } to { opacity: 1; transform: none; } }
@keyframes progress { from { transform: scaleX(0); } to { transform: scaleX(1); } }
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .reveal { animation: reveal linear both; animation-timeline: view(); animation-range: entry 0% cover 28%; }
    .scroll-progress { transform-origin: left; animation: progress linear both; animation-timeline: scroll(root); }
  }
}
```
Keadaan awal elemen **tampak** (opacity 1); keyframes yang menyembunyikan hanya ada di dalam `@supports`, sehingga browser tanpa dukungan tidak menyembunyikan konten. Untuk halaman showcase/onboarding, bukan daftar kerja.

**Micro-interaction:** press `active:scale-[0.97] transition-transform duration-100 ease-[var(--ease-out-expo)]` pada tombol/kartu yang bisa ditekan; toggle bergeser dengan spring `snappy`; saat sukses di perangkat yang mendukung `navigator.vibrate?.(12)` (Android saja, tidak ada di iOS Safari; peningkatan opsional, bukan pengganti feedback visual). Hover `@media (hover: hover)` saja agar tidak menempel di layar sentuh.

### 2.7 Layar hero / showcase

**Rumus layar signature:** satu elemen dominan (kata status, angka, atau ilustrasi) · satu blok warna penuh · satu aksi di zona jempol · informasi pendukung kecil dan tenang.

Layar status pelanggan (mobile, imersif, 100dvh):
```
+------------------------------+  latar penuh warna status (--stage-bg), grain 0.06
| Warung Laundry Bu Sri    [?] |  header 44px, teks kecil
|                              |
|  ORDER LD-2410-007           |  label 14px/600, kode tabular
|                              |
|  Lagi                        |  .text-hero: kata status, baris besar
|  dicuci.                     |
|                              |
|  Perkiraan selesai           |
|  Kamis, 16.00     [ilustrasi]|  angka/jam 3rem; ilustrasi 96px bergeser fill
|                              |
|  o---o---O - - -o            |  stepper (transform scaleX), tahap aktif berlabel
|  [ Hubungi toko ]            |  satu aksi, 48px, zona jempol
+------------------------------+
```
Stage: `min-h-dvh pb-[env(safe-area-inset-bottom)]` (nilainya 0 kecuali `export const viewport: Viewport = { viewportFit: "cover" }` di `app/layout.tsx`), `meta theme-color` ikut status, `aria-live="polite"` pada kata status, tidak ada auto-refresh yang menggeser layout.

Dashboard hero (layar kerja owner): satu angka dominan (`num-xl` dengan clamp lebih kecil, mis. `text-[clamp(2.5rem,1.5rem+6vw,4.5rem)]`) + sparkline + satu kalimat tafsiran; sisanya daftar yang dipakai bekerja. Jangan menaruh 4 kartu statistik setara (antislop). Angka dari data nyata, kosong → empty state yang menyuruh melakukan satu aksi.

Login/onboarding: separuh layar ilustrasi/warna merek di desktop, di mobile hanya strip warna 120px + judul display; form tetap `max-w-sm`, kontras dan label penuh.
Pola: pecah tiga zona vertikal (identitas · konten utama · aksi). Pakai asimetri (rata kiri, bukan semuanya terpusat) dan satu elemen yang sengaja keluar dari grid (angka besar menggantung, stempel miring).

### 2.8 Data viz dengan kepribadian
- Tanya dulu pertanyaan yang dijawab grafik, tulis sebagai judul (aturan antislop).
- Sorot **satu** batang/titik (warna brand), sisanya `muted`; anotasi langsung pada titik penting ("Kamis: 38 order"), tanpa legenda terpisah kalau cuma satu seri.
- Batang: sudut atas membulat saja (`rx` di atas), jarak antar batang ≥ 6px, tanpa grid garis berlebihan; angka `tabular-nums`.
- Sparkline SVG tanpa library:
```tsx
function Spark({ data, w = 160, h = 40 }: { data: number[]; w?: number; h?: number }) {
  const max = Math.max(...data), min = Math.min(...data), span = max - min || 1;
  const pts = data.map((v, i) => [(i / (data.length - 1)) * w, h - 4 - ((v - min) / span) * (h - 8)]);
  const d = pts.map(([x, y], i) => `${i ? "L" : "M"}${x.toFixed(1)} ${y.toFixed(1)}`).join(" ");
  const [lx, ly] = pts[pts.length - 1];
  return (<svg viewBox={`0 0 ${w} ${h}`} className="w-full" role="img" aria-label={`Tren ${data.length} hari, terakhir ${data[data.length - 1]}`}>
    <path d={`${d} L${w} ${h} L0 ${h}Z`} fill="var(--color-brand-300)" opacity=".25" />
    <path d={d} pathLength={1} fill="none" stroke="var(--color-brand-700)" strokeWidth="2"
      strokeLinecap="round" strokeLinejoin="round" vectorEffect="non-scaling-stroke"
      style={{ strokeDasharray: 1, strokeDashoffset: 0 }} />
    <circle cx={lx} cy={ly} r="3.5" fill="var(--color-brand-700)" />
  </svg>);
}
```
Animasi gambar-masuk opsional: `strokeDashoffset` 1 ke 0 dalam 700ms, satu kali, di bawah `prefers-reduced-motion: no-preference`. Selalu sediakan tabel/teks setara (`sr-only` atau tombol "lihat data"). Segmen yang bersebelahan kontras ≥ 3:1. Data nyata atau diberi label data contoh.

### 2.9 Tema gelap showcase
**Kapan:** konteks pakai malam/gelap atau domain yang memang gelap (musik, bioskop, trading, game, alat developer, kendaraan). Bukan alasan "biar keren" (R-21). Kalau light adalah mode kerja, gelap bisa jadi tema khusus layar showcase saja (`data-theme="dark"` pada section).
```css
.dark, [data-theme="dark"] {
  color-scheme: dark;
  --background: #170C09;                    /* gelap bertinta, bukan #000 */
  --card:       #221410;                    /* permukaan lebih terang = lebih tinggi */
  --foreground: #F1EEE7;                    /* bukan #fff (menghindari silau); 16.58 di atas background */
  --muted-foreground: #B3A99E;              /* 7.73 di atas card */
  --primary: #FC9E47;                       /* aksen dinaikkan lightness-nya; 9.26 di atas background */
  --primary-foreground: #170C09;            /* teks gelap di atas primary: 9.26 (putih hanya 1.79, gagal) */
}
.glow-focus { box-shadow: 0 0 0 2px #FC9E47, 0 0 36px -10px oklch(0.78 0.15 60 / .6); } /* cincin solid; hanya halonya yang transparan */
```
Aturan: elevasi dengan **permukaan lebih terang**, bukan bayangan hitam; glow maksimal 1 elemen (R-13) dan statis; kurangi chroma aksen sedikit karena warna jenuh bergetar di latar gelap; cek ulang semua pasangan kontras dengan script (aksen yang lolos di terang belum tentu lolos di gelap, dan sebaliknya teks di atas primary harus dibalik jadi gelap); gambar dan ilustrasi perlu varian atau `filter` penyesuaian. Jangan memilih gelap + neon + gradien (kombinasi default AI).

---

## 3. Katalog momen signature

| # | Aplikasi | Momen | Yang bikin wow | Resep |
|---|---|---|---|---|
| 1 | Pelacak status (laundry, servis, kurir) | Layar status pelanggan | Latar seluruh layar berganti warna per status, kata status raksasa | 2.2d + 2.1 + stepper 2.6 |
| 2 | Kasir/pembayaran | Lunas | Stempel LUNAS menghantam nota yang bergerigi, angka sisa menghitung mundur ke 0 | `animate-stamp` + `.torn` + Ticker |
| 3 | Onboarding | Selamat datang | Warna merek penuh, kalimat besar muncul per baris, satu tombol di zona jempol | 2.2a + stagger ≤ 3 baris |
| 4 | Empty state pertama | Daftar order kosong | Ilustrasi objek domain bergaya fill-bergeser + satu aksi jelas, bukan "No data" | 2.5 |
| 5 | Pencapaian/milestone | Order ke-100 | Letusan partikel objek domain + angka besar menghitung naik, sekali seumur hidup | Burst + Ticker, simpan flag |
| 6 | Pencarian | Hasil pencarian cepat | Sorotan teks yang cocok dengan stabilo warna merek, hasil tanpa jeda animasi | `mark` bergaya, 0ms |
| 7 | Checkout/pembayaran | Pilih metode | Kartu metode yang dipilih terangkat (`shadow-float`) dan sisanya mendatar; harga total angka display | 2.3 + 2.1 |
| 8 | Dashboard owner | Ringkasan hari ini | Satu angka dominan + sparkline dengan satu titik disorot, satu kalimat tafsiran | 2.8 + Ticker saat muat pertama |
| 9 | Login | Masuk | Strip warna + judul display, input besar 48px, OTP slot besar dengan penanda aktif tebal | 2.7 |
| 10 | Pengingat/jatuh tempo | Notifikasi penting | Kartu bertepi sobek dengan hitungan "3 hari lagi" bergaya display, tanpa pulse abadi | `.torn` + 2.1 |
| 11 | Galeri/portofolio | Detail karya | Transisi bersama (shared element) dari thumbnail ke halaman penuh | View Transitions |
| 12 | Unggah/proses panjang | Memproses | Progress `scaleX` + teks tahap konkret ("Menimbang", "Mencuci"), bukan spinner polos | 2.6 stepper |

Pilih dari katalog sebanyak level ambisi menuntut (Spektakuler ≥ 4, Ekspresif 2 sampai 3, Tenang 1 sampai 2); sisanya jadi layar kerja yang tenang.

---

## 4. Anti-pola: ekspresif tapi buruk

| Anti-pola | Kenapa gagal | Perbaikan |
|---|---|---|
| Konten disembunyikan sebagai default (opacity 0, `clip-path` tertutup) menunggu JS/IntersectionObserver/scroll timeline | Kalau pemicu gagal (scroller lain, JS error, browser lama), konten hilang selamanya | Keadaan akhir = CSS default; animasi hanya keyframe `from` + `animation-fill-mode: backwards`, dipasang lewat kelas pemicu |
| Animasi masuk di layar yang dipakai berulang (daftar order, form kasir) | Menunda kerja, terasa lambat | Layar kerja berulang: tanpa animasi masuk; daftar harian: ≤ 250ms total, hanya saat pertama muat |
| Glass di atas latar putih/polos atau tanpa cek kontras | Teks tak terbaca, efek tak terlihat | Glass hanya di atas latar kaya, ukur piksel terburuk |
| Display font (Unbounded, Syne, Bagel, Young Serif) di bawah 28px atau untuk label dan tabel | Tidak terbaca, spasi aneh | Display ≥ 28 sampai 32px, isi pakai font body |
| Teks isi atau paragraf di atas gradien/mesh | Kontras berubah per posisi | Pelat solid di bawah teks, atau gradien hanya untuk blok judul |
| `backdrop-filter` besar di daftar yang di-scroll di mobile | Jank, baterai | Batasi 1 elemen statis, blur ≤ 14px |
| Autoplay loop (pulse, float, gradien bergerak, partikel terus-menerus) | Mengganggu, melanggar WCAG 2.2.2 kalau > 5 detik | Satu kali per momen; jika perlu loop, beri tombol jeda |
| Animasi `width`, `height`, `top`, `box-shadow` pada elemen banyak | Layout/paint thrash | Pakai `transform`/`opacity` |
| Grain/noise di seluruh `body` atau opacity > 0.1 | Mengotori teks, paint mahal | Blok warna besar saja, opacity 0.04 sampai 0.1 |
| Satu momen signature diputar ulang tiap buka layar | Cepat menjemukan | Putar sekali (flag di storage) atau hanya saat status berubah |
| Pegas memantul (`bouncy`) di kontrol harian | Terasa main-main dan lambat | `snappy` untuk kontrol; `bouncy` hanya celebration |
| Warna status sebagai satu-satunya pembeda | Gagal bagi buta warna (WCAG 1.4.1) | Tambah kata, ikon, posisi |
| Clip-path/mask memotong focus ring dan bayangan | Fokus tak terlihat | `drop-shadow` di parent, `outline-offset`, uji keyboard |
| Parallax dan efek scroll di halaman kerja | Mual, performa | Hanya halaman showcase, di bawah `no-preference` |
| Efek yang sama di 5 tempat (semua kartu glow, semua tombol berpanah) | Jadi default, bukan keputusan | Dosis maksimal 2 sampai 3 tempat per efek |
| Teks diselipkan ke dalam gambar/SVG (stempel, judul) | Tidak bisa dipilih, tidak terbaca pembaca layar | Teks asli di DOM, hias dengan CSS |

---

## 5. Checklist "wow tapi bisa dipakai" (untuk reviewer)

- [ ] Ada satu konsep yang bisa disebut dalam satu kalimat, dan muncul di minimal 3 tempat (warna, bentuk, copy, motion).
- [ ] Ada satu elemen dominan per layar signature (skala ≥ 5 kali teks isi); blur mata: hierarki masih terlihat.
- [ ] Jumlah momen signature sesuai level ambisi (Spektakuler ≥ 4, Ekspresif 2 sampai 3, Tenang 1 sampai 2), lokasinya tertulis di 1.6; layar kerja utama tetap membawa satu motif identitas.
- [ ] Layar kerja harian cepat: tanpa animasi masuk bertele-tele, stagger hanya saat daftar pertama muat (maks 8 baris, ≤ 250ms), feedback press ≤ 120ms.
- [ ] Palet tetap 1 primary + netral + 1 sampai 2 warna hero/aksen; warna dasar ada sebagai hex dan semua pasangan teks/latar diukur dengan script; komitmen warna lewat luas area, bukan hue baru; tidak ada gradien biru-ungu.
- [ ] Setiap gradien/mesh dibangun dari ramp token; kontras teks diukur di titik terburuk dan lolos 4.5 (teks besar 3.0).
- [ ] Display font hanya ≥ 28px dan di judul/angka; isi ≥ 16px; ukuran fluid memakai `rem` + `vw` (zoom 200% tidak memotong).
- [ ] Elevasi memakai skala ber-alasan (≤ 3 tingkat), bayangan bertinta; glass ≤ 2 elemen dan di atas latar kaya dengan kontras terukur; glow ≤ 1 sampai 2 elemen.
- [ ] Grain/tekstur hanya di blok besar, opacity ≤ 0.1, punya alasan konsep tertulis.
- [ ] Ilustrasi punya aturan gaya tertulis (stroke, palet, ciri khas), berhubungan langsung dengan produk; dekoratif memakai `aria-hidden`.
- [ ] Semua motion: hanya `transform`/`opacity`, durasi sesuai anggaran, tidak ada loop abadi, `prefers-reduced-motion` ditangani (tampak tanpa gerak, bukan hilang).
- [ ] API eksperimental (View Transitions di Next, scroll-driven, `corner-shape`, `text-box`) punya fallback yang konten-nya tetap terlihat.
- [ ] Status dibedakan oleh kata/ikon/posisi, bukan hanya warna; momen sukses diumumkan lewat `role="status"`/`aria-live`.
- [ ] Diuji di 360px dan zoom 200%: tidak ada overflow, mask/clip-path tidak memotong fokus, tap target ≥ 44px.
- [ ] Setiap perayaan bisa dilewati (ketuk/Esc), tidak menutupi tombol aksi, punya hasil akhir statis untuk reduced-motion.
- [ ] Preview HTML (dengan `-webkit-backdrop-filter` bila memakai glass) menampilkan semua momen signature (termasuk state sebelum dan sesudah) dan satu layar kerja berdampingan untuk membandingkan intensitasnya.

---

## 6. Menerjemahkan ke DESIGN.md

| Hasil keputusan | Ditulis di |
|---|---|
| Level ambisi, konsep, motif identitas, alasan dunia user | 1.3 Keputusan & Alasan |
| Momen signature (jumlah sesuai level), pemicu, timeline, fallback | 1.6 Momen Signature |
| Ramp warna (hex), warna status, kontras | 2.1, 2.2, 2.3 |
| Token font fluid, pasangan font | 2.4 |
| Token elevasi, grain, glass, ilustrasi | 2.6 |
| `--ease-*`, `--animate-*`, spring, anggaran durasi, reduced-motion | 2.7 |
| Blok CSS siap tempel (menyatukan semua token di atas) | 2.8 |
| Resep motif (stempel, tepi sobek, grain) lengkap dengan CSS dan perilaku 360px/zoom 200% | 2.6 dan aturan isi 11 |
| Wireframe layar signature per status, dan layar kerja berdampingan | Bagian 5 |
| Batas dosis efek dan aturan layar kerja vs showcase | 1.3 dan 2.7 |
