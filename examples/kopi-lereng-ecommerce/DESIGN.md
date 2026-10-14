# DESIGN: Kopi Lereng

> Toko online kopi yang terasa seperti dinding ukir tongkonan di pagi hari: soga, arang, kapur, dan kuning, untuk pecinta kopi urban 25 sampai 40 tahun yang memilih biji di HP.

**Draf cepat** (mode cepat: bagian 1, 2, 3 lengkap; bagian 4 sampai 9 hanya poin penting).

| | |
|---|---|
| Versi | 0.1 (draf cepat) |
| Tanggal | 2026-10-14 |
| Berdasarkan | Brief user (tanpa PRD): toko online roastery Kopi Lereng, Toraja |
| Jenis produk | E-commerce / toko online (profil 4), dengan beranda bergaya landing page |
| Platform & stack | Web responsif, desain di 1440, 1024, 768, 390 px · HTML/CSS polos (token lewat `tokens.css`) |

---

## 1. Arah Visual

### 1.1 Konteks Pemakaian
Pecinta kopi urban 25 sampai 40 tahun: membuka dari HP (tautan Instagram, pesan teman), memutuskan lot mana dalam beberapa menit, sering membandingkan tiga lot. Sebagian membeli rutin lewat langganan bulanan. Di laptop mereka membaca cerita petani dan cara seduh dengan tenang.

### 1.2 Konsep & Kepribadian
- **Konsep:** Dinding Tongkonan. Toko terasa seperti dinding ukir sebuah tongkonan di pagi hari: bidang soga, hitam arang, putih kapur, dan kuning, dengan matahari terukir (medali) sebagai matahari toko. Diambil dari logika pola ukir Toraja (ritme, simetri, tangga), bukan salinan motif sakral.
- **Level ambisi:** Spektakuler
- **Tiga kata sifat:** berakar, hangat, tegas
- **Bukan:** etnik klise (pita merah-emas, ikon rumah adat), mewah emas-di-hitam, grid kartu toko generik
- **Kepadatan informasi:** sedang. Beranda lapang dan bergambar; halaman produk padat informasi tetapi tertata (lot, gilingan, cara beli, harga dalam satu layar).
- **Motif khas:** tumpal (segitiga berjajar) sebagai pita atas/bawah, label kemasan, dan pembatas; medali matahari sebagai objek signature.

### 1.3 Keputusan & Alasan
| Keputusan | Pilihan | Alasan |
|---|---|---|
| Konsep terpilih | A "Dinding Tongkonan" (keluarga A3 Nusantara Kontemporer) dari 3 konsep di `design-concepts.html` | User bilang "terserah". Penilaian juri independen (subagen) menaruh A di peringkat 1 (dampak visual 8,5), diikuti C Risograph dan B Log Sangrai; penilaian sendiri sama. Objek signature paling ownable dan paling berakar pada asal produk. |
| Konsep ditolak | B "Log Sangrai" (F2 Generatif dari Data), C "Poster Pasar Subuh" (C2 Risograph) | B terlalu mirip dasbor, kurang menumbuhkan keinginan memiliki; C kuat tetapi judul besar menutupi produk. |
| Mode warna | Warna-penuh: arang sebagai dasar, bidang soga dan kapur sebagai panggung | Produk hitam/kuning tampil menonjol di soga; arang menenangkan layar kerja (PDP, keranjang). |
| Pendekatan layout | Mobile-first, dirancang juga di 1440 | Sebagian besar pembeli datang dari HP. |
| Gaya bentuk | Radius 0, bidang datar, relief ukir halus hanya di objek signature | Menyatu dengan bahasa ukiran: sudut tegas, pola berulang. |

### 1.4 Perlu Konfirmasi
| Keputusan | Default yang dipakai sekarang | Alternatif |
|---|---|---|
| Foto produk asli | Ilustrasi kemasan SVG sebagai pengganti | Foto produk satu latar, rasio 4:5 |
| Kebijakan ongkir dan retur | Tidak ditulis di UI; "Ongkir dihitung di keranjang" | Teks kebijakan dari pemilik toko |
| Data lot (asal, catatan rasa, tanggal sangrai) | Data contoh, ditandai di preview | Data resmi dari roastery |
| Motif ukir | Terinspirasi logika pola, tanpa motif sakral | Konsultasi pengrajin/komunitas Toraja sebelum rilis |
| Pembayaran dan pengiriman | Belum dirancang di draf ini | Penyedia sesuai pilihan pemilik toko |

### 1.6 Momen Signature
| # | Momen | Pemicu | Kenapa penting bagi user | Mockup |
|---|---|---|---|---|
| M1 | Medali terukir (hero beranda) | Membuka beranda | Kesan pertama: toko ini punya jiwa, bukan template | `design-preview.html#m1` |
| M2 | Ganti lot | Memilih tab lot di halaman produk | Membandingkan tiga lot terasa seperti memegang kemasannya | `design-preview.html` bagian Halaman produk |
| M3 | Masuk keranjang | Menekan Tambah ke keranjang | Kepastian fisik bahwa kopi masuk | Hitungan keranjang di preview; animasi terbang belum ada di preview |
| M4 | Pesanan terkonfirmasi | Pembayaran sukses | Perayaan tenang yang meyakinkan | Belum ada di preview mode cepat |

#### M1 · Medali terukir
- **Komposisi:** bidang `primary` penuh; medali 780 px (desktop) terpotong tepi kanan; kemasan Sapan menembus tepi kiri medali; judul tiga baris rata kiri; pita tumpal di dasar.
- **Timeline motion:** 0ms medali berputar dari −28° dan membesar dari 0,9, 1500ms `ease-out-expo` · 90ms, 180ms judul baris 2 dan 3 naik 22px (800ms) · 320ms paragraf dan CTA · 520ms kemasan jatuh 46px (900ms) · 520ms baris harga. Total ≤ 1500ms; tidak memblokir input.
- **Aset:** medali SVG (48 tumpal, 24 berlian bertingkat, 16 sinar bertangga, biji kopi di pusat) dengan filter relief `feDiffuseLighting`; kemasan SVG dengan filter crinkle.
- **Reduced motion:** tampil langsung di posisi akhir; tanpa rotasi dan jatuh.
- **Resep:** keadaan akhir adalah CSS default; `@keyframes from` hanya mendefinisikan titik awal, dipasang lewat kelas `.play` dengan `animation-fill-mode: backwards`.

#### M2 · Ganti lot
- **Komposisi:** panggung `primary` dengan medali besar; kemasan 340 px; tab lot di panel kanan.
- **Timeline motion:** kemasan baru jatuh 46px dari atas, 700ms `ease-out-expo`; nama dan harga berganti seketika (tanpa animasi, aksi berulang).
- **Aset:** tiga kemasan SVG (arang, soga, kuning) dengan label kapur yang sama.
- **Reduced motion:** kemasan berganti tanpa gerak.
- **Resep:** tiga kemasan ada di DOM, yang tidak aktif `hidden`; JS hanya mengganti atribut `hidden` dan menambah kelas `.swap` sesaat.

#### M3 · Masuk keranjang
- **Komposisi:** tombol Tambah tetap di tempat; ikon keranjang di header menerima hitungan baru.
- **Timeline motion:** hitungan membesar 1,25 lalu kembali, 500ms spring `cubic-bezier(.3,1.4,.5,1)`; kemasan mini terbang ke ikon keranjang 420ms (hanya desktop).
- **Aset:** salinan kemasan 48 px.
- **Reduced motion:** hanya hitungan berganti.
- **Resep:** salinan kemasan di-`transform` dari posisi tombol ke ikon; hapus dari DOM saat selesai.

#### M4 · Pesanan terkonfirmasi
- **Komposisi:** bidang `primary` penuh, medali di tengah, kode pesanan besar, satu kalimat tenang.
- **Timeline motion:** pita tumpal tergambar kiri ke kanan 600ms; medali muncul 900ms; kode pesanan 300ms. Total ≤ 1200ms, bisa dilewati dengan tap.
- **Aset:** medali yang sama dengan M1, tanpa kemasan.
- **Reduced motion:** tampil langsung.
- **Resep:** `clip-path: inset()` dari `from` pada pita tumpal; keadaan akhir default.

---

## 2. Design Tokens

### 2.1 Warna
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `background` | #17110E | Latar halaman (arang) |
| `foreground` | #F4EDE0 | Teks utama di atas `background` (kapur) |
| `muted` | #241A15 | Permukaan terangkat di atas `background` |
| `muted-foreground` | #CDBFAE | Teks sekunder, keterangan |
| `border` | #4A3B32 | Garis pemisah dekoratif |
| `input` | #8A7767 | Border kontrol (chip, opsi, stepper), ≥ 3.0 terhadap `background` |
| `primary` | #A22E1D | Bidang hero (soga), bar beli lengket, panggung produk |
| `primary-foreground` | #F4EDE0 | Teks di atas `primary` |
| `primary-deep` | #7C1F12 | Hover dan pressed pada bidang `primary` |
| `accent` | #E2A71A | Aksen kuning: kata penekanan besar, indikator terpilih, ring |
| `accent-foreground` | #17110E | Teks di atas `accent` |
| `ring` | #E2A71A | Focus ring (solid) di atas `background` dan `muted` |
| `surface-light` | #F4EDE0 | Panel terang (panel lot ketiga, label kemasan) |
| `surface-light-foreground` | #17110E | Teks di atas `surface-light` |
| `success` | #8FD3A1 | Teks dan ikon stok tersedia di atas `background` |
| `warning` | #F0B957 | Teks dan ikon stok menipis |
| `destructive` | #F29A8B | Teks dan ikon stok habis, pesan error |

Mode warna: satu mode (warna-penuh), tidak ada varian terang/gelap terpisah.

### 2.2 Warna Status
| Status | Label UI | Latar | Teks | Ikon |
|---|---|---|---|---|
| Stok tersedia | Tersedia | `background` | `success` | centang |
| Stok menipis | Menipis · sisa N kantong | `background` | `warning` | segitiga |
| Stok habis | Habis | `background` | `destructive` | silang |

Status pesanan (menunggu bayar, dikemas, dikirim, selesai, batal) belum dirancang di draf cepat; akan memakai pola badge yang sama (ikon + label + token).

### 2.3 Tabel Kontras
| Teks / elemen | Latar | Rasio | Normal (4.5) | Besar / non-teks (3.0) |
|---|---|---|---|---|
| `foreground` | `background` | 16.06 | PASS | PASS |
| `muted-foreground` | `background` | 10.38 | PASS | PASS |
| `muted-foreground` | `muted` | 9.45 | PASS | PASS |
| `foreground` | `muted` | 14.62 | PASS | PASS |
| `primary-foreground` | `primary` | 6.12 | PASS | PASS |
| `primary-foreground` | `primary-deep` | 8.75 | PASS | PASS |
| `accent` | `background` | 8.71 | PASS | PASS |
| `accent` | `muted` | 7.92 | PASS | PASS |
| `accent` | `primary` | 3.32 | FAIL | PASS |
| `accent-foreground` | `accent` | 8.71 | PASS | PASS |
| `surface-light-foreground` | `surface-light` | 16.06 | PASS | PASS |
| `input` (border) | `background` | 4.38 | n/a | PASS |
| `input` (border) | `muted` | 3.98 | n/a | PASS |
| `ring` | `background` | 8.71 | n/a | PASS |
| `success` | `background` | 10.69 | PASS | PASS |
| `warning` | `background` | 10.49 | PASS | PASS |
| `destructive` | `background` | 8.70 | PASS | PASS |

`accent` di atas `primary` hanya untuk teks besar (≥ 24px bold), misalnya kata "jujur." di judul hero. Garis `border` bersifat dekoratif.

### 2.4 Tipografi
- **Font display:** Familjen Grotesk 700 (Google Fonts), fallback `"Arial Narrow", sans-serif`. Tegas dan manusiawi, cocok dengan potongan tegas ukiran; hanya untuk judul, harga, label, dan tombol.
- **Font teks:** Literata 400/500 (Google Fonts), fallback `Georgia, serif`. Serif hangat yang sangat terbaca untuk deskripsi dan cerita petani.
- **Angka:** `font-variant-numeric: tabular-nums` untuk harga dan jumlah; format `Rp95.000`.

| Token | Ukuran / line-height | Weight | Dipakai untuk |
|---|---|---|---|
| `text-hero` | clamp(2.75rem, 1.2rem + 6.2vw, 6.25rem) / 0.94 | 700 | Judul hero beranda (tracking −0,035em) |
| `text-display` | clamp(2.5rem, 1.4rem + 4vw, 4.5rem) / 1 | 700 | Nama lot di halaman produk, judul section |
| `text-title` | 1.5rem / 2rem | 700 | Judul panel, harga di list |
| `text-body` | 1rem / 1.625rem | 400 | Teks utama (Literata), minimal 16px di mobile |
| `text-small` | 0.875rem / 1.25rem | 400 | Keterangan, catatan |
| `text-caption` | 0.75rem / 1rem | 600 | Label huruf besar, tracking 0,2em (Familjen Grotesk) |

### 2.5 Spacing & Grid
- **Skala spacing:** 4, 8, 12, 16, 24, 32, 48, 72, 96 px.
- **Padding halaman:** mobile 16px, desktop 72px.
- **Lebar konten maksimum:** 1440px untuk hero dan panel penuh; 1120px untuk teks bacaan (cerita, cara seduh).
- **Breakpoint:** 390 (mobile), 768 (tablet), 1024 (laptop), 1440 (desktop); ditulis literal di media query.

### 2.6 Bentuk, Elevasi, Material & Ilustrasi
**Bentuk**
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `radius-none` | 0 | Semua tombol, input, panel (bahasa ukiran) |
| `radius-pill` | 50% | Hanya indikator radio |

**Elevasi** (satu arah cahaya dari kiri atas; bayangan hanya untuk objek, bukan kartu)
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `shadow-object` | drop-shadow(0 24px 22px rgba(30, 4, 0, 0.45)) | Kemasan di atas bidang `primary` |
| `shadow-medal` | drop-shadow(0 34px 44px rgba(40, 6, 0, 0.5)) | Medali di atas bidang `primary` |

**Gradien & material**
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `texture-carve` | SVG `feTurbulence` (baseFrequency .02 .16, 3 oktaf) + `feDiffuseLighting` (azimuth 225, elevation 58) + `feComposite` arithmetic k1 1.2 | Relief ukir pada medali |
| `texture-crinkle` | `feTurbulence` (.012 .05) + `feDiffuseLighting` (elevation 68), k1 1.12 | Kerutan plastik pada kemasan |
| `pattern-tumpal` | Barisan segitiga lebar 24px, tinggi 24px, warna `foreground` di atas `background`, di pita 40px | Pita atas/bawah beranda, pembatas |

Tidak ada gradien warna. Keduanya relief: hanya di medali dan kemasan (2 objek), tidak di panel atau teks.

**Ilustrasi & ikon**
- **Gaya ilustrasi:** bidang datar dua sampai empat warna token, sudut tegas, simetri radial; kedalaman hanya lewat relief dan bayangan objek.
- **Daftar ilustrasi:** `medali` (SVG viewBox 800, hero, panggung produk, konfirmasi), `kemasan` (viewBox 300 x 460, tiga varian warna: arang, soga, kuning).
- **Ikon:** SVG inline sederhana (centang, segitiga, silang, panah), isi `currentColor`, hanya di badge stok dan navigasi.

### 2.7 Motion
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `duration-fast` | 120ms | Press, hover |
| `duration-base` | 220ms | Chip, opsi, tab |
| `duration-slow` | 420ms | Transisi section |
| `duration-signature` | 1500ms | Medali masuk (M1) |
| `ease-out-expo` | cubic-bezier(0.16, 1, 0.3, 1) | Semua elemen masuk |
| `ease-spring` | cubic-bezier(0.3, 1.4, 0.5, 1) | Hitungan keranjang |

- **Pola masuk:** elemen naik 22px + fade, stagger 90ms, maksimal 3 baris judul; hanya saat halaman pertama dimuat.
- **Transisi daftar ke detail:** View Transitions API pada kemasan (`view-transition-name: bag-<lot>`), fallback tanpa animasi.
- **Mikro-interaksi:** tombol turun 1px saat ditekan (120ms); tab dan chip berganti tanpa animasi.
- **Kinerja:** hanya `transform` dan `opacity`; UI ≤ 400ms; momen signature ≤ 1500ms dan bisa dilewati.
- **Reduced motion:** semua animasi dimatikan (durasi 0,01ms); konten tampil di keadaan akhir.

### 2.8 Implementasi Token
Ganti seluruh isi `tokens.css` dengan blok ini (`<link>` Google Fonts dimuat di `<head>`: Familjen Grotesk 400..700 dan Literata 400, 500, `display=swap`).

```css
:root {
  color-scheme: light;
  --background: #17110E;
  --foreground: #F4EDE0;
  --muted: #241A15;
  --muted-foreground: #CDBFAE;
  --border: #4A3B32;
  --input: #8A7767;
  --primary: #A22E1D;
  --primary-foreground: #F4EDE0;
  --primary-deep: #7C1F12;
  --accent: #E2A71A;
  --accent-foreground: #17110E;
  --ring: #E2A71A;
  --surface-light: #F4EDE0;
  --surface-light-foreground: #17110E;
  --success: #8FD3A1;
  --warning: #F0B957;
  --destructive: #F29A8B;

  --font-display: "Familjen Grotesk", "Arial Narrow", sans-serif;
  --font-text: "Literata", Georgia, serif;
  --text-hero: clamp(2.75rem, 1.2rem + 6.2vw, 6.25rem);
  --text-display: clamp(2.5rem, 1.4rem + 4vw, 4.5rem);
  --text-title: 1.5rem;
  --text-body: 1rem;
  --text-small: 0.875rem;
  --text-caption: 0.75rem;

  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px;
  --space-6: 24px; --space-8: 32px; --space-12: 48px; --space-18: 72px; --space-24: 96px;
  --radius-none: 0;
  --shadow-object: drop-shadow(0 24px 22px rgb(30 4 0 / 0.45));
  --shadow-medal: drop-shadow(0 34px 44px rgb(40 6 0 / 0.5));

  --duration-fast: 120ms; --duration-base: 220ms; --duration-slow: 420ms; --duration-signature: 1500ms;
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-spring: cubic-bezier(0.3, 1.4, 0.5, 1);
}
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; background: var(--background); color: var(--foreground); font: 400 var(--text-body)/1.625 var(--font-text); }
button { font: inherit; color: inherit; }
:focus-visible { outline: 3px solid var(--ring); outline-offset: 3px; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; animation-delay: 0s !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; }
}
```
Cabang JS: sebelum memicu animasi JS (mis. kemasan terbang M3), cek `matchMedia('(prefers-reduced-motion: reduce)').matches` dan lewati.

---

## 3. Komponen

### 3.1 Daftar Komponen
| Komponen | Library | Default library → diubah menjadi | Dipakai di halaman |
|---|---|---|---|
| Button | elemen native `button`/`a`, kelas `.btn` | Tidak ada default; tinggi 56 sampai 64px, radius 0, label kata kerja | Semua |
| Header | native `header` + `nav` | Tinggi 80px desktop, 56px mobile; keranjang berhitungan | Semua |
| Hero | native `section`, kelas `.hero` | Bidang `primary`, medali + kemasan | Beranda |
| Lot panel | native `article`, kelas `.lot-panel` | Panel penuh lebar berwarna per lot, kemasan menembus tepi | Beranda, Daftar biji |
| Product gallery | native, kelas `.stage` | Panggung `primary` dengan medali dan kemasan | Produk |
| Lot tabs | native `button role="tab"` | Tab segmen, tinggi 48px | Produk |
| Variant picker | native `button role="radio"` | Chip gilingan, tinggi 44 sampai 48px | Produk |
| Purchase option | native `button role="radio"` | Dua opsi: Langganan bulanan dan Beli sekali | Produk |
| Quantity stepper | native `button` x2 + angka | Tinggi 60px, minimal 1 maksimal 9 | Produk, Keranjang |
| Price | native `b`, kelas `.price` | Familjen Grotesk 700, tabular | Semua |
| Stock badge | native `span`, kelas `.badge` | Ikon + label + warna token | Beranda, Produk |
| Sticky buy bar | native, kelas `.buybar` | Bar `primary` 88px di bawah (mobile) | Produk mobile |
| Tumpal band | native `svg`, kelas `.tumpal` | Pita 28 sampai 40px | Beranda |
| Medal | native `svg`, kelas `.medal` | Objek signature | Beranda, Produk, Konfirmasi |

### 3.2 Spesifikasi Komponen
#### Button
- **Ukuran:** tinggi 56px mobile, 60 sampai 64px desktop; padding horizontal 24 sampai 30px; radius `radius-none`.
- **Varian:** primary (latar `foreground`, teks `background`; di bidang terang dibalik); secondary (border 2px `foreground`, latar transparan); disabled (latar `muted`, teks `muted-foreground`).
- **State:** default / hover (latar `accent`, teks `accent-foreground`) / focus-visible (ring 3px `ring`, offset 3px) / active (turun 1px) / disabled / loading (label tetap, tombol disabled).
- **Aturan:** satu tombol primary per layar; label kata kerja ("Tambah ke keranjang", bukan "Submit"). CTA di header tampil sebagai secondary sampai hero lewat.

#### Lot panel
- **Ukuran:** lebar penuh, tinggi 244px desktop; kemasan 206 x 316px menembus tepi atas panel 26px; angka urut raksasa 150px dengan opasitas 0,16 sebagai dekorasi (`aria-hidden`).
- **Varian:** panel 1 `primary`, panel 2 `accent` (teks `accent-foreground`), panel 3 `surface-light`; posisi kemasan bergantian kanan/kiri.
- **State:** hover pada tombol saja; panel tidak bisa diklik.
- **Aturan:** bukan kartu seragam; warna mengikuti lot; mobile: ditumpuk, kemasan di atas teks.

#### Lot tabs dan Variant picker
- **Ukuran:** tab 48px; chip 44px; jarak 8px; border 1,5px `input`.
- **State:** terpilih = latar `foreground`, teks `background`; focus-visible ring; `aria-selected` / `aria-checked` mengikuti pilihan; panah kiri/kanan berpindah.
- **Aturan:** ganti lot mengganti kemasan, nama, harga, catatan rasa tanpa memuat ulang (M2).

#### Purchase option
- **Ukuran:** dua opsi berdampingan di desktop, bertumpuk di mobile; tinggi minimal 58px; indikator radio 20px.
- **State:** terpilih = border `accent`, latar `accent` 8% (dekoratif), indikator isi `accent`.
- **Aturan:** default "Langganan bulanan" dengan teks "Bisa jeda atau berhenti kapan saja"; harga tampil sama untuk kedua opsi sampai pemilik toko memutuskan potongan langganan (lihat 1.4).

#### Stock badge
- **Ukuran:** tinggi 34px, padding 12px, ikon 10px.
- **Aturan:** selalu ikon + teks; "Menipis · sisa N kantong" hanya dari stok nyata.

#### Medal dan Kemasan (objek signature)
- **Resep:** SVG inline; relief lewat `texture-carve` (medali) dan `texture-crinkle` (kemasan); bayangan lewat `shadow-medal` dan `shadow-object` di elemen pembungkus. Teks pada kemasan adalah bagian ilustrasi (dekoratif, `aria-label` di `svg`); nama lot yang sama selalu ada sebagai teks asli di DOM.
- **Perilaku:** di 360px medali dipotong tepi layar (tidak diskalakan lebih kecil dari 470px); di zoom 200% medali menjadi latar dekoratif dan tidak menutupi teks; reduced motion: tanpa rotasi.

---

## 4. Layout & Navigasi
- **Header:** logo kiri, tautan Biji · Langganan · Cerita Petani · Cara Seduh, keranjang kanan. Mobile: ikon menu di kiri, keranjang kanan, tinggi 56px.
- **Navigasi mobile:** menu penuh layar dari kiri, tautan 56px; keranjang tidak disembunyikan.
- **Pola responsif:** hero: medali di bawah judul (mobile) → di kanan (desktop); panel lot: bertumpuk → baris penuh; produk: panggung di atas → dua kolom 700px/sisanya (≥ 1024px); bar beli lengket di mobile, tombol biasa di desktop.
- **Kepadatan:** beranda hero + CTA muat di atas lipatan 1440 x 900 dan 390 x 844; PDP mobile menampilkan harga dan tombol beli tanpa scroll (bar lengket).

## 5. Spesifikasi Halaman (ringkas)
| Halaman | Route | Isi utama | Status |
|---|---|---|---|
| Beranda | `/` | Hero medali, tiga lot, langganan, cerita petani | Dirancang di preview (hero, panel lot) |
| Daftar biji | `/biji` | Tiga lot, filter sangrai | Belum diisi di mode cepat |
| Produk | `/biji/[lot]` | Panggung, tab lot, gilingan, cara beli, harga, bar beli | Dirancang di preview (desktop dan mobile) |
| Langganan | `/langganan` | Pilih lot, ritme kirim, jeda | Belum diisi di mode cepat |
| Keranjang | `/keranjang` | Item, jumlah, ringkasan | Belum diisi di mode cepat |
| Checkout | `/checkout` | Alamat, pengiriman, pembayaran (satu langkah satu layar) | Belum diisi di mode cepat |
| Konfirmasi | `/pesanan/[kode]` | M4 | Belum diisi di mode cepat |
| Cerita petani | `/cerita` | Cerita dengan foto asli, 60 sampai 75 karakter per baris | Belum diisi di mode cepat |

Wireframe hero mobile (390):
```
┌──────────────────────────┐
│ ☰   KOPI LERENG  (Keranj)│
│      (medali 470px)      │
│   Tiga lereng.           │
│   Satu cangkir           │
│   yang jujur.            │
│ [[ Pilih biji · Rp95.000 ]]│
│ [ Langganan bulanan ]    │
│ ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲  │
└──────────────────────────┘
```
State produk: loading = bidang `muted` seukuran kemasan; stok habis = tombol disabled + badge Habis + tautan "Kabari saya saat tersedia"; error = pesan di 6.

## 6. Feedback & State Global (ringkas)
- Loading: bidang `muted` berbentuk konten; spinner hanya di dalam tombol.
- Error umum: "Stok lot ini baru saja habis. Pilih lot lain atau kabari saya saat tersedia." (teks di bawah tombol, `destructive`).
- 404: "Halaman ini tidak ketemu. Mulai lagi dari daftar biji." + tombol Lihat biji.
- Sukses: "Masuk keranjang" lewat hitungan header (M3), tanpa toast.
- Belum diisi di mode cepat: kode error pembayaran dan voucher.

## 7. Konten & Copywriting (ringkas)
- Sapaan "kamu", hangat dan lugas, kalimat pendek.
- Glosarium: Lot (bukan "varian"), Langganan bulanan, Kantong (satuan 200 g), Gilingan.
- Format: uang `Rp95.000`; berat `200 g`; tanggal `14 Okt 2026`.
- Data contoh: tiga lot Sapan Rp95.000, Pulu-Pulu Rp115.000, Rantekarua Rp140.000; catatan rasa adalah contoh sampai ada data roastery.

## 8. Aksesibilitas (ringkas)
- Kontras: semua pasangan di 2.3; kuning di atas soga hanya teks besar.
- Focus ring 3px `ring` di semua elemen interaktif; tap target ≥ 44px.
- Tab lot dan opsi beli memakai peran `tab` dan `radio` dengan panah keyboard; status stok selalu berteks.
- Kemasan dan medali dekoratif (`aria-hidden`) kecuali bila membawa makna; nama lot selalu teks asli.
- `<html lang="id">`, judul unik per halaman.

## 9. Catatan Implementasi (ringkas)
- File: `tokens.css` (2.8), `index.html`, `style.css`; font lewat `<link>` Google Fonts dengan `preconnect`.
- Gambar: foto produk asli menggantikan SVG kemasan saat tersedia, rasio 4:5, `srcset`, placeholder warna dominan.
- Performa: filter SVG relief hanya di dua objek; medali di mobile dimuat sebagai SVG inline sekali.
- Jangan: gradien warna, grid kartu produk seragam, badge "Terlaris", hitung mundur atau stok palsu, motif sakral di elemen sepele.
