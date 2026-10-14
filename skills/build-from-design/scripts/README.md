# Script build-from-design

Empat script bantu untuk memverifikasi UI hasil build terhadap DESIGN.md. Hanya Python 3.9 (pustaka standar + Pillow) dan JS browser biasa, kecuali `shoot.mjs` yang butuh `playwright-core` (atau memakai jalur cadangan Chrome headless).

## 1. extract-tokens.py

Membaca DESIGN.md (format design-maker) dan menulis tokens.json.

```
python3 extract-tokens.py DESIGN.md --out tokens.json
```

- Warna dari tabel 2.1 (kolom Light dan Dark; sel pasangan `a` / `b` dengan nilai `#x / #y` didukung; hex, rgb, hsl, oklch). Kalau 2.1 kosong, dicoba dari blok CSS di 2.8.
- Tipografi dari 2.4: `size`, `lineHeight`, `weight`, plus angka `sizePx`, `sizeMaxPx` (untuk clamp), `lineHeightPx`, `lineHeightRatio`.
- Font dari baris `**Font ...:**` di 2.4, fallback dari teks `fallback ...`.
- `radius-*` dan `shadow-*` dari tabel 2.6.
- Bagian yang tidak terbaca: peringatan di stderr dan di kunci `warnings`, script lanjut.

## 2. token-audit.js

Snippet browser. Memeriksa halaman yang sedang terbuka: warna di luar token, font di luar desain, `fontSizeNotInScale` (ukuran tidak ada di token tipografi) dan `lineHeightMismatch` (ukuran cocok token tapi line-height tidak; `expected` memuat nilai yang diharapkan), kontras WCAG, target sentuh dua tingkat, overflow horizontal, radius di luar token.

1. Suntik token: `window.__DESIGN_TOKENS = <isi tokens.json>;` (jalankan sebagai satu eksekusi sendiri).
2. Jalankan isi `token-audit.js` lewat alat "execute JavaScript" atau tempel di DevTools. Nilai terakhirnya string JSON ringkas (`summary` berisi hitungan, tiap bagian memuat 20 pelanggar teratas dengan selector). Aman dijalankan berulang.
3. Opsional: `window.__AUDIT_MODE = 'light' | 'dark' | 'both'`. Bawaan: light bila token tidak punya nilai Dark.

Pintasan suntik token: salin `tokens.json` sementara ke folder `public/` dev server project, lalu di halaman jalankan `window.__DESIGN_TOKENS = await (await fetch('/tokens.json')).json();` dan sesudahnya isi `token-audit.js`. Hapus `public/tokens.json` setelah selesai supaya tidak ikut ter-commit.

Cara membaca: `colorsOffToken` dengan `nearest.dE` kecil (sekitar 3 sampai 8) biasanya salah ketik hex atau token yang tidak dipakai; `fromAlpha: true` berarti warnanya hasil campuran transparansi, periksa manual. Entri kontras dengan `opacity` kurang dari 1 mungkin hanya keadaan animasi sementara.

Batasan: pseudo-element, SVG, dan latar gradien/gambar tidak dianalisis (kontras di atasnya dilewati dan dihitung di `skippedUnknownBg`). 

Target sentuh dilaporkan dua tingkat: `targetsBelow24` (gagal WCAG 2.2 AA 2.5.8: lebih kecil dari 24px dan lingkaran 24px di tengahnya menyentuh target lain; pengecualian jarak dihitung kira-kira dari kotak target) dan `targetsBelow44` (di bawah saran 44px, hanya informasi, bukan kegagalan, tidak termasuk yang sudah masuk tingkat 24). Setiap entri memuat lebar dan tinggi terpisah serta `fails` (`width`, `height`, atau `both`) yang menyebut dimensi mana yang kurang. Dikecualikan: tautan inline di tengah teks (display inline dengan teks tetangga), elemen tersembunyi, dan `aria-hidden`.

## 3. shoot.mjs

Screenshot via Node + Playwright, supaya build dan preview dipotret dengan cara yang sama.

```
node shoot.mjs <url> <out.png> --width 390 --height 844 [--full] [--reduced-motion] [--wait 1500] [--selector "#screen-x"] [--scroll-to "#id"] [--dpr 1]
```

- Bawaan emulasi `prefers-reduced-motion: reduce` (keadaan akhir, tanpa noise timing animasi); `--no-reduced-motion` untuk mematikan. Lalu menunggu font siap dan `document.getAnimations()` selesai, maksimal `--wait` ms (animasi berulang tak hingga diabaikan).
- `--selector` memotret satu elemen; `--scroll-to` menggulir elemen ke tengah layar.
- Butuh `playwright` atau `playwright-core` yang bisa ditemukan dari folder kerja: `npm i -D playwright-core` (memakai Chrome sistem di /Applications/Google Chrome.app, tanpa unduh browser). Kalau tidak ada, script mencetak petunjuk pasang dan perintah cadangan Chrome headless (`--headless=new --screenshot --window-size=W,H --force-prefers-reduced-motion`). Chrome headless bisa membatasi lebar jendela kecil, jadi cek ukuran PNG hasilnya.

## 4. compare-screens.py

```
python3 compare-screens.py built.png reference.png --out diff.png [--threshold 0.15]
```

Referensi diskala ke lebar built, dipotong ke tinggi terpendek, lalu dibuat komposit `built | reference | diff`. Mencetak selisih rata-rata, persentase piksel beda lebih dari 10%, warna dominan kedua gambar, dan cek regional: gambar dibagi grid petak (sekitar 150px), tiap petak dibandingkan kepadatan kontennya. Petak yang kontennya hilang atau berlebih (mis. blok transkrip kosong di build) dan petak dengan selisih besar dicetak dengan baris/kolom dan kotak pikselnya, serta diberi garis merah atau oranye di komposit. Verdict (mirip, berbeda sedang, berbeda jauh) adalah yang terburuk antara global dan regional. Selisih piksel tetap sinyal kasar: data contoh vs data nyata, font yang belum termuat, dan pergeseran layout ikut menaikkannya. Nilai komposit dengan mata, jangan putuskan dari angka saja.

Resep perbandingan:
1. Potret build dan preview dengan `shoot.mjs` (reduced motion bawaan, lebar sama, mis. 390 untuk mobile dan 1280 untuk desktop).
2. Layar preview dibuka sendirian lewat `design-preview.html?screen=<id>` (id dari field Id preview di DESIGN.md), bukan seluruh halaman preview. Untuk file lokal pakai URL absolut `file:///...` atau sajikan foldernya lewat server lokal.
3. Jalankan `compare-screens.py`, buka komposit, perbaiki petak bertanda dulu.

## Putaran kerja umum

1. `extract-tokens.py DESIGN.md --out tokens.json`
2. Build halaman sesuai DESIGN.md.
3. Buka halaman di browser (viewport sama dengan preview).
4. Suntik token, jalankan `token-audit.js`, catat pelanggar.
5. `shoot.mjs` untuk halaman build dan layar yang sama di `design-preview.html?screen=<id>`.
6. `compare-screens.py` lalu lihat komposit.
7. Perbaiki kode (token dulu, baru komponen), ulangi dari langkah 3 sampai audit bersih dan komposit mirip.
