---
name: prd-maker
description: Bikin PRD (Product Requirements Document) lengkap dari ide aplikasi, siap dipakai AI coding agent apa pun (Claude Code, Codex, Cursor, Gemini CLI, dsb). Output berisi 7 bagian wajib — Overview, Requirements, Core Features, User Flow, Architecture, Database Schema, Tech Stack — dengan diagram Mermaid dan tabel. Gunakan setiap kali user minta "buat PRD", "bikin PRD", "PRD maker", "product requirements", "dokumen spesifikasi aplikasi", "rencana/blueprint aplikasi sebelum ngoding", atau menjelaskan ide aplikasi dan ingin dijadikan spec, walaupun kata "PRD" tidak disebut. Juga dipicu oleh perintah /prd-maker.
compatibility: Model dan tool AI apa pun yang bisa membaca file Markdown. Opsional - akses file untuk menyimpan PRD.md dan membaca project; tanpa itu PRD diberikan sebagai blok markdown.
---

# PRD Maker

Ubah ide aplikasi (sesingkat apa pun) menjadi PRD yang konkret dan konsisten, sehingga bisa langsung diserahkan ke AI coding agent untuk dibangun.

Prinsip utama: **PRD ini akan dibaca oleh AI agent yang akan menulis kode.** Jadi setiap bagian harus spesifik (nama tabel, nama halaman, nama field, nama role, nama fungsi), bukan kalimat umum seperti "aplikasi yang user-friendly dan scalable". Setiap hal yang dibiarkan ambigu akan ditebak oleh agent, dan tebakan itu sering salah.

## Kompatibilitas (semua model dan tool AI)

Skill ini ditulis netral: bisa dipakai model apa pun (Claude, GPT, Gemini, model open-source) di tool apa pun yang bisa membaca file ini. Istilah yang dipakai:
- **`<SKILL_DIR>`** = folder tempat file SKILL.md ini berada. Semua path script dan referensi relatif terhadap folder ini. Skill pendamping (`prd-maker`, `design-maker`, `build-from-design`) diasumsikan berada berdampingan di folder induk yang sama (`<SKILL_DIR>/../<nama-skill>`).
- Nama tool khusus (mis. AskUserQuestion, tool Agent) hanya contoh. Pakai kemampuan yang setara di platformmu.

| Kemampuan | Dipakai untuk | Kalau tidak ada |
|---|---|---|
| Membaca/menulis file | Membaca project yang ada, menyimpan PRD.md | Tampilkan PRD dalam satu blok markdown agar user menyimpannya |
| Pertanyaan pilihan ganda | Ronde pertanyaan | Tanya lewat teks bernomor |
| Akses web | Cek dokumentasi versi framework | Tulis versi yang diasumsikan dan tandai "perlu dicek" |

## Alur kerja

### 1. Kumpulkan input

Ambil dari pesan user apa yang sudah ada. Informasi yang dibutuhkan:

| Input | Contoh | Default kalau tidak disebut |
|---|---|---|
| Nama & ide aplikasi | "TokoKas — kasir untuk UMKM" | Wajib ada (minimal ide 1 kalimat) |
| Masalah yang diselesaikan | "Pencatatan penjualan masih manual di buku" | Simpulkan dari ide |
| Target user / role | Pemilik toko, kasir | Simpulkan dari ide |
| Platform | Web, mobile, desktop | Web app responsif |
| Fitur yang diinginkan | Catat transaksi, laporan harian | Simpulkan fitur inti dari ide |
| Preferensi tech stack | Next.js + Supabase | Pilih dari panduan di akhir `references/template.md` |
| Kebutuhan khusus | Payment gateway, multi-bahasa, offline | Tidak ada |

Aturan bertanya:
- Kalau ide sudah cukup jelas → **jangan bertanya**, langsung tulis PRD dan cantumkan asumsi di bagian Overview.
- Kalau ide terlalu kabur (misal cuma "bikin aplikasi keuangan"), ajukan **maksimal satu ronde** pertanyaan (≤4 pertanyaan, masing-masing dengan opsi; pakai fitur pilihan ganda kalau platform punya, mis. AskUserQuestion di Claude Code, kalau tidak tanya lewat teks biasa), fokus pada hal yang paling mengubah desain: target user, platform, fitur inti, dan tech stack.
- Kalau user berada di dalam project yang sudah ada, baca dulu `package.json` / struktur folder / schema yang ada supaya PRD mengikuti stack dan data model yang sudah berjalan.

### 2. Tulis PRD

Baca `references/template.md`, lalu ikuti strukturnya:
- 7 bagian utama bernomor, urutan tetap, tanpa bagian utama tambahan.
- Sub-bagian (mis. 4.1, 4.2) boleh ditambah atau dinomori ulang sesuai kebutuhan, asalkan semua sub-bagian template tetap ada. Sub-bagian yang ditandai "hapus kalau tidak relevan" boleh dihapus.
- Tanggal di header = tanggal hari ini.

Bahasa: ikuti bahasa user (default Bahasa Indonesia). Istilah teknis (endpoint, schema, foreign key, dsb) dan semua identifier kode tetap bahasa Inggris.

Skala:
- Jumlah fitur Must mengikuti kemampuan yang **diminta user** — kalau user menyebut 7 kemampuan, wajar ada 7–8 fitur Must. Jangan menambah fitur Must di luar permintaan; fitur usulanmu sendiri ditandai **Should/Could**.
- Jangan mengarang fitur enterprise (multi-tenant, audit log lengkap, analitik kompleks) yang tidak diminta.
- Tulis setiap aturan bisnis **sekali** di tabel Business Rules (BR-xx), lalu bagian lain cukup merujuk ID-nya. Jangan menyalin ulang kalimat aturannya di banyak tempat (termasuk di Asumsi dan Ruang Lingkup).
- Jangan menulis hal yang sama dua kali dalam bentuk berbeda: langkah User Flow hanya untuk hal yang tidak terlihat di diagram, ERD hanya kunci dan relasi (kolom lengkap ada di detail tabel). Panjang wajar untuk MVP kecil–menengah ±400–700 baris.

Hal yang paling sering membuat agent menulis kode salah — pastikan semuanya tertulis eksplisit:
1. **Keamanan setiap aksi tulis.** Untuk setiap server action / endpoint / fungsi DB yang menulis data: siapa yang boleh memanggil, di mana role dicek, dan untuk fungsi DB: `SECURITY DEFINER` atau `INVOKER`, pengecekan role di dalam fungsi, dan `GRANT EXECUTE` ke siapa (cabut dari `anon`/`public` kalau tidak perlu).
2. **Siapa menegakkan aturan apa.** Setiap BR punya satu layer penegak utama (constraint DB, trigger, fungsi RPC, atau kode app). Jangan menegakkan aturan yang sama di dua tempat yang bisa saling bertabrakan (mis. fungsi RPC *dan* trigger yang sama-sama meng-update kolom yang sama).
3. **Versi & konvensi.** Sebut versi major setiap framework utama dan pakai konvensi file versi itu. Kalau tidak yakin konvensi versi terbaru (nama file, API yang berubah), cek dokumentasi resminya sebelum menulis struktur folder — cukup halaman yang menyangkut framework utama, auth, dan layanan eksternal yang dipakai; hal yang tidak bisa dipastikan ditandai "perlu dicek".
4. **Konfigurasi platform & uji lokal.** Setting dashboard (auth provider, signup on/off, konfirmasi email/phone, redirect URL, webhook/hook URL) beserta padanannya di lokal (mis. `supabase/config.toml` untuk `supabase start`). Pastikan setting tidak bertentangan dengan flow (mis. signup dimatikan padahal user baru harus bisa daftar). Endpoint yang dipanggil mesin (webhook, auth hook, cron) harus dikecualikan dari redirect auth di middleware/proxy — tulis matcher-nya.
5. **Risiko layanan pihak ketiga.** Kalau satu layanan eksternal menopang fitur kritis (login, pembayaran, notifikasi), catat risikonya dan fallback-nya di Overview.

### 3. Cek konsistensi sebelum menyerahkan

Sebelum menyimpan, cek silang:
- Setiap fitur **Must** punya minimal satu langkah di User Flow.
- Setiap FR dirujuk oleh minimal satu fitur (F-xx), dan setiap fitur merujuk FR-nya. Prioritas fitur ≥ prioritas tertinggi FR-nya.
- Setiap BR dirujuk oleh minimal satu fitur dan punya satu layer penegak utama yang tercatat di 6.3 (termasuk kalau penegaknya kode app — tulis nama fungsinya). Layer pendukung boleh disebut di kolom keterangan.
- BR yang menyebut verifikasi atau kepemilikan ("terverifikasi", "miliknya sendiri") menunjuk ke mekanisme yang benar-benar mengeceknya (kolom, fungsi, atau setting yang mana).
- Setiap filter/laporan bisa dijalankan dengan query layer yang dipilih (mis. PostgREST tidak bisa membandingkan dua kolom). Kalau tidak bisa, tentukan generated column, view, atau fungsi DB-nya.
- Trigger `BEFORE` tidak membaca nilai baru dari generated column (belum dihitung) — hitung dari kolom dasar atau pakai trigger `AFTER`.
- Setiap entitas di Core Features punya tabel di Database Schema, dan sebaliknya. Setiap trigger/fungsi DB punya fitur atau aksi yang memakainya (tidak ada trigger yatim).
- Nama entity di ERD sama persis dengan nama tabel di detail tabel, dan tipe di ERD = tipe dasar di detail tabel (`varchar(20)` → `varchar`, `numeric(5,2)` → `numeric`).
- Setiap komponen runtime (frontend, backend, database, auth, storage, layanan eksternal) muncul di diagram Architecture dan di Tech Stack.
- Identifier role di tabel Target User = role di Requirements, User Flow, Daftar Halaman, dan nilai kolom `role` di schema. Proses otomatis (cron, trigger, webhook) memakai role `system`, yang tidak perlu ada di tabel Target User maupun kolom `role`.
- Setiap kolom `status` yang diubah oleh aksi user punya diagram lifecycle. Status turunan (dihitung dari kolom lain) cukup dijelaskan aturannya.
- Filter/laporan yang menghitung data yang sama memakai definisi yang sama (mis. "belum lunas" di daftar order dan di ringkasan sama-sama mengecualikan order batal).
- Sintaks Mermaid valid per jenis diagram:
  - `flowchart`: label dengan spasi/kurung/tanda baca dibungkus kutip (`A["Login (email)"]`), tanpa `"` atau `;` di dalam label.
  - `erDiagram`: label relasi dalam kutip, atribut `tipe nama [PK|FK|UK]` dengan tipe satu kata.
  - `sequenceDiagram` dan `stateDiagram-v2`: teks pesan/transisi tanpa kutip, hindari `;`, `#`, dan `:` tambahan di dalam teks.

Perbaiki yang tidak konsisten, lalu cek ulang **hanya bagian yang kamu ubah** dan bagian yang merujuknya. Maksimal dua putaran perbaikan; kalau masih ada konflik yang butuh keputusan user, tulis di 1.6 Asumsi dan sebutkan di ringkasan chat.

### 4. Simpan & laporkan

- Simpan sebagai `PRD.md` di working directory (atau `docs/PRD.md` kalau folder `docs/` sudah ada). Kalau `PRD.md` sudah ada, jangan ditimpa — simpan sebagai `PRD-<nama-app>.md` (slug huruf kecil, pakai tanda hubung).
- Di chat, cukup beri ringkasan singkat (tanpa diagram): nama file, jumlah fitur Must/Should/Could, jumlah tabel, stack yang dipilih, asumsi penting, dan risiko utama. Jangan menempel ulang seluruh PRD ke chat, kecuali tidak ada akses file: tampilkan PRD penuh dalam satu blok markdown.
- Tawarkan langkah lanjutan dalam satu kalimat: membuat `DESIGN.md` (panduan tampilan, lewat skill `design-maker`) dari PRD ini, memecah PRD menjadi task list implementasi bertahap (`TASKS.md`), atau langsung mulai membangun fase pertama.

## Kalau user minta revisi

Edit bagian yang relevan saja di file yang sama, lalu jalankan ulang cek konsistensi langkah 3 — perubahan fitur hampir selalu berdampak ke Business Rules, User Flow, dan Database Schema.

## Opsional: TASKS.md

Kalau user setuju dipecah jadi task, buat `TASKS.md` (kalau `DESIGN.md` sudah ada, task UI merujuk ke spesifikasi halamannya) berisi fase (Setup & konfigurasi platform → Auth → Fitur Must satu per satu → Should → Polish & Deploy). Tiap task berupa checkbox, cukup kecil untuk dikerjakan AI agent dalam satu sesi, merujuk ke ID di PRD (misal `F-02`, `BR-03`), dan punya cara verifikasi singkat.
