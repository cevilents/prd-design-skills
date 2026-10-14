---
name: build-from-design
description: Bangun UI sungguhan dari DESIGN.md + design-preview.html (hasil design-maker) di stack project (Next.js/Tailwind/shadcn, Vue, Svelte, HTML/CSS, React Native, Flutter, SwiftUI), lalu verifikasi hasilnya semirip mungkin dengan desain lewat audit token di browser, perbandingan screenshot dengan preview, cek aksesibilitas, dan putaran perbaikan. Gunakan setiap kali user minta "bangun dari DESIGN.md", "implementasikan desain", "ngoding UI-nya", "bikin tampilannya sesuai preview", "lanjut build", atau setelah design-maker selesai dan user ingin mulai membangun, walaupun nama skill tidak disebut. Juga dipicu oleh /build-from-design.
compatibility: Butuh lingkungan coding dengan akses file dan eksekusi perintah (Python 3 + Pillow, Node). Browser/Playwright atau Chrome untuk verifikasi visual; simulator untuk aplikasi native. Tanpa itu, verifikasi manual lewat checklist.
---

# Build from Design

Ubah `DESIGN.md` + `design-preview.html` menjadi kode UI yang **terlihat dan terasa sama dengan preview**, lalu buktikan kemiripannya dengan pengukuran, bukan klaim.

Prinsip:
- **DESIGN.md adalah kontrak, preview adalah acuan visual.** Kalau keduanya berbeda, DESIGN.md menang untuk nilai (token, ukuran, teks), preview menang untuk komposisi dan rasa. Kalau preview memakai nilai yang **tidak ada** di DESIGN.md (mis. ukuran font di luar tabel 2.4, copy yang hanya ada di preview), ambil nilainya dari preview, tambahkan sebagai token/teks lewat patch DESIGN.md, dan catat sebagai "celah desain" (bukan bug kode). Catat setiap perbedaan yang ditemukan.
- **Token dulu, layar kemudian.** Hampir semua ketidakmiripan berasal dari token yang ditulis ulang dengan tangan. Pasang blok 2.8 persis, lalu semua komponen hanya memakai token.
- **Ukur, jangan mengira.** Setiap halaman diverifikasi di browser (atau simulator) dengan audit token dan perbandingan screenshot sebelum dinyatakan selesai.
- **Jangan mengubah desain diam-diam.** Kalau desain tidak bisa dibangun atau bertentangan, catat di laporan dan tawarkan patch DESIGN.md ke user.

## Kompatibilitas (semua model dan tool AI)

Skill ini ditulis netral: bisa dipakai model apa pun (Claude, GPT, Gemini, model open-source) di tool apa pun yang bisa membaca file ini. Istilah yang dipakai:
- **`<SKILL_DIR>`** = folder tempat file SKILL.md ini berada. Semua path script dan referensi relatif terhadap folder ini. Skill pendamping (`prd-maker`, `design-maker`, `build-from-design`) diasumsikan berada berdampingan di folder induk yang sama (`<SKILL_DIR>/../<nama-skill>`).
- Nama tool khusus (mis. AskUserQuestion, tool Agent) hanya contoh. Pakai kemampuan yang setara di platformmu.

| Kemampuan | Dipakai untuk | Kalau tidak ada |
|---|---|---|
| Membaca/menulis file + menjalankan perintah | Scaffold, build, script verifikasi | Skill ini butuh lingkungan coding; di chat tanpa eksekusi kode, hasilkan kode per file dan berikan checklist verifikasi manual |
| Browser / screenshot | Audit token, perbandingan dengan preview | Jalankan `scripts/shoot.mjs` (Node + Chrome/Playwright); kalau tidak bisa, minta user membuka halaman, menjalankan `token-audit.js` di DevTools, dan mengirim hasil/screenshot |
| Simulator/emulator (native) | Verifikasi visual aplikasi mobile | Review kode + analyzer/test stack, tandai "verifikasi visual belum dilakukan" |
| Sub-agen / sesi terpisah | Review kemiripan independen | Checklist 7 poin di langkah 4d |

## Alur kerja

### 1. Kumpulkan bahan dan kenali stack

- Cari `DESIGN.md`, `design-preview.html`, `PRD.md`, dan `TASKS.md` (kalau ada) di project.
- Tentukan stack dari header DESIGN.md ("Platform & stack") dan file project. Baca adaptornya di `<SKILL_DIR>/../design-maker/references/stack-adapters.md`, dan `<SKILL_DIR>/../design-maker/references/stack-shadcn.md` kalau shadcn/ui.
- Kalau belum ada project, tawarkan scaffold sesuai stack (mis. `create-next-app` + `shadcn init`, `flutter create`). Sebutkan bahwa langkah ini menginstal paket dari internet, dan minta konfirmasi sebelum menjalankannya.
- Kalau DESIGN.md bertanda **Draf cepat**, beri tahu user bahwa bagian 4 sampai 9 belum lengkap; tawarkan menyelesaikannya dulu lewat design-maker mode Penuh, atau lanjut membangun hanya layar yang sudah dispesifikasikan.
- **Baca kode komponen hasil generate, jangan mengandalkan ingatan.** Default library berubah antar versi (mis. shadcn/ui versi baru: tinggi Button, radius, preset gaya saat `init`, utilitas `cn`). Setelah scaffold dan menambah komponen, baca file komponen yang dihasilkan, lalu sesuaikan tabel override DESIGN.md 3.1 dengan default yang sebenarnya.
- Ekstrak token untuk verifikasi:
  ```bash
  python3 <SKILL_DIR>/scripts/extract-tokens.py DESIGN.md --out .design-build/tokens.json
  ```

### 2. Rencana bangun

Tulis `.design-build/progress.md` (atau pakai `TASKS.md` kalau ada) berisi checklist berurutan:
1. **Fondasi:** blok token 2.8 persis (ganti/gabung sesuai instruksi di DESIGN.md), font (2.4) dengan weight yang disebut, token motion dan aturan reduced motion (2.7), base layer, konfigurasi light/dark.
2. **Komponen:** setiap baris tabel 3.1 (override dari default library) dan spesifikasi 3.2, termasuk state (hover, focus-visible, active, disabled, loading) dan motif/teknik visual dengan resepnya (aturan 11 design-maker).
3. **Kerangka:** layout dan navigasi per role/platform (4.1 sampai 4.3), urutan tumpuk elemen tetap.
4. **Halaman/section/layar** (bagian 5), dengan urutan: momen signature dan layar kerja utama dulu, lalu sisanya.
5. **State dan konten:** loading/kosong/error (6), pesan sukses dan error persis seperti tabel, glosarium dan format (7), aksesibilitas (8).

### 3. Aturan saat menulis kode

- **Tanpa nilai lepas.** Komponen hanya memakai token (kelas/variabel/tema). Hex, ukuran font, dan durasi lepas di luar file token dianggap bug. Cek dengan grep, mis. `grep -rnE '#[0-9a-fA-F]{6}\b' src app components --include='*.tsx'` (sesuaikan folder dan ekstensi stack), dan pindahkan temuan ke token. Pengecualian yang wajar: `<meta name="theme-color">`, warna masker (`#000`/`#fff` di `mask`/`clip`), dan data SVG yang memang aset.
- **Fitur yang bergantung pada JavaScript** (efek scroll/stage, pin) memakai penanda "JS aktif" (mis. kelas `js` di `<html>` yang dipasang skrip kecil di `<head>`), sehingga tanpa JS konten tetap tampil di keadaan akhir.
- **Teks persis.** Label, judul, pesan error/sukses, dan format angka/tanggal diambil dari DESIGN.md (bagian 5, 6, 7). Jangan menulis ulang copy.
- **Data contoh hanya sebagai fixture.** Data contoh dari DESIGN.md dipakai di file mock/seed atau Storybook, bukan dikodekan langsung di komponen produksi.
- **Konten tidak bergantung pada animasi.** Keadaan akhir adalah default; animasi hanya mengatur titik awal dan selalu punya jalur reduced motion.
- **Ikuti resep, bukan imajinasi.** Motif, gradien, tekstur, ilustrasi, dan momen signature dibangun sesuai resep di DESIGN.md dan dicocokkan dengan preview. Kalau resepnya tidak bisa dipakai di stack ini, cari padanan terdekat dan catat sebagai deviasi.
- **Satu halaman selesai dulu**, baru pindah ke halaman berikutnya. Verifikasi (langkah 4) dilakukan per halaman.

### 4. Verifikasi per halaman (wajib)

Untuk web: jalankan dev server project (pakai tool preview/browser yang tersedia; kalau tidak ada, minta user menjalankannya). Untuk native: pakai simulator/emulator kalau tool-nya tersedia (mis. iOS Simulator), kalau tidak, lakukan langkah d dan e lewat review kode + analyzer/test stack (`flutter analyze`, `tsc`, dsb.) dan catat bahwa verifikasi visual belum dilakukan.

**a. Build bersih.** Typecheck, lint, dan build project tanpa error.

**Sebelum mengukur:** muat ulang halaman tanpa cache (atau restart dev server) setelah mengubah CSS/token; HMR kadang masih menyajikan CSS lama.

**b. Audit token di browser.** Buka halaman di setiap breakpoint yang disebut DESIGN.md (mis. 390px dan 1440px). Suntikkan token lalu jalankan audit:
1. Jalankan `window.__DESIGN_TOKENS = <isi .design-build/tokens.json>;` di halaman.
2. Jalankan isi `<SKILL_DIR>/scripts/token-audit.js`.
Audit melaporkan warna di luar token, font di luar desain, ukuran teks yang tidak cocok dengan skala, radius di luar token, kontras gagal, target sentuh, dan overflow horizontal. Wajib diperbaiki: semua temuan warna/font/skala/kontras/overflow dan `targetsBelow24` (gagal WCAG 2.2 AA). `targetsBelow44` adalah saran: perbaiki untuk kontrol utama di mobile (tombol, field, item navigasi), boleh dibiarkan untuk tautan sekunder seperti footer. Temuan kontras pada elemen yang sedang beranimasi (opacity < 1) dicek ulang setelah animasi selesai. Yang tidak diperbaiki dicatat sebagai deviasi dengan alasan.

**c. Bandingkan dengan preview.** Ambil screenshot halaman hasil build dan screenshot layar yang sama di `design-preview.html` pada **lebar dan tinggi viewport yang sama persis**. Pakai `scripts/shoot.mjs` (lihat README): mode reduced motion (keadaan akhir, tanpa gangguan timing animasi), tunggu animasi selesai, dan buka layar preview sendiri lewat `?screen=<id>` (id dari field Id preview di DESIGN.md 5.x). Preview lama yang belum mendukungnya: potret bingkai layar itu dengan opsi `--selector` di `shoot.mjs` pada lebar yang sama. Screenshot dari pane browser yang mengecilkan gambar tidak cukup untuk perbandingan. Lalu:
```bash
python3 <SKILL_DIR>/scripts/compare-screens.py built.png reference.png --out .design-build/diff-<halaman>.png
```
Angka selisih piksel hanya sinyal kasar (data dan posisi bisa berbeda), dan rata-rata yang kecil bisa menyembunyikan satu blok konten yang hilang. Perhatikan tile yang ditandai script, lalu **wajib melihat composite** (build | preview | heatmap) dengan mata: tipografi, warna, jarak, motif, hierarki, kepadatan, dan terutama area yang kosong di salah satu sisi.

**d. Review kemiripan independen.** Kalau platform bisa menjalankan sub-agen atau sesi terpisah, minta satu reviewer baru (read-only) membandingkan composite dan screenshot, lalu menilai kemiripan per aspek (warna, tipografi, spasi, motif, komponen, motion, copy) dengan skala 1 sampai 10, beserta daftar perbedaan konkret. Kalau tidak tersedia, lakukan sebagai pass terpisah dengan checklist ini, satu per satu untuk setiap section: (1) ada area yang kosong atau berisi lebih sedikit dari preview? (2) judul: font, berat, ukuran, tracking, pemenggalan baris sama? (3) warna latar dan aksen sama? (4) jarak antar elemen dan section sama ritmenya? (5) motif/objek signature sama detailnya? (6) komponen (tombol, field, kartu) sama bentuk dan state-nya? (7) copy sama persis? Tulis jawabannya sebelum memberi skor, dan jangan memberi 10 tanpa menyebut bukti.

**e. Motion dan reduced motion.** Picu setiap momen signature di halaman itu; bandingkan timeline dengan DESIGN.md 1.6/2.7. Emulasikan `prefers-reduced-motion: reduce` (atau setting platform) dan pastikan semua konten tetap tampil.

**f. Ulangi** perbaikan → b sampai e sampai kemiripan setiap aspek ≥ 9 dan audit bersih, maksimal 3 putaran per halaman. Kalau masih kurang, catat apa yang belum mirip dan kenapa.

### 5. Laporan

Tulis `.design-build/report.md`:
- Tabel per halaman: status, hasil audit (jumlah temuan per kategori), verdict perbandingan, skor kemiripan per aspek, jumlah putaran.
- Deviasi yang disengaja dari DESIGN.md, beserta alasannya.
- Masalah di DESIGN.md yang ditemukan saat membangun (kontradiksi, resep yang tidak bisa dibangun, data yang tidak ada di PRD), beserta usulan patch.

Di chat: ringkas halaman yang selesai, skor kemiripan rata-rata, temuan penting, dan tautan ke screenshot composite. Tawarkan: lanjut ke halaman berikutnya, menerapkan patch DESIGN.md (lewat design-maker), atau menjalankan uji end-to-end.

## Kalau DESIGN.md berubah di tengah jalan

Jalankan ulang `extract-tokens.py`, perbarui blok token, lalu ulangi audit (4b) di semua halaman yang sudah selesai; perubahan token sering berdampak ke seluruh UI.
