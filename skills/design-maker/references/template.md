# Template DESIGN.md

Isi semua bagian di dalam blok `~~~markdown` di bawah, lalu salin hanya isinya (tanpa pagar `~~~`). Semua teks dalam `<...>` adalah instruksi atau contoh: ganti dengan isi nyata atau hapus. Nilai yang diawali "mis." hanya contoh format, bukan rekomendasi; pilih nilai sendiri sesuai arah visual. Hasil akhir tidak boleh menyisakan `<...>`.

---

~~~markdown
# DESIGN: <Nama Aplikasi>

> <Satu kalimat: tampilan aplikasi ini terasa seperti apa, untuk siapa, dan dipakai dalam kondisi apa.>

| | |
|---|---|
| Versi | 1.0 |
| Tanggal | <YYYY-MM-DD> |
| Berdasarkan | <PRD.md v1.0 / brief / kode project yang ada / deskripsi user> |
| Jenis produk | <profil dari references/product-types.md, mis. Landing page + Dashboard SaaS> |
| Platform & stack | <mis. Web desktop-first (1280 sampai 1440px) · Next.js + Tailwind v4 + shadcn/ui; atau iOS + Android · Flutter> |

---

## 1. Arah Visual

### 1.1 Konteks Pemakaian
<Siapa memakai apa, di mana, dengan perangkat apa. Ambil dari target user di PRD/brief. Mis. "Analis keuangan: laptop 14 inci di kantor, membuka dashboard puluhan kali sehari" atau "Calon pembeli: HP, datang dari iklan Instagram, memutuskan dalam 10 detik apakah lanjut scroll".>

### 1.2 Konsep & Kepribadian
- **Konsep:** <nama konsep + ide satu kalimat dari dunia user/produk, mis. "Etalase Malam: aplikasi terasa seperti etalase kaca toko yang menyala di malam hari" atau "Kertas Grafik: dashboard terasa seperti buku catatan insinyur">
- **Level ambisi:** <Spektakuler / Ekspresif / Tenang>
- **Tiga kata sifat:** <mis. hangat, jelas, cekatan>
- **Bukan:** <tiga hal yang sengaja dihindari, mis. korporat kaku, futuristik, ramai>
- **Kepadatan informasi:** <rendah / sedang / tinggi + alasan>
- **Motif khas:** <satu elemen visual yang diambil dari dunia user, mis. garis putus-putus seperti nota laundry. Hapus kalau tidak ada.>

### 1.3 Keputusan & Alasan
| Keputusan | Pilihan | Alasan |
|---|---|---|
| Konsep terpilih | <nama konsep B dari 3 di `design-concepts.html`> | <alasan: pilihan user / penilaian dampak visual + kecocokan user> |
| Mode warna | <light / dark / light + dark / momen signature gelap + layar kerja terang> | <...> |
| Pendekatan layout | <mobile-first / desktop-first> | <...> |
| Gaya bentuk | <mis. sudut sedang 8px, tanpa bayangan, border tipis> | <...> |

### 1.4 Perlu Konfirmasi
| Keputusan | Default yang dipakai sekarang | Alternatif |
|---|---|---|
| <mis. Light saja> | <light saja> | <light + dark ikut sistem> |

<Keputusan yang butuh jawaban user. Agent memakai kolom Default sampai user menjawab. Hapus kalau tidak ada.>

### 1.5 Referensi
| Referensi | Jenis | Diambil | Sengaja tidak diambil |
|---|---|---|---|
| <`referensi/logo.png`> | <logo milik user> | <warna `#E85D04` → `primary` (versi gelap `#B54A03` untuk teks/tombol); sudut membulat → `radius-md` 12px> | <gaya huruf logo, tidak dipakai untuk UI> |
| <screenshot `https://...`> | <website referensi> | <navigasi bawah, kartu tanpa bayangan, judul besar> | <warna & ilustrasi mereka> |

<Hex dari script extract-palette.py; tandai "(perkiraan)" kalau hanya dilihat. Hapus bagian ini kalau tidak ada referensi.>

### 1.6 Momen Signature
<Momen yang dirancang khusus untuk membuat orang bilang "wow". Spektakuler ≥ 4, Ekspresif 2 sampai 3, Tenang 1 sampai 2.>

| # | Momen | Pemicu (PRD) | Kenapa penting bagi user | Mockup |
|---|---|---|---|---|
| M1 | <mis. Layar status "Siap diambil"> | <status `ready`, F-07> | <momen paling ditunggu pelanggan> | `design-preview.html#m1` |

#### M1 · <Nama momen>
- **Komposisi:** <apa yang memenuhi layar: bidang warna/gradien hero, angka/teks raksasa, ilustrasi, posisi elemen>
- **Timeline motion:** <langkah demi langkah dengan ms dan easing/spring, mis. 0ms latar `--gradient-ready` fade 300ms `ease-out-expo` · 120ms ilustrasi naik 24px spring(300, 24) · 280ms judul masuk per kata stagger 40ms · total ≤ 1200ms, bisa dilewati dengan tap>
- **Aset:** <ilustrasi inline SVG apa, ukuran, warna token>
- **Reduced motion:** <tampil langsung di posisi akhir, tanpa gerakan; hanya fade 150ms>
- **Resep:** <CSS/SVG/kode motion inti, atau rujuk komponen di 3.2>

---

## 2. Design Tokens

### 2.1 Warna
| Token | Light | Dark | Dipakai untuk |
|---|---|---|---|
| `background` | <#FAFAF9> | <#...> | Latar halaman |
| `foreground` | <#...> | <#...> | Teks utama |
| `muted` | <#...> | <#...> | Latar sekunder, baris tabel selang-seling |
| `muted-foreground` | <#...> | <#...> | Teks sekunder, keterangan |
| `border` | <#...> | <#...> | Garis pemisah, border kartu |
| `input` | <#...> | <#...> | Border field (harus ≥ 3.0 terhadap latar) |
| `primary` | <#...> | <#...> | Aksi utama, link |
| `primary-foreground` | <#...> | <#...> | Teks di atas primary |
| `ring` | <#...> | <#...> | Focus ring |
| `card` / `card-foreground` | <...> | <...> | Latar kartu, sheet, dialog |
| `popover` / `popover-foreground` | <...> | <...> | Dropdown, menu |
| `destructive` / `destructive-foreground` | <...> | <...> | Aksi destruktif, teks error |
| `success` / `success-subtle` | <...> | <...> | <teks / latar badge sukses> |
| `warning` / `warning-subtle` | <...> | <...> | <...> |
| `info` / `info-subtle` | <...> | <...> | <...> |
| `hero` / `hero-foreground` | <...> | <...> | <bidang warna penuh di momen signature dan header hero> |
| `surface-<nama>` | <...> | <...> | <latar imersif untuk section/status penting, mis. `surface-ready`, `surface-pricing`> |

<Hapus kolom Dark kalau hanya light mode. Hapus token yang tidak dipakai. Nama token dasar mengikuti konvensi library di stack (contoh di atas untuk shadcn/ui). Gradien, elevasi, dan motion ditulis di 2.6 dan 2.7, bukan di tabel ini.>

### 2.2 Warna Status
| Status (PRD 6.4) | Label UI | Latar | Teks | Ikon |
|---|---|---|---|---|
| `<received>` | <Diterima> | <token> | <token> | <nama ikon / tanpa ikon> |

<Satu baris per status di PRD. Warna diambil dari token 2.1, bukan warna baru. Hapus bagian ini kalau produk tidak punya status data (mis. landing page, company profile).>

### 2.3 Tabel Kontras
| Teks / elemen | Latar | Rasio | Normal (4.5) | Besar / non-teks (3.0) |
|---|---|---|---|---|
| `foreground` | `background` | <15.80> | PASS | PASS |
| `input` (border) | `background` | <3.12> | n/a | PASS |

<Isi dengan hasil script contrast-check.py, bukan perkiraan. Pasangan wajib ada di SKILL.md aturan 2. Kalau ada mode dark, ulangi tabel untuk dark. Garis dekoratif: tulis "dekoratif" di kolom verdict.>

### 2.4 Tipografi
- **Font display:** <font berkarakter untuk judul, angka hero, momen signature + sumber + fallback>. <Alasan dari konsep.>
- **Font teks:** <font yang sangat terbaca untuk UI dan teks + sumber + fallback>.
- **Angka:** <mis. `tabular-nums` untuk nominal dan berat>

| Token | Ukuran / line-height | Weight | Dipakai untuk |
|---|---|---|---|
| `text-hero` | <clamp(40px, 12vw, 72px) / 1.0> | <800> | <angka/teks raksasa di momen signature, font display> |
| `text-display` | <28px / 34px> | <700> | <judul halaman utama> |
| `text-title` | <20px / 28px> | <600> | <...> |
| `text-body` | <16px / 24px> | <400> | <teks utama, minimal 16px di mobile agar iOS tidak zoom saat fokus input> |
| `text-small` | <14px / 20px> | <400> | <...> |
| `text-caption` | <12px / 16px> | <500> | <...> |

### 2.5 Spacing & Grid
- **Skala spacing:** <mis. 4, 8, 12, 16, 24, 32, 48 px>
- **Padding halaman:** <mobile 16px, desktop 24px>
- **Lebar konten maksimum:** <mis. 1120px desktop; form 480px>
- **Breakpoint:** <mis. `sm` 640, `md` 768, `lg` 1024>

### 2.6 Bentuk, Elevasi, Material & Ilustrasi
**Bentuk**
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `radius-sm` | <6px> | <badge, input> |
| `radius-md` | <8px> | <kartu, tombol> |
| `radius-xl` | <28px> | <panel hero, sheet; sesuai bahasa bentuk konsep> |

**Elevasi** (bayangan berlapis, konsisten satu arah cahaya)
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `shadow-1` | <mis. 0 1px 2px oklch(0.2 0.02 250 / 0.08), 0 1px 1px oklch(0.2 0.02 250 / 0.04)> | <kartu di atas latar> |
| `shadow-3` | <3 sampai 4 lapis> | <sheet, dialog, kartu hero melayang> |

**Gradien & material**
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `gradient-hero` | <mis. radial-gradient(120% 80% at 20% 0%, <hue brand terang> 0%, <hue brand> 45%, <hue gelap> 100%)> | <latar momen signature, header hero> |
| `texture-grain` | <SVG feTurbulence data URI, opacity 0.06, mix-blend-mode overlay> | <di atas bidang warna besar agar tidak terasa plastik> |

<Hapus yang tidak dipakai. Teks di atas gradien/material dicek kontrasnya terhadap titik terburuk (SKILL.md aturan 2).>

**Ilustrasi & ikon**
- **Gaya ilustrasi:** <mis. garis 2px, sudut membulat, isi 2 warna token, perspektif datar; dipakai di momen signature dan empty state>
- **Daftar ilustrasi:** <nama + tempat pakai + ukuran, mis. `illo-ready` (keranjang terlipat rapi, 160px) di M1>
- **Ikon:** <library + kustomisasi (stroke, ukuran, duotone) + aturan pemakaian>

### 2.7 Motion
| Token | Nilai | Dipakai untuk |
|---|---|---|
| `duration-fast` | <120ms> | <press, hover> |
| `duration-base` | <220ms> | <sheet, dialog, transisi elemen> |
| `duration-slow` | <400ms> | <transisi halaman, masuk momen signature> |
| `ease-out-expo` | <cubic-bezier(0.16, 1, 0.3, 1)> | <elemen masuk> |
| `spring-snappy` | <stiffness 400, damping 30 (library `motion`)> | <kartu, tombol, angka> |

- **Pola masuk:** <mis. item list masuk stagger 30ms, naik 8px + fade, maksimal 8 item pertama>
- **Transisi daftar → detail:** <mis. View Transitions `view-transition-name: order-<kode>` pada kode order, fallback fade>
- **Mikro-interaksi:** <tombol scale 0.97 saat ditekan, angka berubah dengan ticker, badge status berganti dengan crossfade>
- **Kinerja:** hanya `transform` dan `opacity`; UI ≤ 400ms (perpindahan layar ≤ 450ms); perayaan ≤ 1200ms; momen signature multi-fase ≤ 2500ms, bisa dilewati dengan tap, tidak memblokir input.
- **Reduced motion:** <saat `prefers-reduced-motion: reduce`: tanpa gerakan posisi/skala, hanya fade ≤ 150ms; perayaan tampil di keadaan akhir>

### 2.8 Implementasi Token
<Blok kode siap tempel dalam bahasa stack (lihat references/stack-adapters.md): CSS + Tailwind, CSS biasa, `ThemeData` Flutter, objek tema React Native, SwiftUI, atau tabel design token JSON. Tulis di atas blok: "Ganti seluruh isi `<file>` dengan blok ini" atau "Gabungkan dengan ...". Contoh kerangka untuk Tailwind v4 + shadcn/ui:>
```css
@import "tailwindcss";
@import "tw-animate-css";
/* + import bawaan lain dari globals.css hasil shadcn init versi yang dipakai */
/* light saja: @custom-variant dark (&:is(.dark *)); dan color-scheme: light di :root */

:root {
  --background: <#...>;
  --foreground: <#...>;
  /* ...semua token 2.1 */
  --radius: <0.5rem>;
}
.dark {
  /* varian dark, hapus kalau light saja */
}
@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  /* ... */
}
@layer base {
  * { @apply border-border outline-ring; }
  body { @apply bg-background text-foreground; }
}
```

---

## 3. Komponen

### 3.1 Daftar Komponen
| Komponen | Library | Default library → diubah menjadi | Dipakai di halaman |
|---|---|---|---|
| Button | <shadcn/ui `Button`> | <mis. h-9, hover /90 → h-11, hover token `primary-hover`; atau "tanpa perubahan"> | <...> |

<Satu-satunya tempat override komponen. Setiap komponen yang di-install punya baris di sini.>

### 3.2 Spesifikasi Komponen
#### <Button>
- **Ukuran:** <mis. default tinggi 44px, padding 16px; sm 36px hanya di desktop>
- **Varian:** <kapan memakai masing-masing>
- **State:** default / hover / focus-visible (ring 2px `ring`, offset 2px) / active / disabled (opacity, cursor) / loading (spinner + label tetap, tombol disabled)
- **Aturan:** <mis. satu tombol primary per layar; label kata kerja ("Simpan Order", bukan "Submit")>

<Ulangi untuk setiap komponen yang punya aturan khusus. Komponen standar tanpa aturan khusus cukup ada di tabel 3.1.>

---

## 4. Layout & Navigasi

### 4.1 Kerangka & Navigasi per Role/Platform
| Role (PRD) | Mobile | Desktop |
|---|---|---|
| `<owner>` | <mis. bottom navigation 4 item + tombol aksi utama> | <sidebar kiri 240px> |

### 4.2 Struktur Navigasi
<Item navigasi per role, urutan, ikon, dan halaman tujuannya (route dari PRD). Rujuk User Flow PRD.>

### 4.3 Pola Responsif
<Apa yang berubah di tiap breakpoint: tabel → kartu list, sheet → dialog, kolom tunggal → dua kolom, dsb.>

---

## 5. Spesifikasi Halaman / Section / Layar

<Ikuti profil produk: web app dan dashboard per halaman/route; landing page per section dari hero sampai footer (sertakan koreografi scroll dan CTA tiap section); aplikasi native per layar dengan pola navigasi platform; situs konten per tipe halaman (beranda, artikel, kategori).>

### 5.1 <Nama Halaman>: `<route>`
- **Role:** <...> · **Fitur terkait:** <F-xx> · **Id preview:** `<id-pendek, mis. order-list>` (dibuka lewat `design-preview.html?screen=<id>`)
- **Tujuan:** <satu kalimat: apa yang ingin diselesaikan user di sini>
- **Prioritas konten:** <1. ... 2. ... 3. ...>

**Wireframe mobile:**
<Notasi baku: `[[ Label ]]` = tombol primary (maksimal satu per layar), `[ Label ]` = secondary/outline, `( Label )` = ghost atau tautan, `‹ ›` = navigasi kembali/maju. Kalau ada notasi lain (mis. sorotan), jelaskan sekali di 3.2. Satu blok kode = satu layar di satu breakpoint (linter menghitung `[[ ]]` per blok); gambar mobile dan desktop di blok terpisah.>
```
┌──────────────────────────┐
│ <Header>                 │
├──────────────────────────┤
│ <konten dengan data       │
│  contoh realistis>        │
│                          │
├──────────────────────────┤
│ [[ Aksi Utama ]]         │
└──────────────────────────┘
```
<Tambahkan wireframe desktop hanya kalau layoutnya berbeda secara struktur.>

**Komponen:** <daftar komponen dari bagian 3>

**Koreografi scroll** (landing page/section naratif; hapus kalau tidak relevan): <pemicu (masuk viewport 30%, pinned 200vh), apa yang bergerak, fallback tanpa scroll-driven animation dan saat reduced motion>

**State:**
| State | Tampilan | Teks |
|---|---|---|
| Loading | <skeleton berbentuk konten asli / spinner di tombol> | (tanpa teks) |
| Kosong | <...> | <"Belum ada order hari ini. Order baru akan muncul di sini."> |
| Error | <...> | <pesan + aksi, mis. tombol "Coba lagi"> |

<Ulangi 5.x untuk setiap halaman di Daftar Halaman PRD.>

---

## 6. Feedback & State Global

### 6.1 Pola Loading
<Kapan skeleton, kapan spinner di tombol, kapan optimistic update.>

### 6.2 Pesan Error
| Kode (PRD) | Pesan ke user | Ditampilkan sebagai |
|---|---|---|
| `<WEIGHT_REQUIRED>` | <"Isi berat cucian dulu sebelum menyimpan."> | <teks di bawah field> |

<Satu baris per kode error di PRD. Pesan menjelaskan apa yang terjadi dan apa yang harus dilakukan. Jangan menyalin ulang kondisi error dari PRD; cukup kode + pesan + cara tampil.>

### 6.3 Halaman Sistem
| Kondisi | Tampilan | Teks & aksi |
|---|---|---|
| Halaman tidak ditemukan (404) | <...> | <...> |
| Error tak terduga (`error.tsx`) | <...> | <...> |
| Sesi berakhir | <...> | <...> |
| Role tidak berhak (mis. customer membuka halaman owner) | <redirect ke ... / pesan> | <...> |
| Offline / koneksi putus | <...> | <...> |

### 6.4 Sukses & Konfirmasi
- **Toast sukses:** <kapan dipakai, posisi, durasi>
- **Konfirmasi aksi destruktif/irreversible:** <dialog dengan judul berupa pertanyaan spesifik dan tombol berlabel aksi, mis. "Batalkan order #A-0012?" → "Batalkan Order">

---

## 7. Konten & Copywriting

### 7.1 Gaya Bahasa
<Sapaan (kamu/Anda), tingkat formalitas, panjang kalimat. Sesuaikan dengan target user.>

### 7.2 Glosarium
| Istilah dipakai | Jangan pakai | Catatan |
|---|---|---|
| <Order> | <Pesanan, Transaksi> | <...> |

### 7.3 Format
- **Uang:** <mis. `Rp8.000` (tanpa spasi, titik ribuan, tanpa desimal)>
- **Berat:** <mis. `3,5 kg`>
- **Tanggal & waktu:** <mis. `13 Okt 2026, 14.30` (WIB)>
- **Nomor HP:** <mis. tampil `0812-3456-7890`, simpan `+6281234567890`>

---

## 8. Aksesibilitas
- **Kontras:** semua pasangan di 2.3 lolos; tidak ada teks di atas foto/gradient tanpa lapisan.
- **Focus:** focus ring terlihat di semua elemen interaktif (`:focus-visible`), tidak pernah `outline: none` tanpa pengganti.
- **Tap target:** ≥ 44×44 px di mobile, jarak antar target ≥ 8px.
- **Form:** setiap field punya label terlihat (bukan placeholder saja); error dikaitkan ke field (`aria-describedby`).
- **Status:** tidak hanya dibedakan warna, selalu ada label teks.
- **Keyboard:** <urutan tab, shortcut kalau ada, dialog menjebak fokus dan menutup dengan Esc>
- **Dokumen:** `<html lang="id">`, judul halaman unik per route (mis. "Order Baru · <Nama App>"), landmark `nav`/`main`.
- **Autofill:** atribut `autocomplete` yang tepat (mis. `tel`, `one-time-code`, `email`), `inputmode` untuk angka.
- <Tambahkan hal khusus aplikasi ini.>

---

## 9. Catatan Implementasi
- **Library komponen:** <mis. shadcn/ui; daftar komponen yang perlu di-install: `button`, `input`, `sheet`, ...>
- **Hook/utilitas tambahan:** <yang tidak disediakan library beserta implementasi singkatnya; hapus kalau tidak ada>

- **Pola form:** <validasi (mis. zod + react-hook-form atau server action dengan `useActionState`), kapan error tampil (saat submit / saat blur), tombol disabled saat pending>
- **Ikon:** <library + ukuran default + kapan ikon dipakai (hanya kalau membantu memindai, bukan dekorasi)>
- **Font loading:** <cara memuat font sesuai stack>
- **Lokasi file:** <mis. token di `app/globals.css`, komponen di `components/ui/`>
- **Jangan:** <daftar singkat larangan spesifik untuk aplikasi ini, mis. "jangan pakai gradient", "jangan stat card berisi angka dummy", "jangan ikon di setiap tombol">
~~~
