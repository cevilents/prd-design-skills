# Rubrik Penilaian DESIGN.md

Dipakai reviewer (sub-agen/sesi terpisah, atau pass review tersendiri) untuk menilai DESIGN.md sebelum diserahkan. Target: **setiap bagian ≥ 9 dan skor total ≥ 9.0**.

Cara menilai:
- Reviewer memberi **tiga skor**: skor rubrik (di bawah), skor holistik (penilaian sendiri sebagai senior product designer + frontend engineer, tanpa rubrik), dan **skor dampak visual** (dari screenshot `design-preview.html`, lihat bagian "Dampak Visual"). **Skor akhir = yang terendah.** Rubrik mencegah kesalahan teknis; holistik mencegah dokumen yang rapi tapi tidak enak dipakai; dampak visual mencegah desain yang benar tapi biasa saja.
- Nilai setiap bagian 1–10 berdasarkan kriteria di bawah. Skor total = rata-rata 9 bagian, lalu **dikurangi 0.3 untuk setiap temuan "pemblokir"** yang belum beres (lihat daftar di akhir).
- Setiap poin yang membuat skor < 10 harus disertai: nomor baris, masalahnya, dan perbaikan konkret (teks pengganti atau aturan yang harus ditambah).
- Bersikap skeptis. Jangan menaikkan skor untuk hal yang "kira-kira benar". Kalau tidak bisa diverifikasi, anggap belum benar.

---

## Dampak Visual (dinilai dari screenshot preview, bukan dari teks)
Buka `design-preview.html` di browser (atau lihat screenshot yang dilampirkan). Nilai seperti juri desain yang melihat karya untuk pertama kali, dengan standar jenis produknya: landing page dibandingkan dengan landing page terbaik, dashboard dengan dashboard terbaik, aplikasi native dengan aplikasi terbaik di platformnya.
- **≤ 6:** rapi tapi bisa jadi aplikasi apa saja; terlihat seperti template shadcn/Tailwind bawaan dengan warna diganti.
- **7:** ada karakter (warna atau font khas), tapi tidak ada yang membuat berhenti melihat.
- **8:** konsep jelas dan konsisten, beberapa momen yang cantik, kualitas setara aplikasi komersial yang baik.
- **9:** tes 5 detik: orang langsung bilang "wah, keren". Konsep kuat dan bisa dikenali tanpa logo; momen signature memukau (komposisi, warna, tipografi, motion bekerja bersama); detail craft terasa (ritme spasi, tipografi mikro, bayangan berlapis yang meyakinkan); layar kerja tetap terasa bagian dari dunia yang sama.
- **10:** setara karya yang dipilih untuk showcase desain kelas dunia, dan tetap enak dipakai sehari-hari.

Scroll seluruh preview (termasuk isi bingkai yang bisa di-scroll) dan pastikan tidak ada area kosong atau konten yang tidak muncul; konten yang tersembunyi menunggu animasi adalah pemblokir. Periksa juga: apakah ekspresinya bertujuan (bukan hiasan acak), apakah teks di atas warna/gradien tetap terbaca, apakah motion terasa cepat dan tidak menghambat kerja, apakah ada versi reduced-motion yang layak.

## 1. Arah Visual
- **7:** ada kata sifat dan alasan, tapi bisa dipakai untuk aplikasi apa saja.
- **8:** konteks pemakaian spesifik (siapa, di mana, perangkat apa), keputusan punya alasan.
- **9+:** ada satu konsep bernama yang dipilih dari 3 alternatif yang benar-benar berbeda; momen signature sesuai level ambisi, masing-masing dengan pemicu, timeline motion, aset, fallback reduced-motion, dan mockup; identitas visual diturunkan dari dunia user (benda, kebiasaan, bahasa visual mereka) dan bisa disebut dalam satu kalimat; terlihat di layar kerja utama role utama; setiap keputusan yang butuh konfirmasi punya default; klaim angka (mis. "4 order terlihat di 360px") cocok dengan hitungan tinggi elemen.

## 2. Design Tokens
- **7:** token lengkap, kontras dicek sebagian.
- **8:** semua pasangan yang dipakai tercatat dengan rasio hasil script.
- **9+:** linter 0 ERROR; tabel 2.1 = blok 2.8 persis; setiap token tipografi ada di `@theme`; kompatibel dengan stack (mode gelap ditangani dengan benar, import bawaan disebut, ring solid); palet inti kecil dan setiap warna punya satu fungsi jelas; varian yang latarnya mirip latar halaman punya pembeda (border).

## 3. Komponen
- **7:** daftar komponen dan varian.
- **8:** ukuran, state lengkap (default, hover, focus-visible, active, disabled, loading), aturan pemakaian.
- **9+:** setiap baris berisi beberapa elemen punya hitungan anggaran lebar di lebar terkecil platform yang benar (mis. 360px untuk web mobile, 1024px untuk dashboard desktop-first); **setiap** komponen library yang di-install punya baris override (termasuk primitif seperti `Card`, `Dialog`, `Badge`) atau ditulis "tanpa perubahan"; setiap motif punya resep CSS yang bisa langsung ditulis (elemen/pseudo-element, positioning, ukuran, permukaan di belakangnya) dan perilaku di 360px dan zoom 200%; tidak ada kontrol < 44px tanpa area sentuh 44px.

## 4. Layout & Navigasi
- **7:** app shell dan navigasi per role.
- **8:** pola responsif per breakpoint.
- **9+:** header, tombol kembali, dan state navigasi aktif ditulis untuk setiap breakpoint; breakpoint yang sama persis di semua bagian; posisi elemen tetap (dock, FAB, toast, navigasi) tidak saling menimpa dan disebut urutan tumpuknya; navigasi aktif jelas untuk setiap route termasuk route detail.

## 5. Spesifikasi Halaman
- **7:** setiap halaman punya wireframe.
- **8:** state loading/kosong/error lengkap dengan teks, data contoh realistis.
- **9+:** setiap langkah alur multi-langkah dan setiap sheet/dialog berisi form punya wireframe; ukuran yang berisiko meluap sudah diukur di render (kalau ada browser); aturan kepadatan dan breakpoint profil produk terpenuhi dan dihitung (mis. ≥ 3 item list di 360×640 untuk web app mobile-first, baris tabel di 1280×800 untuk dashboard, hero + CTA di atas lipatan untuk landing page, panjang baris 60 sampai 75 karakter untuk konten); data contoh konsisten di seluruh dokumen (kode, tanggal berurutan, angka cocok); setiap status yang mengubah layout punya wireframe; wireframe memakai notasi baku (`[[ ]]` primary, `[ ]` secondary, `( )` ghost/link) dan **maksimal satu `[[ ]]` per layar**; tabel aksi per status untuk halaman yang aksinya berubah menurut status, dan wireframe cocok dengan tabel itu; setiap data yang diwajibkan fitur PRD tampil; filter/pencarian punya kontrak query param; tidak ada kontradiksi antara wireframe, teks, dan bagian 3.

## 6. Feedback & State Global
- **7:** pola loading dan beberapa pesan error.
- **8:** setiap kode error PRD punya pesan.
- **9+:** setiap aksi tulis punya teks sukses; pesan menjelaskan apa yang terjadi dan apa yang harus dilakukan, dengan cara tampil yang jelas (di field, toast, alert); halaman sistem lengkap (404, error, sesi habis, role tidak berhak, offline); konfirmasi aksi irreversible berupa pertanyaan spesifik dengan tombol berlabel aksi.

## 7. Konten & Copywriting
- **7:** gaya bahasa disebut.
- **8:** glosarium dan format uang/tanggal/nomor.
- **9+:** glosarium hanya istilah yang rawan tidak konsisten dan benar-benar dipakai konsisten di seluruh dokumen; label tombol kata kerja spesifik; tidak ada em/en dash; nada cocok dengan target user.

## 8. Aksesibilitas
- **7:** daftar umum (kontras, focus).
- **8:** spesifik: tap target, label form, status tidak hanya warna.
- **9+:** hanya aturan yang belum tercakup di bagian lain (tidak mengulang); `lang`, judul halaman per route, landmark, `autocomplete`/`inputmode`, perilaku `prefers-reduced-motion`, perilaku zoom 200%, dan elemen dekoratif (motif) aman untuk pembaca layar (`aria-hidden` bila dekoratif).

## 9. Catatan Implementasi
- **7:** library dan lokasi file.
- **8:** daftar komponen yang di-install dan ikon.
- **9+:** tabel override lengkap; pola form (validasi, kapan error tampil, state pending); cara memuat font sesuai stack; instruksi `globals.css` jelas (ganti atau gabung); daftar "Jangan" spesifik untuk aplikasi ini.

---

## Temuan pemblokir (masing-masing −0.3 dari skor total)
00. Tidak ada `design-preview.html`, atau preview tidak sesuai token/isi DESIGN.md.
01. Skor dampak visual < 8 untuk level Spektakuler (desain terlalu aman).
0. Aturan kepadatan/breakpoint profil produk dilanggar tanpa alasan kuat (lihat `product-types.md`).
1. Linter (`scripts/lint-design.py`) masih melaporkan ERROR.
2. Ada dua instruksi yang saling bertentangan sehingga agent pembangun harus menebak.
3. Ada aksi di fitur PRD yang tidak punya titik masuk di halaman mana pun.
4. Ada bug yang membuat UI tampil salah di kondisi umum (mode gelap sistem, zoom, layar terkecil platform).
5. Ada motif atau komponen custom tanpa resep implementasi.
6. Panjang > 900 baris (1000 untuk stack non-web), atau fakta yang sama ditulis di dua tempat atau lebih (spesifikasi komponen, token, aturan aksesibilitas).
7. Kontrol di wireframe yang tidak punya komponen di daftar install, atau hook/utilitas yang tidak ada di library tanpa implementasi.
8. Data contoh yang saling bertentangan antar wireframe.

## Format laporan reviewer
```
SKOR AKHIR: x.x / 10 (= min(rubrik, holistik, dampak visual))
Rubrik: x.x (rata-rata y.y, pemblokir: n) · Holistik: x.x — alasan satu kalimat · Dampak visual: x.x — kesan 5 detik pertama dalam satu kalimat
1 Arah Visual: n — alasan satu baris
... (sampai 9)
PEMBLOKIR:
- [baris] masalah → perbaikan
PERBAIKAN UNTUK NAIK KE 9+ (urut dampak):
- [baris] masalah → perbaikan konkret
```
