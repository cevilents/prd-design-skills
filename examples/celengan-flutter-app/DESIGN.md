# DESIGN: Celengan

> Aplikasi nabung bareng yang terasa seperti menempel stiker tebal di buku: terang, gemuk, bertinta, dipakai satu tangan oleh anak muda Indonesia di sela kuliah, kerja, dan perjalanan, dan puncaknya memecahkan celengan saat target tercapai.

| | |
|---|---|
| Versi | 1.0 |
| Tanggal | 2026-10-14 |
| Berdasarkan | Brief user (tanpa PRD): target tabungan, setor rutin, tantangan 52 minggu, tabungan grup, pengingat; halaman: onboarding, beranda, detail target, setor, tantangan, grup, profil |
| Jenis produk | Aplikasi mobile native (profil 7), potret saja |
| Platform & stack | iOS + Android · Flutter (Material 3), satu basis kode |

---

## 1. Arah Visual

### 1.1 Konteks Pemakaian
- Pengguna 18 sampai 30 tahun: mahasiswa, pekerja pemula, anak kos. Mayoritas memakai Android kelas menengah (layar 360 sampai 412dp), sebagian iPhone (375 sampai 430pt). Desain harus ringan di perangkat menengah.
- Dipakai satu tangan, berdiri atau di kendaraan, sesi 10 sampai 30 detik: lihat progres, setor, colek teman. Momen emosional jarang: target tercapai.
- Waktu penting: Jumat sore, gajian tanggal 25, sebelum liburan. Sinyal naik turun, jadi setoran harus tetap bisa dicatat saat offline.

### 1.2 Konsep & Kepribadian
- **Konsep:** Stiker Celengan: setiap target adalah stiker tebal berpinggir tinta yang kamu tempel di layar; setiap setoran mengisi celengannya; saat penuh, kamu memecahkannya seperti orang tua kita dulu.
- **Level ambisi:** Spektakuler
- **Tiga kata sifat:** gemuk, riang, taktil
- **Bukan:** bank korporat (biru-hijau, abu dingin), fintech gelap bertabur neon, ilustrasi orang blob generik
- **Kepadatan informasi:** sedang. Layar kerja memuat 4 target sekaligus; wow dicurahkan di 5 momen jarang.
- **Motif khas:** sudut mengelupas pada kartu target (maksimal 4 kartu per layar) dan celah koin pada tombol Setor di bar bawah dan di punggung celengan. Hanya dua motif ini; tidak ada ornamen lain.

### 1.3 Keputusan & Alasan
| Keputusan | Pilihan | Alasan |
|---|---|---|
| Jenis produk | Profil 7, Aplikasi mobile native | Brief menyebut Flutter, iOS dan Android, notifikasi pengingat |
| Konsep terpilih | Stiker Celengan (A) dari 3 konsep di `design-concepts.html` (B Toples Cahaya, C Buku Tabungan Cetak) | User menjawab "terserah". Penilaian independen oleh satu juri terpisah: dampak 5 detik A 8, B 7, C 5. A paling dikenali tanpa logo, paling akrab bagi 18 sampai 30 tahun, dan termurah dirender (tanpa blur) di Android menengah. Dari B diambil isi yang naik di dalam celengan kaca |
| Mode warna | Light saja | Konsep mengandalkan tinta di atas kertas terang; satu palet diukur penuh. Profil 7 menyebut dark hampir wajib: ditunda sadar, lihat 1.4 |
| Pendekatan layout | Potret, satu kolom, aksi utama di zona jempol bawah | Satu tangan; v1 tanpa lanskap |
| Gaya bentuk | Outline tinta 2,5dp, bayangan keras tanpa blur 3 sampai 5dp, radius 8 / 12 / 16 / 24 | Bisa dibangun murah di Flutter, identik di iOS dan Android |
| Wow vs kerja | Wow di M1 sampai M5; layar kerja memakai tipografi, warna, outline, dan satu motif | Aturan frekuensi pakai |

### 1.4 Perlu Konfirmasi
| Keputusan | Default yang dipakai sekarang | Alternatif |
|---|---|---|
| Apakah Celengan memegang uang atau hanya mencatat | Hanya mencatat dan mengingatkan; transfer dilakukan di aplikasi bank atau e-wallet user. Setor = catat setoran, dengan sumber Tunai, Transfer, atau E-wallet | Integrasi pembayaran: tambah layar verifikasi, status tertunda dan gagal |
| Maskot celengan | Babi tanah liat (tradisi celengan) | Ayam jago tanah liat bila sensitif bagi sebagian pengguna; geometri di 2.6 diganti, pecahan dan momen sama |
| Mode gelap | Light saja (`themeMode: ThemeMode.light`) | Light + dark ikut sistem; palet gelap perlu diukur ulang |
| Tombol Setor di tengah tab bar iOS | Dipakai di kedua platform | iOS: tombol melayang di atas tab bar 4 item |
| Switch | Switch M3 bertema di kedua platform (kontras non-teks lolos) | `Switch.adaptive` (bentuk sistem iOS) |
| Autentikasi (masuk, OTP) | Belum didesain, tidak ada di brief | Pola form 5.8 + slot OTP 48dp |
| Versi minimum | iOS 15, Android 8 (API 26) | Ikuti minimum Flutter stabil yang dipakai tim |
| Batas colek | Satu colekan per anggota per 24 jam | Tanpa batas |
| Kode error | Id sementara `ERR_*` di 6.2 | Ganti dengan kode PRD bila ada |

### 1.5 Referensi
Tidak ada gambar referensi dari user. Dunia visual: celengan tanah liat, stiker, toples kerupuk, stempel buku tabungan.

### 1.6 Momen Signature
| # | Momen | Pemicu | Kenapa penting bagi user | Mockup |
|---|---|---|---|---|
| M1 | Koin Masuk Celah | Setoran tersimpan (5.4) | Aksi paling sering; dibuat singkat dan memuaskan | `design-preview.html#m1` |
| M2 | Pecah Celengan | Target mencapai 100%, user menahan celengan (5.9) | Ritual hadiah terbesar | `design-preview.html#m2` |
| M3 | Onboarding Tempel | Peluncuran pertama (5.1) | Memperkenalkan bahasa stiker sebelum satu pun form | `design-preview.html#m3` |
| M4 | Cap Minggu | Setoran minggu berjalan tersimpan (5.5) | Kepuasan mengisi kotak, seperti stempel buku tabungan | `design-preview.html#m4` |
| M5 | Toples Berlapis | Anggota grup menyetor (5.6) | Semua melihat lapisan warnanya naik | `design-preview.html#m5` |

Aturan bersama: layar signature memakai `gradient-hero`; tombol aksi aktif sejak detik 0; ketuk di mana saja melewati animasi; hasil akhir sudah benar di frame pertama bila reduced motion. Animasi di preview adalah aproksimasi `cubic-bezier` dari pegas Flutter.

#### M1 · Koin Masuk Celah
- **Komposisi:** latar `gradient-hero` penuh, celengan koral 250dp di tengah, `+Rp250.000` di `text-hero`, kartu ringkasan target di bawah, tombol Selesai.
- **Timeline:** 0ms judul masuk 380ms · 60ms celengan menempel (`spring-slap`) · 180ms koin jatuh 780ms `ease-fall` · 740ms koin masuk celah: celengan memipih 380ms (skala 1,1 x 0,88), 6 percikan, haptik `success` · 820ms jumlah menghitung naik 700ms · 1000ms bar naik 65% ke 70%, angka 3.250.000 ke 3.500.000. Total 1560ms.
- **Aset:** `CelenganPig` 250dp, `Coin` 52dp, 6 garis percikan 5 x 26dp.
- **Reduced motion:** langsung keadaan akhir, fade 150ms; haptik tetap.
- **Resep:** satu `AnimationController(duration: 1560ms)`; tiap bagian `CurvedAnimation(curve: Interval(start/1560, end/1560, curve: ...))` dibaca dengan `AnimatedBuilder`; koin `Transform.translate` + `Transform.rotate`, dipangkas ke celah dengan `ClipRect` setinggi celah; haptik dipicu `controller.addListener` saat nilai melewati 740/1560 sekali.

#### M2 · Pecah Celengan
- **Komposisi:** pra-tahan: latar `primary`, celengan 250dp, teks "Tahan celengannya." berwarna `primary-foreground`. Pasca: latar `gradient-hero`, 4 pecahan dan 10 koin tersebar, judul "Target tercapai!", `Rp5.000.000` di `text-hero`.
- **Timeline:** tahan 0 sampai 1200ms: getar naik (rotasi 1,5 sampai 7 derajat), 3 retakan tergambar, haptik ringan, sedang, berat · lepas 1200ms: kilat putih 130ms, latar gelap menjadi hero, pecahan dan koin terlempar 760ms `ease-out-expo` · 1500ms judul masuk · 1580ms jumlah menghitung naik. Pasca-lepas 1800ms.
- **Aset:** celengan dipotong 4 poligon (`ShardClipper`), tiap pecahan diberi stroke 2,5dp pada tepi potongan; koin 30 sampai 34dp.
- **Reduced motion dan pembaca layar:** tidak ada tahan; tombol "Pecahkan celengan" biasa; hasil akhir tampil dengan fade 150ms.
- **Resep:** `HoldToBreak` (9) memakai `Listener` + `Ticker` 1200ms; pecahan `Transform.translate/rotate` dari 0 ke posisi akhir lewat `TweenSequence` (puncak 1,2x lalu turun); poligon pecahan dalam 5.9.

#### M3 · Onboarding Tempel
- **Komposisi:** `gradient-hero` penuh, celengan besar, 4 stiker target contoh miring, judul "Nabung itu seru kalau ada temannya.", dua baris teks, titik langkah, tombol Lanjut.
- **Timeline:** 120ms celengan menempel 560ms · 380ms, 530ms, 680ms, 830ms stiker menempel 480ms (`spring-slap`) · 1050ms judul naik 14dp + fade 520ms · 1150ms subjudul. Total 1670ms. Haptik `light` sekali di stiker terakhir.
- **Aset:** `CelenganPig`, `GoalSticker` x4 (pictogram 22dp).
- **Reduced motion:** semua tampil langsung, fade 150ms.
- **Resep:** `TweenAnimationBuilder` per stiker dengan `Interval` bertingkat 150ms; skala 1,9 ke 1 dan rotasi +22 derajat ke sudut akhir.

#### M4 · Cap Minggu
- **Komposisi:** layar Tantangan (5.5) dengan kotak minggu 18 di grid.
- **Timeline:** 150ms stempel tinta (kotak `primary`, centang `primary-foreground`) jatuh dari skala 2,6 ke 1, haptik `heavy` di 330ms · 420ms cincin riak 600ms · 520ms kotak berubah menjadi hero · 560ms total dan bar menghitung naik 17/52 ke 18/52 (Rp720.000 ke Rp810.000). Total 1150ms.
- **Aset:** centang 30dp stroke 4,5.
- **Reduced motion:** kotak langsung hero, tanpa stempel.
- **Resep:** `Stack` di atas `WeekTile` dengan `ScaleTransition` + `RotationTransition`, lalu `FadeTransition` keluar; cincin `DecoratedBox` yang diskalakan.

#### M5 · Toples Berlapis
- **Komposisi:** header grup berlatar `accent`, `Toples` 120dp berlapis warna anggota, total dan persen di sebelahnya.
- **Timeline:** 200ms koin jatuh ke celah toples 700ms · 880ms lapisan anggota naik 520ms (lapisan di atasnya terdorong), haptik `light` hanya untuk setoran milik sendiri · 900ms chip "Salsa +Rp500.000" muncul 2,6 detik · total dan persen menghitung naik: Rp5.000.000 ke Rp5.500.000, 62,5% ke 68,8%.
- **Aset:** `Toples`, `Coin` 30dp.
- **Reduced motion:** fade 150ms; chip tidak muncul, baris aktivitas dan pengumuman layar yang menyampaikan.
- **Resep:** `ToplesPainter` (2.6); tinggi lapisan = nilai / target x 176 (unit viewBox); `Transform.scale(alignment: bottomCenter)` untuk lapisan yang tumbuh.

---

## 2. Design Tokens

### 2.1 Warna
| Token | Light | Peran Flutter | Dipakai untuk |
|---|---|---|---|
| `background` | #EEF2E2 | `ColorScheme.surface` | Latar halaman |
| `foreground` | #14161A | `onSurface` | Teks utama, tinta outline stiker |
| `card` | #FFFFFF | `surfaceContainerLowest` | Kartu, sheet, field |
| `muted` | #E3EAD0 | `surfaceContainer` | Latar sekunder, tombol dan kotak nonaktif |
| `muted-foreground` | #4A5240 | `onSurfaceVariant` | Teks sekunder |
| `border` | #14161A | `outline` | Outline stiker, garis kontrol |
| `border-subtle` | #C5CDB0 | `outlineVariant` | Pemisah baris (dekoratif) |
| `input` | #14161A | `InputDecorationTheme.enabledBorder` | Border field |
| `primary` | #14161A | `primary` | Tombol utama, latar pra-tahan M2 |
| `primary-foreground` | #CBF54A | `onPrimary` | Teks di atas primary |
| `hero` / `hero-foreground` | #CBF54A / #14161A | `primaryContainer` / `onPrimaryContainer` | Bidang warna penuh, kotak selesai, pilihan terpilih |
| `accent` / `accent-foreground` | #FF5C6C / #14161A | `secondary` / `onSecondary` | Celengan, tepi tombol utama, minggu ini |
| `accent-light` | #FF8F9B | `AppColors.accentLight` | Moncong celengan |
| `accent-subtle` | #FFE0E3 | `secondaryContainer` | Latar lembut koral |
| `sky` | #6FC7FF | `tertiary` | Stiker target, anggota |
| `sun` | #FFD23F | `AppColors.sun` | Koin, stiker, anggota |
| `ring` | #2F4BFF | `ThemeData.focusColor` | Fokus, field aktif |
| `destructive` / `destructive-foreground` | #C4122F / #FFFFFF | `error` / `onError` | Keluar, hapus, error |
| `destructive-subtle` | #FFD9DE | `errorContainer` | Latar badge error |
| `success` / `success-subtle` | #12703A / #CFF0D9 | `AppColors.success*` | Teks dan latar sukses |
| `warning` / `warning-subtle` | #8A5A00 / #FFE9B0 | `AppColors.warning*` | Teks dan latar peringatan |

Peran `surfaceContainerLow` = `card`, `surfaceContainerHigh` dan `Highest` = `muted`, `surfaceTint` transparan, `scrim` = `primary` pada alpha 60%, `inverseSurface` = `primary`. Peran lain tidak dipakai. Lime di atas koral dilarang (2,39).

### 2.2 Warna Status
| Status | Label UI | Latar | Teks | Ikon |
|---|---|---|---|---|
| `on-track` (target) | Sesuai jadwal | `success-subtle` | `success` | centang |
| `behind` (target) | Terlambat | `warning-subtle` | `warning` | peringatan |
| `done` (target) | Tercapai | `hero` | `hero-foreground` | bendera |
| `paused` (target) | Dijeda | `muted` | `muted-foreground` | tanpa ikon |
| `week-done` | Selesai | `hero` | `foreground` | centang |
| `week-missed` | Terlewat | `warning-subtle` + garis serong | `warning` | peringatan |
| `week-current` | Minggu ini | `card`, tepi `accent` 3,5dp | `foreground` | tanpa ikon |
| `week-upcoming` | Belum | `muted`, tepi putus-putus | `muted-foreground` | tanpa ikon |
| `member-paid` | Lunas | `success-subtle` | `success` | centang |

### 2.3 Tabel Kontras
| Teks / elemen | Latar | Rasio | Normal (4.5) | Besar / non-teks (3.0) |
|---|---|---|---|---|
| `foreground` | `background` | 15.90 | PASS | PASS |
| `foreground` | `card` | 18.11 | PASS | PASS |
| `foreground` | `muted` | 14.62 | PASS | PASS |
| `muted-foreground` | `background` | 7.17 | PASS | PASS |
| `muted-foreground` | `card` | 8.16 | PASS | PASS |
| `muted-foreground` | `muted` | 6.59 | PASS | PASS |
| `primary-foreground` | `primary` | 14.40 | PASS | PASS |
| `hero-foreground` | `hero` | 14.40 | PASS | PASS |
| `foreground` | #B4E22C (titik terburuk `gradient-hero`) | 11.95 | PASS | PASS |
| `accent-foreground` | `accent` | 6.04 | PASS | PASS |
| `foreground` | `accent-light` | 8.33 | PASS | PASS |
| `foreground` | `accent-subtle` | 14.68 | PASS | PASS |
| `foreground` | `sky` | 9.74 | PASS | PASS |
| `foreground` | `sun` | 12.54 | PASS | PASS |
| `foreground` | `warning-subtle` | 15.12 | PASS | PASS |
| `foreground` | `success-subtle` | 14.77 | PASS | PASS |
| `ring` | `background` | 5.16 | PASS | PASS |
| `ring` | `card` | 5.88 | PASS | PASS |
| `ring` | `hero` | 4.68 | PASS | PASS |
| `input` (border) | `card` | 18.11 | n/a | PASS |
| `input` (border) | `background` | 15.90 | n/a | PASS |
| `accent` (tepi minggu ini) | `card` | 3.00 | n/a | PASS |
| `destructive` | `card` | 6.04 | PASS | PASS |
| `destructive` | `background` | 5.31 | PASS | PASS |
| `destructive` | `destructive-subtle` | 4.67 | PASS | PASS |
| `destructive-foreground` | `destructive` | 6.04 | PASS | PASS |
| `success` | `success-subtle` | 5.03 | PASS | PASS |
| `success` | `card` | 6.17 | PASS | PASS |
| `success` | `background` | 5.41 | PASS | PASS |
| `warning` | `warning-subtle` | 4.95 | PASS | PASS |
| `warning` | `card` | 5.93 | PASS | PASS |
| `warning` | `background` | 5.20 | PASS | PASS |
| `border-subtle` | `background` | 1.45 | n/a | dekoratif |

Teks di atas halftone memakai `foreground` dan titik halftone hanya alpha 16%, jadi kontras tidak turun di bawah 11,9. Ring fokus digambar di luar elemen dengan jarak 2dp sehingga selalu dibandingkan dengan latar sekitarnya, bukan dengan `primary`.

### 2.4 Tipografi
- **Font display:** Bagel Fat One (Google Fonts, satu weight 400 yang sudah sangat tebal, fallback `sans-serif` bulat sistem). Hanya untuk angka hero, judul layar, dan judul momen, selalu 28sp ke atas. Alasan: bentuk gemuk membulat meniru huruf stiker dan angka celengan.
- **Font teks:** Rethink Sans (400, 500, 600, 700, 800; fallback `sans-serif`). Hangat, terbaca di 12 sampai 20sp.
- **Angka:** `FontFeature.tabularFigures()` pada Rethink Sans untuk nominal `[?]` (cek font mendukung `tnum`; bila tidak, nominal tetap rata kanan di daftar).
- **Skala font sistem (`TextScaler`):** semua teks ikut sampai 200%. Pengecualian yang boleh dibatasi: `text-hero` memakai `FittedBox(scaleDown)` pada lebar kontainer; `text-display`, label bar bawah, judul inline iOS maksimal 1,3; angka di `WeekTile` dan keypad maksimal 1,5.

| Token | Ukuran / line-height | Weight | Peran TextTheme | Dipakai untuk |
|---|---|---|---|---|
| `text-hero` | 44 / 44 | 400 (Bagel) | `displayLarge` | Total tabungan, jumlah setor, nominal momen |
| `text-display` | 32 / 36 | 400 (Bagel) | `headlineLarge` | Judul layar signature dan onboarding |
| `text-title` | 20 / 26 | 800 | `titleLarge` | Judul bagian, judul app bar Android |
| `text-title-sm` | 16 / 22 | 800 | `titleMedium` | Judul kartu, nama anggota |
| `text-body` | 16 / 24 | 400 | `bodyLarge` | Teks utama |
| `text-small` | 14 / 20 | 500 | `bodyMedium` | Keterangan, nominal baris |
| `text-button` | 16 / 20 | 800 | `labelLarge` | Label tombol |
| `text-caption` | 12 / 16 | 700 | `labelSmall` | Label bar bawah, badge, caption |

### 2.5 Spacing & Grid
- **Skala spacing (dp):** 4, 8, 12, 16, 20, 24, 32, 48.
- **Padding halaman:** 16. Lebar konten maksimum 480dp, di tengah (tablet dan lipat: potret saja, konten tidak melebar).
- **Perangkat acuan:** iPhone SE 375x667 (status bar 20, tab bar 49, tanpa home indicator) · iPhone 15 393x852 (status bar 54 dengan Dynamic Island, home indicator 34) · iPhone Pro Max 430x932 · Android 360x800 (status bar 24 sampai 30, bar gestur 24, `NavigationBar` 80) · Android 412x915.
- **Safe area:** hero boleh menembus ke bawah status bar (`SafeArea(top: false)` + padding atas = `MediaQuery.paddingOf(context).top`); konten di dalam safe area; bar bawah menambah inset bawah; sheet form menambah `viewInsets.bottom`.
- **Breakpoint:** tidak ada pada v1; satu kolom untuk semua lebar.

### 2.6 Bentuk, Elevasi, Material & Ilustrasi
**Bentuk**
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `radius-sm` | 8dp | Badge, bar progres |
| `radius-md` | 12dp | Chip, kotak minggu, tombol keypad, tombol ikon, chip "berikutnya" |
| `radius-lg` | 16dp | Tombol, kartu, field, segmented |
| `radius-xl` | 24dp | Stiker besar, dialog |
| `radius-sheet` | 28dp (iOS 38dp) | Sheet dan sudut bawah hero |
| `stroke-sticker` | 2,5dp | Semua outline tinta |
| `stroke-focus` | 3,5dp | Border field aktif, kotak minggu ini. Bentuk pil penuh hanya untuk indikator navigasi dan switch |

**Elevasi** (tanpa blur, satu arah: kanan-bawah; maksimal 3 tingkat)
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `shadow-sticker` | offset (3, 3), blur 0, warna `foreground` | Kartu, tombol sekunder, chip |
| `shadow-sticker-lg` | offset (5, 5), blur 0, warna `foreground` | Stiker besar, dialog |
| `shadow-cta` | offset (3, 3), blur 0, warna `accent` | Satu tombol utama per layar |
| `shadow-pressed` | tanpa bayangan, elemen bergeser (3, 3) | Keadaan ditekan |

**Gradien & material**
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `gradient-hero` | linear dari kiri-atas ke kanan-bawah (sekitar 160 derajat): #E6FF8C 0%, #CBF54A 48%, #B4E22C 100% | Header Beranda, Tantangan, Profil, layar M1 sampai M3 |
| `texture-halftone` | titik radius 1,4dp, jarak 10dp, `foreground` alpha 16%, masker radial 68% | Pojok bidang hero besar saja |
| `texture-hatch` | garis serong 135 derajat: 5dp `warning-subtle`, 4dp `card` | Kotak minggu terlewat |

**Ilustrasi & ikon**
- **Gaya:** outline tinta (stroke 4 pada viewBox 200, 2,5dp pada UI), isi datar maksimal 3 warna token, kilap putih alpha 65% di satu sudut, ujung membulat. Subjek hanya benda dunia user.
- **Celengan** (`CelenganPig`, viewBox 200 x 150): badan elips pusat (100, 80) radius 78 x 54; kaki dua persegi 26 x 30 radius 10 di (48, 110) dan (124, 110); telinga segitiga (126, 36), (152, 12), (160, 52); moncong elips (178, 90) radius 16 x 14 warna `accent-light` dengan dua lubang hidung r 2,2; mata (148, 70) r 4,5; celah koin persegi (78, 27) 48 x 9 radius 4,5 warna `foreground`; ekor kurva `M26 82 q-18 -4 -12 -22 q5 10 14 8`; kilap busur `M40 66 Q50 48 74 42`. Varian: koral (default), kaca (badan `card`, isi `hero` setinggi progres dengan gelombang dan 2 koin), retak.
- **Pecahan M2** (persentase kotak 250 x 188): kiri-atas `0 0, 50% 0, 44% 28%, 54% 48%, 20% 52%, 0 46%`; kiri-bawah `0 46%, 20% 52%, 54% 48%, 46% 70%, 52% 100%, 0 100%`; kanan-atas `50% 0, 100% 0, 100% 58%, 78% 50%, 54% 48%, 44% 28%`; kanan-bawah `54% 48%, 78% 50%, 100% 58%, 100% 100%, 52% 100%, 46% 70%`.
- **Toples** (`Toples`, viewBox 160 x 208): badan persegi (14, 40) 132 x 176 radius 26 warna `card`; tutup (24, 12) 112 x 32 radius 10 `foreground` dengan celah (52, 24) 56 x 8 `hero`; lapisan per anggota, tinggi = nilai / target x 176, dari bawah ke atas, outline 3.
- **Koin:** lingkaran r 12 `sun`, cincin dalam r 7,5, huruf P. **Stiker target:** kotak 52dp radius 12, warna dari `sky`, `sun`, `hero`, atau `accent`, dengan pictogram (gelombang, laptop, kotak centang, orang, tiket, gunung).
- **Ikon:** Material Symbols Rounded, weight 600, tanpa isi, 24dp (`material_symbols_icons` `[?]`; cadangan `Icons.*_rounded`). Ikon kembali: `Icons.arrow_back` di Android, `CupertinoIcons.chevron_back` di iOS.

### 2.7 Motion
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `duration-fast` | 120ms | Tekan tombol dan kartu |
| `duration-base` | 220ms | Switch, chip, elemen masuk |
| `duration-slow` | 420ms | Transisi layar, sheet |
| `duration-moment` | sampai 1800ms | Momen signature multi-fase, bisa dilewati |
| `ease-out-expo` | `Cubic(0.16, 1, 0.3, 1)` | Elemen masuk |
| `ease-emphasized` | `Cubic(0.2, 0, 0, 1)` | Transisi layar (padanan emphasized M3) |
| `ease-fall` | `Cubic(0.55, 0.085, 0.68, 0.53)` | Koin jatuh |
| `spring-snappy` | `SpringDescription(mass: 1, stiffness: 520, damping: 38)` | Switch, kartu, angka |
| `spring-slap` | `SpringDescription(mass: 1, stiffness: 380, damping: 14)` | Menempel (hanya momen) |

- **Pola masuk:** kartu target masuk sekali saat Beranda pertama dimuat: stagger 40ms, naik 12dp + fade 220ms; tidak diputar ulang saat refresh atau kembali.
- **Transisi daftar ke detail:** `Hero(tag: 'sticker-<id>')` pada gambar celengan dan stiker; cadangan fade `duration-base`.
- **Mikro-interaksi:** tombol dan kartu ditekan: bergeser (3, 3) dan bayangan menciut 120ms; switch bergeser 220ms; angka berubah dengan hitung naik 700ms `ease-out-expo`.
- **Kinerja:** hanya `Transform` dan `Opacity`; tanpa `BackdropFilter`; panggung momen dibungkus `RepaintBoundary`; `CustomPainter.shouldRepaint` hanya saat nilai berubah; target 60fps di Android menengah.
- **Reduced motion:** `MediaQuery.disableAnimationsOf(context)` (iOS Reduce Motion dan Android Remove animations sama-sama menyalakannya): durasi `Duration.zero` atau fade 150ms; momen langsung ke keadaan akhir; tahan celengan menjadi tombol; koin pemuatan berputar menjadi ikon statis.

**Gestur**
| Gestur | Tempat | Perilaku |
|---|---|---|
| Tarik untuk muat ulang | Beranda, Grup, Tantangan | `RefreshIndicator.adaptive`; haptik `selection` saat lewat ambang |
| Geser kembali | Semua layar dalam | iOS: tepi kiri (`CupertinoPageTransitionsBuilder`); Android: gestur kembali sistem (predictive back); tidak ada tombol kembali yang mematikan gestur |
| Tahan celengan 1,2 detik | 5.9 | Memecahkan celengan; dilepas sebelum 1,2 detik membatalkan dengan pegas kembali |
| Tarik sheet ke bawah | Setor, Target Baru | Menutup; ketinggian sheet dihitung dari isi |
| Tekan lama kotak minggu | 5.5 | Tooltip jumlah dan tanggal setor |

**Haptik** (satu per aksi; mengikuti pengaturan sistem; tidak menggantikan umpan balik visual)
| Kejadian | Pola | Cara Flutter |
|---|---|---|
| Pilih chip, ganti segmen, toggle | `selection` | `HapticFeedback.selectionClick()` |
| Ketuk tombol keypad | `light` | `HapticFeedback.lightImpact()` |
| M1 setoran, colek terkirim | `success` | paket `haptic_feedback` `[?]`; cadangan `mediumImpact` lalu `lightImpact` 90ms kemudian |
| M2 tahan | ramp ringan, sedang, berat (satu pola) | `lightImpact`, `mediumImpact`, `heavyImpact` di 300, 600, 900ms |
| M3 stiker terakhir, M5 setoran sendiri | `light` | `lightImpact()` |
| M4 stempel | `heavy` | `heavyImpact()` |
| Validasi gagal | `error` | paket `haptic_feedback` `[?]`; cadangan `heavyImpact` |

### 2.8 Implementasi Token
Buat `lib/theme/app_theme.dart` (file baru, tidak menggabung). Kode ini belum dikompilasi di lingkungan penyusun; jalankan `flutter analyze` dan sesuaikan nama parameter dengan versi Flutter stabil yang dipakai.

```dart
import 'dart:ui' show FontFeature;
import 'package:flutter/cupertino.dart' show CupertinoPageTransitionsBuilder;
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

abstract final class Space {
  static const double s1 = 4, s2 = 8, s3 = 12, s4 = 16, s5 = 20, s6 = 24, s8 = 32, s12 = 48;
}

abstract final class Rad {
  static const double sm = 8, md = 12, lg = 16, xl = 24, sheet = 28, sheetIos = 38;
  static const double stroke = 2.5, focus = 3.5;
}

const _ink = Color(0xFF14161A);
const _lime = Color(0xFFCBF54A);
const _coral = Color(0xFFFF5C6C);
const _card = Color(0xFFFFFFFF);

@immutable
class AppColors extends ThemeExtension<AppColors> {
  const AppColors();
  Color get sun => const Color(0xFFFFD23F);
  Color get accentLight => const Color(0xFFFF8F9B);
  Color get success => const Color(0xFF12703A);
  Color get successSubtle => const Color(0xFFCFF0D9);
  Color get warning => const Color(0xFF8A5A00);
  Color get warningSubtle => const Color(0xFFFFE9B0);
  @override
  AppColors copyWith() => this;
  @override
  AppColors lerp(ThemeExtension<AppColors>? other, double t) => this;
}

@immutable
class AppTokens extends ThemeExtension<AppTokens> {
  const AppTokens();
  List<BoxShadow> get shadowSticker => const [BoxShadow(color: _ink, offset: Offset(3, 3), blurRadius: 0)];
  List<BoxShadow> get shadowStickerLg => const [BoxShadow(color: _ink, offset: Offset(5, 5), blurRadius: 0)];
  List<BoxShadow> get shadowCta => const [BoxShadow(color: _coral, offset: Offset(3, 3), blurRadius: 0)];
  Gradient get gradientHero => const LinearGradient(
      begin: Alignment(-0.34, -1), end: Alignment(0.34, 1),
      colors: [Color(0xFFE6FF8C), _lime, Color(0xFFB4E22C)], stops: [0, 0.48, 1]);
  Duration get durFast => const Duration(milliseconds: 120);
  Duration get durBase => const Duration(milliseconds: 220);
  Duration get durSlow => const Duration(milliseconds: 420);
  Curve get easeOutExpo => const Cubic(0.16, 1, 0.3, 1);
  Curve get easeEmphasized => const Cubic(0.2, 0, 0, 1);
  Curve get easeFall => const Cubic(0.55, 0.085, 0.68, 0.53);
  SpringDescription get springSnappy => const SpringDescription(mass: 1, stiffness: 520, damping: 38);
  SpringDescription get springSlap => const SpringDescription(mass: 1, stiffness: 380, damping: 14);
  @override
  AppTokens copyWith() => this;
  @override
  AppTokens lerp(ThemeExtension<AppTokens>? other, double t) => this;
}

TextTheme _text() {
  TextStyle rs(double s, double lh, FontWeight w) => GoogleFonts.rethinkSans(
      fontSize: s, height: lh / s, fontWeight: w, color: _ink,
      fontFeatures: const [FontFeature.tabularFigures()]);
  TextStyle bagel(double s, double lh) =>
      GoogleFonts.bagelFatOne(fontSize: s, height: lh / s, color: _ink, letterSpacing: -0.01 * s);
  return TextTheme(
    displayLarge: bagel(44, 44), headlineLarge: bagel(32, 36),
    titleLarge: rs(20, 26, FontWeight.w800), titleMedium: rs(16, 22, FontWeight.w800),
    bodyLarge: rs(16, 24, FontWeight.w400), bodyMedium: rs(14, 20, FontWeight.w500),
    labelLarge: rs(16, 20, FontWeight.w800), labelSmall: rs(12, 16, FontWeight.w700),
  );
}

ThemeData buildAppTheme() {
  const scheme = ColorScheme(
    brightness: Brightness.light,
    primary: _ink, onPrimary: _lime,
    primaryContainer: _lime, onPrimaryContainer: _ink,
    secondary: _coral, onSecondary: _ink,
    secondaryContainer: Color(0xFFFFE0E3), onSecondaryContainer: _ink,
    tertiary: Color(0xFF6FC7FF), onTertiary: _ink,
    error: Color(0xFFC4122F), onError: Color(0xFFFFFFFF),
    errorContainer: Color(0xFFFFD9DE), onErrorContainer: _ink,
    surface: Color(0xFFEEF2E2), onSurface: _ink,
    surfaceContainerLowest: _card, surfaceContainerLow: _card,
    surfaceContainer: Color(0xFFE3EAD0), surfaceContainerHigh: Color(0xFFE3EAD0),
    surfaceContainerHighest: Color(0xFFE3EAD0),
    onSurfaceVariant: Color(0xFF4A5240),
    outline: _ink, outlineVariant: Color(0xFFC5CDB0),
    shadow: _ink, scrim: _ink, surfaceTint: Colors.transparent,
    inverseSurface: _ink, onInverseSurface: _lime, inversePrimary: _lime,
  );
  const ring = Color(0xFF2F4BFF);
  final text = _text();
  const line = BorderSide(color: _ink, width: Rad.stroke);
  RoundedRectangleBorder shape(double r) =>
      RoundedRectangleBorder(borderRadius: BorderRadius.circular(r), side: line);
  OutlineInputBorder field(Color c, double w) => OutlineInputBorder(
      borderRadius: BorderRadius.circular(Rad.lg), borderSide: BorderSide(color: c, width: w));

  return ThemeData(
    useMaterial3: true, colorScheme: scheme, scaffoldBackgroundColor: scheme.surface,
    textTheme: text, focusColor: ring, highlightColor: Colors.transparent,
    splashFactory: InkRipple.splashFactory, splashColor: const Color(0x1F14161A),
    materialTapTargetSize: MaterialTapTargetSize.padded,
    pageTransitionsTheme: const PageTransitionsTheme(builders: {
      TargetPlatform.android: PredictiveBackPageTransitionsBuilder(),
      TargetPlatform.iOS: CupertinoPageTransitionsBuilder(),
    }),
    filledButtonTheme: FilledButtonThemeData(style: FilledButton.styleFrom(
        minimumSize: const Size(64, 52), elevation: 0, shape: shape(Rad.lg),
        side: line, textStyle: text.labelLarge)),
    outlinedButtonTheme: OutlinedButtonThemeData(style: OutlinedButton.styleFrom(
        minimumSize: const Size(64, 52), backgroundColor: _card, foregroundColor: _ink,
        shape: shape(Rad.lg), side: line, textStyle: text.labelLarge)),
    textButtonTheme: TextButtonThemeData(style: TextButton.styleFrom(
        minimumSize: const Size(48, 48), foregroundColor: _ink,
        textStyle: text.labelLarge?.copyWith(decoration: TextDecoration.underline))),
    inputDecorationTheme: InputDecorationTheme(
        filled: true, fillColor: _card, contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 14),
        enabledBorder: field(_ink, Rad.stroke), focusedBorder: field(ring, Rad.focus),
        errorBorder: field(scheme.error, Rad.focus), focusedErrorBorder: field(scheme.error, Rad.focus),
        disabledBorder: field(scheme.onSurfaceVariant, Rad.stroke),
        errorStyle: text.bodyMedium?.copyWith(color: scheme.error, fontWeight: FontWeight.w600)),
    cardTheme: CardThemeData(color: _card, elevation: 0, margin: EdgeInsets.zero,
        surfaceTintColor: Colors.transparent, shadowColor: Colors.transparent, shape: shape(Rad.lg)),
    chipTheme: ChipThemeData(backgroundColor: _card, selectedColor: _lime, side: line,
        shape: shape(Rad.md), labelStyle: text.bodyMedium?.copyWith(fontWeight: FontWeight.w800),
        checkmarkColor: _ink, showCheckmark: true, padding: const EdgeInsets.symmetric(horizontal: 10)),
    segmentedButtonTheme: SegmentedButtonThemeData(style: SegmentedButton.styleFrom(
        backgroundColor: _card, selectedBackgroundColor: _lime, foregroundColor: _ink,
        selectedForegroundColor: _ink, side: line, shape: shape(Rad.lg),
        minimumSize: const Size(48, 48), textStyle: text.bodyMedium?.copyWith(fontWeight: FontWeight.w800))),
    switchTheme: SwitchThemeData(
        thumbColor: const WidgetStatePropertyAll(_ink),
        trackColor: WidgetStateProperty.resolveWith((s) => s.contains(WidgetState.selected) ? _lime : _card),
        trackOutlineColor: const WidgetStatePropertyAll(_ink), trackOutlineWidth: const WidgetStatePropertyAll(Rad.stroke)),
    bottomSheetTheme: BottomSheetThemeData(backgroundColor: _card, modalBarrierColor: const Color(0x9914161A),
        showDragHandle: true, dragHandleColor: _ink, dragHandleSize: const Size(32, 4),
        clipBehavior: Clip.antiAlias, shape: const RoundedRectangleBorder(
            borderRadius: BorderRadius.vertical(top: Radius.circular(Rad.sheet)), side: line)),
    snackBarTheme: SnackBarThemeData(behavior: SnackBarBehavior.floating, backgroundColor: _ink,
        contentTextStyle: text.bodyMedium?.copyWith(color: _lime, fontWeight: FontWeight.w700),
        actionTextColor: _lime, shape: shape(Rad.md)),
    dialogTheme: DialogThemeData(backgroundColor: _card, surfaceTintColor: Colors.transparent, shape: shape(Rad.xl)),
    datePickerTheme: DatePickerThemeData(backgroundColor: _card, shape: shape(Rad.xl),
        todayBorder: line, headerBackgroundColor: _lime, headerForegroundColor: _ink),
    extensions: const <ThemeExtension<dynamic>>[AppColors(), AppTokens()],
  );
}
// main.dart: MaterialApp(theme: buildAppTheme(), themeMode: ThemeMode.light, locale: const Locale('id', 'ID'))
// iOS: Info.plist UIUserInterfaceStyle = Light
```

---

## 3. Komponen

### 3.1 Daftar Komponen
| Komponen | Library | Default M3 → diubah menjadi | Adaptasi iOS | Dipakai di |
|---|---|---|---|---|
| `FilledButton` | Material | tinggi 40, stadion → 52, radius 16, outline 2,5 `foreground`; dibungkus bayangan `shadow-cta` | sama | 5.1, 5.3, 5.4, 5.8, 5.9 |
| `OutlinedButton` | Material | tinggi 40 → 52, latar `card`, outline `foreground`, `shadow-sticker` | sama | 5.9, 5.10 |
| `TextButton` | Material | label bergaris bawah, minimum 48 | sama | 5.1, 5.5, 5.6 |
| `IconButton` | Material | 40 → 48, varian outlined: latar `card`, outline 2,5 | sama | semua app bar |
| `TextField` | Material | outline tipis → outline 2,5 `input`, fokus 3,5 `ring`, label di atas field | sama | 5.8 |
| `SegmentedButton` | Material | tinggi 40 → 48, terpilih `hero` + centang | sama; di atas 130% menjadi kolom vertikal | 5.4, 5.8 |
| `ChoiceChip` | Material | tinggi 32 → 48 (area sentuh), radius 12, outline 2,5, terpilih `hero` + centang | sama | 5.4, 5.6 |
| `Switch` | Material | trek tanpa outline → outline 2,5, trek aktif `hero`, jempol `foreground`, selalu berlabel Aktif atau Mati | tetap M3 (lihat 1.4) | 5.3, 5.7 |
| `StickerCard` | kustom di atas `Card` | tanpa elevasi → outline 2,5 + `shadow-sticker`, sudut mengelupas opsional, ditekan bergeser | sama | 5.2, 5.3, 5.5, 5.6, 5.7 |
| `StickerProgressBar` | kustom | `LinearProgressIndicator` tidak dipakai (tak bisa berborder) | sama | 5.2, 5.3, 5.5, 5.6, 5.9 |
| `StatusBadge` | kustom | `Badge` M3 tidak dipakai; ikon + label, outline 2dp warna teks | sama | 5.2, 5.3, 5.6 |
| `WeekTile` | kustom | tidak ada di M3 | sama | 5.1, 5.5 |
| `GoalSticker` | kustom | kotak 52dp berwarna + pictogram | sama | 5.1, 5.2, 5.4, 5.8 |
| `CelenganNavBar` | kustom meniru `NavigationBar` | 5 slot, 4 tujuan + Setor di tengah; Android tinggi 80 + indikator pil `hero`; iOS tinggi 49 + inset | tinggi dan label mengikuti tab bar iOS | semua tab |
| `BottomSheet` | `showModalBottomSheet` | pegangan 32x4, sudut 28 + outline | pegangan 36x5, sudut 38 | 5.4, 5.8 |
| `AlertDialog` | `showAdaptiveDialog` | M3 bertema (radius 24 + outline) | `CupertinoAlertDialog` bawaan sistem | 5.7, 6.4 |
| `DatePicker` | `showDatePicker` | M3 bertema | `CupertinoDatePicker` di `showCupertinoModalPopup` | 5.8 |
| `SnackBar` | Material | melayang, latar `primary`, teks `primary-foreground`, radius 12 + outline | sama | 6.4 |
| `RefreshIndicator` | `.adaptive` | warna `primary` | indikator iOS bawaan | 5.2, 5.5, 5.6 |
| `CelenganPig` | `CustomPainter` | tidak ada di M3 | sama | 5.1, 5.2, 5.3, 5.9 |
| `Toples` | `CustomPainter` | tidak ada di M3 | sama | 5.6 |
| `CoinKeypad` | kustom | tidak memakai keyboard sistem | sama | 5.4 |
| `Avatar` | `CircleAvatar` | latar warna anggota, outline 2,5, inisial | sama | 5.6, 5.7 |
| `Hero` | Flutter | transisi daftar ke detail | sama | 5.2, 5.3 |

### 3.2 Spesifikasi Komponen
Notasi wireframe: `[[ Label ]]` tombol utama (satu per layar), `[ Label ]` sekunder, `( Label )` ghost atau tautan, `‹` kembali. Semua target sentuh minimal 48 x 48dp (di atas 44pt iOS), jarak antar target minimal 8.

#### FilledButton
- **Ukuran:** tinggi 52, padding horizontal 20, radius 16. Lebar penuh di dock dan sheet.
- **State:** default `primary` + `shadow-cta` · ditekan: bergeser (3, 3), bayangan hilang, 120ms · fokus: border 3,5 `ring` di luar, jarak 2 · nonaktif: latar `muted`, teks `muted-foreground`, outline putus-putus · memuat: koin berputar 22dp + label tetap, tombol nonaktif.
- **Aturan:** satu primary per layar (satu tombol utama); di Beranda, Tantangan, Grup, dan Profil tombol utama adalah slot Setor di bar bawah; label kata kerja ("Setor Rp250.000", "Buat Target").

#### StickerCard
- **Anatomi:** latar `card`, outline 2,5, `radius-lg`, `shadow-sticker`. Sudut mengelupas (kartu target): kotak 26dp di pojok kanan atas, setengahnya `background` (sudut terpotong), garis diagonal `border`, setengah lain `muted` (lipatan); recipe `ClipPath` memotong segitiga + `CustomPainter` untuk garis dan lipatan.
- **State:** ditekan: bergeser (3, 3), bayangan 0; fokus: ring 3,5.

#### StickerProgressBar
Tinggi 14 (12 pada baris padat), `radius-sm`, outline 2,5, trek `card`, isi `hero` dengan garis tinta di ujung kanan; diisi dengan `FractionallySizedBox(widthFactor)` yang dianimasikan `duration-slow`. Variasi grup: segmen warna anggota berurutan. `Semantics(value: '65 persen')`.

#### WeekTile
48 x 48, `radius-md`, outline 2,5; nomor `text-caption` 14sp (maksimal skala 1,5); keadaan di 2.2; ikon 12dp di pojok kanan atas. Ketuk: tooltip jumlah dan tanggal.

#### CelenganNavBar
- **Anggaran lebar di 360dp:** 5 slot x 72 = 360, minimal 48 per slot; label `text-caption` (maksimal 1,3), tidak pernah menyempit lebih dari 12sp x 1,3.
- **Setor di tengah:** kotak 60 x 60, radius 16, `primary`, `shadow-cta`, terangkat 22dp di atas bar, ikon panah ke celah dan garis celah `primary-foreground`; label "Setor" di bawah.
- **Aktif:** indikator pil `hero` 58 x 30 dengan outline 2,5 di belakang ikon, label `foreground`; tidak aktif `muted-foreground`.
- **Safe area:** tinggi bar + `MediaQuery.paddingOf(context).bottom`; lihat 4.1.

#### TextField, SegmentedButton, CoinKeypad
- **TextField:** label di atas (`text-small` w700), tinggi 56, fokus 3,5 `ring`, error 3,5 `destructive` + ikon + teks bantu di bawah.
- **SegmentedButton:** hingga 3 opsi; terpilih diberi centang, bukan warna saja.
- **CoinKeypad:** 3 x 4 tombol 52dp (tinggi), jarak 8; tombol `000` dan hapus; terkontrol (9): `CoinKeypad(value, onChanged)`; nominal minimal Rp10.000.

#### StatusBadge
Tinggi minimal 24, `radius-sm`, outline 2dp warna teks, ikon 12dp + label `text-caption`; warna dari 2.2. Selalu ada label, tidak pernah warna saja.

#### Sheet (BottomSheet)
Tinggi mengikuti isi sampai 94% layar, dapat di-scroll; tombol utama menempel di bawah (`sticky` lewat `Column` + `Expanded(SingleChildScrollView)`); safe area bawah + `viewInsets`.

---

## 4. Layout & Navigasi

### 4.1 Kerangka & Navigasi per Platform
| Elemen | Android | iOS |
|---|---|---|
| Navigasi utama | `CelenganNavBar` 80dp + inset gestur; indikator pil | `CelenganNavBar` 49pt + inset 34pt; indikator pil lebih kecil |
| Header layar dalam | App bar 64dp: kembali, judul `text-title`, aksi | Bar 44pt: chevron + label kembali, judul inline di tengah (`text-title-sm` w800), aksi |
| Kembali | Gestur sistem (predictive back) | Geser dari tepi kiri |
| Sheet | Pegangan 32 x 4, sudut 28 | Pegangan 36 x 5, sudut 38 |
| Status bar | Ikon gelap di atas hero; terang di M2 pra-tahan | sama |
| Haptik dan ripple | Ripple `InkRipple` tipis + translate | Tanpa ripple sistem; hanya translate |
| Dialog dan picker | M3 bertema | Alert dan picker iOS bawaan |

Detail target dan layar tanpa bar bawah: bar navigasi disembunyikan, tombol utama menempel di dasar (dock) dengan inset bawah. Urutan tumpuk (bawah ke atas): isi, dock atau bar navigasi, sheet, scrim, SnackBar, lapisan perayaan (di bawah tombol aksi).

### 4.2 Struktur Navigasi
- **Tab:** Beranda `/home` · Tantangan `/challenge` · Setor (aksi, membuka sheet `/deposit`) · Grup `/groups` · Profil `/profile`. Status tiap tab dipertahankan (`StatefulShellRoute`, `go_router` `[?]`).
- **Dalam:** `/onboarding`, `/goal/:id`, `/goal/:id/celebrate`, `/goal/new` (sheet), `/group/:id`.
- Tombol Setor membawa konteks: dari Detail Target mengisi target itu; dari Tantangan mengisi nominal minggu berjalan; dari Grup mengisi target grup.

### 4.3 Perangkat & Safe Area
- **Kepadatan (aturan profil: daftar utama minimal 4 baris di 375x667 setelah bar atas dan bar bawah):** Beranda di iPhone SE: status bar 20, hero 189 (sapaan 48, total 63, chip berikutnya 48 + jarak), judul bagian 42, kartu target 84 + jarak 8. Kartu ke-4 berakhir di 611 dari 618 (awal bar bawah). 4 baris terlihat penuh, diukur.
- **Android 360x800:** bar bawah mulai di 720; 4 kartu muat dengan sisa ruang.
- **Teks 200%:** semua layar berubah menjadi gulir vertikal; tidak ada teks terpotong; baris boleh bertambah tinggi; judul bagian dan kartu membungkus ke baris kedua; sheet scroll dengan tombol menempel.
- **Anggaran lebar di 360dp (diukur di preview):**
  | Baris | Tersedia | Terpakai terpanjang |
  |---|---|---|
  | Judul + persen kartu target | 241 | 193 ("Tantangan 52 Minggu" + "10,4%") |
  | Chip "setor berikutnya" | 328 | 294 |
  | Chip nominal di sheet (3 chip, padding 10, jarak 6) | 323 | 300 |
  | Grid minggu (6 x 48 + 5 x 8) | 328 | 328 |
  | Bar bawah (5 slot) | 360 | 5 x 71 |
  | Kolom nama anggota (kanan 92 tetap) | 139 | muat, label boleh membungkus |

---

## 5. Spesifikasi Halaman / Section / Layar

Wireframe Android (360dp) sebagai acuan; perbedaan iOS ditulis di bawahnya. Semua nominal dan nama adalah data contoh yang sama dengan `design-preview.html`.

### 5.1 Onboarding: `/onboarding`
- **Tujuan:** memperkenalkan stiker dan celengan, mendapat izin pengingat. **Fitur:** target, setor rutin, tantangan, grup, notifikasi.
- **Prioritas konten:** 1. judul 2. ilustrasi 3. tombol Lanjut.
- **Komponen:** `CelenganPig`, `GoalSticker`, `WeekTile`, `FilledButton`, `TextButton`.

Langkah 1 (M3, `design-preview.html#m3`):
```
┌──────────────────────────┐
│                  ( Lewati )│
│   [Liburan Bali] [Laptop] │
│      (celengan koral)     │
│   [Konser]  [Naik Gunung] │
│ Nabung itu seru kalau ada │
│ temannya.                 │
│ Bikin target, setor rutin │
│        ● ○ ○              │
│ [[ Lanjut ]]              │
└──────────────────────────┘
```
Langkah 2: kartu miring berisi 24 `WeekTile` contoh; judul "Setor dikit, lama-lama jadi liburan."; teks "Minggu pertama Rp5.000, minggu kedua Rp10.000, dan seterusnya. Pelan tapi pasti."; titik 2/3; `[[ Lanjut ]]`.
```
┌──────────────────────────┐
│                  ( Lewati )│
│ ┌ Tantangan 52 Minggu ───┐│
│ │ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓        ││
│ │ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓  [18] ││
│ └────────────────────────┘│
│ Setor dikit, lama-lama    │
│ jadi liburan.             │
│        ○ ● ○              │
│ [[ Lanjut ]]              │
└──────────────────────────┘
```
Langkah 3 (pra-izin notifikasi):
```
┌──────────────────────────┐
│     (stiker lonceng)      │
│ Boleh kami ingatkan di    │
│ hari setor?               │
│ Kamu cuma dapat satu      │
│ pengingat di hari dan jam │
│ yang kamu pilih.          │
│        ○ ○ ●              │
│ [[ Aktifkan Pengingat ]]  │
│ ( Nanti saja )            │
└──────────────────────────┘
```
Dialog izin sistem baru muncul setelah "Aktifkan Pengingat". iOS: "Lewati" di kanan atas; titik langkah di atas tombol; sama.

**State:** tidak ada pemuatan. Izin ditolak: lanjut ke Beranda, banner di Profil (6.3).

### 5.2 Beranda: `/home`
- **Tujuan:** melihat ringkasan semua target dan setor berikutnya. **Fitur:** target, setor rutin, tantangan, grup.
- **Prioritas konten:** 1. total tabungan 2. setor berikutnya 3. daftar target 4. status.
- **Komponen:** `StickerCard`, `StickerProgressBar`, `CelenganPig` (kecil), `IconButton`, `CelenganNavBar`, `RefreshIndicator`, `Hero`.
```
┌──────────────────────────┐
│ (pig) Halo, Dinda    (🔔)│  hero gradien
│       Rabu, 14 Okt 2026  │
│ Total tabunganmu         │
│ Rp10.270.000             │
│ ┌ Setor berikutnya · Jum ┐│
│ │ Liburan Bali  Rp250.000││
│ └────────────────────────┘│
│ Target kamu        4 aktif│
│ ┌ [≈] Liburan Bali   65% ┐│
│ │ Rp3.250.000 dari Rp5.0…││
│ │ ▓▓▓▓▓▓▓▓▓▓░░░░░        ││
│ └────────────────────────┘│
│ ┌ Laptop Baru        40% ┐│
│ ┌ Tantangan 52 Mgg  10,4%┐│
│ ┌ Karimunjawa Sq    62,5%┐│
├──────────────────────────┤
│ Beranda Tantang [[⇩]] Grup Profil│
└──────────────────────────┘
```
iOS: header sama, bar bawah 49pt + inset; kartu dan hero tidak berubah.

**State:**
| State | Tampilan | Teks |
|---|---|---|
| Loading | 4 kerangka kartu berbentuk kartu asli, tanpa shimmer abadi | (tanpa teks) |
| Kosong | `CelenganPig` kaca kosong 120dp; tombol Setor di bar bawah tetap satu-satunya utama, CTA di sini berupa `TextButton` | "Belum ada target. Mulai dari yang kecil: satu target, satu stiker, satu setoran." + `( Buat Target Pertama )` |
| Error | Banner `destructive-subtle` di bawah hero | "Gagal memuat targetmu. Tarik ke bawah untuk coba lagi." |
| Offline | Banner `warning-subtle` | "Kamu sedang offline. Setoran tetap tercatat dan disinkron nanti." |

### 5.3 Detail Target: `/goal/:id`
- **Tujuan:** melihat progres satu target, jadwal, dan riwayat; setor. **Fitur:** target, setor rutin.
- **Prioritas konten:** 1. celengan kaca terisi + nominal 2. sisa dan estimasi 3. jadwal rutin 4. riwayat.
- **Komponen:** `CelenganPig` (kaca), `StatusBadge`, `StickerCard`, `Switch`, `IconButton`, `FilledButton`, `Hero`.
```
┌──────────────────────────┐
│ ‹  Liburan Bali       (⋮)│  latar warna stiker
│     (celengan kaca 65%)  │
│ Rp3.250.000              │
│ dari Rp5.000.000 [Sesuai │
│                  jadwal] │
│ ┌ Sisa ────┐ ┌ Tercapai ─┐│
│ │Rp1.750.000│ │27 Nov 2026││
│ Setor rutin  Aktif [●━]  │
│ Tiap Jumat · Rp250.000   │
│ Riwayat setoran          │
│ ✓ Jumat, 9 Okt Rp250.000 │
│ ✓ Jumat, 2 Okt Rp250.000 │
├──────────────────────────┤
│ [[ Setor ke Liburan Bali ]]│
└──────────────────────────┘
```
**Aksi per status:**
| Status target | Tombol dock | Aksi lain |
|---|---|---|
| `on-track`, `behind` | `[[ Setor ke <nama> ]]` | Ubah target, jeda, hapus (menu ⋮) |
| `done` | `[[ Pecahkan Celengan ]]` membuka 5.9 | Lihat riwayat |
| `paused` | `[[ Lanjutkan Target ]]` | Hapus |

**State:** Loading: hero kerangka. Kosong riwayat: "Belum ada setoran. Setoran pertama akan muncul di sini." Error: "Gagal memuat riwayat. Coba lagi." + `( Coba lagi )`. iOS: bar 44pt, judul inline di tengah.

### 5.4 Setor: `/deposit` (sheet)
- **Tujuan:** mencatat setoran dalam kurang dari 10 detik. **Fitur:** setor, setor rutin.
- **Prioritas konten:** 1. nominal 2. target tujuan 3. chip cepat 4. sumber.
- **Komponen:** `BottomSheet`, `GoalSticker`, `ChoiceChip`, `SegmentedButton`, `CoinKeypad`, `FilledButton`.
```
┌──────────────────────────┐
│ (Beranda di balik scrim) │
├────────── ▬▬ ────────────┤
│ [≈] Setor ke             │
│     Liburan Bali [Ganti›]│
│      Rp250.000           │
│ Sesuai jadwal rutin kamu │
│ [Rp50.000][Rp100.000][✓Rp250.000]│
│ [Tunai][✓Transfer][E-wallet]│
│  1    2    3             │
│  4    5    6             │
│  7    8    9             │
│ 000    0    ⌫            │
│ [[ Setor Rp250.000 ]]    │
└──────────────────────────┘
```
Dari Tantangan: nominal awal Rp90.000 dan target "Tantangan 52 Minggu"; dari Grup: nominal jatah. Setelah berhasil: SnackBar tidak dipakai; tampil M1 penuh.

**State:** Loading: tombol memuat. Kosong (nominal 0): tombol nonaktif, "Masukkan nominal dulu". Error: `ERR_AMOUNT_MIN` di bawah nominal. Offline: tersimpan lokal, badge "Menunggu sinkron" di riwayat.

### 5.5 Tantangan 52 Minggu: `/challenge`
- **Tujuan:** melihat dan mengisi kotak minggu. **Fitur:** tantangan.
- **Prioritas konten:** 1. minggu ke-n dan total 2. minggu ini 3. minggu terlewat 4. grid.
- **Komponen:** `WeekTile`, `StickerCard`, `StickerProgressBar`, `TextButton`, `RefreshIndicator`, `Hero`.
```
┌──────────────────────────┐
│ Tantangan 52 Minggu      │  hero
│ Minggu ke-18             │
│ Rp720.000 dari Rp6.890.000│
│ ▓▓▓▓▓░░░░░░░░░░░         │
│ 17 dari 52 minggu        │
│ ┌ Minggu 18 · 12 sampai 18 Okt ┐│
│ │ Setor Rp90.000    ( Setor )  ││
│ ┌ ⚠ Minggu 9 belum disetor Rp45.000 ( Kejar )┐│
│ Semua minggu             │
│ ✓1 ✓2 ✓3 ✓4 ✓5 ✓6      │
│ ✓7 ✓8 ⚠9 ✓10 ✓11 ✓12   │
│ ✓13 ✓14 ✓15 ✓16 ✓17 [18]│
│ 19 20 21 22 23 24 ...    │
├──────────────────────────┤
│ Beranda Tantang [[⇩]] Grup Profil│
└──────────────────────────┘
```
Jumlah minggu n = Rp5.000 x n; total akhir Rp6.890.000; terkumpul Rp720.000 (minggu 9 terlewat). Setelah setor: M4 (810.000, 18/52).

**State:** Loading: kerangka grid. Kosong (belum ikut): `CelenganPig` + "Mulai tantangan 52 minggu: Rp5.000 di minggu pertama, naik Rp5.000 tiap minggu." + `( Mulai Tantangan )`. Error: "Gagal memuat tantangan. Tarik ke bawah." Semua selesai: arahkan ke 5.9.

### 5.6 Grup: `/groups` dan `/group/:id`
- **Tujuan:** semua anggota melihat progres bersama dan saling mengingatkan. **Fitur:** grup.
- **Prioritas konten:** 1. total grup 2. jatah tiap anggota 3. aktivitas 4. colek.
- **Komponen:** `Toples`, `Avatar`, `StatusBadge`, `StickerCard`, `StickerProgressBar`, `ChoiceChip`, `TextButton`, `RefreshIndicator`.
```
┌──────────────────────────┐
│ [Karimunjawa Squad] [＋] │  header koral
│ ┌toples┐ Terkumpul bareng│
│ │▒▒▒▒▒▒│ Rp5.000.000     │
│ │▓▓▓▓▓▓│ dari Rp8.000.000 · 62,5%│
│ └──────┘ Tenggat 15 Jan 2027│
│ Anggota  4 orang · Rp2.000.000 per orang│
│ (B) Bagas       Rp2.000.000 [✓ Lunas]│
│ (D) Dinda (kamu)Rp1.500.000   75%│
│ (S) Salsa       Rp1.000.000   50%│
│ (K) Kevin         Rp500.000 ( Colek )│
│ Aktivitas                │
│ Bagas setor Rp500.000  kemarin, 19.12│
├──────────────────────────┤
│ Beranda Tantang [[⇩]] Grup Profil│
└──────────────────────────┘
```
Chip ＋ membuka "Gabung dengan kode" atau "Buat grup". M5 menampilkan keadaan setelah Salsa setor Rp500.000 (Rp5.500.000, 68,8%).

**State:** Loading: kerangka toples + 4 baris. Kosong (belum punya grup): `Toples` kosong + "Nabung bareng teman lebih seru. Buat grup atau gabung dengan kode." + `( Buat Grup )`, `( Gabung dengan Kode )`. Error: `ERR_INVITE_INVALID`. Colek terkirim: SnackBar "Kevin sudah kamu colek."

### 5.7 Profil: `/profile`
- **Tujuan:** mengatur pengingat dan akun. **Fitur:** notifikasi.
- **Komponen:** `Avatar`, `StickerCard`, `Switch`, `AlertDialog`.
```
┌──────────────────────────┐
│ (D) Dinda Pratiwi        │  hero
│ Bandung · gabung Jun 2026│
│ [13 minggu rutin][4 target][1 grup]│
│ Pengingat                │
│ Pengingat setor   Aktif [●━]│
│ Kabar dari grup   Aktif [●━]│
│ Jam pengingat       18.00 ›│
│ Akun                     │
│ Ubah nama dan foto      ›│
│ Bantuan                 ›│
│ Keluar                   │
├──────────────────────────┤
│ Beranda Tantang [[⇩]] Grup Profil│
└──────────────────────────┘
```
**State:** Izin notifikasi ditolak: banner `warning-subtle` "Pengingat mati karena izin ditolak." + `( Buka Pengaturan )`. Keluar: `AlertDialog` (6.4). Error: "Gagal menyimpan pengaturan. Coba lagi."

### 5.8 Buat Target: `/goal/new` (sheet)
- **Tujuan:** membuat target dengan saran setoran. **Fitur:** target, setor rutin.
- **Komponen:** `BottomSheet`, `TextField`, `DatePicker`, `SegmentedButton`, `ChoiceChip`, `FilledButton`, `IconButton`.
```
┌──────────────────────────┐
│ Target baru            (✕)│
│ Nama target              │
│ [Konser Jakarta]         │
│ Berapa yang dibutuhkan  Tenggat│
│ [Rp1.200.000]      [12 Des 2026]│
│ Setor rutin              │
│ [✓Mingguan][Bulanan][Bebas]│
│ ┌ Saran: Rp150.000 tiap Jumat ┐│
│ │ 8 setoran, tercapai 4 Des 2026┐│
│ Warna stiker  [✓][ ][ ][ ]│
│ [[ Buat Target ]]        │
└──────────────────────────┘
```
Saran = target dibagi jumlah hari rutin sampai tenggat, dibulatkan ke atas ke kelipatan Rp5.000. **State:** Error per field: `ERR_NAME_EMPTY`, `ERR_AMOUNT_MIN`, `ERR_DEADLINE_PAST`. Memuat: tombol memuat. Keyboard: sheet naik sebesar `viewInsets.bottom`.

### 5.9 Tercapai & Pecah Celengan: `/goal/:id/celebrate`
- **Tujuan:** merayakan target 100%. **Fitur:** target. **Mockup:** `design-preview.html#m2`.
- **Komponen:** `CelenganPig`, `FilledButton`, `OutlinedButton`, `StickerProgressBar` (di sheet ringkasan).
```
Pra-tahan (latar gelap)          Pasca-pecah (gradien hero)
┌────────────────────┐          ┌────────────────────┐
│ (✕)                │          │ (✕)                │
│    (celengan)      │          │ Liburan Bali       │
│ Tahan celengannya. │          │ Target tercapai!   │
│ Terus tahan sampai │          │ (pecahan, koin)    │
│ pecah.             │          │ Rp5.000.000        │
│                    │          │ [[ Selesai ]]      │
│                    │          │ [ Bagikan ke teman ]│
└────────────────────┘          └────────────────────┘
```
Alternatif tanpa tahan (reduced motion, TalkBack, VoiceOver): `[[ Pecahkan celengan ]]` langsung ke keadaan pasca. Setelah Selesai, target pindah ke arsip dan Beranda menampilkan stiker "Tercapai".

### 5.10 Notifikasi
- **Pengingat setor:** notifikasi lokal terjadwal, hari dan jam pilihan user. Android: judul "Celengan · Jumat, 16 Okt", isi "Hari ini jadwal setor. Liburan Bali, Rp250.000. Cuma semenit, yuk.", aksi `[ Setor ]` dan `( Tunda 1 jam )`, ikon kecil monokrom celengan. iOS: judul "Celengan", isi sama, ketuk membuka sheet Setor.
- **Di dalam app:** setoran anggota dan colekan tampil sebagai SnackBar dan baris Aktivitas; colekan: "Dinda mencolek kamu. Jatah setor kamu belum masuk." Izin ditolak: pengingat dalam app saja, `ERR_NOTIF_DENIED`.

---

## 6. Feedback & State Global

### 6.1 Pola Loading
Kerangka berbentuk konten asli saat muat pertama (tanpa shimmer abadi, statis atau satu sapuan); koin berputar di tombol saat menyimpan (label tetap); setoran memakai pembaruan optimis: nominal langsung naik, dibatalkan dengan SnackBar bila gagal.

### 6.2 Pesan Error
| Kode | Pesan ke user | Ditampilkan sebagai |
|---|---|---|
| `ERR_NETWORK` | "Tidak ada koneksi. Perubahanmu tersimpan dan akan dikirim saat online." | Banner di bawah hero |
| `ERR_AMOUNT_MIN` | "Nominal minimal Rp10.000. Naikkan sedikit ya." | Teks di bawah field atau nominal |
| `ERR_NAME_EMPTY` | "Beri nama dulu targetmu, misalnya Liburan Bali." | Teks di bawah field |
| `ERR_DEADLINE_PAST` | "Tenggat sudah lewat. Pilih tanggal setelah hari ini." | Teks di bawah field |
| `ERR_INVITE_INVALID` | "Kode grup tidak ditemukan. Cek lagi atau minta kode baru ke temanmu." | Teks di bawah field |
| `ERR_SAVE_FAILED` | "Setoran belum tersimpan. Coba lagi." | SnackBar dengan aksi "Coba lagi" |
| `ERR_NOTIF_DENIED` | "Pengingat mati karena izin ditolak. Aktifkan di Pengaturan." | Banner di Profil |

### 6.3 Halaman Sistem
| Kondisi | Tampilan | Teks & aksi |
|---|---|---|
| Rute tidak dikenal (tautan rusak) | `CelenganPig` retak + judul | "Halaman ini tidak ada." + `[[ Ke Beranda ]]` |
| Error tak terduga | `CelenganPig` + judul | "Ada yang tidak beres." + `[[ Coba Lagi ]]` |
| Sesi berakhir | Layar penuh | "Sesimu habis. Masuk lagi untuk melanjutkan." + `[[ Masuk ]]` |
| Tanpa jaringan | Banner `warning-subtle` di atas konten | "Kamu sedang offline. Setoran tetap tercatat." |
| Izin ditolak (notifikasi) | Banner di Profil | "Pengingat mati karena izin ditolak." + `( Buka Pengaturan )` |
| Versi usang | Layar penuh tidak bisa ditutup | "Versi Celengan ini sudah terlalu lama." + `[[ Perbarui Sekarang ]]` |

### 6.4 Sukses & Konfirmasi
- **Sukses:** setoran = M1; target dibuat = SnackBar "Target Konser Jakarta sudah ditempel." dan stiker masuk (`Hero`); colek = "Kevin sudah kamu colek."; pengaturan disimpan: SnackBar singkat 3 detik, melayang di atas bar bawah.
- **Konfirmasi:** `AlertDialog` berisi pertanyaan spesifik dan tombol berlabel aksi, mis. "Hapus target Liburan Bali?" dengan "Hapus Target" dan "Batal"; "Keluar dari Celengan?" dengan "Keluar" dan "Batal". Aksi destruktif memakai teks `destructive`, bukan tombol utama.

---

## 7. Konten & Copywriting

### 7.1 Gaya Bahasa
Santai dan hangat, sapaan "kamu", kalimat pendek, tanpa istilah bank, tanpa emoji, tanpa tanda seru berlebihan (satu di momen perayaan). Bercanda secukupnya tentang kebiasaan nabung, tidak menghakimi saat telat.

### 7.2 Glosarium
| Istilah dipakai | Jangan pakai | Catatan |
|---|---|---|
| Target | Goal, tujuan | Satu tabungan dengan nominal dan tenggat |
| Setor, setoran | Deposit, isi, top up | Mencatat uang masuk ke target |
| Celengan | Piggy bank | Nama app dan objeknya |
| Grup, anggota | Squad, tim | Nama grup dibuat user |
| Colek | Poke, ping | Mengingatkan anggota yang belum setor |
| Pecah celengan | Klaim, cairkan | Merayakan target tercapai |
| Tantangan 52 Minggu | Challenge | Nama fitur, ditulis lengkap |

### 7.3 Format
- **Uang:** `Rp5.000.000` (tanpa spasi, titik ribuan, tanpa desimal); tambahan `+Rp250.000`; `NumberFormat.currency(locale: 'id_ID', symbol: 'Rp', decimalDigits: 0)` `[?]` (periksa tidak ada spasi setelah simbol).
- **Persen:** koma desimal, satu angka bila perlu: `65%`, `62,5%`, `10,4%`.
- **Tanggal & waktu:** `16 Okt 2026`, `Jumat, 16 Okt`, jam `18.00` (WIB, 24 jam); relatif: "baru saja", "kemarin, 19.12".

---

## 8. Aksesibilitas
- **Pembaca layar (TalkBack, VoiceOver):** kartu target dibaca satu kalimat ("Liburan Bali, Rp3.250.000 dari Rp5.000.000, 65 persen, sesuai jadwal") lewat `Semantics` + `MergeSemantics`; `WeekTile` dibaca "Minggu 9, Rp45.000, terlewat"; celengan, toples, koin, halftone, dan stiker dekoratif `ExcludeSemantics`.
- **Momen signature:** hasil diumumkan sekali (`SemanticsService`), mis. "Setoran Rp250.000 tersimpan. Liburan Bali sekarang 70 persen."; tahan celengan punya `Semantics(onLongPress)` dan tombol cadangan.
- **Urutan fokus:** atas ke bawah, kiri ke kanan; di sheet, fokus masuk ke judul lalu nominal; tombol utama terakhir; sheet menutup dengan gestur kembali sistem.
- **Skala font:** pengecualian di 2.4; `SegmentedButton` menjadi kolom di atas 130%; sheet dan layar bergulir; tidak ada tinggi tetap pada teks.
- **Warna bukan satu-satunya:** semua status ada label atau ikon dan pola (garis serong, putus-putus); anggota grup selalu berinisial dan bernama.
- **Bahasa:** `locale: Locale('id', 'ID')`; judul rute untuk `Semantics(header: true)` di judul layar.

---

## 9. Catatan Implementasi
- **Preview:** `design-preview.html` hanya simulasi; implementasi memakai widget Flutter dan Material 3, bukan HTML. Ripple, haptik, font sistem, dan pegas native tidak tergambar penuh.
- **Library:** `flutter` (Material 3), `google_fonts`, `go_router` `[?]`, `material_symbols_icons` `[?]`, `haptic_feedback` `[?]`, `intl`. Komponen di 3.1 memakai widget bawaan kecuali yang berlabel kustom.
- **Komponen terkontrol:** `CoinKeypad(value, onChanged)`, `SegmentedButton(selected, onSelectionChanged)`, `StickerProgressBar(value)`; state nominal disimpan di `ValueNotifier<int>` milik sheet Setor.
- **Hook/utilitas yang ditulis sendiri:**
```dart
// lib/core/motion.dart
extension MotionX on BuildContext {
  bool get reduceMotion => MediaQuery.disableAnimationsOf(this);
  Duration dur(Duration d) => reduceMotion ? Duration.zero : d;
}
// lib/widgets/money_text.dart
class MoneyText extends StatelessWidget {
  const MoneyText(this.value, {super.key, this.style});
  final int value; final TextStyle? style;
  @override
  Widget build(BuildContext context) => FittedBox(
      fit: BoxFit.scaleDown, alignment: Alignment.centerLeft,
      child: Text(formatRupiah(value), maxLines: 1, style: style));
}
// HoldToBreak: Listener(onPointerDown: mulai Ticker 1200ms, onPointerUp: t < 1 ? kembali dengan springSlap : onBreak())
```
- **Pola form:** validasi saat kirim dan saat field kehilangan fokus; error ditampilkan di field; tombol utama nonaktif selama nominal kosong atau saat menyimpan; keypad tidak memakai keyboard sistem.
- **Font loading:** bundel file font di `assets/google_fonts/` (nama file asli), daftarkan folder di `pubspec.yaml` bagian `assets:` (bukan `fonts:`), set `GoogleFonts.config.allowRuntimeFetching = false`; weight yang dibundel: Bagel Fat One 400; Rethink Sans 400, 500, 600, 700, 800.
- **Aset toko:** ikon aplikasi (celengan koral di atas lime), ikon adaptif Android (foreground, background, monochrome), splash lime dengan celengan, ikon notifikasi monokrom, ukuran `@2x/@3x`.
- **Lokasi file:** `lib/theme/app_theme.dart`, `lib/widgets/`, `lib/features/{onboarding,home,goal,deposit,challenge,group,profile}/`.
- **Jangan:** memakai UI web yang dibungkus; menimpa gestur kembali; teks ukuran tetap yang menolak `TextScaler`; `BackdropFilter` atau bayangan blur; animasi berulang tanpa henti (kecuali koin pemuatan); lebih dari satu haptik per aksi; stat atau nominal karangan di UI sungguhan; emoji di teks UI; meminta izin notifikasi di peluncuran pertama tanpa 5.1 langkah 3.
