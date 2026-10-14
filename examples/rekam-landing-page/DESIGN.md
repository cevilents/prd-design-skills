# DESIGN: Rekam

> Landing page yang terasa seperti struk rapat yang sedang dicetak: merah REC penuh, kertas termal bergerigi, untuk tim startup dan agency Indonesia yang memutuskan dalam beberapa detik, dari HP atau laptop, apakah Rekam layak dicoba.

| | |
|---|---|
| Versi | 1.0 |
| Tanggal | 2026-10-14 |
| Berdasarkan | Brief user (tanpa PRD), pratinjau `design-preview.html`, tiga konsep di `design-concepts.html` |
| Jenis produk | Landing page / marketing site (profil 1). Aplikasi Rekam sendiri di luar lingkup dokumen ini |
| Platform & stack | Web desktop-first (desain di 1440 dan 390) · Next.js (App Router) + Tailwind v4 + shadcn/ui |

---

## 1. Arah Visual

### 1.1 Konteks Pemakaian
- **Pembuat keputusan startup:** founder atau lead produk, datang dari tautan di grup WhatsApp atau LinkedIn, buka di HP 390 sambil antre atau di sela rapat. Memutuskan dalam 10 detik apakah lanjut scroll.
- **Pemilik agency:** kerja di laptop 14 inci, membandingkan harga Pro dan Tim sebelum menagih ke klien.
- Keduanya sudah muak mencatat notulen. Mereka membaca cepat, suka bukti yang terlihat (contoh hasil), dan curiga pada klaim besar tanpa data.

### 1.2 Konsep & Kepribadian
- **Konsep:** Struk Rapat. Setiap rapat dicetak jadi struk: kertas termal keluar dari celah mesin merah, lalu disobek jadi tiga lembar (transkrip, ringkasan, tugas).
- **Level ambisi:** Spektakuler.
- **Tiga kata sifat:** tegas, mekanis, jujur.
- **Bukan:** ungu-biru "AI", dashboard korporat, lelucon (struknya serius: isinya rapat sungguhan).
- **Kepadatan informasi:** sedang. Section naratif lega, section harga dan demo padat. Satu gagasan per section.
- **Motif khas:** barcode yang tingginya mengikuti gelombang suara, tepi gerigi kertas termal, garis putus-putus perforasi. Muncul di hero (struk), demo, hasil, harga, CTA, footer.

### 1.3 Keputusan & Alasan
| Keputusan | Pilihan | Alasan |
|---|---|---|
| Jenis produk | Profil 1, landing page | Brief hanya meminta halaman promosi SaaS; tidak ada PRD, login, atau data per user. Dashboard Rekam tidak dispesifikasikan |
| Konsep terpilih | B · Struk Rapat (dari A Studio Malam, C Koran Rapat) | User menjawab "terserah". Dipilih karena: (1) merah = REC, warna yang tidak dipakai kompetitor notulen AI yang seragam ungu-biru; (2) struk itu vertikal, jadi narasi scroll mobile dan desktop memakai bentuk yang sama; (3) mekanisme cetak, sobek, centang adalah gambaran harfiah produk (rekam → tiga hasil), bukan dekorasi. A terlalu mirip produk audio gelap neon, C paling dekat dengan gaya editorial bawaan dan paling tenang |
| Mode warna | Light, dengan satu bab gelap (Hasil) dan footer gelap | Landing dibaca siang hari di HP dan kantor; bab gelap dipakai untuk momen sobek agar lembar kertas menyala. Tidak ada toggle dark mode |
| Pendekatan layout | Desktop-first, dua tata letak: stacked di bawah `lg` 1024, dua kolom di atasnya | Calon pembeli agency membandingkan di laptop; HP mendapat urutan konten yang sama, bukan versi lain |
| Gaya bentuk | Sudut tajam untuk kertas (radius 4px), tombol 8px, tanpa pil | Kertas termal tidak bulat; radius kecil dibedakan dari tombol agar kontrol terbaca sebagai kontrol |
| Bukti sosial | Tidak ada logo, testimoni, atau angka pengguna | Rekam belum punya data itu. Diganti: contoh hasil nyata (data contoh berlabel), kalkulator harga yang bisa dicoba, dan jawaban FAQ konkret |
| Penekanan harga | Baris Tim diberi stabilo pada harganya, tanpa badge "Terpopuler" | Target brief adalah tim; Tim juga paket dengan nilai terbesar per akun. Tidak ada data "terpopuler" yang bisa diklaim |
| CTA | Satu: "Coba gratis", ke `/daftar` di aplikasi | Dari brief. Tombol nav baru muncul setelah hero lewat agar tidak ada dua CTA primer di satu layar |

### 1.4 Perlu Konfirmasi
| Keputusan | Default yang dipakai sekarang | Alternatif |
|---|---|---|
| Cara Rekam masuk ke rapat (bot, ekstensi, aplikasi, rekam dari mic) | Copy tidak menyebut mekanisme, hanya "merekam rapat Zoom, Google Meet, atau tatap muka" | Tambah section cara kerja dengan langkah sebenarnya |
| Batas pemakaian dan pembeda fitur per paket | Baris harga hanya menjelaskan model tagihan; catatan "rincian batas pemakaian mengikuti paket final" | Daftar fitur per paket di 5.7 |
| Jumlah anggota minimum paket Tim | Kalkulator 2 sampai 50 | Angka dari produk |
| Kalimat campur Indonesia-Inggris dalam satu kalimat | Tag bahasa per baris transkrip (bukan per kata) | Tag per segmen |
| Pemilik tugas dan tenggat otomatis | Contoh tugas menampilkan nama dan hari | Hapus nama dan hari jika produk belum mengekstrak keduanya |
| Privasi, persetujuan peserta rapat, penyimpanan rekaman | Footer menautkan Kebijakan Privasi dan Syarat Layanan; FAQ memuat 4 pertanyaan non-privasi | Tambah FAQ privasi dengan jawaban resmi sebelum rilis (wajib) |
| Kontak | Footer tanpa email atau nomor | Tambah alamat kontak nyata |
| Bukti sosial | Section dihapus | Tambah section "Dipakai oleh" hanya setelah ada pelanggan yang setuju dinamai |
| Contoh rapat (Sprint planning, Briefing klien) | Data contoh berlabel "data contoh" di semua tempat | Ganti dengan rapat nyata yang diizinkan |

### 1.6 Momen Signature
Pemetaan section ke momen:

| # | Momen | Section | Pemicu | Kenapa penting | Mockup |
|---|---|---|---|---|---|
| M1 | Cetak | 5.2 Hero, 5.9 CTA | Halaman dimuat; CTA masuk viewport | Tiga detik pertama: orang melihat struk keluar dari mesin dan langsung paham produk mencetak notulen | `design-preview.html` bingkai hero |
| M2 | Dua Bahasa | 5.3 Demo | Baris struk masuk viewport; klik filter | Bukti bahasa Indonesia + Inggris tanpa klaim kosong | `design-preview.html` bab Transkrip |
| M3 | Sobek | 5.5 Hasil | Scroll melewati stage (desktop pin 300%, mobile per lembar) | Satu rapat menjadi tiga hasil; centang tugas tergambar | `design-preview.html` bab Hasil, bingkai mobile kedua |
| M4 | Struk Tagihan | 5.7 Harga | Klik tambah/kurang anggota | Total tim dihitung di depan mata, tidak ada biaya tersembunyi | `design-preview.html` bab Harga |
| M5 | Pergantian Bab | Seluruh halaman | Scroll melintasi batas section | Merah → kertas → tinta → kertas → merah: bab berganti seperti lembar dibalik | Halaman utuh di `design-preview.html` |

#### M1 · Cetak
- **Komposisi:** hero merah penuh dengan `gradient-hero` dan grain. Judul 3 baris di kiri (`text-hero`), struk di kanan bawah miring -2 derajat keluar dari celah di garis tinta di dasar hero (celah ini sekaligus pembatas bab). Struk keluar ke atas supaya baris pertama tetap terbaca dari atas ke bawah.
- **Timeline motion:** 0ms baris judul naik dari mask (`rise`, 760ms, `ease-out-expo`, stagger 110ms) · 420ms sub fade 500ms · 520ms CTA fade 500ms · 640ms stabilo `sweep` pada "sudah jadi." 520ms · 300ms struk naik 2400ms dengan `steps(24, end)` (umpan kertas bertahap) · total animasi tutup di 2700ms. CTA bisa diklik sejak 0ms. Klik atau ketuk struk melewati animasi.
- **Aset:** struk HTML asli (teks di DOM), jendela dengan `overflow: hidden`, celah gelap di dasar jendela. Isi: 6 baris transkrip ID/EN dan 3 tugas, berlabel "data contoh".
- **Reduced motion:** judul, stabilo, dan struk tampil langsung di posisi akhir; tanpa fade.
- **Resep:** `.win` (jendela 436×600, `overflow: hidden`, `transform: rotate(-2deg)`) berisi `.paper` yang dianimasikan `transform: translateY(var(--win-h))` ke 0 dengan `steps(24, end)`; `.win::after` adalah celah 12px di dasar jendela. Pada CTA penutup (5.9) komponen yang sama dipakai, animasi mulai saat jendela terlihat 35 persen.

#### M2 · Dua Bahasa
- **Komposisi:** struk transkrip lebar 520 di kanan, penjelasan lengket di kiri (desktop). Tag `ID` kosong, tag `EN` berlatar `accent`.
- **Timeline motion:** tiap baris dicetak dengan `clip-path: inset(0 100% 0 0)` ke `inset(0)` 520ms `ease-out-expo` saat masuk viewport (sekali). Klik filter: baris yang tidak cocok turun ke opacity 0.22 dalam 220ms, baris cocok tetap penuh; tidak ada perubahan tinggi.
- **Aset:** struk dengan 9 baris, barcode gelombang di dasar.
- **Reduced motion:** semua baris tampil penuh; filter mengganti opacity tanpa transisi.
- **Resep:** `ToggleGroup` radio menulis `data-dim` pada `.dl`; baris dim tidak dihapus dari DOM sehingga pembaca layar tetap bisa membaca semuanya.

#### M3 · Sobek
- **Komposisi:** bab tinta (`surface-ink`). Judul di atas; tiga lembar kertas bergerigi (`slip`).
- **Timeline motion (desktop ≥ `lg`):** stage setinggi 3 layar, `.pin` lengket. Progres p dari scroll: lembar Transkrip, Ringkasan, Tugas awalnya bertumpuk di tengah (selisih vertikal 0, 72, 144px), lalu menyebar ke tiga kolom pada p 0.14 sampai 0.56 (`ease-out` kubik, translate + rotate -2.5, 1.2, 2.4 derajat); centang tugas tergambar berurutan pada p 0.62, 0.72, 0.82 (masing-masing rentang 0.1). Mobile dan tablet: tanpa pin; tiap lembar naik 56px dan menjadi opak mengikuti posisi scroll, centang tergambar saat lembar Tugas masuk.
- **Aset:** tiga lembar HTML; centang SVG 26px dengan `pathLength="1"`.
- **Reduced motion:** stage tanpa pin, tiga lembar sudah terbuka (tiga kolom desktop, tumpuk mobile), centang tampak tergambar penuh.
- **Resep:** hook `useStage` (9) menulis `--t`, `--k1`, `--k2`, `--k3` pada elemen stage; CSS membaca `translate(calc((1 - var(--t)) * var(--sx)), calc((1 - var(--t)) * var(--sy))) rotate(calc(var(--t) * var(--rot)))`. Nilai awal tanpa JS adalah keadaan akhir (`--t: 1`).

#### M4 · Struk Tagihan
- **Komposisi:** daftar harga satu struk panjang (Gratis, Pro, Tim). Baris Tim membuka kalkulator di bawah harga.
- **Timeline motion:** angka total menghitung dari nilai lama ke baru 420ms (`ease-out` kubik, rAF) setiap klik; persamaan di atasnya (`5 anggota × Rp249.000`) berganti seketika. Tombol kurang nonaktif di 2, tambah nonaktif di 50.
- **Aset:** `Stepper` custom 48px, `output` mono.
- **Reduced motion:** total berganti seketika.
- **Resep:** total = anggota × 249000, diformat `Rp` + `toLocaleString("id-ID")`; teks untuk pembaca layar ada di wilayah `aria-live="polite"` terpisah, angka animasi `aria-hidden`.

#### M5 · Pergantian Bab
- **Komposisi:** blok warna penuh berganti per bab: `hero` (hero), `background` (demo), `secondary` (sumber), `surface-ink` (hasil), `background` (tim, harga, FAQ), `hero` (CTA), `surface-ink` (footer). Batas hero dan CTA adalah garis tinta tempat struk keluar.
- **Timeline motion:** nav berganti tema (transparan merah, kertas solid, tinta) dalam 220ms saat batas bab melewati dasar nav; stabilo di bab Sumber menyapu (`scaleX` 0 ke 1, 600ms) pada baris yang melewati tengah layar.
- **Reduced motion:** nav berganti tema tanpa transisi; stabilo tampil di semua baris.
- **Resep:** nav membaca `data-chap` tiap section dan `data-edge="-36"` untuk section setelah garis tinta (tinggi garis 36px). Di produksi, `meta name="theme-color"` ikut `data-chap` aktif.

---

## 2. Design Tokens

### 2.1 Warna
| Token | Light | Dipakai untuk |
|---|---|---|
| `background` | #F7F5EF | Latar halaman (kertas) |
| `foreground` | #17130F | Teks utama (tinta), tombol di atas hero |
| `card` / `card-foreground` | #FFFEFA / #17130F | Kertas struk, lembar |
| `popover` / `popover-foreground` | #FFFEFA / #17130F | Konten Sheet bila diubah ke kertas (tidak dipakai default) |
| `primary` | #CC2A0E | Tombol utama di atas kertas, centang |
| `primary-foreground` | #FFF8F0 | Teks di atas primary |
| `secondary` / `secondary-foreground` | #ECE8DD / #17130F | Bab Sumber, chip |
| `muted` | #ECE8DD | Latar sekunder |
| `muted-foreground` | #5A5348 | Teks sekunder, keterangan |
| `accent` / `accent-foreground` | #FFE14A / #17130F | Stabilo (kata kunci, tag EN, harga Tim) |
| `border` | #D8D2C3 | Garis dekoratif, tepi kertas |
| `input` | #837B6C | Border field dan stepper (≥ 3.0) |
| `ring` | #17130F | Focus ring di kertas dan hero |
| `ring-inverse` | #F7F5EF | Focus ring di bab tinta |
| `hero` | #FF4B2B | Bidang merah REC penuh, tombol di bab tinta |
| `hero-glow` | #FF6F47 | Titik terang gradien hero |
| `hero-deep` | #EE4424 | Tepi bawah gradien hero |
| `hero-foreground` | #17130F | Teks di atas hero |
| `surface-ink` | #1C1713 | Bab Hasil, footer, menu Sheet |
| `surface-ink-foreground` | #F7F5EF | Teks di atas surface-ink |
| `surface-ink-muted` | #B9AE9E | Teks sekunder di atas surface-ink |

Light saja. Token `destructive` dan semua `success/warning/info` sengaja tidak ada: halaman tidak punya form, status data, atau aksi destruktif. Varian Button `destructive` dihapus dari `buttonVariants`.

### 2.3 Tabel Kontras
| Teks / elemen | Latar | Rasio | Normal (4.5) | Besar / non-teks (3.0) |
|---|---|---|---|---|
| `foreground` | `background` | 16.95 | PASS | PASS |
| `foreground` | `card` | 18.31 | PASS | PASS |
| `foreground` | `secondary` | 15.09 | PASS | PASS |
| `muted-foreground` | `background` | 6.96 | PASS | PASS |
| `muted-foreground` | `secondary` | 6.20 | PASS | PASS |
| `muted-foreground` | `card` | 7.52 | PASS | PASS |
| `primary-foreground` | `primary` | 5.11 | PASS | PASS |
| `primary` | `background` | 4.93 | PASS | PASS |
| `primary` | `card` | 5.33 | PASS | PASS |
| `hero-foreground` | `hero` | 5.54 | PASS | PASS |
| `hero-foreground` | `hero-glow` | 6.70 | PASS | PASS |
| `hero-foreground` | `hero-deep` | 4.83 | PASS | PASS |
| `background` | `foreground` | 16.95 | PASS | PASS |
| `hero-foreground` | `accent` | 14.19 | PASS | PASS |
| `surface-ink-foreground` | `surface-ink` | 16.31 | PASS | PASS |
| `surface-ink-muted` | `surface-ink` | 8.14 | PASS | PASS |
| `hero` | `surface-ink` | 5.33 | PASS | PASS |
| `input` (border) | `background` | 3.84 | FAIL | PASS |
| `input` (border) | `card` | 4.15 | FAIL | PASS |
| `ring` | `background` | 16.95 | PASS | PASS |
| `ring` | `hero` | 5.54 | PASS | PASS |
| `ring-inverse` | `surface-ink` | 16.31 | PASS | PASS |
| `border` | `background` | dekoratif | n/a | n/a |

- Teks di atas gradien hero diukur di titik terburuk (`hero-deep`, 4.83). `primary` tidak dipakai sebagai teks di atas `secondary` (4.39, gagal): bab Sumber hanya memakai teks `foreground` dan `muted-foreground`.
- Baris transkrip yang disaring turun ke opacity 0.22 sebagai keadaan sementara (bukan teks yang dibaca); isinya tetap di DOM dan dibaca penuh oleh pembaca layar.

### 2.4 Tipografi
- **Font display:** Archivo variabel, sumbu lebar 68 persen, bobot 800. Judul raksasa sempit seperti kepala struk dan label kasir. Dari `next/font/google`, sumbu `wdth`; fallback `"Arial Narrow", sans-serif`.
- **Font teks:** Archivo lebar normal 400 sampai 600 untuk isi dan UI; fallback `system-ui, sans-serif`. Satu keluarga, kontras lewat lebar.
- **Font struk:** DM Mono 400 dan 500, khusus teks di dalam kertas dan label kecil, karena printer termal memang mencetak monospace. Fallback `ui-monospace, monospace`.
- **Angka:** `tabular-nums lining-nums` untuk harga, waktu, dan total.

| Token | Ukuran / line-height | Weight | Dipakai untuk |
|---|---|---|---|
| `text-hero` | clamp(3.25rem, 1.4rem + 9vw, 8rem) / 0.9 | 800 | Judul hero (3 baris). Maks 2.46 kali minimum |
| `text-display` | clamp(2.5rem, 1.2rem + 5.6vw, 5.5rem) / 0.94 | 800 | Judul section |
| `text-title` | clamp(1.5rem, 1.1rem + 1.6vw, 2.25rem) / 1.05 | 800 | Judul lembar, nama paket |
| `text-lead` | clamp(1.125rem, 1rem + 0.5vw, 1.375rem) / 1.5 | 400 | Sub hero, pengantar section |
| `text-body` | 1.0625rem / 1.6 | 400 | Isi (17px) |
| `text-small` | 0.9375rem / 1.5 | 400 | Catatan, keterangan |
| `text-receipt` | 0.875rem / 1.5 | 400 | Isi struk (DM Mono) |
| `text-caption` | 0.8125rem / 1.4 | 500 | Eyebrow, meta (DM Mono) |

Judul memakai `font-stretch: 68%`, `letter-spacing: -0.03em`, `text-wrap: balance`, `overflow-wrap: anywhere`. Eyebrow mono dengan tracking 0.02em, bukan huruf kapital lebar.

### 2.5 Spacing & Grid
- **Skala spacing:** 4, 8, 12, 16, 24, 32, 48, 56, 80, 112, 128, 144 px. Ritme section sengaja berganti: sumber 112, demo 128, harga 144, hasil pin penuh layar.
- **Padding halaman:** 20px di bawah `md`, 32px di `md`, 56px dari `lg`.
- **Lebar konten maksimum:** 1328px (isi 1216px di desktop). Hero dan CTA penuh lebar, isi tetap di 1328.
- **Breakpoint:** `sm` 640, `md` 768, `lg` 1024, `xl` 1280. Desain di 1440 dan 390; 768, 1024, 1920 diperiksa.

### 2.6 Bentuk, Elevasi, Material & Ilustrasi
**Bentuk**
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `radius-sm` | 4px | Tag bahasa, chip, struk kecil |
| `radius-md` | 8px | Tombol, stepper, toggle |
| `radius-lg` | 20px | Bingkai pratinjau saja, tidak dipakai di halaman |

Kertas struk tanpa radius; tepi bawahnya gerigi (9px per gigi). Satu-satunya "bulat" di halaman adalah titik logo.

**Elevasi** (satu arah cahaya dari atas)
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `shadow-1` | 0 1px 0 oklch(0.25 0.03 60 / 0.10), 0 1px 3px oklch(0.25 0.03 60 / 0.08) | Struk dan kartu mini di atas kertas |
| `shadow-2` | 0 2px 2px oklch(0.30 0.10 30 / 0.14), 0 10px 18px -8px oklch(0.30 0.10 30 / 0.38), 0 26px 40px -18px oklch(0.30 0.10 30 / 0.34) | Struk di atas bidang merah (bayangan bertinta merah tua) |
| `shadow-3` | 0 2px 3px oklch(0.10 0.01 60 / 0.30), 0 14px 24px -10px oklch(0.10 0.01 60 / 0.55), 0 40px 60px -26px oklch(0.10 0.01 60 / 0.55) | Lembar di atas bab tinta |

Tepi gerigi memotong `box-shadow`, jadi bayangan lembar dan struk dibuat dengan `filter: drop-shadow()` pada pembungkus (`.strip-wrap`, `.slip-w`, `.ptab-w`).

**Gradien & material**
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `gradient-hero` | radial-gradient(90% 70% at 72% 0%, var(--hero-glow) 0%, var(--hero) 55%, var(--hero-deep) 100%) | Hero dan CTA penutup; satu titik terang di atas struk |
| `grain-dark` | SVG feTurbulence butir gelap, opacity 0.07, `mix-blend-mode: multiply` | Di atas hero dan CTA |
| `grain-light` | SVG feTurbulence butir terang, opacity 0.06, `mix-blend-mode: screen` | Opsional di atas bab tinta (di pratinjau hanya pada contoh) |

Gradien hanya ada di dua bidang merah; hue tetap dalam keluarga merah-oranye, tanpa biru atau ungu. Grain hanya di blok merah, tidak di seluruh `body`.

**Ilustrasi & ikon**
- **Gaya ilustrasi:** garis 3px ink pada viewBox 80, sudut membulat, satu bidang isi bergeser 3px ke kanan bawah (efek cetak meleset) berwarna `hero-glow` atau `accent`. Dipakai di bab Sumber saja.
- **Daftar ilustrasi:** `ic-zoom` (jendela video, 80px desktop, 52px mobile), `ic-meet` (kisi rapat dengan dua peserta), `ic-room` (meja bundar dan tiga orang). Ketiganya generik, bukan logo Zoom atau Google.
- **Barcode:** batang SVG 64 batang, tinggi mengikuti fungsi gelombang suara, `aria-hidden`, di dasar struk demo, CTA, dan atas footer.
- **Ikon:** custom inline SVG garis 2.5px (menu 3 garis berbeda panjang, tutup, tambah, kurang, centang). Tanpa library ikon; hanya 5 ikon dan semuanya dekoratif atau berlabel pada tombolnya.

### 2.7 Motion
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `duration-fast` | 120ms | Hover, press tombol |
| `duration-base` | 220ms | Nav berganti tema, filter, akordeon, sheet |
| `duration-slow` | 420ms | Total harga, sheet masuk |
| `ease-out-expo` | cubic-bezier(0.16, 1, 0.3, 1) | Elemen masuk, stabilo |
| `ease-in-out-soft` | cubic-bezier(0.65, 0, 0.35, 1) | Perubahan warna |
| `ease-spring` | linear(0, 0.2 6%, 0.62 13%, 0.98 22%, 1.08 28%, 1.05 34%, 1.01 44%, 0.995 56%, 1) | Cadangan, tidak dipakai di default |
| `ease-print` | steps(24, end) | Umpan kertas hero dan CTA (2400ms) |

- **Pola masuk:** judul hero naik dari mask per baris; section lain memakai `data-reveal`: naik 28px dan fade 620ms `ease-out-expo`, sekali per elemen (IntersectionObserver, `threshold 0.08`, margin bawah -12 persen).
- **Transisi daftar → detail:** tidak ada (halaman tunggal).
- **Mikro-interaksi:** tombol hover naik 2px dengan bayangan keras 4px di bawah, ditekan turun 1px dan skala 0.98; tombol CTA hero dan penutup bergeser maksimal 5px ke arah kursor (hanya `hover: hover`); stabilo menyapu.
- **Kinerja:** hanya `transform` dan `opacity`, kecuali tiga pengecualian kecil: `clip-path` pada baris cetak demo (sekali), `grid-template-rows` pada akordeon (sekali per klik), warna latar nav (220ms). Tidak ada loop abadi. Satu-satunya animasi di atas 1200ms adalah umpan kertas hero (2400ms), bisa dilewati dengan klik dan tidak memblokir CTA.
- **Reduced motion:** `prefers-reduced-motion: reduce` mematikan semua animasi dan transisi (durasi 0.01ms), stage Hasil kembali tanpa pin dengan tiga lembar terbuka, struk hero tampil di posisi akhir, `data-reveal` langsung terlihat.

### 2.8 Implementasi Token
Gabungkan dengan `app/globals.css` hasil `shadcn init` (Tailwind v4): ganti blok `:root`, hapus blok `.dark`, pertahankan `@import "tailwindcss"` dan `@import "tw-animate-css"` bawaan. Light saja.

```css
@import "tailwindcss";
@import "tw-animate-css";
@custom-variant dark (&:is(.dark *));

:root {
  color-scheme: light;
  --background: #F7F5EF;
  --foreground: #17130F;
  --card: #FFFEFA;
  --card-foreground: #17130F;
  --popover: #FFFEFA;
  --popover-foreground: #17130F;
  --primary: #CC2A0E;
  --primary-foreground: #FFF8F0;
  --secondary: #ECE8DD;
  --secondary-foreground: #17130F;
  --muted: #ECE8DD;
  --muted-foreground: #5A5348;
  --accent: #FFE14A;
  --accent-foreground: #17130F;
  --border: #D8D2C3;
  --input: #837B6C;
  --ring: #17130F;
  --ring-inverse: #F7F5EF;
  --hero: #FF4B2B;
  --hero-glow: #FF6F47;
  --hero-deep: #EE4424;
  --hero-foreground: #17130F;
  --surface-ink: #1C1713;
  --surface-ink-foreground: #F7F5EF;
  --surface-ink-muted: #B9AE9E;

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 20px;
  --shadow-1: 0 1px 0 oklch(0.25 0.03 60 / .10), 0 1px 3px oklch(0.25 0.03 60 / .08);
  --shadow-2: 0 2px 2px oklch(0.30 0.10 30 / .14), 0 10px 18px -8px oklch(0.30 0.10 30 / .38), 0 26px 40px -18px oklch(0.30 0.10 30 / .34);
  --shadow-3: 0 2px 3px oklch(0.10 0.01 60 / .30), 0 14px 24px -10px oklch(0.10 0.01 60 / .55), 0 40px 60px -26px oklch(0.10 0.01 60 / .55);
  --gradient-hero: radial-gradient(90% 70% at 72% 0%, var(--hero-glow) 0%, var(--hero) 55%, var(--hero-deep) 100%);
  --grain-dark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .6 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  --grain-light: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .6 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  --duration-fast: 120ms;
  --duration-base: 220ms;
  --duration-slow: 420ms;
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out-soft: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-spring: linear(0, 0.2 6%, 0.62 13%, 0.98 22%, 1.08 28%, 1.05 34%, 1.01 44%, 0.995 56%, 1);
  --ease-print: steps(24, end);
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-ring-inverse: var(--ring-inverse);
  --color-hero: var(--hero);
  --color-hero-glow: var(--hero-glow);
  --color-hero-deep: var(--hero-deep);
  --color-hero-foreground: var(--hero-foreground);
  --color-surface-ink: var(--surface-ink);
  --color-surface-ink-foreground: var(--surface-ink-foreground);
  --color-surface-ink-muted: var(--surface-ink-muted);

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 20px;
  --font-display: var(--font-archivo), "Arial Narrow", sans-serif;
  --font-sans: var(--font-archivo), system-ui, sans-serif;
  --font-mono: var(--font-dm-mono), ui-monospace, monospace;

  --text-hero: clamp(3.25rem, 1.4rem + 9vw, 8rem);
  --text-hero--line-height: 0.9;
  --text-hero--letter-spacing: -0.03em;
  --text-hero--font-weight: 800;
  --text-display: clamp(2.5rem, 1.2rem + 5.6vw, 5.5rem);
  --text-display--line-height: 0.94;
  --text-display--letter-spacing: -0.03em;
  --text-display--font-weight: 800;
  --text-title: clamp(1.5rem, 1.1rem + 1.6vw, 2.25rem);
  --text-title--line-height: 1.05;
  --text-title--font-weight: 800;
  --text-lead: clamp(1.125rem, 1rem + 0.5vw, 1.375rem);
  --text-lead--line-height: 1.5;
  --text-body: 1.0625rem;
  --text-body--line-height: 1.6;
  --text-small: 0.9375rem;
  --text-small--line-height: 1.5;
  --text-receipt: 0.875rem;
  --text-receipt--line-height: 1.5;
  --text-caption: 0.8125rem;
  --text-caption--line-height: 1.4;
  --text-caption--font-weight: 500;
}

@layer base {
  * { @apply border-border outline-ring; }
  body { @apply bg-background text-foreground font-sans; font-size: var(--text-body); line-height: 1.6; }
  h1, h2, h3 { font-family: var(--font-display); font-stretch: 68%; font-weight: 800; letter-spacing: -0.03em; text-wrap: balance; overflow-wrap: anywhere; }
  :focus-visible { outline: 3px solid var(--ring); outline-offset: 3px; }
  [data-surface="hero"] { --btn-bg: var(--foreground); --btn-fg: var(--background); color: var(--hero-foreground); }
  [data-surface="paper"] { --btn-bg: var(--primary); --btn-fg: var(--primary-foreground); }
  [data-surface="ink"] { --btn-bg: var(--hero); --btn-fg: var(--hero-foreground); --ring: var(--ring-inverse); background: var(--surface-ink); color: var(--surface-ink-foreground); }
}

@media (prefers-reduced-motion: reduce) {
  *, ::before, ::after { animation-duration: 0.01ms !important; animation-delay: 0s !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; }
}
```

Catatan pakai: ring dan outline solid (`--ring` tidak transparan). Kelas motif (`.strip`, `.slip`, `.win`, `.paper`, `.mark`, `.torn`) ada di `@layer components` file yang sama; resepnya di 3.2.

---

## 3. Komponen

### 3.1 Komponen & Override
| Komponen | Library | Default library → diubah menjadi | Dipakai di |
|---|---|---|---|
| Button | shadcn/ui `Button` | h-9, `rounded-md`, hover `/90`, `outline-none` + `ring-ring/50` → h-12 (48px), px-6, `radius-md`, 600/17px, warna dari `--btn-bg` dan `--btn-fg` per `data-surface`, hover naik 2px + bayangan keras, fokus `outline` 3px solid; `lg` h-15 (60px) px-8 19px; varian `outline` = transparan + border 2px `currentColor`; `ghost` = tautan bergaris bawah 2px, tinggi 44px; `destructive`, `secondary`, `link` dihapus | Nav, Hero, Harga, CTA, Sheet |
| Accordion | shadcn/ui `Accordion` | border-b, chevron, `text-sm` → `type="single" collapsible`, pemicu min-h 64px grid `44px 1fr 44px`, nomor mono, ikon plus berputar 45 derajat, garis atas 2px `foreground` dan garis putus-putus 2px `input` antar item, judul 18 sampai 22px/700 | FAQ |
| Sheet | shadcn/ui `Sheet` | `side="right"`, `bg-background`, `shadow-lg` → `side="top"` dengan `h-dvh`, `bg-surface-ink`, tanpa bayangan, tautan `text-hero` 3rem, tombol tutup 48px | Menu mobile (nav) |
| ToggleGroup | shadcn/ui `ToggleGroup` | `variant="default"`, `h-9` → `type="single"` `variant="outline"`, item h-12 px-[18px], border 2px `input`, aktif `bg-foreground text-background`; nilai kosong diabaikan | Demo |
| Receipt (`Strip`) | custom | n/a | Demo, Harga, Sumber mini |
| PrintWindow | custom | n/a | Hero, CTA |
| StageScrub | custom | n/a | Hasil |
| Stepper | custom | n/a | Harga |
| Marker | custom | n/a | Hero, Sumber, Harga |
| Barcode | custom | n/a | Demo, CTA, Footer |

Tidak ada `Card` shadcn: kertas dibuat dengan elemen biasa + kelas motif agar tidak membawa `py-6`, `px-6`, `rounded-xl`.

### 3.2 Spesifikasi Komponen
#### Button
- **Ukuran:** default 48px, `lg` 60px (CTA hero dan CTA penutup), ghost 44px. Semua di atas 44px sentuh. Anggaran 390: CTA hero "Coba gratis" 160px, ghost "Lihat contoh hasilnya" disembunyikan di bawah `md` (satu CTA di hero mobile).
- **Warna per permukaan:** di `hero` tombol ink (`foreground` di atas `hero`, 5.54) dengan teks `background`; di kertas tombol `primary`; di `surface-ink` tombol `hero` dengan teks `hero-foreground`. Diatur oleh `data-surface` pada section, bukan prop.
- **State:** default / hover (`translateY(-2px)` + `0 4px 0` warna latar lebih gelap 55 persen) / focus-visible (outline 3px `ring`, offset 3px) / active (`translateY(1px) scale(0.98)`) / disabled (opacity 0.5, `cursor: not-allowed`) / loading tidak ada (tombol hanya tautan).
- **Aturan:** satu tombol primary per section; label kata kerja spesifik. Tombol Pro dan Tim memakai `outline`. Tombol nav "Coba gratis" muncul (opacity dan translate 6px, 220ms) hanya setelah hero lewat, tersembunyi dari pembaca layar saat belum terlihat (`visibility: hidden`).

#### Receipt (`Strip`)
- **Resep:** `<div class="strip-wrap"><div class="strip">…</div></div>`. `.strip { background: var(--card); padding: 28px 28px 44px; font: var(--text-receipt) var(--font-mono); border: 1px solid var(--border); --tear: 9px; mask: conic-gradient(from -45deg at bottom, #0000, #000 1deg 89deg, #0000 90deg) 50% / calc(var(--tear) * 2) 100%; }` dan `.strip-wrap { filter: drop-shadow(0 12px 14px oklch(0.25 0.03 60 / .16)); }`. Di bawah `md`: padding 20px 16px 36px, `--tear: 7px`.
- **Perilaku:** isi selalu teks asli. Tidak ada elemen interaktif di zona gerigi. Di zoom 200% padding tetap, teks membungkus.

#### PrintWindow
- **Ukuran:** desktop 436×600 (kertas 380 lebar) di kanan bawah hero; `lg` sampai `xl` 340 lebar; di bawah `lg` 360 lebar di tengah; di bawah `md` 300 lebar, tinggi jendela 290 (hero) dan 260 (CTA). Posisi: dasar jendela menempel garis tinta di dasar section (36px, 28px mobile).
- **Perilaku:** jendela `overflow: hidden`; kertas lebih tinggi dari jendela, hanya bagian atas terlihat setelah animasi (sisanya "tertahan di mesin"). `role="img"` dengan label ringkas; isi struk adalah teks DOM yang diulang di demo (5.3), jadi tidak kehilangan informasi.
- **Lewati:** `pointerdown` pada jendela menambah kelas yang memadatkan animasi menjadi 0.01ms.

#### StageScrub
- Kontainer `.stage` (tinggi 3 layar bila JS aktif dan lebar ≥ `lg`) berisi `.pin` (`position: sticky; top: 0; height: 100svh`). Tanpa JS atau di bawah `lg` stage berkinerja normal (`height: auto`). `--t`, `--k1..3` default 1.
- Anggaran lebar desktop: tiga lembar masing-masing (1216 − 2 × 40) / 3 = 378px; lembar memuat teks 17px tanpa potongan, diukur.

#### Stepper
- `output` mono 20px di antara dua tombol 48px; lebar total 156px (diukur di 390). Tombol kurang nonaktif di 2, tambah nonaktif di 50; `aria-label` "Kurangi anggota" dan "Tambah anggota"; `output` dikaitkan ke label "Jumlah anggota tim".
- **Terkontrol:** `useState<number>` di `PricingCalculator` (client), nilai awal 5; total dihitung dari state, ditampilkan oleh `Ticker`.

#### Marker (stabilo)
- `.mark::before { content: ""; position: absolute; left: -.05em; right: -.05em; top: 55%; bottom: .04em; background: var(--accent); z-index: -1; transform-origin: left; }` pada `.mark { position: relative; display: inline-block; isolation: isolate; }`. Animasi `scaleX(0)` ke 1. Teks tetap `foreground` di atas `accent` (14.19). Dipakai maksimal di 3 tempat: hero, baris Sumber aktif, harga Tim.

#### Barcode
- Fungsi `barcode(seed)` menghasilkan 64 `<rect>` dengan lebar 1 sampai 3 dan tinggi dari `0.22 + |0.4 sin(i × 0.52) + 0.3 sin(i × 1.37) + 0.2 cos(i × 0.21)|` (dipotong di 1), `preserveAspectRatio="none"`, `aria-hidden`. Warna `currentColor`.

#### Accordion
- Pemicu 350px lebar di 390 (diukur); judul dibungkus `h3` yang gayanya dinetralkan. Satu item terbuka sekaligus; item pertama terbuka awal. Tinggi panel beranimasi lewat `grid-template-rows` 0fr ke 1fr, 220ms.

---

## 4. Layout & Navigasi

### 4.1 Nav & footer
| Bagian | Mobile (di bawah `lg`) | Desktop (`lg` ke atas) |
|---|---|---|
| Nav | Sticky 60px (di bawah `md`) atau 72px: logo kiri, tombol menu 48px kanan; membuka Sheet penuh layar | Sticky 72px: logo kiri; Hasil, Harga, FAQ; tombol "Coba gratis" muncul setelah hero |
| Tema nav | Transparan di atas merah, kertas solid + garis `border` di bab kertas, tinta di bab Hasil dan footer | Sama |
| Footer | Kolom tunggal: logo, satu kalimat, tautan | Satu baris: logo + kalimat kiri, tautan kanan |

Urutan tumpuk (z-index): konten 0, garis tinta (hero, CTA) 2, jendela struk 3, celah jendela 4, nav 40, Sheet 60 (menutupi nav), skip link 90.

### 4.2 Struktur Navigasi
Jangkar: `/#hero`, `/#demo`, `/#sumber`, `/#hasil`, `/#tim`, `/#harga`, `/#faq`, `/#coba`, `/#footer`. Nav: Hasil (`/#hasil`), Harga (`/#harga`), FAQ (`/#faq`). Semua CTA "Coba gratis" menuju `/daftar` (aplikasi). Scroll halus ke jangkar dengan offset tinggi nav; `scroll-padding-top` 72px. Footer: Hasil, Harga, FAQ, `/privasi`, `/syarat`.

### 4.3 Pola Responsif
| Lebar | Perubahan |
|---|---|
| 1440 (desain utama) | Hero dua kolom (judul kiri, jendela struk kanan), Demo 5:6 dengan teks lengket, Hasil pin 300% dengan tiga lembar menyebar, Harga 5:7, FAQ 5:7, nav lengkap |
| `xl` 1280 sampai `lg` 1024 | Sama dengan 1440; jendela struk 340 lebar, judul CTA dibatasi sisa lebar |
| `md` 768 sampai di bawah `lg` | Semua grid satu kolom; hero bertumpuk (judul, lalu jendela struk di dasar), Hasil tanpa pin (lembar bertumpuk, muncul saat scroll), nav jadi tombol menu |
| 390 (desain mobile) | Padding 20px; hero 3 baris di 57.5px; ghost hero disembunyikan; baris Sumber ikon 52px; harga bertumpuk satu kolom |
| 1920 | Isi tetap di 1328; bidang merah dan tinta penuh lebar |

Hitungan hero di atas lipatan (diukur di browser): 1440×900, hero setinggi 900, judul berakhir di y 503, sub di 623, CTA di 719, jendela struk mulai y 257, garis tinta 864 sampai 900, tidak ada tumpang tindih. 390×844, hero setinggi 844, sub berakhir di y 379, CTA di 459, jendela struk mulai y 521, garis tinta 816 sampai 844.

---

## 5. Spesifikasi Halaman / Section / Layar

Aturan baca tiap section: tujuan satu kalimat, satu CTA primer atau tidak ada, wireframe, koreografi scroll, aset, reduced motion. Notasi wireframe: `[[ ]]` tombol primary, `[ ]` outline, `( )` ghost atau tautan. Tiap section terbaca dalam 5 detik.

### 5.1 Nav: `/#nav`
- **Tujuan:** memberi jalan pintas ke tiga bab tanpa bersaing dengan CTA hero.
- **Prioritas konten:** 1. logo 2. tautan 3. CTA (baru setelah hero).
- **Koreografi:** transparan di atas hero; setelah dasar nav melewati batas bab berganti tema 220ms (5 M5). CTA nav naik 6px dan fade 220ms.

```
┌───────────────────────────────────────────────────────────────┐
│ ● Rekam                         Hasil  Harga  FAQ  [[ Coba gratis ]] │
└───────────────────────────────────────────────────────────────┘
```
Mobile, menu tertutup dan menu terbuka (Sheet `side="top"`):
```
● Rekam                                    [ ☰ ]
┌──────────────────────────┐
│ ● Rekam            [ ✕ ] │
│ Hasil                    │
│ ───────────────────────  │
│ Harga                    │
│ ───────────────────────  │
│ FAQ                      │
│ Notulen rapat otomatis…  │
│ [[ Coba gratis ]]        │
└──────────────────────────┘
```
**Komponen:** Button, Sheet. **State:** tidak ada loading; menu terbuka menjebak fokus dan menutup dengan Esc atau tombol tutup, fokus kembali ke tombol menu.

### 5.2 Hero: `/#hero`
- **Tujuan:** dalam 3 detik orang paham Rekam mencetak notulen dari rapat, dan ada satu tombol untuk mencoba.
- **Prioritas konten:** 1. judul "Rapat selesai. Notulen sudah jadi." 2. struk yang tercetak 3. sub 4. CTA "Coba gratis" 5. tautan "Lihat contoh hasilnya".
- **Koreografi:** M1. Tidak ada scroll-jacking; hero hanya bergulir normal.
- **Aset:** struk HTML (6 baris transkrip, 3 tugas), `gradient-hero`, `grain-dark`.
- **Sub:** "Rekam merekam rapat Zoom, Google Meet, atau tatap muka, lalu mencetak transkrip Indonesia dan Inggris, ringkasan, dan daftar tugas."

```
1440×900
┌────────────────────────────────────────────────────────────────────────────┐
│ ● Rekam                                        Hasil  Harga  FAQ           │
│                                                                            │
│ Rapat selesai.                                     ┌────────────────┐      │
│ Notulen                                            │ REKAM · NOTULEN│      │
│ sudah jadi.                                        │ ID Dinda 00:12 │      │
│                                                    │ Oke, kita mulai│      │
│ Rekam merekam rapat Zoom, Google Meet, atau        │ EN Raka  00:31 │      │
│ tatap muka, lalu mencetak transkrip ...            │ We still have… │      │
│                                                    │ TUGAS [ ] Raka │      │
│ [[ Coba gratis ]]   ( Lihat contoh hasilnya )      └──────┬─────────┘      │
├────────────────────────────────────────────────────────────┴───────────────┤
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ garis tinta + celah ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
└────────────────────────────────────────────────────────────────────────────┘
```
```
390×844
┌──────────────────────────┐
│ ● Rekam            [ ☰ ] │
│ Rapat selesai.           │
│ Notulen                  │
│ sudah jadi.              │
│ Rekam merekam rapat Zoom,│
│ Google Meet, …           │
│ [[ Coba gratis ]]        │
│     ┌──────────────┐     │
│     │ REKAM · NOTU…│     │
│     │ ID Dinda 00:1│     │
│ ▓▓▓▓▓▓▓▓ celah ▓▓▓▓▓▓▓▓ │
└──────────────────────────┘
```
**Komponen:** Button, PrintWindow, Marker. **State:** JS gagal: struk tampil di posisi akhir (animasi hanya CSS, tanpa JS). Reduced motion: lihat M1.

### 5.3 Demo Dua Bahasa: `/#demo`
- **Tujuan:** membuktikan transkrip Indonesia dan Inggris dengan contoh yang bisa disaring.
- **Prioritas konten:** 1. judul "Dua bahasa, satu transkrip." 2. struk transkrip 3. filter.
- **CTA:** tidak ada tombol primer; section ini naratif.
- **Koreografi:** M2.
- **Aset:** struk 9 baris, barcode. Judul eyebrow mono "Transkrip".

```
1440
┌─────────────────────────────────────────────────────────┐
│ Transkrip                      ┌───────────────────────┐│
│ Dua bahasa,                    │ REKAM · TRANSKRIP     ││
│ satu transkrip.                │ ID Dinda        00:12 ││
│ Tiap baris ditandai bahasanya. │ Oke, kita mulai dari… ││
│ [ Semua ] [ Indonesia ] [ English ] EN Raka     00:31 ││
│ Menampilkan 9 dari 9 baris.    │ We still have two…    ││
│ (kolom kiri lengket)           │ … 9 baris + barcode   ││
└─────────────────────────────────────────────────────────┘
```
390: judul, filter (305 lebar dari 350), struk satu kolom 350 lebar; baris 94px, 3 baris terlihat tanpa scroll kedua.
**Komponen:** ToggleGroup, Receipt, Barcode.

**State:**
| State | Tampilan | Teks |
|---|---|---|
| Semua | Semua baris penuh | "Menampilkan 9 dari 9 baris." |
| Indonesia | 5 baris ID penuh, 4 EN redup | "Menampilkan 5 dari 9 baris." |
| English | 4 baris EN penuh, 5 ID redup | "Menampilkan 4 dari 9 baris." |

### 5.4 Sumber Rapat: `/#sumber`
- **Tujuan:** menunjukkan bahwa rapat dari Zoom, Google Meet, dan tatap muka sama-sama bisa dicetak.
- **Prioritas konten:** 1. tiga nama raksasa 2. satu kalimat per sumber 3. tautan "Lihat hasilnya".
- **CTA:** tautan ghost ke `/#hasil` (tidak ada tombol primer).
- **Koreografi:** baris yang melewati tengah layar mendapat stabilo (M5); tanpa pin atau parallax.
- **Aset:** `ic-zoom`, `ic-meet`, `ic-room`. Latar `secondary` (bab berganti).

```
1440
┌───────────────────────────────────────────────────────────┐
│ Sumber rapat                                              │
│ Dari mana saja rapatnya.                 ( Lihat hasilnya )│
│ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - │
│ [ico]  Zoom           Rapat video dengan klien atau tim…  │
│ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - │
│ [ico]  Google Meet    Standup harian dan rapat mingguan…  │
│ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - │
│ [ico]  Tatap muka     Rapat di ruangan, dengan kopi…      │
└───────────────────────────────────────────────────────────┘
```
390: ikon 52px + nama (maksimal "Google Meet" 198px dari 274), kalimat di bawah nama.
**Komponen:** Marker, Button (ghost).

### 5.5 Hasil: `/#hasil`
- **Tujuan:** menunjukkan satu rapat menjadi tiga hasil yang jelas.
- **Prioritas konten:** 1. "Satu rapat, tiga lembar." 2. tiga lembar 3. centang tugas.
- **CTA:** tidak ada tombol primer di bab ini (CTA hadir di nav, harga, dan penutup).
- **Koreografi:** M3.
- **Aset:** tiga lembar (Transkrip 3 baris, Ringkasan 3 poin, Tugas 3 centang). Latar `surface-ink`.

```
1440 (pin 300%, p = 0)           (p ≥ 0.56)
        ┌────────────┐            ┌────────┐ ┌────────┐ ┌────────┐
        │ Transkrip  │            │Transkr.│ │Ringkas.│ │ Tugas  │
        │ (lembar 2,3│            │ 3 baris│ │ 3 poin │ │ ☑ ☑ ☑  │
        │  tertumpuk)│            └~~~~~~~~┘ └~~~~~~~~┘ └~~~~~~~~┘
        └────────────┘
```
390: tiga lembar tertumpuk vertikal, tiap lembar 350 lebar, muncul saat scroll.
**Komponen:** StageScrub, Receipt.

### 5.6 Untuk Siapa: `/#tim`
- **Tujuan:** pembaca mengenali timnya sendiri (startup atau agency).
- **Prioritas konten:** 1. "Untuk tim yang rapatnya banyak." 2. Startup 3. Agency 4. dua kartu mini contoh.
- **CTA:** tidak ada.
- **Koreografi:** `data-reveal` per kolom; kolom kedua turun 112px (asimetris, bukan kartu sejajar).
- **Aset:** kartu mini berputar -1 dan 1.4 derajat. Teks "CONTOH · SPRINT PLANNING" dan "CONTOH · BRIEFING KLIEN" menandai data contoh.

```
1440
┌─────────────────────────────────────────────────────────┐
│ Untuk siapa                                             │
│ Untuk tim yang rapatnya banyak.                         │
│ Startup  (7 kolom)                                      │
│ Sprint planning, standup…               Agency (5 kol.) │
│ ┌ CONTOH · SPRINT PLANNING ┐            Briefing klien… │
│ └──────────────────────────┘            ┌ CONTOH ... ┐  │
└─────────────────────────────────────────────────────────┘
```
390: satu kolom, Startup lalu Agency.
**Komponen:** Receipt (mini).

### 5.7 Harga: `/#harga`
- **Tujuan:** pembaca menghitung biaya timnya sendiri dan memilih paket.
- **Prioritas konten:** 1. tiga paket dengan harga 2. kalkulator Tim 3. catatan.
- **CTA primer:** "Coba gratis" di baris Gratis; Pro dan Tim "Pilih Pro", "Pilih Tim" (outline).
- **Koreografi:** M4. Struk harga muncul sekali dengan `data-reveal`.
- **Aset:** struk harga bergerigi di bawah, stabilo pada Rp249.000.
- **Data:** Gratis Rp0 · Pro Rp99.000 per bulan · Tim Rp249.000 per user per bulan. Contoh: 5 anggota × Rp249.000 = Rp1.245.000 per bulan.

```
1440
┌────────────────────────────────────────────────────────────┐
│ Harga                      ┌──────────────────────────────┐│
│ Harga bulanan,             │ REKAM · DAFTAR HARGA         ││
│ dicetak apa adanya.        │ Gratis                  Rp0  ││
│ Mulai gratis. Kalau…       │ [[ Coba gratis ]]            ││
│ Semua harga dalam rupiah…  │ - - - - - - - - - - - - - -  ││
│                            │ Pro            Rp99.000      ││
│                            │ [ Pilih Pro ]                ││
│                            │ Tim          Rp249.000       ││
│                            │ Anggota [−] 5 [+]            ││
│                            │ TOTAL / BULAN   Rp1.245.000  ││
│                            │ [ Pilih Tim ]                ││
│                            └~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~┘│
└────────────────────────────────────────────────────────────┘
```
390: satu kolom; baris paket: nama, harga (maks "Rp249.000" 133px dari 314), deskripsi, tombol.
**Komponen:** Receipt, Stepper, Button, Marker.

**State:**
| State | Tampilan | Teks |
|---|---|---|
| Anggota di batas bawah (2) | Tombol kurang nonaktif | "2 anggota × Rp249.000" total Rp498.000 |
| Anggota di batas atas (50) | Tombol tambah nonaktif | "50 anggota × Rp249.000" total Rp12.450.000 |

### 5.8 FAQ: `/#faq`
- **Tujuan:** menjawab pertanyaan paling awal tanpa membuat orang menulis ke siapa pun.
- **Prioritas konten:** 1. "Sebelum mencoba." 2. empat pertanyaan.
- **CTA:** tidak ada.
- **Koreografi:** satu item terbuka; membuka/menutup 220ms.
- **Isi:** (1) "Rekam bisa merekam rapat apa saja?" Rapat Zoom, Google Meet, dan tatap muka. (2) "Apa yang saya dapat setelah rapat?" Transkrip Indonesia dan Inggris, ringkasan, daftar tugas, disusun otomatis. (3) "Berapa harganya?" Harga tiga paket dan contoh 5 anggota. (4) "Kami agency kecil. Paket mana yang cocok?" Pro untuk satu orang, Tim untuk beberapa orang dan menagih per anggota.

```
1440
┌─────────────────────────────────────────────────────────┐
│ FAQ                                                     │
│ Sebelum mencoba.     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                      01  Rekam bisa merekam rapat…  ✕  │
│                          Rapat Zoom, Google Meet…       │
│                      - - - - - - - - - - - - - - - - - │
│                      02  Apa yang saya dapat…        +  │
└─────────────────────────────────────────────────────────┘
```
390: judul di atas, daftar penuh lebar (350).
**Komponen:** Accordion.

### 5.9 CTA Penutup: `/#coba`
- **Tujuan:** satu ajakan terakhir tepat setelah pembaca selesai membaca harga dan FAQ.
- **Prioritas konten:** 1. "Rapat berikutnya, sudah ada yang mencatat." 2. tombol 3. struk penutup.
- **Koreografi:** M1 (komponen PrintWindow sama): struk "Terima kasih. Sampai rapat berikutnya." dicetak saat 35 persen jendela terlihat.
- **Aset:** `gradient-hero`, `grain-dark`, barcode, label "Contoh struk · bukan transaksi".

```
1440
┌────────────────────────────────────────────────────────────┐
│ Rapat berikutnya,                       ┌─────────────┐    │
│ sudah ada yang                          │ Terima kasih│    │
│ mencatat.                               │ ||||||||||| │    │
│ Coba Rekam di satu rapat…               └──────┬──────┘    │
│ [[ Coba gratis ]]                              │           │
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ garis tinta + celah ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
└────────────────────────────────────────────────────────────┘
```
390: judul 48px, tombol 56px, jendela struk 300 lebar di dasar.
**Komponen:** Button, PrintWindow, Barcode.

### 5.10 Footer: `/#footer`
- **Tujuan:** menutup halaman dengan tautan yang memang ada.
- **Isi:** barcode gelombang di atas, logo, "Notulen rapat otomatis untuk tim Indonesia.", Hasil, Harga, FAQ, Kebijakan Privasi, Syarat Layanan, "© 2026 Rekam".
```
1440
│ ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| │
│ ● Rekam                          Hasil  Harga  FAQ  Privasi  Syarat │
│ Notulen rapat otomatis untuk tim Indonesia.            © 2026 Rekam │
```
390: logo, kalimat, tautan bertumpuk berjarak 44px. **Komponen:** Barcode, tautan.

### 5.11 Halaman pendukung
- `/privasi` dan `/syarat`: halaman teks panjang memakai tipografi `text-body` dengan lebar baris 65ch, header dan footer sama; isi dari tim hukum (wajib ada sebelum rilis).
- `/daftar`: aplikasi Rekam, di luar dokumen ini.
- 404 dan 500: lihat 6.3.

---

## 6. Feedback & State Global

### 6.1 Pola Loading
Halaman statis, tidak ada skeleton. Font dimuat `display: swap`. Tombol CTA adalah tautan biasa, tanpa state pending. Kalkulator tidak memanggil jaringan.

### 6.2 Pesan Error
| Kondisi | Pesan ke user | Ditampilkan sebagai |
|---|---|---|
| Anggota Tim di bawah 2 | Tombol kurang nonaktif; keterangan "Paket Tim untuk 2 anggota atau lebih." di `aria-describedby` stepper | Teks `text-small` di bawah stepper |
| Anggota Tim di atas 50 | Tombol tambah nonaktif; keterangan "Butuh lebih dari 50 anggota? Hubungi kami lewat halaman daftar." | Teks `text-small` di bawah stepper |

Form validasi tidak ada di halaman ini (CTA membuka `/daftar`).

### 6.3 Halaman Sistem
| Kondisi | Tampilan | Teks & aksi |
|---|---|---|
| Halaman tidak ditemukan (404) | Latar `hero`, struk kosong bergerigi dengan satu baris | Judul "Struk ini tidak ada." sub "Alamat yang kamu buka tidak ditemukan." tombol `[[ Kembali ke beranda ]]` |
| Error tak terduga (`error.tsx`) | Latar `surface-ink`, lembar kertas | Judul "Mesin cetaknya macet." sub "Ada yang salah di sisi kami. Muat ulang halaman ini." tombol `[[ Muat ulang ]]` |
| Offline | Banner kertas di atas halaman | "Tidak ada koneksi. Beberapa bagian mungkin belum termuat." |

### 6.4 Sukses & Konfirmasi
Tidak ada toast atau aksi tulis di halaman. Satu-satunya perpindahan adalah tautan ke `/daftar`.

---

## 7. Konten & Copywriting

### 7.1 Gaya Bahasa
Kamu (bukan Anda), kalimat pendek dengan subjek jelas ("Rekam merekam rapat…"), santai tapi tidak bercanda soal pekerjaan orang. Tanpa kata hiperbola, tanpa klaim jumlah pengguna, tanpa emoji, tanpa tanda pisah panjang. Metafora struk dipakai di judul dan label (struk, cetak, sobek, lembar), tidak di tombol.

### 7.2 Glosarium
| Istilah dipakai | Jangan pakai | Catatan |
|---|---|---|
| Rapat | Meeting | Kecuali "Google Meet" |
| Notulen | Minutes, catatan rapat | Di judul; di isi boleh "transkrip, ringkasan, daftar tugas" |
| Transkrip | Teks rekaman | |
| Tugas | Action item | Daftar tugas |
| Coba gratis | Daftar sekarang, Mulai | Satu label CTA di seluruh halaman |
| Paket | Plan, tier | Gratis, Pro, Tim |

### 7.3 Format
- **Uang:** `Rp99.000` (tanpa spasi, titik ribuan); tarif ditulis "per bulan" dan "per user per bulan".
- **Waktu transkrip:** `00:12` (menit:detik).
- **Tanggal:** `Sel 13 Okt 2026` di struk, `Rabu 14 Okt` di tugas.
- **Label data contoh:** "data contoh" di struk, "CONTOH ·" di kartu mini.

---

## 8. Aksesibilitas
- **Keyboard:** urutan tab mengikuti urutan visual; ToggleGroup memakai panah (roving tabindex); Accordion memakai Enter dan spasi; Sheet menjebak fokus, Esc menutup, fokus kembali ke tombol menu. Skip link "Lewati ke isi" muncul saat fokus.
- **Dokumen:** `<html lang="id">`; transkrip berbahasa Inggris diberi `lang="en"`; judul halaman "Rekam: transkrip, ringkasan, dan tugas dari setiap rapat"; satu `h1`; `h2` per section berurutan; landmark `header`, `nav`, `main`, `footer`.
- **Dekoratif:** barcode, ikon sumber, gigi gerigi, grain, dan stabilo `aria-hidden` atau CSS murni. Struk hero `role="img"` dengan label karena animasinya; isinya diulang sebagai teks di 5.3.
- **Pembaca layar:** total harga diumumkan lewat wilayah `aria-live="polite"` terpisah; angka animasi `aria-hidden`; jumlah baris tersaring diumumkan lewat `aria-live` yang sama dengan catatan filter.
- **Gerak:** `prefers-reduced-motion` ditangani penuh (2.7); tidak ada konten yang hanya muncul lewat animasi.
- **Zoom 200%:** diuji di lebar viewport 236px (batas terkecil emulator): tidak ada scroll horizontal; kelas judul memakai `overflow-wrap: anywhere`.

---

## 9. Catatan Implementasi
- **Library komponen:** shadcn/ui; install `button`, `accordion`, `sheet`, `toggle-group`. Ikon tidak memakai library (SVG inline). Motion: CSS murni plus dua hook kecil; paket `motion` tidak diperlukan.
- **Hook/utilitas tambahan:** `useStage` untuk M3, ditulis di `components/stage.tsx`:
```tsx
"use client";
import { useEffect, useRef } from "react";
const clamp = (v: number) => Math.min(1, Math.max(0, v));
const ease = (t: number) => 1 - Math.pow(1 - t, 3);
export function useStage(reduced: boolean) {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const el = ref.current; if (!el) return;
    const pinned = () => getComputedStyle(el.firstElementChild as Element).position === "sticky";
    const run = () => {
      const vh = window.innerHeight, r = el.getBoundingClientRect();
      let p = 1;
      if (!reduced) p = pinned() ? clamp(-r.top / Math.max(1, r.height - vh)) : clamp((vh * 0.85 - r.top) / (vh * 0.7));
      el.style.setProperty("--t", String(ease(clamp((p - 0.14) / 0.42))));
      [0.62, 0.72, 0.82].forEach((s, i) => el.style.setProperty(`--k${i + 1}`, String(clamp((p - s) / 0.1))));
    };
    let raf = 0;
    const on = () => { if (!raf) raf = requestAnimationFrame(() => { raf = 0; run(); }); };
    run(); window.addEventListener("scroll", on, { passive: true }); window.addEventListener("resize", on);
    return () => { window.removeEventListener("scroll", on); window.removeEventListener("resize", on); };
  }, [reduced]);
  return ref;
}
```
- **Pola form:** tidak ada form. Kalkulator memakai `useState` di client component `PricingCalculator`; section lain server component.
- **Ikon:** SVG inline, tidak ada library; ukuran 22 sampai 24px; hanya untuk menu, tutup, tambah, kurang, centang.
- **Font loading:** `next/font/google`: `Archivo({ subsets: ["latin"], axes: ["wdth"], variable: "--font-archivo", display: "swap" })` (bobot 800 dan 400 sampai 600 lewat sumbu variabel) dan `DM_Mono({ subsets: ["latin"], weight: ["400", "500"], variable: "--font-dm-mono", display: "swap" })`; tempel variabelnya di `<html>`.
- **Lokasi file:** token di `app/globals.css`; komponen halaman di `components/landing/` (`hero.tsx`, `demo.tsx`, `sources.tsx`, `results.tsx`, `who.tsx`, `pricing.tsx`, `faq.tsx`, `closing.tsx`, `site-footer.tsx`); `components/ui/` hanya komponen shadcn.
- **Anggaran performa:** LCP di bawah 2.5s (LCP = judul hero, teks; tidak ada gambar hero), CLS di bawah 0.1 (jendela struk dan font punya ukuran tetap), INP di bawah 200ms; JS klien hanya untuk nav, filter demo, kalkulator, akordeon, stage Hasil. Tanpa gambar bitmap; seluruh visual adalah HTML dan SVG. Maksimal 2 keluarga font (Archivo, DM Mono), subset Latin.
- **SEO:** `metadata.title` "Rekam: transkrip, ringkasan, dan tugas dari setiap rapat"; description "Rekam merekam rapat Zoom, Google Meet, dan tatap muka, lalu membuat transkrip Indonesia dan Inggris, ringkasan, dan daftar tugas. Mulai gratis."; Open Graph image berupa struk Rekam 1200×630 (dibuat dari HTML, berlabel contoh); teks asli di DOM; `theme-color` ikut bab aktif.
- **Override Sheet dan Accordion di Tailwind v4:** buang `outline-none` bawaan pada Button, pemicu Accordion, dan ToggleGroupItem, ganti `focus-visible:outline-3 focus-visible:outline-solid focus-visible:outline-offset-3`; `Sheet` memakai `side="top"` (prop, bukan kelas) dan `SheetTitle` tersembunyi secara visual untuk pembaca layar.
- **Jangan:** grid tiga kartu fitur berikon, bar logo "Dipercaya oleh", testimoni atau angka pengguna karangan, mockup laptop miring, gradien ungu-biru, pop-up penutup layar, scroll-jacking di luar stage Hasil, video autoplay, loop animasi abadi, tombol dengan panah dekoratif, badge "Terpopuler", badge kecil di atas judul hero, ikon AI (bintang, percikan), emoji.
