---
name: design-maker
description: Bikin DESIGN.md + preview HTML high-fidelity untuk jenis produk apa pun (landing page, company profile, portfolio, blog/media, e-commerce, dashboard SaaS, web app, aplikasi mobile native, admin) dan stack apa pun (Tailwind/shadcn, CSS biasa, Vue, Svelte, React Native, Flutter, SwiftUI), dengan desain berani yang bikin orang bilang "wow" (3 konsep visual untuk dipilih, design tokens, motion, momen signature, komponen, spesifikasi halaman, aksesibilitas) yang tetap enak dipakai dan siap dibangun AI coding agent. Bisa dari PRD (mis. hasil prd-maker), brief, project yang ada, atau ide, plus gambar referensi (logo, screenshot, moodboard). Gunakan setiap kali user minta "buat DESIGN.md", "design system", "panduan UI", "style guide", "desain website/aplikasi/landing page/dashboard", "UI spec", "desain yang keren/wow", atau melampirkan gambar referensi warna/gaya, walaupun kata "DESIGN.md" tidak disebut. Juga dipicu oleh /design-maker.
compatibility: Model dan tool AI apa pun. Disarankan - akses file, Python 3 (Pillow opsional untuk ekstraksi warna gambar), Node + Chrome atau browser untuk screenshot. Setiap kemampuan punya jalur cadangan manual (lihat bagian Kompatibilitas).
---

# Design Maker

Ubah PRD, brief, ide, atau project yang sudah ada — untuk **jenis produk apa pun** (landing page, company profile, portfolio, blog/media, e-commerce, dashboard SaaS, web app, aplikasi mobile native, admin internal) dan **stack apa pun** — menjadi **desain yang membuat orang berhenti dan bilang "wow"**, lalu tuliskan sebagai `DESIGN.md` + `design-preview.html` yang cukup spesifik sehingga AI coding agent bisa membangunnya persis tanpa menebak.

Prinsip utama:
- **Wow adalah syarat, bukan bonus.** Desain yang rapi tapi biasa dianggap gagal. Setiap desain harus punya satu konsep visual yang kuat dan beberapa momen yang dirancang khusus untuk memukau.
- **Wow di momen signature, cepat dan tenang di layar kerja.** Layar yang dipakai berulang (daftar, tabel, form, artikel panjang) tetap efisien dan nyaman dibaca, tapi membawa bahasa visual yang sama. Kemewahan visual (warna penuh, ilustrasi, animasi koreografi) dicurahkan di momen yang tepat — yang berbeda per jenis produk: hero landing page, halaman produk, status pesanan, sukses transaksi, ringkasan dashboard, onboarding, empty state.
- **Wow harus dilihat, bukan dibaca.** Konsep ditunjukkan sebagai mockup HTML, dan desain akhir selalu disertai preview high-fidelity yang bisa dibuka di browser.
- **PRD menjawab "apa yang dibangun", DESIGN.md menjawab "seperti apa tampilannya dan rasanya".** Jangan mengulang isi PRD (fitur, aturan bisnis, schema); rujuk ID-nya (F-02, BR-04, `/orders`).
- **Setiap keputusan visual harus bisa langsung jadi kode**: warna dasar dalam hex + nama token (oklch boleh di dalam gradien dan bayangan; hex dibutuhkan untuk cek kontras otomatis), ukuran dalam px/rem, kurva motion dalam angka, nama komponen sesuai library. Hindari kalimat seperti "modern, clean, dan elegan" tanpa angka.
- **Desain untuk user nyata di PRD/brief.** Ekspresif tidak berarti mengorbankan pemakaian: target sentuh cukup besar, alur tetap pendek, teks tetap terbaca, kontras tetap lolos.
- **Universal, bukan satu cetakan.** Aturan kepadatan, layar wajib, momen signature, dan cara menulis token mengikuti **profil jenis produk** (`references/product-types.md`) dan **adaptor stack** (`references/stack-adapters.md`). Jangan memaksakan pola aplikasi CRUD ke landing page, atau pola web ke aplikasi native.

## Kompatibilitas (semua model dan tool AI)

Skill ini ditulis netral: bisa dipakai model apa pun (Claude, GPT, Gemini, model open-source) di tool apa pun yang bisa membaca file ini. Istilah yang dipakai:
- **`<SKILL_DIR>`** = folder tempat file SKILL.md ini berada. Semua path script dan referensi relatif terhadap folder ini. Skill pendamping (`prd-maker`, `design-maker`, `build-from-design`) diasumsikan berada berdampingan di folder induk yang sama (`<SKILL_DIR>/../<nama-skill>`).
- Nama tool khusus (mis. AskUserQuestion, tool Agent) hanya contoh. Pakai kemampuan yang setara di platformmu.

| Kemampuan | Dipakai untuk | Kalau tidak ada |
|---|---|---|
| Membaca/menulis file | Membaca PRD, menyimpan DESIGN.md dan preview | Tampilkan isi file dalam blok kode agar user menyimpannya sendiri |
| Menjalankan perintah (Python 3, Node opsional) | Linter, cek kontras, ekstraksi warna | Hitung kontras dengan rumus WCAG secara manual, cek konsistensi dengan daftar langkah 5, perkirakan warna gambar secara visual dan tandai "(perkiraan)" |
| Melihat gambar | Gambar referensi, screenshot | Minta user mendeskripsikan gambar atau mengirim kode warnanya |
| Browser / screenshot | Kritik diri konsep, ukur preview | `<SKILL_DIR>/../build-from-design/scripts/shoot.mjs` (Node + Chrome); kalau tidak bisa, nilai dari kode dan tandai "tanpa screenshot" |
| Pertanyaan pilihan ganda | Ronde pertanyaan, memilih konsep | Tanya lewat teks bernomor |
| Sub-agen / sesi terpisah | Review independen | Review sebagai pass terpisah dengan mata segar (langkah 7b) |
| Penyimpanan permanen | Riwayat gaya `<SKILL_DIR>/data/style-history.md` | Simpan di project (`.design-maker/style-history.md`); kalau tidak ada file sama sekali, minta user menyebut gaya yang pernah dipakai |

## Level ambisi visual

| Level | Kapan | Isi |
|---|---|---|
| **Spektakuler** (default) | Hampir semua produk: landing page, brand, e-commerce, aplikasi konsumen, UMKM, produk baru | Konsep art direction kuat, tipografi display berani, warna berkomitmen (bidang warna penuh, gradien khas brand), kedalaman/material, ilustrasi custom, koreografi motion lengkap, ≥ 4 momen signature |
| **Ekspresif** | Dashboard padat data, alat kerja internal, dokumentasi yang tetap ingin berkarakter | Konsep dan tipografi khas, warna berani di aksen dan momen penting, motion halus, 2 sampai 3 momen signature |
| **Tenang** | User meminta minimalis, atau domain menuntut ketenangan (mis. medis kritis) | Disiplin dan rapi, karakter dari detail kecil, 1 sampai 2 momen signature |

Pakai **Spektakuler** kecuali user meminta level lain atau domainnya jelas menuntut ketenangan. Catat level di 1.3.

## Mode kerja

| Mode | Kapan | Yang dikerjakan | Perkiraan |
|---|---|---|---|
| **Penuh** (default kalau user minta DESIGN.md untuk dibangun) | Proyek sungguhan yang akan dikoding | Semua langkah 1 sampai 8 | 25 sampai 40 menit |
| **Cepat** | User bilang "cepat", "draf", "lihat arah dulu", "konsep saja", atau masih eksplorasi ide | Langkah 1 ringkas → langkah 2 dengan 3 konsep ringkas (kartu konsep + 1 layar momen signature per konsep) → pilihan user → `design-preview.html` berisi 1 momen signature + 2 layar inti → `DESIGN.md` draf (bagian 1, 2, dan 3 lengkap; bagian 4 sampai 9 cukup poin penting atau "Belum diisi di mode cepat"; header ditandai **Draf cepat**) → lint 7a saja, tanpa putaran review. Kritik diri 2c tetap wajib tapi cukup oleh sesi sendiri (tanpa sub-agen juri). Layar inti dipilih dari profil produk (mis. e-commerce: beranda + halaman produk) | 12 sampai 20 menit |

Kalau mode tidak jelas, pakai Penuh untuk permintaan DESIGN.md dan Cepat untuk permintaan "lihat konsep/arah". Di akhir mode Cepat, tawarkan melanjutkan ke mode Penuh dari konsep yang sama (langkah 3 sampai 8, tanpa mengulang langkah 2).

## Alur kerja

### 1. Kumpulkan bahan

**a. Cari PRD atau brief.** Cek `PRD.md`, `docs/PRD.md`, `PRD-*.md`, atau dokumen brief lain di working directory, dan isi pesan user. PRD tidak harus dari `prd-maker`; petakan berdasarkan **makna**, bukan nomor bagian:

| Cari informasi tentang | Dipakai untuk | (di PRD `prd-maker`) |
|---|---|---|
| Target user dan konteks pemakaian | Arah visual, kepadatan, ukuran target sentuh | 1.3 |
| Jenis produk dan platform | Profil produk, breakpoint utama | 1.5, 7 |
| Fitur, acceptance criteria, kode error | Komponen, pesan error, kandidat momen signature | 3, 5.4 |
| Alur dan daftar halaman/section/layar | Navigasi dan spesifikasi per halaman/section | 4 |
| Status dan siklus hidup data (kalau ada) | Badge status dan momen transisi | 6.4 |
| Tech stack | Adaptor stack, format token, library motion, font loading | 7 |

**a2. Tentukan profil produk dan adaptor stack.** Baca `references/product-types.md` dan pilih profil (boleh lebih dari satu, mis. SaaS = landing page + dashboard). Baca `references/stack-adapters.md` dan pilih adaptor dari tech stack di PRD atau file project (`package.json`, `pubspec.yaml`, `*.xcodeproj`, `nuxt.config.*`, `svelte.config.*`, `tailwind.config.*`). Kalau stack memakai shadcn/ui, baca juga `references/stack-shadcn.md`. Kalau jenis produk atau stack tidak jelas, tanyakan di ronde pertanyaan langkah d, atau simpulkan dan catat di 1.3.

**b. Kalau tidak ada PRD:**
- Di project yang sudah ada → baca konfigurasi styling (mis. `globals.css`, `tailwind.config.*`, `components.json`, tema Flutter/React Native, folder komponen) dan halaman/layar yang ada. DESIGN.md mengikuti token dan komponen yang sudah dipakai, kecuali user minta redesign.
- Tanpa project → minta deskripsi singkat (jenis produk, target user, halaman/layar utama, stack) atau tawarkan menjalankan `prd-maker` dulu.

**c. Gambar referensi (kalau ada).** User bisa memberi logo, screenshot website/app, moodboard, foto produk, atau gambar apa pun — sebagai lampiran di chat, path file, folder (mis. `referensi/`), atau URL website.
- **Kumpulkan semuanya dulu.** Lampiran chat sudah bisa dilihat langsung; cek juga apakah lampiran itu punya path file (mis. folder upload milik tool yang dipakai) supaya bisa diproses script. Path file atau folder: buka setiap gambar dengan kemampuan membaca file/gambar yang tersedia. URL website: buka di browser yang tersedia dan ambil screenshot halaman utamanya (desktop dan lebar HP); kalau tidak ada browser, minta user mengirim screenshot.
- **Ambil warna dengan script, bukan dikira-kira** (untuk gambar yang ada sebagai file):
  ```bash
  python3 <SKILL_DIR>/scripts/extract-palette.py logo.png screenshot.png
  ```
  Script memberi hex persis + porsi piksel + label (netral/berwarna), dan tetap melaporkan warna aksen yang porsinya kecil. Abaikan warna sisa anti-aliasing atau kompresi JPEG (porsi kecil, mirip warna di sebelahnya). Script menangani PNG, JPG, WebP, HEIC (dikonversi otomatis lewat `sips` di macOS), dan SVG. Untuk lampiran tanpa path file, perkirakan secara visual dan tandai "(perkiraan)" — jangan menunggu user.
- **Baca tiap referensi sesuai jenisnya:**

  | Jenis | Yang diambil |
  |---|---|
  | Logo | Warna brand, bentuk (bulat/tajam → radius, shape language), ketebalan garis, nuansa. Logo bukan sumber font UI kecuali user minta. |
  | Screenshot website/app | Kepadatan, pola layout dan navigasi, gaya tipografi, radius, kedalaman, gaya tombol dan kartu, motion yang terlihat. |
  | Foto, ilustrasi, moodboard | Palet dan suasana, tekstur, motif, gaya ilustrasi yang bisa jadi ciri khas. |

- **Ambil prinsipnya, jangan menyalin identitas.** Jangan meniru persis layout + warna + font produk lain sampai terlihat seperti tiruan, dan jangan memakai aset mereka. Logo yang dilampirkan dianggap milik user kecuali dia bilang sebaliknya.
- **Warna brand tetap harus lolos kontras.** Kalau warna logo gagal sebagai teks atau tombol, pertahankan hue-nya tapi buat varian lebih gelap untuk `primary`, dan pakai warna aslinya di bidang warna besar, ilustrasi, gradien, dan aksen. Catat keduanya di tabel token.
- **Pembagian peran:** PRD menentukan halaman, fitur, platform, kepadatan informasi, dan ukuran tap target; referensi menentukan warna, tipografi, bentuk, dan suasana. Kalau project sudah punya token, token project > referensi, kecuali user minta rebrand.
- **Prioritas kalau bertentangan:** referensi dari user > default skill ini dan antislop. Aturan aksesibilitas (kontras, tap target, focus, reduced motion) tidak bisa dikalahkan oleh referensi.
- **Kalau referensi saling bertentangan**, tanyakan referensi mana yang menentukan warna dan mana yang menentukan gaya — dalam ronde pertanyaan langkah 1d.
- Catat semua di bagian 1.5 Referensi DESIGN.md.

**d. Pertanyaan ke user (satu ronde, opsional).** Kalau referensi sudah menjawab nuansa dan warna, jangan tanyakan lagi. Kalau belum, ajukan satu ronde pertanyaan lewat fitur pilihan ganda kalau platform punya (mis. AskUserQuestion di Claude Code); kalau tidak, tanya lewat teks, maksimal 3 pertanyaan:
- Jenis produk dan stack, kalau belum jelas.
- Level ambisi visual (Spektakuler direkomendasikan).
- Warna brand yang sudah ada (logo, warna toko) atau bebas.
- Mode warna: light, dark, atau keduanya.

Nuansa tidak ditanyakan lewat teks — itu dijawab dengan 3 konsep visual di langkah 2. Kalau user bilang "terserah", lanjut tanpa bertanya.

### 2. Art direction: 3 konsep visual (wajib)

Desain yang wow lahir dari satu konsep yang kuat, bukan dari kumpulan aturan. Sebelum menulis spesifikasi, buat **3 konsep yang benar-benar berbeda**.

**a. Pilih 3 keluarga gaya, lalu rumuskan 3 konsep.** Baca `references/style-families.md` dan riwayat gaya di `<SKILL_DIR>/data/style-history.md`:
- Ketiga konsep berasal dari **3 wilayah gaya yang berbeda** (lihat aturan keragaman di katalog). Paling banyak satu konsep boleh memakai garis tebal/bayangan offset keras.
- Hindari keluarga yang terpilih di 5 proyek terakhir di riwayat, kecuali user memintanya atau referensinya menuntut.
- Cek setiap konsep terhadap daftar "Penanda gaya rumahan AI" di katalog; konsep yang memenuhi 3 penanda atau lebih harus dirumuskan ulang.
- **Jangan pakai formula tiga serangkai** "satu neo-brutalis berisik + satu gelap berpendar + satu editorial kalem bertema kertas". Formula ini sudah terbukti muncul berulang di setiap proyek; minimal satu konsep harus dari wilayah yang belum pernah dipakai di riwayat.
- Setiap konsep menyebut **analogi dunia nyata yang spesifik** (mis. "poster pameran Bauhaus 1923", "kemasan parfum niche", "UI kokpit pesawat", "majalah arsitektur Jepang"), bukan sekadar nama gaya, supaya arah visualnya punya acuan rasa yang jelas.
- Pasangan font yang sudah tercatat di riwayat tidak dipakai ulang kecuali user memintanya.
- Keluarga gaya adalah titik awal, bukan template: konsep tetap diturunkan dari dunia user dan produknya.

Setiap konsep punya:
- **Nama dan ide satu kalimat** yang diambil dari dunia user atau produknya (benda, tempat, kebiasaan, budaya visual mereka), mis. "Etalase kaca toko laundry di malam hari", "Kertas grafik insinyur" untuk dashboard teknik, "Majalah kopi edisi cetak" untuk landing page kedai kopi — bukan "modern minimalis".
- **Palet berkomitmen**: warna dasar, warna hero (bidang warna penuh atau gradien khas brand), aksen.
- **Pasangan tipografi**: font display yang berkarakter + font teks yang sangat terbaca (lihat `references/visual-craft.md`).
- **Bahasa bentuk dan material**: radius, kedalaman, tekstur, gaya ilustrasi.
- **Satu momen signature** yang paling memukau.
- **Satu objek signature**: visual utama yang dikerjakan dengan kualitas tinggi (ilustrasi SVG terperinci dengan filter/tekstur, canvas, WebGL ringan, atau komposisi tipografi besar), bukan kotak-kotak CSS sederhana. Maskot atau karakter dirancang sebagai karakter (ekspresi, kepribadian, pose yang konsisten di beberapa layar), bukan ikon vektor generik.

Ketiga konsep harus berbeda di minimal 3 sumbu: suhu warna, genre tipografi (mis. serif editorial vs grotesk tebal vs rounded), kedalaman (datar grafis vs berlapis/material), light vs dark, energi motion. Jangan membuat 3 variasi warna dari layout yang sama.

**b. Render sebagai mockup.** Buat `design-concepts.html` (satu file, tanpa build step, font dari Google Fonts, ikon/ilustrasi inline SVG). Untuk setiap konsep tampilkan berdampingan:
- nama + ide + palet + tipografi,
- **momen signature** dengan animasi CSS yang benar-benar berjalan,
- **layar/section inti** sesuai profil produk (mis. layar kerja utama untuk web app, hero + satu section untuk landing page, overview + tabel untuk dashboard, halaman produk untuk e-commerce, artikel untuk situs konten), memakai data/konten contoh realistis.

Bingkai mengikuti platform utama profil: bingkai HP 390px untuk mobile-first dan aplikasi native (gaya iOS atau Android sesuai target), bingkai browser desktop 1440px (diskalakan) untuk desktop-first, atau keduanya.

Pakai teknik di `references/visual-craft.md`. Kualitas mockup harus setara karya portofolio: tipografi rapi, ritme spasi konsisten, detail kecil diperhatikan.
Catatan teknis mockup (HTML/CSS vanilla, tanpa Tailwind/`motion`): tulis keadaan akhir sebagai CSS default dan animasikan hanya keyframe `from` dengan `animation-fill-mode: backwards`, sehingga reduced-motion cukup mematikan animasi dan tampilan tetap benar; bingkai HP 390px diskalakan (mis. variabel `--s` = lebar tersedia / 390 lewat `transform: scale`) supaya halaman tidak scroll horizontal di 375px. Di dalam bingkai yang diskalakan, satuan `vw`/`vh` mengacu ke jendela browser, bukan bingkai: pakai container query units (`container-type: inline-size` pada bingkai + `cqw`/`cqh`) atau variabel lebar bingkai.

**c. Kritik diri dari screenshot (wajib sebelum ditunjukkan).** Buka `design-concepts.html` di browser, scroll semuanya, putar animasinya, dan ambil screenshot. Kalau tidak ada tool browser: `node <SKILL_DIR>/../build-from-design/scripts/shoot.mjs file:///<path-absolut>/design-concepts.html shot.png --width 1440 --full`, lalu buka PNG-nya dengan kemampuan membaca gambar yang tersedia; kalau itu juga gagal, nilai dari kode dan tandai "tanpa screenshot" di ringkasan. Nilai setiap konsep dengan skala "Dampak Visual" di `references/rubric.md` dan dengan daftar "Penanda gaya rumahan AI" di `references/style-families.md`. Perbaiki yang ditemukan: area kosong, panel yang kosong saat memuat, objek signature yang terlihat murah, hierarki yang datar (semua elemen punya bayangan/garis yang sama), dan teks terpotong. Konsep di bawah 8 dirumuskan ulang, bukan dipoles (di mode Cepat boleh tetap ditampilkan dengan catatan kelemahannya kalau waktu tidak cukup, asalkan konsep terkuat ≥ 8).

**d. Tunjukkan ke user.** Kalau ada browser, buka dan ambil screenshot setiap konsep; kirim file-nya ke user (kalau langkah ini dikerjakan sub-agen, sub-agen hanya menyiapkan file dan screenshot; sesi utama yang mengirim ke user dan bertanya) (mis. lewat SendUserFile atau tautan file) beserta ringkasan satu kalimat per konsep, lalu tanyakan pilihannya (pakai fitur pilihan ganda kalau ada, kalau tidak lewat teks): konsep A, B, C, atau gabungan (mis. "warna A + tipografi C"). Kalau user sebelumnya bilang "terserah" atau tidak bisa ditanya, pilih konsep terkuat sendiri — kalau platform bisa menjalankan sub-agen, minta satu sub-agen menilai ketiga screenshot secara independen untuk dampak visual dan kecocokan dengan user — lalu catat alasannya di 1.3.

### 3. Muat aturan kualitas

Kalau terpasang, muat (atau baca langsung file SKILL.md-nya): `antislop` (inti), `antislop-ui`, `antislop-human`, `antislop-layoutmobile`, `antislop-copywriting`. Baca juga `references/visual-craft.md` (selalu), profil di `references/product-types.md`, adaptor di `references/stack-adapters.md`, dan `references/stack-shadcn.md` (kalau stack memakai shadcn/ui).

Kalau antislop tidak terpasang, abaikan istilah khususnya (dial, Design Read): maknanya cukup "hindari default generik yang tidak punya alasan dari konsep", dan tabel kalibrasi di bawah tetap berlaku.

Antislop dipakai sebagai **filter terhadap desain generik**, bukan larangan terhadap desain ekspresif: jangan jalankan wizard instalasinya, jangan menulis apa pun ke `CLAUDE.md`, dan jangan tanyakan mode DURING/AFTER-nya. Design Read dan dial antislop dipakai untuk berpikir saja; jangan tulis istilah antislop di DESIGN.md.

**Kalibrasi antislop untuk level Spektakuler dan Ekspresif:**

| Teknik | Dilarang (generik) | Boleh (ekspresif) |
|---|---|---|
| Gradien | biru→ungu bawaan, gradien acak di setiap kartu, gradien di teks body | gradien multi-stop dari hue brand/konsep, sebagai token bernama, di bidang hero atau momen signature |
| Glow | glow di semua tombol/kartu | satu sumber cahaya yang punya alasan konsep (mis. lampu etalase), dipakai di momen tertentu |
| Glass/blur | glassmorphism di mana-mana, kaca di atas latar polos | kaca di atas latar kaya (foto/gradien) dengan kontras teks terverifikasi, tidak di daftar panjang (berat di HP) |
| Animasi | pulse/loop tanpa henti, animasi template bertumpuk | koreografi bertujuan: masuk berurutan, transisi status, perayaan sukses, semua dengan `prefers-reduced-motion` |
| Ilustrasi | ikon AI generik, stok yang tidak nyambung, emoji dekoratif | ilustrasi inline SVG custom dengan gaya konsisten dari dunia user |
| Radius/bayangan | radius dan bayangan lembut seragam di semua elemen | skala elevasi berlapis yang konsisten, radius besar bila menjadi bahasa bentuk konsep |
| Angka | stat karangan di UI sungguhan | angka besar dari data nyata user (mis. "Rp86.000 belum lunas") sebagai hero |
| Harga | tiga kolom kartu seragam + badge "Terpopuler" bawaan template | tier sungguhan produk (berapa pun jumlahnya) ditampilkan dengan bahasa visual konsep; penekanan pada tier yang direkomendasikan boleh, asalkan ada alasannya dan bukan badge generik |
| Navigasi landing | CTA di nav dan di hero berebut perhatian | CTA nav muncul setelah hero lewat (sticky), atau ditandai sekunder `[ ]` sampai hero lewat |

Aturan tetap:
- **Tanda baca:** jangan pakai em dash (—) maupun en dash (–) di DESIGN.md dan teks UI; pakai titik dua, koma, titik tengah (·), atau kata "sampai". Tanda minus matematika (−, U+2212) untuk nominal boleh.
- **Data contoh** di wireframe/mockup boleh dan diberi tanda "data contoh"; angka karangan di UI sungguhan dilarang.
- **Mode warna:** light, dark, atau keduanya — pilih yang paling kuat untuk konsep, dengan alasan dari konteks pemakaian. Dark yang kaya sering lebih memukau untuk momen signature; layar kerja di tempat terang mungkin lebih baik light. Boleh campur (mis. momen signature gelap, layar kerja terang) kalau dirancang sebagai satu sistem.
- **Ikon:** pakai library bawaan stack sebagai dasar, dikustomisasi (stroke, ukuran, duotone) sesuai konsep; ilustrasi custom untuk momen signature dan empty state.

### 4. Tulis DESIGN.md

Baca `references/template.md`, lalu ikuti strukturnya:
- 9 bagian utama bernomor, urutan tetap. Sub-bagian boleh ditambah; yang ditandai "hapus kalau tidak relevan" boleh dihapus.
- Bahasa mengikuti user (default Bahasa Indonesia). Nama token, nama komponen, dan kode tetap bahasa Inggris.
- Tanggal di header = tanggal hari ini.
- **Ringkas tapi lengkap.** Tulis keputusan dan nilainya, bukan proses berpikirnya: hitungan cukup satu baris hasil, catatan zoom 200% cukup sekali di 4.3, tabel kontras hanya pasangan yang benar-benar dipakai. Pecah paragraf panjang jadi poin pendek.
- **Satu fakta, satu tempat.** Spesifikasi komponen (ukuran, state, motion, override dari default library) hanya di bagian 3; daftar komponen per halaman cukup nama. Token hanya di bagian 2. Aturan aksesibilitas yang sudah ada di komponen tidak diulang di bagian 8. Target panjang ±650 sampai 850 baris (momen signature dan motion menambah isi); di atas 900 hampir pasti ada duplikasi.
- Halaman yang strukturnya sama dengan halaman lain cukup ditulis "sama dengan 5.x, kecuali: ...". Route yang hanya redirect cukup satu baris.

Aturan isi:
1. **Palet berkomitmen, tetap disiplin.** Warna ilustrasi, objek signature, dan motif juga ditulis sebagai token (di 2.1 atau 2.6), sehingga tidak ada hex lepas di bagian lain. Warna inti: 1 primary, 1 keluarga netral bertint (bukan abu-abu mati), 1 sampai 2 warna hero/aksen dari konsep, dan warna semantik yang benar-benar dipakai. Gradien, warna permukaan hero, dan warna status imersif ditulis sebagai **token bernama** (mis. `--gradient-hero`, `--surface-ready`). **Nama token dasar mengikuti library di stack** — untuk shadcn/ui: `background`, `foreground`, `card`, `popover`, `primary`, `secondary`, `muted`, `accent`, `destructive`, `border`, `input`, `ring` (masing-masing dengan `-foreground` bila ada), ditambah token sendiri.
2. **Kontras diverifikasi, bukan dikira-kira.** Setiap pasangan teks/latar dan elemen non-teks penting dicek dengan script:
   ```bash
   python3 <SKILL_DIR>/scripts/contrast-check.py "#FFFFFF" "#1F2937"
   ```
   Teks normal ≥ 4.5, teks besar dan elemen non-teks ≥ 3.0. Untuk teks di atas gradien, foto, atau kaca: cek terhadap titik **terburuk** di area teks (warna gradien yang paling dekat dengan warna teks), atau tambahkan lapisan/scrim lalu cek terhadap scrim. Pasangan wajib: setiap token teks di atas setiap permukaan tempat ia muncul; setiap `*-foreground` di atas pasangannya; `input` dan `ring` di atas permukaan field. Garis dekoratif ditulis "dekoratif".
3. **Setiap halaman/section/layar di PRD punya spesifikasi** sesuai profil produk (landing page: satu spesifikasi per section dengan koreografi scroll; dashboard: per halaman dengan tabel/grafik/filter; native: per layar dengan pola navigasi platform), dengan wireframe ASCII untuk platform utama (dan platform lain kalau layoutnya berbeda), komponen yang dipakai, urutan prioritas konten, dan state loading/kosong/error lengkap dengan teksnya. Halaman yang tampilannya berubah menurut status punya wireframe (atau diff singkat) untuk setiap status yang mengubah layout. Halaman yang menjadi momen signature menunjuk ke mockup hi-fi-nya di `design-preview.html`.
3a. **Wireframe untuk setiap langkah dan setiap breakpoint yang berbeda.** Alur multi-langkah (mis. login → OTP), sheet dan dialog berisi form punya wireframe sendiri. Header, tombol kembali, dan state navigasi aktif ditulis untuk setiap breakpoint.
3b. **Kepadatan dan breakpoint mengikuti profil produk** (`references/product-types.md`). Contoh: web app mobile-first menghitung item list yang terlihat penuh di 360×640 (target ≥ 3); dashboard menghitung baris tabel di 1280×800; landing page memastikan hero + CTA utama muat di atas lipatan 1440×900 dan 390×844; situs konten menjaga panjang baris 60 sampai 75 karakter. Ekspresi visual di layar kerja datang dari tipografi, warna, dan detail — bukan dari dekorasi yang memakan ruang.
4. **Konten dan data contoh realistis dan konsisten di seluruh dokumen dan preview.** Satu set data/konten contoh: ID tidak dipakai ulang, urutan waktu masuk akal, angka saling cocok (mis. jumlah × harga = total). Nama, mata uang, dan bahasa sesuai pasar target. Untuk landing page dan situs konten, tulis copy yang sungguhan (judul, subjudul, CTA). Jangan "Lorem ipsum", "John Doe", atau testimoni dan statistik karangan.
5. **Kalau produk punya status data, setiap status punya badge** (label + token warna + ikon kalau perlu), dan setiap transisi status yang penting bagi user punya momen visual (lihat aturan 14). Status tidak boleh dibedakan dengan warna saja.
6. **Jangan mengarang data yang tidak ada di PRD.** Kalau desain butuh data yang tidak ada di schema, sesuaikan desainnya dan catat di 1.4 Perlu Konfirmasi. Nomor HP contoh memakai pola jelas palsu seperti `0812-0000-1234`.
6b. **Semua copy ada di DESIGN.md.** Judul, subjudul, label tombol, isi section (untuk landing page: semua teks per section), dan teks state ditulis di DESIGN.md, bukan hanya di preview, supaya agent pembangun tidak perlu menyalin dari HTML.
7. **Setiap aksi tulis di PRD punya pesan sukses, dan setiap kode error punya pesan untuk user** — jelaskan apa yang terjadi dan apa yang harus dilakukan, tanpa jargon teknis.
8. **Komponen hanya yang dipakai, dan semua yang dipakai tercantum.** Setiap kontrol di wireframe punya komponen di daftar install, atau ditulis memakai elemen native. Hook/utilitas yang tidak disediakan library ditulis implementasinya. Library motion (mis. `motion`) dan font disebut versi dan cara pakainya. Aturan yang bergantung pada lebar kontainer dihitung dari lebar kontainer.
8b. **Komponen terkontrol.** Kalau state komponen custom diubah dari luar, tulis komponennya terkontrol (`value`/`onValueChange`) dan di mana state disimpan.
9. **Token siap tempel, sesuai adaptor stack.** Blok implementasi token lengkap dalam bahasa stack (CSS + Tailwind, CSS biasa, tema Flutter, objek tema React Native, SwiftUI, atau tabel design token JSON untuk stack lain; lihat `references/stack-adapters.md`), dan menyebut apakah blok itu **mengganti** atau **digabung** dengan file bawaan. Kalau "gabungkan", blok hanya berisi baris yang ditambahkan/diubah. Untuk Tailwind v4 + shadcn/ui versi lengkap: `@import "tailwindcss"` dan import animasi bawaan, CSS variables (termasuk token gradien, elevasi, motion), `@theme inline`, dan `@layer base` dengan aturan border default. Ring dan outline solid (tanpa transparansi).
10. **Override komponen library.** Setiap komponen dari library UI yang dipakai (shadcn/ui, Nuxt UI, Material, komponen native, dll.) punya satu baris (default library → diubah menjadi). Kalau stack shadcn/ui, pastikan setiap jebakan di `references/stack-shadcn.md` yang relevan sudah dijawab (termasuk anggaran lebar di 360px dan urutan tumpuk elemen tetap). Checklist:
    - Light saja → `@custom-variant dark (&:is(.dark *));` dan `color-scheme: light`.
    - Setiap token tipografi di 2.4 ada di `@theme`.
    - Sebutkan import bawaan yang dipertahankan dari `globals.css` hasil `shadcn init`; kalau ragu, pilih "gabungkan".
    - Varian tombol yang latarnya mirip latar halaman punya border atau pembeda lain.
11. **Setiap teknik visual bisa dibangun.** Motif, gradien, tekstur, bentuk custom, ilustrasi, dan animasi ditulis beserta resepnya (CSS/SVG/kode motion, ukuran, posisi, permukaan di belakangnya) dan perilakunya di 360px, zoom 200%, dan `prefers-reduced-motion`. Teknik yang tidak bisa dijelaskan resepnya jangan dipakai.
12. **Identitas yang bisa dimiliki, terlihat di mana-mana.** Seseorang yang melihat satu screenshot tanpa logo harus bisa mengenali aplikasinya. Konsep terlihat di layar kerja utama (lewat tipografi, warna, dan detail) dan memuncak di momen signature. Dasar visual tidak boleh resep umum (biru dongker/teal + abu-abu dingin + font sans populer) tanpa pilihan lain yang berani.
13. **Setiap keputusan di 1.4 Perlu Konfirmasi punya default** yang dipakai agent selama user belum menjawab.
14. **Momen signature (bagian 1.6).** Level Spektakuler: minimal 4; Ekspresif: 2 sampai 3; Tenang: 1 sampai 2. Setiap momen punya: pemicu (aksi/status PRD), komposisi layar, timeline motion (ms per langkah, easing/spring), aset (ilustrasi/SVG), fallback reduced-motion, dan tautan ke mockup di `design-preview.html`. Kandidat diambil dari profil produk (`references/product-types.md`), mis. hero landing page dengan koreografi scroll, halaman produk e-commerce, sukses checkout, layar status pelanggan, ringkasan dashboard dengan angka hero, login/onboarding, empty state pertama, transisi daftar → detail.
15. **Sistem motion (2.7).** Token durasi, easing, dan spring (dengan padanannya di stack: CSS, `motion`, Reanimated, Flutter `Curves`, SwiftUI `Animation`); pola masuk (stagger), transisi halaman/elemen bersama (View Transitions atau `motion` layout animation), mikro-interaksi tombol/kartu, animasi angka, dan aturan kinerja (hanya `transform`/`opacity`; UI ≤ 400ms (perpindahan layar ≤ 450ms); perayaan ≤ 1200ms; momen signature multi-fase ≤ 2500ms, bisa dilewati dengan tap, tidak memblokir input, dan informasi utamanya terbaca sejak awal). Animasi masuk di layar kerja hanya saat list pertama kali dimuat (bukan saat refresh/filter); preview menampilkan perilaku yang sama dengan aplikasi sungguhan.

### 5. Cek konsistensi

- Setiap halaman di Daftar Halaman PRD punya spesifikasi di bagian 5, dan sebaliknya (tidak ada halaman karangan selain halaman sistem di 6.3).
- Setiap aksi di fitur PRD punya titik masuk yang jelas: tombol apa, di halaman mana, muncul dan tersembunyi pada status apa.
- Data yang diwajibkan fitur PRD tampil di halaman yang relevan.
- Wireframe, mockup preview, spesifikasi komponen, dan aturan layout tidak saling bertentangan.
- Jumlah tombol primary di tiap wireframe sesuai aturan komponen, dan tombol aksi di wireframe sama dengan tabel aksi per status.
- Breakpoint yang disebut di semua bagian sama persis.
- Klaim angka dihitung, bukan dikira.
- Filter, pencarian, dan pagination punya kontrak yang jelas (query param, perilaku, tampilan mobile).
- Setiap komponen yang disebut di halaman ada di bagian 3, dan sebaliknya.
- Setiap warna, gradien, dan bayangan yang dipakai ada sebagai token di bagian 2; tidak ada hex lepas di bagian lain.
- Setiap referensi di 1.5 terlihat pengaruhnya, dan token dari referensi menyebut sumbernya.
- Setiap momen signature punya resep, fallback reduced-motion, dan mockup di preview.
- Setiap status di PRD punya badge; setiap kode error punya pesan di bagian 6.
- Istilah di glosarium dipakai konsisten.
- Tap target ≥ 44×44 px untuk semua kontrol di mobile.
- Token di blok implementasi sama persis dengan tabel token, dan sama dengan yang dipakai di preview.

Konflik yang butuh keputusan user dicatat di 1.4 Perlu Konfirmasi.

### 6. Preview high-fidelity (wajib)

Buat `design-preview.html` — sumber kebenaran visual yang bisa dibuka agent pembangun. Satu file tanpa build step, token dari 2.8 (nilai persis sama), font dari Google Fonts, ikon dan ilustrasi inline SVG, animasi CSS/JS vanilla yang benar-benar berjalan.

**Tidak boleh ada layar atau section yang kosong, sekecil apa pun jedanya.** Konten tampil penuh sejak render pertama; animasi masuk hanya memperhalus (≤ 300ms tunda untuk konten). Section panjang tanpa isi saat di-scroll ("zona mati") adalah cacat, bukan efek dramatis.

**Konten tidak boleh bergantung pada animasi untuk terlihat.** Keadaan akhir (konten tampil penuh) adalah CSS default; animasi hanya mendefinisikan titik awal (`@keyframes` dengan `from` + `animation-fill-mode: backwards`) dan dipasang lewat kelas pemicu. Jangan pernah menyembunyikan konten sebagai default lalu menunggu JavaScript, IntersectionObserver, atau scroll-driven animation untuk menampilkannya: kalau pemicunya gagal (mis. di dalam bingkai preview yang di-scroll terpisah, JS error, atau browser lama), konten hilang. Aturan ini juga berlaku untuk spesifikasi motion di DESIGN.md.

Isi:
- **Pembuka**: nama konsep, ide satu kalimat, dan satu komposisi hero yang memperlihatkan karakter desain.
- **Semua momen signature** dalam bingkai platform utama (HP 390px atau browser desktop), dengan animasi yang bisa diputar ulang (tombol "Putar ulang").
- **Layar/section inti sesuai profil produk** (lihat bagian "Isi preview" di profil; minimal 3 layar atau section) dengan data/konten contoh, dalam bingkai platform utama; versi platform lain kalau layoutnya berbeda.
- **Sistem visual**: palet dan gradien, tipografi, elevasi, bentuk, ilustrasi, motion tokens (demo kurva), komponen beserta state-nya, badge status.
- Tombol untuk mensimulasikan `prefers-reduced-motion` (mematikan animasi) supaya fallback-nya bisa dilihat.
- **Mode layar tunggal:** setiap layar/section inti dan momen signature bisa dibuka sendiri pada lebar asli tanpa bingkai, toolbar, atau skala lewat `design-preview.html?screen=<id>`, dengan `<id>` = field **Id preview** di spesifikasi 5.x DESIGN.md (momen signature memakai `m1`, `m2`, dst.). Sediakan juga tombol "Layar penuh" di setiap bingkai yang membuka URL itu. Mode ini dipakai `build-from-design` untuk memotret acuan pada viewport yang sama persis dengan hasil build.

**Preview harus konsisten dengan token.** Jalankan audit dari skill `build-from-design` pada preview itu sendiri (suntikkan token hasil `<SKILL_DIR>/../build-from-design/scripts/extract-tokens.py DESIGN.md`, lalu jalankan `<SKILL_DIR>/../build-from-design/scripts/token-audit.js`; kalau build-from-design tidak terpasang, bandingkan nilai di CSS preview dengan tabel token secara manual). Setiap warna, ukuran font, atau radius yang dipakai preview tapi tidak ada di DESIGN.md adalah celah: tambahkan sebagai token (mis. ukuran font baru di tabel 2.4) atau ubah preview supaya memakai token yang ada. Tanpa langkah ini, agent pembangun akan menemukan nilai yang tidak tercatat.

Kalau ada browser: buka di lebar yang relevan untuk profil (mis. 360px, 390px dalam bingkai, 1280px, 1440px); ukur dengan JavaScript (`scrollWidth`, `getBoundingClientRect`, elemen yang meluap) untuk baris berisiko (list dengan data terpanjang, dock/grup tombol, slot OTP, chip, header, tabel desktop) dan di lebar 180px (setara zoom 200%). Perbaiki DESIGN.md sesuai hasil ukur dan tulis hasilnya satu baris per komponen ("muat: 308/328px, diukur"). Ambil screenshot momen signature dan layar kerja utama untuk review langkah 7.

### 7. Lint, review, dan revisi (wajib, target skor ≥ 9)

**a. Lint mekanis.**
```bash
python3 <SKILL_DIR>/scripts/lint-design.py DESIGN.md --prd PRD.md
```
(tanpa `--prd` kalau tidak ada PRD). Linter menebak stack dari blok kode 2.8 (`tailwind`, `css`, atau `other` untuk Flutter/React Native/SwiftUI) dan hanya menjalankan pemeriksaan yang relevan; paksa dengan `--stack` kalau tebakannya salah. Untuk stack `other`, cocokkan tabel token dengan kode secara manual. Perbaiki semua ERROR, periksa setiap WARN. Ulangi sampai 0 ERROR.

**b. Review independen.** Baca `references/rubric.md`.
- Kalau platform bisa menjalankan sub-agen atau sesi terpisah (mis. tool Agent di Claude Code, sub-agent di tool lain): jalankan **reviewer baru di setiap putaran** (read-only, konteks segar; jangan pakai ulang reviewer sebelumnya dan jangan kirim laporan sebelumnya). Instruksinya: baca DESIGN.md, PRD/brief, `references/rubric.md`, `references/visual-craft.md`, profil yang dipakai di `references/product-types.md`, adaptor di `references/stack-adapters.md`, dan `references/stack-shadcn.md` (kalau shadcn); **buka `design-preview.html` di browser dan lihat screenshot-nya** (atau screenshot yang kamu lampirkan kalau reviewer tidak punya browser); beri **tiga skor**: (1) rubrik, (2) holistik sebagai senior product designer + engineer di stack itu (enak dipakai? cocok dengan jenis produknya? bisa dibangun tanpa menebak?), (3) **dampak visual** dari screenshot (apakah orang akan bilang "wow"?). **Skor akhir = yang terendah.** Jangan beri tahu reviewer skor yang kamu harapkan.
- Kalau tidak bisa: review sebagai pass terpisah — buka preview, lihat screenshot dengan mata segar, nilai dengan rubrik, tulis temuan sebelum mengubah apa pun.

**c. Revisi.** Perbaiki semua pemblokir dan semua temuan yang menurunkan skor di bawah 9. Verifikasi dulu setiap klaim reviewer; tolak klaim yang salah dengan alasan. Kalau skor dampak visual yang terendah, naikkan ambisi visual (warna lebih berkomitmen, tipografi lebih berani, momen signature lebih kaya) — bukan menambah aturan teknis. Setiap perubahan bisa merusak tempat lain: ukur ulang komponen yang diubah, sinkronkan DESIGN.md dan preview, jalankan lint lagi.

**d. Ulangi b–c** sampai skor akhir ≥ 9.0 tanpa pemblokir, maksimal **3 putaran**. Kalau masih < 9, serahkan dengan jujur: sebutkan skor terakhir dan apa yang kurang.

### 8. Simpan & laporkan

- Simpan `DESIGN.md` dan `design-preview.html` (dan `design-concepts.html`) di folder yang sama dengan PRD. Kalau sudah ada, jangan ditimpa — simpan dengan akhiran nama app.
- Riwayat gaya ditulis **sekali**, segera setelah konsep dipilih di langkah 2d (juga di mode Cepat), oleh sesi utama: tambahkan satu baris ke `<SKILL_DIR>/data/style-history.md` (buat kalau belum ada; kalau folder skill tidak bisa ditulis, pakai `.design-maker/style-history.md` di project; tanpa akses file sama sekali, tulis barisnya di ringkasan chat supaya user bisa menyimpannya): `YYYY-MM-DD · <nama produk> · <jenis produk> · terpilih: <keluarga> (<font display> + <font teks>) · ditolak: <keluarga>, <keluarga>`.
- Kirim `design-preview.html` ke user supaya bisa langsung dilihat (dengan cara yang tersedia di platform: lampiran, tautan file, tampilan render, atau isi file dalam blok kode kalau tidak ada akses file).
- Di chat, beri ringkasan singkat: konsep terpilih dalam satu kalimat, warna hero dan primary (hex), font, daftar momen signature, jumlah halaman dan komponen, skor review terakhir (rubrik/holistik/dampak visual) dan jumlah putaran, hasil lint, dan keputusan yang perlu dikonfirmasi.
- Tawarkan dalam satu kalimat: revisi arah visual, atau mulai membangun dengan skill `build-from-design` (mengimplementasikan DESIGN.md ke kode lalu memverifikasi kemiripannya dengan preview).

## Kalau user minta revisi

Ubah token di bagian 2 dulu, lalu cek ulang tabel kontras, blok implementasi token, dan preview. Bagian lain yang hanya merujuk nama token tidak perlu diubah. Setelah revisi, jalankan lint; untuk revisi besar (konsep, warna, layout), perbarui preview dan ulangi satu putaran review langkah 7b.
