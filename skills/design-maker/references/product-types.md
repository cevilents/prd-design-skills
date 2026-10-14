# Profil Jenis Produk

Baca file ini di langkah 1 (setelah PRD/brief terbaca, sebelum ronde pertanyaan 1d) untuk menentukan **profil** yang dipakai, lalu patuhi profil itu di langkah 2 sampai 7. Skill ini tidak boleh berasumsi semua produk adalah web app mobile-first dengan role, daftar order, dan status lifecycle. Profil menentukan: apa arti "wow", layar apa yang wajib dispesifikasikan, aturan kepadatan, isi preview, dan bagian template mana yang disesuaikan atau dihapus.

Prinsip lintas profil:
- **Level ambisi default Spektakuler, kecuali profil 5 (dashboard) dan 8 (internal tool) yang default Ekspresif.** Yang berubah per profil adalah tempat kemewahan visual dicurahkan, bukan besarnya ambisi. Wow selalu di momen jarang, tenang dan cepat di tempat orang bekerja berulang (visual-craft 1.2).
- **Profil menggantikan aturan generik** yang bertentangan: "≥ 3 item di 360×640" (SKILL 3b), "mobile-first", "bingkai HP 390px" di preview, "role", "status badge", "kode error". Aturan aksesibilitas (kontras, focus, reduced motion, zoom 200%) tidak pernah dikalahkan profil.
- **Tidak ada bagian template baru.** Semua aturan profil dipetakan ke bagian yang sudah ada. Bagian yang tidak relevan (mis. 2.2 Warna Status, kode error di 6.2) memakai izin "hapus kalau tidak relevan" dari template; lint token (2.1, 2.3, 2.8) tetap berlaku untuk semua profil.
- Bagian 5 template ("Spesifikasi Halaman / Section / Layar") diisi sesuai profil, tetap sebagai `### 5.x <Nama>: \`<route>\`` (landing: satu 5.x per section dengan route berupa jangkar, mis. `/#hero`), dengan wireframe ASCII (desktop dulu untuk profil desktop-first), komponen, prioritas konten, dan state.
- **Semua angka kepadatan di file ini adalah "titik awal, sesuaikan dengan konten"**, bukan aturan keras. Tulis angka final dan hitungannya di 4.3 Pola Responsif.
- **Kepekaan budaya pasar target:** periksa maskot, simbol, warna, gestur tangan, dan ilustrasi terhadap budaya dan agama pengguna (mis. untuk pasar Indonesia mayoritas Muslim, hindari maskot babi untuk produk umum; celengan bisa digambar sebagai ayam jago atau bentuk lain). Catat alternatif di 1.4 kalau ragu.
- Pemetaan umum: aturan kepadatan dan breakpoint → 4.3 dan 2.5; aturan visualisasi data → 2.6 (bahasa visual) dan 3.2 (komponen grafik); aturan membaca → 2.4; performa dan SEO → 9; gestur/haptik → 2.7 dan 3.2.

---

## Daftar isi profil

1. Landing page / marketing site
2. Company profile / portfolio / personal site
3. Konten: blog, media, dokumentasi, edukasi
4. E-commerce / katalog / toko online
5. Web app / SaaS dashboard
6. Web app mobile-first / PWA (default lama)
7. Aplikasi mobile native
8. Internal tool / admin panel
9. Hybrid
10. Tabel keputusan dan aturan kalau brief tidak jelas

---

## 1. Landing page / marketing site

**Cara mengenali:** PRD/brief menyebut hero, CTA, waitlist, pricing, "launch", "kampanye", "konversi", "sign up"; halaman tunggal atau 3 sampai 6 halaman statis; tidak ada login atau data per user; sukses diukur dari klik CTA, bukan dari tugas selesai.

**Arti "wow" di sini:** orang berhenti di 3 detik pertama dan scroll sampai habis.
- Hero dengan satu pernyataan raksasa (skala ≥ 8× teks isi) dan satu visual yang hanya mungkin untuk produk ini (demo produk nyata, objek 3D/SVG dari dunia produk, tipografi kinetik).
- Narasi scroll: tiap section satu gagasan, ritme berganti antara padat dan lega, perubahan warna latar sebagai bab.
- Tipografi editorial, bidang warna penuh, komposisi asimetris, satu elemen yang keluar dari grid.

**Jebakan:**
- Grid 3 kolom kartu fitur (ikon + judul + 2 baris), logo bar "Dipercaya oleh" dengan logo karangan, testimoni dengan foto stok dan nama karangan, hitungan angka "10.000+ pengguna" tanpa data, gradien ungu-biru di hero, mockup laptop miring bawaan, FAQ akordeon default tanpa suara brand.
- Animasi scroll berlebihan sampai konten tertahan (scroll-jacking), parallax di mobile, video autoplay berat di hero.
- Banyak CTA berbeda yang bersaing.

**Layar/section inti yang wajib dispesifikasikan (bagian 5):** satu entri per section dari atas ke bawah, bukan per "halaman":
- Nav (tipe: sticky/transparan→solid saat scroll, menu mobile), Hero, Bukti/demo produk, 2 sampai 4 section narasi (masalah → cara kerja → hasil), Pricing (kalau ada), Bukti sosial **nyata** (kalau tidak ada, section dihapus), FAQ, CTA penutup, Footer.
- Untuk tiap section: tujuan satu kalimat, **satu CTA primer**, wireframe desktop 1440 dan mobile 390, **koreografi scroll** (pemicu, ms, easing, apa yang ditahan/di-pin), aset (SVG/foto, art direction), state reduced-motion.
- Halaman pendukung: 404, terima kasih setelah submit, halaman legal (satu baris).

**Kandidat momen signature:**
1. Hero reveal (kata per kata / mask / objek masuk) yang selesai ≤ 1200ms dan bisa dilewati.
2. Demo produk interaktif atau animasi "cara kerja" yang dikendalikan scroll.
3. Pergantian bab: latar berubah warna/tema saat section masuk.
4. Hitung angka hero dari data nyata (hanya bila datanya ada).
5. Micro-interaction CTA (tombol magnetik tipis, kursor kustom tidak wajib) dan transisi ke form/waitlist.

**Aturan kepadatan & breakpoint (titik awal, sesuaikan dengan konten; tulis di 4.3):**
- Desain di **1440** dan **390** (juga cek 768, 1024, 1920 sebagai maksimal lebar konten).
- Hero muat di atas lipatan di **1440×900** dan **390×844** (headline + sub + CTA primer + petunjuk ada isi di bawah terlihat).
- Satu CTA primer per section. Ukuran teks isi ≥ 16px mobile; lebar baris paragraf 45 sampai 75 karakter.
- Pengganti SKILL 3b: tidak ada hitungan item per layar; ganti dengan "tiap section terbaca dalam 5 detik".

**Isi preview HTML:** halaman utuh dari nav sampai footer sebagai satu scroll di desktop (frame lebar 1440 diskalakan), plus frame mobile 390 untuk hero, satu section narasi, dan nav terbuka. Animasi scroll benar-benar berjalan (IntersectionObserver / CSS scroll-driven dengan fallback). Tombol "Putar ulang" untuk hero. Tombol simulasi reduced-motion.

**Template yang disesuaikan/dihapus:**
- 2.2 Warna Status: hapus kalau tidak relevan (kecuali status form: sukses/error submit). 6.2 Pesan Error: hanya validasi form (email salah, sudah terdaftar); hapus baris kode error PRD yang tidak ada. 6.3: hanya 404, 500, offline ringan.
- 4.1 Kerangka & Navigasi: isi sebagai "Nav & footer" (satu baris, bukan per role). 4.2: peta section dan tautan jangkar. 4.3: perubahan layout per breakpoint 1440/768/390.
- 3: komponen hanya yang dipakai (Button, Input, Accordion, Dialog video); hapus komponen dashboard.
- Tambah di 1.6: pemetaan section → momen signature. Tambah di 9: anggaran performa.

**Kebutuhan khusus:**
- **Performa:** LCP < 2.5s, CLS < 0.1, INP < 200ms; gambar hero dengan `fetchpriority="high"`, format AVIF/WebP, ukuran ditentukan (`width`/`height`), font maksimal 2 keluarga dengan `font-display: swap` dan subset; video hanya setelah interaksi atau berkas poster ringan; JS animasi di-load setelah hero.
- **Art direction citra:** tulis arahan per gambar (subjek, sudut, cahaya, palet token); tanpa foto stok klise (orang tertawa di depan laptop, jabat tangan, kota dari udara). Alternatif: ilustrasi SVG custom, tangkapan layar produk nyata, tipografi sebagai gambar.
- **SEO:** satu `h1`, hierarki heading berurutan, landmark, meta title/description per halaman, Open Graph image, teks asli di DOM (bukan di gambar), tautan jangkar bernama.
- **Konversi:** satu CTA primer per section, label kata kerja spesifik ("Coba gratis 14 hari"), form sependek mungkin, tanpa pop-up penutup layar.
- **Tanpa bukti sosial palsu:** logo, testimoni, angka, dan rating hanya dari data nyata; kalau belum ada, ganti dengan bukti lain (demo, jaminan, proses, cuplikan hasil) dan catat di 1.4.

---

## 2. Company profile / portfolio / personal site

**Cara mengenali:** "tentang kami", layanan, tim, studio, kasus/proyek, CV, kontak; sedikit halaman (5 sampai 10); tujuan: dipercaya, diingat, dihubungi; kata kunci "portfolio", "company profile", "personal brand".

**Arti "wow" di sini:** **kepribadian yang tidak bisa ditiru** dan karya yang tampil besar.
- Tipografi bersuara (display khas, kerning dikerjakan), tata letak editorial atau eksperimental yang tetap terbaca, kursor/hover yang punya karakter.
- Karya/proyek sebagai pahlawan: gambar besar, transisi bersama dari thumbnail ke halaman proyek, detail studi kasus yang bercerita.
- Cara menyajikan diri yang konsisten: nada copy, motif, dan warna terasa seperti satu orang/tim.

**Jebakan:** template portofolio (nama besar + "Hi, I'm ..." + grid kartu proyek yang seragam), "Our values" 3 ikon, foto tim stok, slider hero otomatis, "Let's work together" tanpa kontak nyata, animasi berlebihan sampai karya sulit dilihat, menu eksperimental yang menyulitkan navigasi.

**Layar/section inti (bagian 5):**
- Beranda (pernyataan posisi + karya unggulan + ajakan kontak), Daftar karya/proyek (dengan filter ringan bila lebih dari 8), **Detail proyek/studi kasus** (templat naratif: konteks → proses → hasil, galeri, kredit), Tentang/tim, Layanan (kalau perusahaan), Kontak (form + alternatif langsung: email, WhatsApp, peta), 404.
- Tiap layar: wireframe desktop dan mobile, urutan prioritas, state gambar loading, spesifikasi galeri/lightbox, transisi antarhalaman.

**Kandidat momen signature:**
1. Pembuka beranda (intro tipografis/nama yang menyusun diri, ≤ 1200ms, bisa dilewati).
2. Transisi shared-element thumbnail → halaman proyek (View Transitions dengan fallback fade).
3. Hover/fokus karya: pratinjau bergerak, kursor kontekstual.
4. Studi kasus dengan scroll naratif (before/after, penyingkapan proses).
5. Footer/kontak sebagai penutup yang berkesan (jam lokal, ketersediaan nyata, tombol salin email).

**Aturan kepadatan & breakpoint (titik awal, sesuaikan dengan konten; tulis di 4.3):** desain di **1440**, **1024**, **390**. Hero beranda muat di 1440×900 dan 390×844. Galeri: kolom 12-grid desktop, 1 kolom mobile dengan rasio gambar tetap. Tidak ada aturan "≥ 3 item"; ganti dengan "karya unggulan terlihat tanpa scroll kedua".

**Isi preview HTML:** beranda penuh (desktop skala), halaman detail proyek, halaman kontak, nav mobile terbuka, 2 layar mobile. Transisi antarhalaman didemokan (single-file SPA sederhana atau tab). Hover/kursor didemokan.

**Template yang disesuaikan/dihapus:** sama dengan landing untuk 2.2 (hapus kalau tidak relevan), 6.2, 6.3; 4.1 diisi "Nav & footer"; komponen: Gallery/Lightbox, Project card, Contact form. Tambah 2.4 skala tipografi editorial (hero bisa sampai 160px di desktop, clamp). 7: pedoman suara pribadi/brand lebih panjang dari glosarium.

**Kebutuhan khusus:** gambar karya adalah aset kunci: kompresi tanpa merusak kualitas, `srcset`/`sizes`, blur-up atau warna dominan sebagai placeholder, `alt` deskriptif. Tidak ada klaim klien/penghargaan palsu. Kontak harus bekerja (alamat nyata atau ditandai "data contoh" di preview). Dark/light mengikuti karakter, bukan tren. Anggaran performa sama dengan landing.

---

## 3. Konten: blog, media, dokumentasi, edukasi

**Cara mengenali:** artikel, kategori, tag, pencarian, penulis, "baca", "kursus", "modul", "docs", "changelog"; tujuan: dibaca, ditemukan, dipelajari; volume konten besar dan terus bertambah.

**Arti "wow" di sini:** **pengalaman membaca yang luar biasa** dan identitas editorial yang kuat, bukan efek.
- Tipografi membaca yang sempurna (ritme vertikal, ukuran, kontras), halaman artikel yang terasa seperti majalah, kartu artikel dengan hierarki tegas.
- Navigasi dan pencarian yang cepat dan cerdas; penanda progres baca; mode baca nyaman.
- Untuk edukasi: rasa maju (progres, pencapaian) yang memuaskan; untuk dokumentasi: kecepatan menemukan jawaban dan blok kode yang indah.

**Jebakan:** grid kartu artikel seragam dengan gambar stok, hero besar menutup judul artikel, lebar baris terlalu lebar, teks abu-abu muda 14px, popup newsletter, iklan yang merusak tata letak, sidebar penuh widget, "Baca selengkapnya" di setiap kartu, animasi masuk di halaman baca.

**Layar/section inti (bagian 5):**
- Beranda/indeks (artikel unggulan + terbaru + kategori), **Halaman artikel** (spek tipografi penuh), Daftar kategori/tag/penulis, **Pencarian** (kontrak query `?q=`, hasil, sorotan teks, kosong), Profil penulis, Newsletter/langganan (inline, bukan popup).
- Edukasi: Katalog kursus, Halaman kursus, **Pemutar pelajaran** (video/teks + daftar modul + progres), Kuis dan hasil, Sertifikat.
- Dokumentasi: Shell docs (sidebar pohon + daftar isi kanan + pencarian ⌘K), Halaman referensi/API, Blok kode, Changelog.
- Tiap layar: wireframe desktop dan mobile, state loading/kosong/error, versi cetak bila relevan.

**Kandidat momen signature:**
1. Halaman artikel pembuka (judul display besar, drop cap/inisial, pengantar yang menarik masuk).
2. Penanda progres baca + daftar isi yang menyala mengikuti scroll.
3. Pencarian instan (⌘K) dengan hasil bersorot, tanpa jeda.
4. Edukasi: layar selesai modul / streak / sertifikat.
5. Blok kode atau diagram interaktif yang menyorot langkah.

**Aturan kepadatan & breakpoint:**
- **Aturan membaca (ditulis di 2.4 dan dirujuk 5.x artikel; aturan 60 sampai 75 karakter adalah kaidah, bukan titik awal):** lebar baris (measure) **60 sampai 75 karakter** (≈ 65ch, `max-width: 65ch` pada kolom isi); ukuran isi 17 sampai 20px desktop, ≥ 16px mobile; line-height 1.6 sampai 1.75; ritme vertikal berbasis kelipatan baseline; judul `text-wrap: balance`; paragraf `text-wrap: pretty`; kontras isi ≥ 7:1 dianjurkan (minimum 4.5).
- Titik awal breakpoint (tulis di 4.3): **1440**, **1024**, **768**, **390**. Sidebar docs runtuh di bawah 1024; daftar isi pindah ke atas artikel di bawah 1280.
- Pengganti 3b: "indeks menampilkan ≥ 4 judul artikel tanpa scroll di 1440×900 dan ≥ 2 di 390×844".

**Isi preview HTML:** beranda, satu artikel panjang lengkap (dengan gambar, kutipan, kode, tabel, daftar), pencarian dengan hasil, halaman kategori, dan (bila edukasi/docs) pemutar pelajaran atau shell docs. Tampilkan desktop dan mobile; mode baca terang/gelap bila dipilih. Tunjukkan spesimen tipografi (ukuran, measure) sebagai bagian "sistem visual".

**Template yang disesuaikan/dihapus:** 2.2 Warna Status: hanya untuk status konten (draft/terbit) jika ada, selain itu hapus kalau tidak relevan. 2.4 diperluas dengan token prosa (`prose-*`: h1 sampai h4, blockquote, kode inline, blok kode, tabel, daftar, tautan, `figcaption`). Tambah komponen: Article card, Table of contents, Code block, Callout, Pagination/Prev-Next, Breadcrumb. 4.1 diisi "Header, footer, sidebar docs".

**Kebutuhan khusus:** tipografi variabel dengan subset aksara (Latin + tanda Indonesia), `font-display: swap`, ukuran font menghormati preferensi pengguna (`rem`). SEO penuh (skema Article, canonical, breadcrumb, heading berurutan). Aksesibilitas: tautan terlihat (garis bawah), skip link, kontras kode, urutan heading. Cetak: `@media print` untuk artikel/dokumen. Jangan memasang animasi masuk pada isi bacaan. Pencarian harus tahan typo bila memungkinkan.

---

## 4. E-commerce / katalog / toko online

**Cara mengenali:** produk, SKU, varian, keranjang, checkout, ongkir, voucher, stok, katalog, "beli", "pesan"; ada pembayaran; pembeli anonim atau berakun; juga katalog tanpa pembayaran (tanya via WhatsApp).

**Arti "wow" di sini:** **produk terasa ingin dimiliki** dan beli semudah mungkin.
- Fotografi/visual produk sebagai bintang, bidang warna yang menonjolkan produk, tipografi harga yang jelas dan percaya diri.
- Interaksi produk yang memuaskan (galeri zoom, pemilih varian yang mengubah gambar/warna halaman, penambahan keranjang yang terasa fisik).
- Checkout yang tenang, singkat, dan meyakinkan.

**Jebakan:** grid kartu produk identik berlapis bayangan dengan tombol "Add to cart" di setiap kartu, banner diskon berkedip, countdown palsu, "Hanya tersisa 2!" palsu, rating bintang karangan, badge "Terlaris" di semua produk, pop-up diskon saat masuk, checkout multi-halaman tanpa penanda progres, gambar tidak seragam rasio.

**Layar/section inti (bagian 5):**
- **PLP** (daftar produk: filter, urutan, grid, kontrak query `?kategori=&harga=&urut=&hal=`, state kosong hasil), **PDP** (galeri, judul, harga, varian, stok, ongkir, deskripsi, ulasan nyata, produk terkait, bar beli lengket di mobile), **Keranjang** (ubah jumlah, hapus, voucher, ringkasan), **Checkout** (alamat, pengiriman, pembayaran, ringkasan; per langkah satu wireframe), Konfirmasi pesanan, Lacak/riwayat pesanan, Pencarian (autocomplete), Beranda toko (koleksi, kategori), Akun (opsional).
- Status pesanan (menunggu bayar, dikemas, dikirim, selesai, batal): wajib badge di 2.2 bila ada riwayat pesanan. Kode error pembayaran/stok/voucher wajib di 6.2.
- Tiap layar: wireframe mobile dan desktop (strukturnya sering berbeda: filter sidebar vs sheet).

**Kandidat momen signature:**
1. Hero koleksi/produk unggulan (sinematik, satu produk, satu pernyataan).
2. Pemilih varian yang mengubah gambar, warna aksen halaman, dan harga secara mulus.
3. Tambah ke keranjang: produk "terbang" ke ikon keranjang + haptic + ringkasan mini.
4. Checkout sukses / pesanan dikonfirmasi (perayaan tenang, bukan konfeti berlebihan).
5. Galeri produk (zoom, geser, transisi shared-element dari PLP ke PDP).

**Aturan kepadatan & breakpoint (titik awal, sesuaikan dengan konten; tulis di 4.3):**
- Desain di **1440**, **1024**, **768**, **390**. PLP: desktop 4 kolom (≥ 8 produk terlihat di 1440×900), tablet 3, mobile 2 kolom (≥ 4 produk terlihat penuh di 390×844). Tap target ≥ 44px; bar beli lengket tidak menutupi konten.
- PDP mobile: harga dan tombol beli terlihat tanpa scroll ke bawah galeri (bar lengket di zona jempol).
- Pengganti 3b: "PLP dan keranjang diukur seperti di atas".

**Isi preview HTML:** beranda toko, PLP (dengan filter terbuka di mobile sebagai sheet), PDP (desktop dan mobile dengan bar lengket), keranjang, checkout (semua langkah), konfirmasi. Interaksi pemilih varian dan tambah-ke-keranjang berjalan. Data produk realistis (nama, harga Rupiah, varian, stok).

**Template yang disesuaikan/dihapus:** 2.2 untuk status pesanan dan stok (tersedia/menipis/habis dengan teks, bukan warna saja). Tambah komponen: Product card, Gallery, Variant picker, Quantity stepper, Price, Cart item, Order summary, Address form, Payment method picker. 7.3 Format: uang `Rp149.000`, harga coret, ongkir, estimasi tiba. 4.1: header dengan pencarian + keranjang + akun; density PLP/PDP di 4.3.

**Kebutuhan khusus:**
- **Performa:** LCP < 2.5s di PLP dan PDP; `srcset` + `sizes`, lazy-load di bawah lipatan, rasio gambar tetap (cegah CLS), placeholder warna dominan; font ≤ 2 keluarga.
- **Art direction citra produk:** satu aturan latar dan sudut untuk seluruh katalog (latar konsisten, bayangan seragam, rasio 4:5 atau 1:1); tanpa foto stok orang.
- **Kepercayaan:** ulasan, rating, stok, dan "terjual" hanya dari data nyata; kebijakan retur, ongkir, dan keamanan dekat tombol bayar.
- **SEO:** skema Product (harga, ketersediaan), canonical untuk varian/filter, heading berurutan.
- **Konversi:** satu tombol primer per layar (beli/lanjut); checkout tanpa distraksi (navigasi minimal); guest checkout bila PRD mengizinkan.

---

## 5. Web app / SaaS dashboard (desktop-first, data-dense)

**Cara mengenali:** login lalu area kerja, tabel, grafik, filter, laporan, workspace/tim, role dan izin, "dashboard", "analytics", "CRM", "ERP ringan"; dipakai berjam-jam di laptop/monitor; mobile hanya pendamping.

**Arti "wow" di sini:** **kejelasan dan kecepatan di bawah kepadatan**, dengan karakter.
- Shell yang terasa seperti perkakas profesional bermerek: tipografi data yang tajam (angka tabular, skala rapat), warna semantik yang disiplin, satu aksen khas.
- Visualisasi data dengan kepribadian (visual-craft 2.8): satu seri disorot, anotasi langsung, jawaban atas pertanyaan, bukan dekorasi.
- Interaksi cepat: command palette, shortcut, inline edit, transisi 120 sampai 200ms.
- Momen kemewahan dipakai hemat: onboarding, empty state pertama, ringkasan hari/bulan, pencapaian.

**Jebakan:** deretan 4 kartu statistik setara berisi angka dummy, grafik garis/donut default dengan palet pelangi, sidebar 12 ikon tanpa label, tabel tanpa urutan/filter/kolom yang bisa diatur, glassmorphism dan glow di semua panel, animasi masuk di tabel yang dibuka puluhan kali sehari, mode gelap neon.

**Layar/section inti (bagian 5):**
- **Shell** (sidebar/topbar, workspace switcher, ⌘K, notifikasi, profil), **Ringkasan/Dashboard** (satu angka dominan + tren + daftar kerja), **Tabel data** (kolom, urut, filter, pencarian, seleksi massal, paginasi/infinite, kepadatan, ekspor), **Detail rekaman** (drawer atau halaman), **Form buat/ubah** (validasi inline), **Grafik/Laporan** (rentang tanggal, perbandingan), **Pengaturan** (profil, tim, izin, tagihan), **Onboarding/empty state**, Halaman sistem.
- Wajib: state loading (skeleton berbentuk baris), kosong (dengan aksi), error (per panel dan per halaman), tanpa izin, dan data parsial.
- Kontrak filter: query param, perilaku saat kombinasi, penyimpanan tampilan (saved views).

**Kandidat momen signature:**
1. Onboarding / setup workspace (penyusunan ruang kerja secara bertahap).
2. Ringkasan dengan angka hero + sparkline (hitung naik sekali saat muat pertama).
3. Command palette ⌘K.
4. Empty state pertama yang mengajak satu aksi (ilustrasi domain).
5. Pencapaian/milestone atau laporan siap ("Laporan Oktober sudah jadi").

**Aturan kepadatan & breakpoint:**
- Desain di **1440** dan **1280**; minimum didukung **1024**; tablet 768 dan mobile 390 sebagai versi ringkas (sidebar jadi drawer, tabel jadi daftar kartu atau tabel dengan scroll horizontal terkontrol).
- **Kepadatan dihitung (titik awal, sesuaikan dengan konten):** tabel utama menampilkan **≥ 12 baris** di 1440×900 pada kepadatan normal (tinggi baris 44px; kompak 36px → ≥ 15 baris; lega 52px). Tulis hasil hitungan: 900 − topbar − toolbar − header tabel − footer = ruang ÷ tinggi baris.
- Tap/klik target ≥ 32px desktop (24px minimum WCAG 2.2) dan ≥ 44px di breakpoint sentuh.
- Panel konten maksimal 1600px; di atas itu, pusatkan atau tambah kolom.

**Isi preview HTML:** frame desktop 1440 (diskalakan) untuk: dashboard, tabel dengan filter aktif dan baris terpilih, detail rekaman (drawer terbuka), form, laporan/grafik, ⌘K terbuka, empty state, loading skeleton. Frame mobile 390 untuk dashboard dan satu tabel. Toggle kepadatan (normal/kompak/lega) berfungsi. Dua sampai tiga momen signature (level Ekspresif).

**Template yang disesuaikan/dihapus (tanpa bagian baru):** 4.1 tetap per role (role relevan); 2.2 Warna Status untuk status rekaman. **Data viz** ditulis di 2.6 sebagai sub-judul tebal "Visualisasi data" (palet kategorikal/sekuens/divergen dari token, aturan warna, warna buta-aman) dan komponennya di 3.2 (Chart wrapper, tooltip, legenda, tabel setara); format angka di 7.3. **Kepadatan** (mode normal/kompak/lega: tinggi baris, padding sel, ukuran teks) ditulis di 4.3 Pola Responsif dan nilainya di 2.5. Komponen tambahan di 3.1/3.2: Data table (sortable, sticky header, seleksi), Filter bar, Stat/KPI, Command, Drawer, Tabs, Date range picker. SKILL 3b diganti dengan angka kepadatan di atas.

**Kebutuhan khusus:**
- **Format angka:** `tabular-nums`, pemisah ribuan Indonesia (titik), singkatan (`1,2 jt`, `3,4 M`) dengan tooltip nilai penuh, persentase satu desimal, delta dengan tanda dan ikon (bukan warna saja), satuan konsisten.
- **Data viz:** pertanyaan sebagai judul grafik, satu seri disorot, anotasi langsung, tabel setara untuk pembaca layar, warna tidak satu-satunya pembeda, rentang sumbu jujur (batang mulai dari nol).
- **Tabel:** header lengket, kolom pertama lengket di scroll horizontal, penyelarasan angka kanan, teks kiri, truncation dengan tooltip, aksi baris muncul saat hover/fokus (tetap bisa diakses keyboard).
- **Keyboard:** semua aksi inti tersedia lewat keyboard, daftar shortcut di 8.
- Mode gelap umum dipakai; rancang kedua mode bila pengguna bekerja lama.

---

## 6. Web app mobile-first / PWA (UMKM tools, booking, tracking)

Ini profil bawaan lama skill ini dan template sudah ditulis untuknya.

**Cara mengenali:** PRD menyebut "mobile-first", "PWA", Android kelas menengah, dipakai berdiri/di sela aktivitas, role (owner, staf, pelanggan), order/booking/antrean, status lifecycle, kode error, WhatsApp, pembayaran lokal; target user UMKM atau pelanggan umum.

**Arti "wow" di sini:** momen emosional yang jarang (status pelanggan, sukses bayar, onboarding, empty state) dengan layar kerja yang cepat dan padat (visual-craft 1.2).

**Jebakan:** daftar order dengan kartu berbayangan tebal dan stagger tiap refetch, glass di semua tempat, status hanya warna, dashboard 4 kartu statistik, pop-up izin instal PWA sebelum nilai terlihat, animasi masuk di form kasir.

**Layar/section inti (bagian 5):** satu spesifikasi per halaman di Daftar Halaman PRD, wireframe mobile (desktop bila berbeda), state loading/kosong/error, tabel aksi per status, wireframe per langkah alur multi-langkah (login → OTP). Semua aturan template (bagian 5 sampai 6) berlaku apa adanya.

**Kandidat momen signature:** layar status pelanggan, perayaan lunas/selesai, ringkasan owner dengan angka hero, login/onboarding, empty state pertama (katalog visual-craft 3).

**Aturan kepadatan & breakpoint (aturan lama, tetap berlaku untuk profil ini):** desain di **360** (minimum), **390** (bingkai preview), **430**, lalu desktop **1024+** sebagai bonus. **≥ 3 item penuh di 360×640** untuk daftar kerja utama (SKILL 3b, dihitung). Tap target ≥ 44px; anggaran lebar 360px (stack-shadcn.md); zona jempol untuk aksi utama; zoom 200% (180px) aman.

**Isi preview HTML:** semua momen signature dalam bingkai HP 390px, ≥ 3 layar kerja per role, versi desktop bila beda, sistem visual, simulasi reduced motion (sesuai SKILL langkah 6).

**Template yang disesuaikan/dihapus:** tidak ada; ini profil acuan. Tambahan PWA di 9: manifest, `theme-color`, ikon maskable, perilaku offline/instal, safe area (`env(safe-area-inset-*)`).

**Kebutuhan khusus:** konektivitas buruk (skeleton, optimistic update, antrean offline), data seluler hemat (gambar kecil, font subset), `inputmode`/`autocomplete`, notifikasi push berkonteks, berbagi ke WhatsApp/ cetak nota bila PRD memintanya.

---

## 7. Aplikasi mobile native (iOS/Android; React Native, Flutter, SwiftUI)

**Cara mengenali:** PRD menyebut iOS/Android, App Store/Play Store, React Native/Expo, Flutter, SwiftUI/Jetpack Compose, push notification, kamera, biometrik, gestur, offline, widget; bukan sekadar PWA.

**Arti "wow" di sini:** **terasa asli dan hidup di tangan**: gestur, haptik, transisi fisik, dan detail platform, dengan identitas merek yang tetap terbaca.
- Transisi shared-element, sheet yang bisa ditarik, gestur geser dengan momentum, animasi pegas yang meyakinkan, haptik tepat guna.
- Layar hero/onboarding sinematik; ikon aplikasi dan splash menjadi bagian pengalaman.
- Mengikuti konvensi platform di tempat pengguna mengharapkannya, memberi identitas di tempat lain.

**Jebakan:** UI web dibungkus (hover, sidebar, tabel lebar), navigasi atas dengan hamburger di mana tab bar lebih tepat, tombol kembali kustom yang mematikan gestur geser-kembali, ukuran teks tetap yang mengabaikan Dynamic Type/font scaling, mengabaikan safe area (notch, home indicator, status bar), animasi 60fps yang jatuh di Android menengah, haptik berlebihan, dialog izin tanpa konteks.

**Layar/section inti (bagian 5):**
- Splash + onboarding, **Navigasi utama** (tab bar iOS / navigation bar Material 3 bawah, atau drawer bila ≥ 5 tujuan), layar utama per tab, detail, **sheet/modal** (bottom sheet), form dan keyboard, pengaturan, izin (kamera, lokasi, notifikasi: layar pra-izin dengan alasan), offline/sinkron, notifikasi (tampilan push dan in-app), widget/Live Activity bila ada.
- Per layar: wireframe untuk **kedua platform bila berbeda** (atau satu dengan catatan "iOS: ..., Android: ..."), orientasi (potret; lanskap bila relevan), state loading/kosong/error/offline, perilaku keyboard.
- Wajib: tabel gestur (tarik untuk muat ulang, geser baris, tahan lama, geser kembali) dan tabel haptik.

**Kandidat momen signature:**
1. Onboarding sinematik dengan ilustrasi/animasi bergaya merek.
2. Transisi shared-element daftar → detail (hero image/angka).
3. Momen sukses (transaksi/target tercapai): animasi + haptik `success` + suara opsional.
4. Layar utama dengan angka hero / kartu interaktif yang bisa ditarik.
5. Sheet bergaya khas (tarik, snap ke ketinggian) atau gestur khas merek.

**Aturan kepadatan & breakpoint:**
- Titik awal (sesuaikan dengan konten; tulis di 4.3 yang diisi sebagai "Perangkat & safe area"): iPhone kecil **375×667** (SE) sampai **430×932** (Pro Max), Android **360×800** sampai **412×915**; tablet/lipat sebagai catatan.
- **Safe area:** konten di dalam safe area; latar boleh menembus ke bawah status bar/home indicator; tab bar menghormati inset bawah.
- **Target sentuh:** **44×44pt** (iOS) dan **48×48dp** (Android), jarak antar target ≥ 8.
- Pengganti 3b: "daftar utama menampilkan ≥ 4 baris di layar 375×667 setelah bar atas dan tab bar" (hitung dengan satuan pt/dp).
- **Dynamic Type / font scaling:** layout tetap utuh di 200% (iOS kategori aksesibilitas, Android font 200%): tidak ada teks terpotong, baris bisa tumbuh; tentukan teks mana yang boleh dibatasi.

**Isi preview HTML:** bingkai perangkat (iPhone dengan Dynamic Island/notch dan Android dengan gesture bar) menampilkan layar utama, onboarding, momen signature, sheet, dan satu layar dengan teks besar. Tampilkan varian iOS dan Android bila navigasi berbeda. Preview HTML hanya **simulasi**; tulis di 9 bahwa implementasi memakai komponen native/library resmi. Gestur didemokan dengan pointer (tarik sheet) bila memungkinkan; haptik ditulis sebagai catatan di animasi.

**Template yang disesuaikan/dihapus:**
- 2.5: isi dengan perangkat acuan dan safe area sebagai pengganti breakpoint web (tetap di 2.5). 2.8 Implementasi Token → format sesuai stack: React Native (objek `theme.ts`/NativeWind), Flutter (`ThemeData`/`ColorScheme`/`ThemeExtension`), SwiftUI (`Color` set di asset catalog + `Font`/`Spacing` enum), Jetpack Compose (`MaterialTheme`). Kontras tetap diukur dengan script.
- Bagian 3: komponen memakai nama native (mis. `NavigationStack`, `BottomSheet`, `Scaffold`), bukan shadcn/ui; stack-shadcn.md tidak dipakai.
- 4.1 diisi "Kerangka & navigasi per platform" (iOS/Android). 6.3: tambahkan izin ditolak, versi aplikasi usang, tanpa jaringan. 8: pembaca layar (VoiceOver/TalkBack), label aksesibilitas, urutan fokus, gerak dikurangi (`reduceMotion`).

**Kebutuhan khusus:**
- **Ikuti HIG / Material 3** pada: struktur navigasi, tombol kembali dan gestur sistem, kontrol sistem (picker tanggal, switch, alert), tipografi sistem sebagai dasar, ikon sistem (SF Symbols / Material Symbols). Identitas merek ditaruh di warna, tipografi display, ilustrasi, dan momen, tidak dengan menggantikan kontrol sistem.
- **Haptik:** `selection`/`light` untuk toggle dan pilihan, pola sukses/peringatan/gagal untuk hasil; satu pola per aksi (pola bertahap, mis. tahan-untuk-memecahkan, dihitung satu pola); tidak menggantikan umpan balik visual; bisa dimatikan sistem. Tulis API per stack: iOS `UINotificationFeedbackGenerator` (`.success/.warning/.error`) dan `UIImpactFeedbackGenerator`; Flutter inti hanya punya `HapticFeedback.selectionClick/lightImpact/mediumImpact/heavyImpact/vibrate` (pola sukses/gagal perlu paket tambahan atau kombinasi impact); Expo `expo-haptics` (`notificationAsync`, `impactAsync`, `selectionAsync`).
- **Gerak:** pegas (iOS) dan kurva emphasized (Material 3), gestur interruptible, 60fps dijaga (animasikan transform/opacity); dukung Reduce Motion.
- **Mode gelap:** pengguna aplikasi native sering memakai mode gelap sistem, jadi pertimbangkan dua palet (keduanya diukur kontrasnya). Light saja boleh kalau konsepnya kuat di terang, dengan alasan di 1.3 dan tema dikunci di platform (Flutter `themeMode: ThemeMode.light`, iOS `UIUserInterfaceStyle`, Expo `userInterfaceStyle`).
- **Aset:** ikon aplikasi dan splash sesuai ukuran toko, ikon adaptif Android (foreground/background + monochrome), `@2x/@3x`.
- **Izin & privasi:** layar pra-izin menjelaskan manfaat sebelum dialog sistem; tidak meminta di peluncuran pertama tanpa konteks.

---

## 8. Internal tool / admin panel

**Cara mengenali:** "admin", "back office", "CMS", moderasi, operasional, laporan internal, pengguna adalah staf yang sama setiap hari; fungsi di atas gaya; sering CRUD atas banyak entitas; tim kecil, sedikit waktu desain.

**Arti "wow" di sini:** **efisiensi yang terasa nikmat** dan sedikit karakter: alat kerja yang ingin dibuka.
- Keputusan cepat: tabel yang bisa dipindai, aksi massal, pencarian instan, shortcut, aksi inline.
- Karakter datang dari tipografi, warna aksen, dan satu atau dua momen kecil (ringkasan harian, antrean selesai).
- Level ambisi default untuk profil ini: **Ekspresif** (konsisten dengan tabel level di SKILL); naikkan ke Spektakuler hanya bila user meminta. Catat di 1.3.

**Jebakan:** template admin generik (sidebar gelap + kartu statistik + tabel putih), formulir 30 field dalam satu halaman, warna status tanpa label, konfirmasi hapus tanpa konsekuensi dijelaskan, tidak ada log aktivitas/undo, pencarian yang hanya bisa tepat-sama, dekorasi yang memperlambat.

**Layar/section inti (bagian 5):**
- Shell + navigasi per modul, **Daftar entitas** (tabel: filter, urut, kolom, seleksi massal, ekspor), **Detail/ubah entitas** (form bagian-bagian, validasi, riwayat perubahan), **Buat baru** (form cepat vs lengkap), Antrean kerja/moderasi (setujui/tolak cepat, shortcut), Impor/ekspor massal (unggah, validasi per baris, hasil), Log aktivitas, Pengguna & izin, Pengaturan, Halaman sistem.
- Wajib: tabel aksi per status/role, konfirmasi aksi destruktif dengan konsekuensi, pesan error per aturan, hak akses per role (tombol tersembunyi vs nonaktif dengan alasan).

**Kandidat momen signature (2 sampai 3):**
1. Layar "antrean kosong"/selesai hari ini (kepuasan menyelesaikan kerja).
2. Ringkasan awal hari (angka yang perlu perhatian, bukan semua angka).
3. Command palette / pencarian global.
4. Hasil impor massal (peringkasan sukses/gagal per baris dengan perbaikan satu klik).

**Aturan kepadatan & breakpoint (titik awal, sesuaikan dengan konten; tulis di 4.3):**
- Desain di **1440** dan **1280**, minimum **1024**; mobile hanya bila PRD meminta (390, aksi inti saja).
- Tabel ≥ **14 baris** (titik awal) di 1440×900 dengan baris 36 sampai 40px (kompak) dan opsi lega; form desktop dua kolom dengan label di atas field, lebar form maksimal 720px.
- Prioritas: pindai cepat > estetika; ruang kosong secukupnya.

**Isi preview HTML:** shell desktop 1440 dengan tabel utama (filter aktif, seleksi massal), detail/form, antrean moderasi, dialog konfirmasi destruktif, impor, log; satu frame mobile bila relevan. Toggle kepadatan. Momen signature kecil.

**Template yang disesuaikan/dihapus:** sama dengan profil 5 (data viz di 2.6/3.2, kepadatan di 4.3), tetapi 1.6 hanya 2 sampai 3 momen; matriks izin role × aksi ditulis di 4.1 (tabel yang sudah ada, kolom ditambah); 6.4 konfirmasi destruktif diperluas (jumlah item terdampak, bisa dibatalkan berapa lama). Hapus pertimbangan marketing, onboarding panjang, dan ilustrasi besar.

**Kebutuhan khusus:** audit trail terlihat, undo/pembatalan untuk aksi massal, validasi inline dengan kontrak yang jelas, shortcut keyboard terdokumentasi, bahasa teknis internal diperbolehkan tetapi konsisten (glosarium), kecepatan input (tab order, autofocus, simpan dengan ⌘↵), aksesibilitas tetap penuh. Gunakan pustaka tabel/form yang sudah ada di stack sebelum membuat komponen sendiri.

---

## 9. Hybrid

Banyak produk gabungan; satu DESIGN.md menyatukan beberapa profil lewat **satu sistem token**.

- **SaaS = landing page + dashboard:** hasilkan bagian profil 1 (marketing) dan profil 5 (aplikasi) dalam satu dokumen. Satu bagian 5 saja, sub-bagian bernomor berurutan `### 5.1`, `### 5.2`, ... dikelompokkan dengan label tebal seperti **Bagian A · Landing page** (5.1 sampai 5.6) lalu **Bagian B · Aplikasi** (5.7 dan seterusnya); tiap heading tetap `### 5.x <Nama>: \`<route>\``. Token, tipografi, dan motif identitas **sama**; kepadatan, ukuran teks, dan intensitas motion **berbeda** (marketing: display besar, motion kaya; aplikasi: kompak, motion minimal). Tulis di 1.3 "di mana batas keduanya". Preview: dua bagian (halaman marketing dan frame aplikasi).
- **E-commerce + admin toko:** profil 4 untuk etalase, profil 8 untuk admin; token sama, etalase Spektakuler dan admin Ekspresif.
- **Blog/dokumentasi + landing:** profil 3 dan 1; header/footer dibagi.
- **Mobile native + situs marketing + admin:** tiga profil; satu sumber token, dipetakan ke tiap platform.
- **PWA + landing:** profil 6 dan 1.
- Level ambisi boleh berbeda per bagian (catat di 1.3), tetapi **identitas visual harus bisa dikenali** di semuanya.
- Lint dan rubrik dijalankan sekali terhadap satu DESIGN.md; panjang target dapat naik sampai ±1000 baris untuk hybrid (kurangi duplikasi dengan "sama dengan 5.7, kecuali: ...").

---

## 10. Keputusan profil

### Tabel: jenis produk → profil

| Jenis produk | Profil | Catatan |
|---|---|---|
| Situs peluncuran produk, waitlist, kampanye, event, undangan digital | 1 Landing | Profil 3 bila ada banyak artikel |
| Company profile, studio, agensi, portfolio, CV online | 2 Company/portfolio | Profil 1 bila tujuan utamanya satu konversi |
| Blog, majalah, berita, dokumentasi, kursus, perpustakaan, wiki | 3 Konten | Kursus dengan akun/progres: tambah elemen dashboard ringan dari profil 5 |
| Toko online, katalog, marketplace, pemesanan makanan | 4 E-commerce | Katalog tanpa bayar tetap 4 (PDP + tanya WhatsApp) |
| SaaS, analytics, CRM, keuangan, manajemen proyek (desktop) | 5 Dashboard | Dengan situs marketing: Hybrid |
| Booking, antrean, kasir UMKM, pelacak status, tools lapangan (dipakai di HP) | 6 Mobile-first/PWA | Default bila brief tidak jelas dan PRD menyebut mobile |
| Aplikasi iOS/Android (toko aplikasi, React Native/Flutter/Swift/Kotlin) | 7 Native | Dengan admin web: Hybrid 7 + 8 |
| Admin, back office, CMS, moderasi, alat operasional staf | 8 Internal tool | Naikkan ke 5 bila dijual sebagai produk |
| SaaS lengkap, toko + admin, produk multi-platform | 9 Hybrid | Pilih profil per bagian |

### Aturan kalau brief tidak jelas
1. **Baca sinyal** di tabel "Cara mengenali" tiap profil; ambil profil dengan sinyal terbanyak. PRD bagian 1.5 (platform), 4 (daftar halaman), dan 7 (stack) paling menentukan.
2. Kalau dua profil seimbang atau sinyalnya lemah, **tanyakan di ronde pertanyaan tunggal langkah 1d** sebagai pertanyaan tambahan (masih dalam batas 3 pertanyaan; buang pertanyaan yang sudah terjawab referensi): "Produk ini paling mirip yang mana?" dengan 2 sampai 4 pilihan profil, atau "Utamanya dipakai di HP atau laptop?".
3. Kalau tidak bisa bertanya (user bilang "terserah" atau tidak responsif): **simpulkan sendiri** dengan sinyal terkuat dan **catat di 1.3** ("Jenis produk: profil X, alasan: ...") dan di 1.4 ("Perlu konfirmasi: profil Y bila ..."), dengan default profil yang dipakai.
4. Tanpa PRD dan tanpa petunjuk sama sekali: pakai **profil 6** (default lama) kalau ada role/transaksi/order; **profil 1** kalau hanya ide promosi; jangan menggabungkan profil tanpa alasan.
5. Selalu tulis profil yang dipakai di header DESIGN.md (kolom "Platform utama") dan di 1.3, supaya reviewer menilai terhadap profil yang benar (kepadatan, breakpoint, preview).
