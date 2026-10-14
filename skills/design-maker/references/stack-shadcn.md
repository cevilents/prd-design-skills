# Jebakan Stack: Next.js + Tailwind v4 + shadcn/ui

> **Default komponen berubah antar versi shadcn/ui** (mis. tinggi Button, radius, preset gaya yang dipilih saat `init`, letak utilitas `cn`). Nilai "default" di file ini adalah contoh dari versi tertentu, bukan kebenaran tetap. Saat menulis tabel override, sebut versi yang diasumsikan dan minta agent pembangun membaca file komponen hasil generate sebelum menerapkan override.

Baca file ini kalau stack di PRD memakai shadcn/ui. Setiap poin di sini pernah membuat DESIGN.md salah dibangun. Untuk setiap komponen yang dipakai, pastikan DESIGN.md menyebut perilakunya secara eksplisit.

## Tema & CSS
- **Light saja:** `@custom-variant dark (&:is(.dark *));` dan `color-scheme: light` di `:root`. Tanpa ini, kelas `dark:` bawaan komponen aktif mengikuti mode gelap HP.
- **Sonner (`<Toaster>`):** wrapper shadcn membaca tema dari `next-themes` (default `"system"`). Light saja → tulis `<Toaster theme="light" />`. Sebutkan juga posisi, `offset` (di bawah header + safe-area, dan versi tiap breakpoint kalau header berubah), `closeButton` dan ukuran area sentuhnya (mis. `toastOptions.classNames.closeButton`). Sonner memakai satu wilayah `aria-live` untuk semua toast, bukan `role` per toast; kalau error perlu diumumkan tegas, tulis caranya (mis. `toast.custom()` dengan elemen `role="alert"`) atau terima `polite` untuk semua.
- **Ikon & radius Sonner:** wrapper shadcn versi terbaru memasang ikon sendiri per varian dan membaca `--border-radius`; kalau ikon atau radius diubah, tulis override `icons` dan sertakan `--border-radius` saat memberi prop `style`.
- **Gaya toast Sonner:** CSS Sonner tidak ber-layer, sehingga mengalahkan utilitas Tailwind di `toastOptions.classNames`. Tulis `!` pada kelas warna atau set variabel Sonner (`--normal-bg`, `--normal-border`, `--normal-text`) per varian.
- **Hasil aksi di dalam Sheet/Dialog:** kalau aturan toast berbeda saat Sheet/Dialog terbuka, tabel pesan error harus menyebut cara tampil di dalam Sheet juga.
- **Focus ring:** bawaan komponen memakai `ring-ring/50` (transparan). Kalau rasio kontras ring dihitung untuk warna penuh, override ke ring solid di tabel override.
- **`outline-none` di Tailwind v4:** komponen bawaan (Button, Input, Select, Toggle, Switch) membawa `outline-none`, yang men-set `--tw-outline-style: none`; `focus-visible:outline-2` memakai variabel itu sehingga outline tetap tak terlihat. Kalau fokus memakai outline, tulis "buang `outline-none`" atau tambah `focus-visible:outline-solid`.
- **Ring offset:** `--tw-ring-offset-color` tidak diwariskan; jangan mengandalkan mengubahnya di parent. Pakai outline + `outline-offset` atau `ring-offset-<token>` langsung di elemennya.
- **Token tipografi Tailwind v4:** `--text-<nama>`, `--text-<nama>--line-height`, `--text-<nama>--font-weight` di `@theme`. Setiap token di tabel tipografi harus punya ketiganya bila weight-nya berbeda dari default.
- **`@layer` dan urutan:** kelas custom di `@layer components` kalah oleh utilitas Tailwind. Komponen custom yang punya padding/radius sendiri jangan dibangun dari subkomponen yang membawa utilitas bawaan (mis. `CardHeader`/`CardContent` membawa `px-6`); tulis "elemen biasa dengan kelas `.xxx`" atau sebutkan override-nya.

## Komponen
- **Card:** default `rounded-xl`, `border`, `shadow-sm`, `py-6`, `gap-6`, subkomponen `px-6`. Tulis apa yang dipertahankan atau dibuang.
- **Button:** default tinggi 36px (`h-9`), hover `/90`. Mobile butuh 44px; tulis override tinggi, padding, hover.
- **Input:** default `h-9`, `ring-ring/50`. Tulis tinggi 44px dan ring.
- **Badge:** default kecil (teks 12px, padding tipis); bentuk sudutnya berbeda antar versi shadcn. Tulis bentuk, tinggi, dan ikon secara eksplisit.
- **Latar overlay:** `SheetContent`, `DialogContent`, `AlertDialogContent`, `PopoverContent` memakai `bg-background`/`bg-popover` bawaan. Kalau permukaannya harus token lain (mis. `card`), tulis di override.
- **Sheet:** arah (`side`) adalah **prop**, bukan kelas CSS. Kalau sheet berubah dari bawah (mobile) ke kanan (desktop), tulis caranya, mis. `useMediaQuery('(min-width: 768px)')` dengan default `bottom` saat SSR.
- **Dialog / AlertDialog:** Radix AlertDialog memfokuskan tombol Cancel saat dibuka. Untuk konfirmasi non-destruktif yang ingin fokus di aksi, tulis `onOpenAutoFocus`. Tulis juga lebar maksimum dan perilaku di 360px.
- **ToggleGroup:** `type="single"` merender `role="radio"` + `aria-checked` (bukan `aria-pressed`) dan mengirim nilai `""` saat item aktif diklik lagi. Tulis apakah boleh kosong; kalau tidak, abaikan `""` di `onValueChange`.
- **RadioGroup sebagai kartu pilihan:** tulis apakah titik radio terlihat, elemen mana yang jadi `<label>`, dan di mana ring fokus tampil (mis. wadah dengan `has-[:focus-visible]:ring-2`).
- **Tabs vs navigasi:** tab yang berpindah route adalah tautan → `nav` + `aria-current="page"`, bukan `role="tab"`.
- **Switch:** kalau track diperbesar, tulis juga ukuran thumb dan jarak geser (mis. track 44×24 → thumb `size-5`, aktif `translate-x-5`). Tinggi default ±20px; tulis area sentuh 44px, state pending (disabled saat menyimpan), dan perilaku saat gagal (kembali ke posisi semula + pesan).
- **InputOTP:** jumlah slot × lebar slot + jarak harus muat di lebar kontainer (lihat anggaran lebar di bawah). Slot berada di dalam `InputOTPGroup` (flex), jadi pembungkusan baris diatur di group (`flex-wrap`), bukan di `containerClassName`; slot bawaan memakai border gabungan (`border-y border-r`, sudut di first/last) yang perlu diganti kalau slot diberi jarak. Tulis penanda slot aktif (mis. `data-[active=true]:border-ring`), terutama kalau ring bawaan dibuang.
- **Ukuran Button:** `size` bawaan (`default`, `sm`, `lg`, `icon`) punya padding dan ukuran teks sendiri (mis. `lg` = `px-6`). Tulis nilai override setiap size yang dipakai, lalu hitung anggaran lebar dengan nilai itu.

## Form & perilaku mobile
- **Form GET pencarian/filter:** `<form method="get">` hanya mengirim field di dalamnya. Filter lain yang aktif (status, toggle) harus ikut sebagai `<input type="hidden">`, atau pencarian akan menghapusnya.
- **Keyboard virtual vs elemen `fixed` bawah:** di Chrome Android, dock/tombol `fixed bottom-0` tertutup keyboard saat mengetik. Untuk input yang sering dipakai, tulis `enterKeyHint` + Enter mengirim form, atau `<meta name="viewport" content="..., interactive-widget=resizes-content">`.
- **Angka besar:** field nominal uang ditampilkan dengan pemisah ribuan saat mengetik (`inputmode="numeric"`), nilai yang dikirim tetap angka polos.
- **Validasi "nonaktif sampai valid"** butuh validasi klien; kalau dokumen menyebut tidak ada validasi saat mengetik, tulis kondisi nonaktif yang sederhana (mis. field kosong).

## Font
- `next/font/google` butuh `subsets` (mis. `['latin']`) dan `variable` yang dipetakan ke `--font-sans` / `--font-mono` di `@theme`. Sebutkan weight yang di-load; weight yang tidak di-load akan disintesis browser.

## Anggaran lebar di 360px (wajib untuk setiap baris berisi beberapa elemen)
Lebar tersedia = 360 − 2 × padding halaman − 2 × (padding + border) setiap kontainer pembungkus. Hati-hati dengan padding ganda: baris list yang punya `px-4` sendiri di dalam halaman ber-padding 16px hanya punya 296px; kalau ingin 328px, tulis list-nya full-bleed (`-mx-4`).
Contoh: halaman 16px, kartu padding 16px + border 1px → 360 − 32 − 34 = **294px**.
Untuk baris berisi beberapa elemen (slot OTP, pager, grup tombol, chip filter, baris angka), tulis hitungannya di spesifikasi komponen: jumlah elemen × lebar minimum + jarak ≤ lebar tersedia. Lebar minimum tombol = padding kiri-kanan + panjang label (±9px per karakter untuk 16px/600). Kalau tidak muat: pecah baris, singkatkan label, atau ganti ikon + `aria-label`. Setiap elemen yang bisa disentuh tetap ≥ 44px.

## Elemen tetap & tumpukan
Kalau ada lebih dari satu elemen `fixed`/`sticky` (header, dock, FAB, toast, banner offline), tulis tabel urutan tumpuk: posisi, tinggi, `z-index`, dan bagaimana mereka tidak saling menutupi (termasuk `env(safe-area-inset-*)`).
