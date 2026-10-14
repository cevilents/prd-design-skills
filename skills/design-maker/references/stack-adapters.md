# Adaptor Stack: Cara Mengungkapkan Token per Teknologi

Baca file ini kalau stack di PRD BUKAN Next.js + Tailwind v4 + shadcn/ui, atau kalau perlu ringkasan stack itu. Untuk shadcn/ui, jebakan lengkap ada di `references/stack-shadcn.md`.

Tujuan: bagian 2.8 (Implementasi Token), aturan 9 dan 10 di SKILL.md, dan tabel override di 3.1 tetap terisi lengkap walau stack-nya lain. Nilai token (hex, skala tipografi, spacing, radius, elevasi, gradien, motion) SAMA di semua stack; yang berbeda hanya cara menulisnya. Pakai satu adaptor per proyek. Kalau PRD memakai lebih dari satu (mis. web + mobile), tulis satu blok 2.8 per target.

Penanda: `[?]` = belum diverifikasi ke dokumentasi resmi, cek ulang sebelum dipakai sebagai fakta.

Aturan umum semua adaptor:
- Warna selalu ditulis hex penuh di blok token (6 digit, atau 8 digit hanya kalau transparansi memang token). Tulis juga rasio kontras seperti di bagian 2.
- Di atas setiap blok kode tulis "Ganti seluruh isi `<file>`" atau "Gabungkan dengan `<file>`", sama seperti aturan 9.
- Setiap token di tabel bagian 2 muncul di blok kode dengan nama yang sama (atau pemetaan nama yang ditulis eksplisit).
- Motion: tulis ekuivalen reduced motion yang BENAR-BENAR dipakai stack itu, bukan hanya `prefers-reduced-motion`.
- Satuan: web memakai px/rem, iOS memakai pt, Android dan Flutter memakai dp. Di 360 lebar layar angka yang sama dipakai sebagai dp/pt.

---

## Cara memilih adaptor

Urutan deteksi: (1) kolom Tech Stack di PRD, (2) file proyek kalau ada, (3) tanya user dengan default.

| Sinyal | Adaptor |
|---|---|
| `package.json` punya `next` + `tailwindcss` v4 (`@tailwindcss/postcss`, atau integrasi bundler lain seperti Turbopack/Vite) + `components.json` | 1. Tailwind v4 + shadcn/ui |
| `tailwind.config.js` / `.ts` ada, `tailwindcss` `^3.x` di deps | 2. Tailwind v3 |
| Hanya `index.html` + `.css`, tanpa bundler | 3. HTML/CSS polos |
| `nuxt.config.ts`, atau `vue` + `vite` di deps | 4. Vue 3 / Nuxt |
| `svelte.config.js`, `@sveltejs/kit` | 5. Svelte / SvelteKit |
| `app.json` dengan `expo`, `react-native` di deps | 6. React Native / Expo |
| `pubspec.yaml` | 7. Flutter |
| `*.xcodeproj`, `Package.swift`, `*.swift` | 8. SwiftUI |
| Tidak ada yang cocok, atau PRD menyebut stack yang tidak ada di daftar (Android Compose, Angular, Qwik, dsb.) | 9. Lain / tidak diketahui |

Aturan tambahan:
- `tailwindcss` v4 ditandai oleh `@import "tailwindcss"` di CSS dan tidak adanya `tailwind.config.*` (config JS tidak dibaca otomatis di v4, harus dimuat dengan `@config`).
- NativeWind v4 memerlukan Tailwind v3 (`^3.4.17`), jadi proyek Expo + NativeWind memakai pola adaptor 2 untuk `tailwind.config.js`, bukan adaptor 1. NativeWind v5 masih rilis kandidat saat riset ini ditulis; cek versinya dulu.
- Kalau PRD kosong soal stack dan tidak ada proyek: default ke adaptor 1 dan catat di 1.4 Perlu Konfirmasi.
- Kalau hanya "aplikasi mobile": tanya (React Native/Expo vs Flutter vs native). Default ke Expo kalau tim web, Flutter kalau tim tanpa latar web.

---

## 1. Tailwind CSS v4 + shadcn/ui (React / Next.js)

Rujukan utama: `references/stack-shadcn.md` (wajib dibaca). Ringkasan:

1. **Token.** `:root { --background: #...; ... --radius: 0.5rem; }`, lalu `@theme inline { --color-background: var(--background); }`. Tipografi: `--text-<nama>`, `--text-<nama>--line-height`, `--text-<nama>--font-weight`. Elevasi: `--shadow-<nama>`; gradien dan motion sebagai variabel biasa (`--gradient-hero`, `--duration-base`, `--ease-out-expo`). Ring dan outline solid.
2. **Font.** `next/font/google` dengan `subsets` dan `variable` ke `--font-sans`/`--font-mono`; sebut weight yang di-load.
3. **Motion.** `motion` (Framer Motion) atau View Transitions; reduced motion: `useReducedMotion()` / `MotionConfig reducedMotion="user"` dan `motion-reduce:` di Tailwind.
4. **A11y.** Fokus: `focus-visible:outline-2` + buang `outline-none`; target sentuh 44px; teks 16px+; `rem` supaya ikut ukuran font browser; `aria-*` dari Radix.
5. **Override.** Tabel 3.1: Button h-9 → h-11, Input h-9 → h-11, Card `rounded-xl shadow-sm py-6` → nilai token, Sheet/Dialog `bg-background` → token, Switch, Toggle, Badge, Sonner.
6. **Jebakan.** Lihat `stack-shadcn.md`: light saja (`@custom-variant dark`), Sonner `theme="light"`, `outline-none` v4, `ring-ring/50` transparan, anggaran lebar 360px, tabel urutan elemen `fixed`.

Perbedaan penting v4 (resmi): `@import "tailwindcss"` menggantikan `@tailwind base/components/utilities`; `shadow-sm` lama menjadi `shadow-xs`, `shadow` lama menjadi `shadow-sm` (juga `rounded`, `blur`); `ring` default 1px dan `currentColor`; `border` default `currentColor`; `outline-none` jadi `outline-hidden` kalau mau perilaku lama; `bg-[--x]` jadi `bg-(--x)`; `!` ditulis di akhir (`flex!`). Sumber: https://tailwindcss.com/docs/upgrade-guide

---

## 2. Tailwind CSS v3 (`tailwind.config.js` + `theme.extend`)

Dipakai kalau proyek belum migrasi, atau NativeWind v4 untuk Expo.

**1. Token.** Gabungkan ke `tailwind.config.js`; gunakan `extend` supaya skala bawaan tidak hilang, kecuali PRD memang mengganti seluruh skala (maka taruh di `theme` langsung dan tulis alasannya).

```js
// Gabungkan dengan tailwind.config.js
module.exports = {
  content: ['./app/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  darkMode: 'class', // light saja: jangan pernah pasang kelas "dark"
  theme: {
    extend: {
      colors: {
        background: '#FBF8F3',
        foreground: '#1B1A17',
        primary: { DEFAULT: '#0F5C4D', hover: '#0B4A3E', foreground: '#FFFFFF' },
      },
      fontFamily: { sans: ['var(--font-sans)', 'system-ui', 'sans-serif'] },
      fontSize: {
        display: ['1.75rem', { lineHeight: '2.125rem', fontWeight: '700' }],
        body: ['1rem', { lineHeight: '1.5rem', fontWeight: '400' }],
      },
      spacing: { 18: '4.5rem' },
      borderRadius: { sm: '6px', md: '8px', xl: '28px' },
      boxShadow: {
        1: '0 1px 2px rgb(27 26 23 / 0.08), 0 1px 1px rgb(27 26 23 / 0.04)',
        3: '0 12px 32px rgb(27 26 23 / 0.14), 0 4px 8px rgb(27 26 23 / 0.08)',
      },
      backgroundImage: {
        'gradient-hero': 'radial-gradient(120% 80% at 20% 0%, #2FA58E 0%, #0F5C4D 45%, #082B24 100%)',
      },
      transitionDuration: { fast: '120ms', base: '220ms', slow: '420ms' },
      transitionTimingFunction: { 'out-expo': 'cubic-bezier(0.16, 1, 0.3, 1)' },
      keyframes: { 'rise-in': { from: { opacity: '0', transform: 'translateY(8px)' }, to: { opacity: '1', transform: 'none' } } },
      animation: { 'rise-in': 'rise-in 220ms cubic-bezier(0.16, 1, 0.3, 1) both' },
    },
  },
  plugins: [require('tailwindcss-animate')],
}
```

Kalau token harus dipakai juga di luar Tailwind (CSS biasa, JS), tulis sebagai CSS variables di `:root` dan rujuk dari config: `primary: 'rgb(var(--primary) / <alpha-value>)'` (nilai variabel berupa kanal `15 92 77`). Itu perlu kalau mau modifier opasitas (`bg-primary/50`) tetap jalan; hex langsung tidak mendukung `<alpha-value>`.

**2. Font.** Sama dengan v4 (`next/font`, atau `@fontsource` / `<link>`), dipetakan lewat `fontFamily` di config.

**3. Motion.** Varian `motion-reduce:` dan `motion-safe:` tersedia: `motion-safe:animate-rise-in`, `motion-reduce:transition-none`. Library `motion` / `tailwindcss-animate` seperti adaptor 1.

**4. A11y.** Sama dengan adaptor 1. Perhatikan default v3: `outline-none` = outline transparan 2px (tetap menyisakan outline di mode kontras tinggi), `ring` = 3px biru (`blue-500`).

**5. Override.** shadcn/ui versi lama (v3) memakai warna `hsl(var(--x))` dengan kanal HSL; kalau token PRD hex, tulis konversinya atau ganti pola ke hex langsung dan catat bahwa komponen shadcn yang memakai `hsl(var(--primary))` harus diubah.

**6. Jebakan.**
- `darkMode`: tanpa `darkMode: 'class'`, kelas `dark:` mengikuti mode gelap sistem (default `media`). Untuk light saja pasang `'class'` dan jangan pernah menambah kelas `dark`.
- Perbedaan dengan v4 yang sering membuat spesifikasi salah bangun: border default `gray-200` (bukan `currentColor`), `ring` 3px biru, `shadow-sm` = shadow kecil lama, `@tailwind base;` bukan `@import "tailwindcss"`, `theme()` dan `resolveConfig` masih ada.
- `content` harus mencakup semua folder komponen; kelas yang dirangkai string dinamis (`` `bg-${x}` ``) tidak terdeteksi.
- Kunci angka di `spacing`/`boxShadow` (`1`, `3`) valid, tetapi nama `DEFAULT` menggantikan utilitas tanpa akhiran (`shadow`).
- Jangan mencampur v3 dan v4: plugin `tailwindcss-animate` untuk v3, `tw-animate-css` untuk v4.
- `fontSize` tuple dengan `fontWeight` didukung versi 3 yang baru; versi lama hanya `lineHeight` dan `letterSpacing` `[?]`.

---

## 3. HTML / CSS polos (tanpa framework)

**1. Token.** Satu file `tokens.css` (atau blok `:root` di `<style>`), dipakai lewat `var()`. Ini juga format yang dipakai `design-preview.html`.

```css
/* Ganti seluruh isi tokens.css */
:root {
  color-scheme: light;
  --color-bg: #FBF8F3;
  --color-fg: #1B1A17;
  --color-primary: #0F5C4D;
  --font-sans: "Inter", system-ui, sans-serif;
  --text-body: 1rem/1.5rem var(--font-sans);
  --space-1: 4px; --space-2: 8px; --space-4: 16px;
  --radius-md: 8px;
  --shadow-1: 0 1px 2px rgb(27 26 23 / 0.08), 0 1px 1px rgb(27 26 23 / 0.04);
  --gradient-hero: radial-gradient(120% 80% at 20% 0%, #2FA58E 0%, #0F5C4D 45%, #082B24 100%);
  --duration-fast: 120ms; --duration-base: 220ms; --duration-slow: 420ms;
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
}
```

**2. Font.** Self-host dengan `@font-face` (`font-display: swap`, `unicode-range` kalau perlu, `font-weight` rentang untuk variable font) dan `<link rel="preload" as="font" crossorigin>` untuk font utama; atau Google Fonts dengan `<link rel="preconnect">` + `display=swap`. Sebut weight yang di-load.

```css
@font-face {
  font-family: "Inter";
  src: url("/fonts/Inter-Variable.woff2") format("woff2");
  font-weight: 100 900;
  font-display: swap;
}
```

**3. Motion.** CSS `transition`/`@keyframes` dengan token; View Transitions API untuk transisi halaman (fallback tanpa animasi).

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; }
}
```
Untuk JS: `matchMedia('(prefers-reduced-motion: reduce)').matches` dan dengarkan `change`.

**4. A11y.** `:focus-visible { outline: 2px solid var(--color-primary); outline-offset: 2px; }`; tombol/tautan min 44×44px; ukuran font `rem`; HTML semantik (`button`, `nav`, `label`); `lang="id"`; `<meta name="viewport" content="width=device-width, initial-scale=1">` (jangan `user-scalable=no`).

**5. Override.** Tidak ada library: tabel 3.1 tulis "elemen native" dan kelas CSS-nya; reset (`box-sizing`, margin, `button` font) ditulis di blok token.

**6. Jebakan.**
- `rem` mengikuti ukuran font browser; kalau spesifikasi dalam px, tulis apakah dikonversi (16px = 1rem).
- Variabel CSS tidak bisa dipakai di media query (`@media (min-width: var(--bp))` tidak jalan); tulis breakpoint sebagai angka literal.
- `prefers-reduced-motion` di reset di atas tidak mematikan animasi yang digerakkan JS atau video; tulis cabang JS-nya.
- Input 16px+ supaya iOS Safari tidak zoom saat fokus.
- `100vh` di mobile salah karena bar alamat; pakai `100dvh`.
- Urutan `@font-face` dan `font-display: swap` menyebabkan lompatan layout; sebut `size-adjust` fallback atau terima lompatan.

---

## 4. Vue 3 / Nuxt (+ Tailwind, Nuxt UI atau shadcn-vue)

Pecah dua jalur, tergantung PRD.

**A. Nuxt UI (v3 ke atas, berbasis Tailwind v4)**

**1. Token.** `app/assets/css/main.css` dengan `@import "tailwindcss"; @import "@nuxt/ui";`. Warna kustom lewat `@theme static` (wajib `static` agar variabel selalu ada; semua shade 50 sampai 950 wajib didefinisikan). Lalu pilih warna semantik di `app/app.config.ts`. Sumber: https://ui.nuxt.com/docs/getting-started/theme/design-system

```css
/* Gabungkan dengan app/assets/css/main.css */
@import "tailwindcss";
@import "@nuxt/ui";
@theme static {
  --color-brand-50: #E8F6F2; /* ... lengkap sampai 950 */
  --color-brand-500: #0F5C4D;
  --color-brand-950: #04201B;
  --font-sans: "Inter", system-ui, sans-serif;
  --radius-md: 8px;
}
```
```ts
// Gabungkan dengan app/app.config.ts
export default defineAppConfig({ ui: { colors: { primary: 'brand', neutral: 'stone' } } })
```
Kalau mau menambah warna semantik baru (mis. `tertiary`), daftarkan di `nuxt.config.ts` `ui.theme.colors`, lalu pasang di `app.config.ts`. Variabel `--ui-*` (latar, teks, border, radius semantik Nuxt UI) boleh ditimpa di `:root`; nama persis perlu dicek di dokumentasi versi yang dipakai `[?]`.

**B. shadcn-vue**: sama dengan adaptor 1 (`:root`/`.dark`, `@theme inline`, `@custom-variant dark (&:is(.dark *));`; file CSS ditentukan field `css` di `components.json`). Sumber: https://www.shadcn-vue.com/docs/theming

**2. Font.** Nuxt: modul `@nuxt/fonts` membaca `font-family` di CSS dan memuat font otomatis; default weight 400 dan 700, jadi sebut weight lain di konfigurasi `fonts` (nama opsi `[?]`). Vue + Vite polos: `@fontsource-variable/<nama>` diimpor di `main.ts`. Sumber: https://fonts.nuxt.com/get-started/installation

**3. Motion.** `<Transition>` / `<TransitionGroup>` bawaan Vue (kelas `*-enter-active` pakai token durasi), `pageTransition` / `layoutTransition` di Nuxt, atau `motion-v` untuk spring `[?]`. Reduced motion: utamakan CSS `@media (prefers-reduced-motion: reduce)` (aman untuk SSR); versi JS: `usePreferredReducedMotion()` dari VueUse `[?]`.

**4. A11y.** Nuxt UI memakai Reka UI di bawahnya `[?]` sehingga ARIA dan keyboard sudah ada; tetap tulis ring fokus, tinggi 44px, `aria-label` untuk tombol ikon (`<UButton icon="..." aria-label="Tutup" />`).

**5. Override.** Nuxt UI: tulis di tabel kolom "slot / varian yang diubah", bukan kelas; override lewat `app.config.ts` `ui: { button: { slots: { base: '...' }, variants: {...}, defaultVariants: {...} } }` `[?]`. shadcn-vue: seperti adaptor 1 (file komponen disalin ke proyek dan diedit).

**6. Jebakan.**
- `nuxt.config.ts` `ui.theme.colors` (daftar nama warna semantik) BERBEDA dari `app.config.ts` `ui.colors` (pemetaan nama ke palet). Salah tempat = warna diam-diam diabaikan.
- Warna kustom tanpa semua shade 50 sampai 950 membuat varian (hover, soft, subtle) memakai shade yang hilang.
- `@theme` tanpa `static` di Nuxt UI membuat variabel yang tidak dipakai di-tree-shake, sehingga `var(--color-brand-500)` kosong di runtime.
- Light saja: Nuxt UI/shadcn-vue memakai color mode (`@nuxtjs/color-mode`); tulis `colorMode: { preference: 'light' }` di `nuxt.config.ts` dan hilangkan toggle `[?]`.
- `<style scoped>` tidak menembus komponen anak; pakai `:deep()` atau slot/props, jangan menimpa lewat selektor global.
- Hydration mismatch: jangan baca `matchMedia`/`window` saat setup SSR; gunakan CSS media query atau `onMounted`. Komponen overlay Nuxt UI (toast, tooltip) memerlukan pembungkus `<UApp>` `[?]`.

---

## 5. Svelte / SvelteKit (+ Tailwind, shadcn-svelte)

**1. Token.** Tailwind v4 lewat `@tailwindcss/vite`. File CSS global (di versi baru `src/routes/layout.css`, sebelumnya `src/app.css`, ikuti `components.json`): `:root`/`.dark`, lalu `@theme inline` memetakan `--color-*`. Warna kustom: tiga langkah (variabel di `:root`, petakan di `@theme inline`, pakai utilitas). Sumber: https://www.shadcn-svelte.com/docs/theming

```css
/* Gabungkan dengan src/routes/layout.css */
:root { --background: #FBF8F3; --primary: #0F5C4D; --radius: 0.5rem; }
@theme inline { --color-background: var(--background); --color-primary: var(--primary); }
```
Tanpa shadcn-svelte: pola yang sama atau CSS variables polos (adaptor 3). Gradien, elevasi, motion sebagai variabel biasa.

**2. Font.** `@fontsource-variable/<nama>` diimpor di layout root, atau `<link>` di `src/app.html`. Sebut weight yang di-load.

**3. Motion.** `svelte/transition` (`fade`, `fly`, `slide`, `scale`, `crossfade`) dengan `duration` token, `animate:flip` untuk reorder, `Spring` dan `Tween` dari `svelte/motion` (sejak Svelte 5.8.0). `svelte/easing` hanya punya fungsi bawaan; cubic-bezier kustom (mis. `0.16, 1, 0.3, 1`) harus ditulis sebagai fungsi atau dipakai lewat CSS. Reduced motion TIDAK otomatis. Pakai `prefersReducedMotion` dari `svelte/motion` (sejak 5.7.0, baca `.current`):

```svelte
<script>
  import { fly } from 'svelte/transition';
  import { prefersReducedMotion } from 'svelte/motion';
</script>
<div in:fly={{ y: prefersReducedMotion.current ? 0 : 8, duration: prefersReducedMotion.current ? 0 : 220 }}>...</div>
```
Transisi antar-rute: `onNavigate` + `document.startViewTransition` `[?]`.

**4. A11y.** shadcn-svelte memakai Bits UI `[?]` (ARIA dan keyboard sudah ada). Svelte memberi peringatan a11y saat kompilasi (label, `alt`, klik di `div`); anggap peringatan itu blocker. Fokus, 44px, `aria-label` seperti adaptor 1.

**5. Override.** Sama dengan adaptor 1 (komponen disalin ke `$lib/components/ui`, diedit). Toast: `svelte-sonner` `[?]`; aturan Sonner di `stack-shadcn.md` berlaku sebagian (tema, posisi, offset, `aria-live`).

**6. Jebakan.**
- Reduced motion tidak otomatis; setiap `transition:`/`in:`/`out:` butuh penanganan eksplisit (durasi 0 atau fade pendek).
- Transisi bersifat lokal secara default (hanya jalan saat blok langsungnya dibuat/dihapus, bukan induknya); untuk halaman/rute tulis `|global` bila perlu `[?]`.
- `animate:flip` hanya jalan di item langsung `{#each}` yang ber-key; tulis `(item.id)`.
- Svelte 5: state dengan runes (`$state`, `$derived`, `$props`); kode contoh Svelte 4 (`export let`, `$:`) salah untuk proyek runes.
- Gaya komponen di-scope; kelas Tailwind aman, tetapi selektor `.parent .child` ke komponen anak butuh `:global()`.
- SSR: `prefersReducedMotion.current` di server tidak punya nilai pengguna; hindari menyetel state awal dari sana yang mengubah markup (hydration).

---

## 6. React Native / Expo

**1. Token.** Dua pola; pilih satu dan tulis alasannya.

(a) Objek tema + `StyleSheet` (default, tanpa dependensi):
```ts
// Buat file theme/tokens.ts
export const color = { bg: '#FBF8F3', fg: '#1B1A17', primary: '#0F5C4D', onPrimary: '#FFFFFF' } as const
export const space = { 1: 4, 2: 8, 3: 12, 4: 16, 6: 24 } as const
export const radius = { sm: 6, md: 8, xl: 28 } as const
export const text = {
  body: { fontFamily: 'Inter_400Regular', fontSize: 16, lineHeight: 24 },
  display: { fontFamily: 'Inter_700Bold', fontSize: 28, lineHeight: 34 },
} as const
export const duration = { fast: 120, base: 220, slow: 420 } as const
export const shadow1 = {
  shadowColor: '#1B1A17', shadowOffset: { width: 0, height: 1 }, shadowOpacity: 0.08, shadowRadius: 2, elevation: 1,
} as const
```
(b) NativeWind v4 (Tailwind v3): token di `tailwind.config.js` seperti adaptor 2, ditambah `presets: [require('nativewind/preset')]`, `global.css`, `babel`, dan `metro.config.js` `withNativeWind`. Sumber: https://www.nativewind.dev/docs/getting-started/installation

Gradien: `expo-linear-gradient` (`<LinearGradient colors={[...]} start end />`); radial tidak ada bawaan (pakai `react-native-svg` `RadialGradient`). Teks bergradien: `@react-native-masked-view/masked-view`. Elevasi: iOS memakai `shadow*`, Android memakai `elevation` (satu lapis, abu-abu sistem); bayangan berlapis memerlukan prop `boxShadow` pada arsitektur baru RN `[?]` atau gambar/SVG. Tulis perbedaan ini di token elevasi.

**2. Font.** `expo-font`: hook `useFonts` (Android, iOS, web, jalan di Expo Go) atau config plugin `expo-font` di `app.json` (tertanam saat build, butuh development build). Google Fonts: paket `@expo-google-fonts/<nama>`. Tahan splash dengan `SplashScreen.preventAutoHideAsync()` sampai `loaded || error`. Sumber: https://docs.expo.dev/develop/user-interface/fonts/
```tsx
const [loaded, error] = useFonts({ Inter_400Regular, Inter_700Bold })
if (!loaded && !error) return null
```
Setiap weight adalah NAMA FAMILY terpisah (`Inter_400Regular`, `Inter_700Bold`); jangan mengandalkan `fontWeight` pada font kustom.

**3. Motion.** `react-native-reanimated`: `withTiming(v, { duration: 220, easing: Easing.bezier(0.16, 1, 0.3, 1) })`, `withSpring(v, { stiffness: 400, damping: 30 })`, layout animation (`FadeInDown.duration(220)`). Reduced motion (resmi): opsi `reduceMotion: ReduceMotion.System` per animasi (default; animasi loncat ke nilai akhir), `.reduceMotion(...)` pada entering animation (exiting dan shared transition dihilangkan), `<ReducedMotionConfig mode={ReduceMotion.System} />` untuk satu pengaturan global, dan `useReducedMotion()` untuk memilih animasi pengganti (fade). Catatan: `useReducedMotion()` membaca nilai saat aplikasi mulai dan tidak memicu render ulang kalau pengguna mengubahnya. Untuk perubahan langsung: `AccessibilityInfo.addEventListener('reduceMotionChanged', ...)` `[?]`. Sumber: https://docs.swmansion.com/react-native-reanimated/docs/guides/accessibility/

**4. A11y.** Prop resmi: `accessible`, `accessibilityLabel`, `accessibilityHint`, `accessibilityRole` (`button`, `header`, `switch`, `checkbox`, ...), `accessibilityState` (`disabled`, `selected`, `checked`, `busy`, `expanded`); `role` dan `aria-label` adalah alternatif dan `role` lebih diutamakan (nilainya sedikit beda: `heading`, `img`). Sumber: https://reactnative.dev/docs/accessibility. Target sentuh: 44pt iOS / 48dp Android; pakai `hitSlop` atau `minHeight`. Skala font: `allowFontScaling` (default true) dan `maxFontSizeMultiplier` `[?]`; tulis batas (mis. 1.3) untuk teks yang rusak layoutnya, jangan mematikan scaling. Fokus keyboard/switch control: `Pressable` + `focusable`; di mobile fokus tampak lewat state `pressed`/ripple, tulis ekuivalennya.

**5. Override.** Tidak ada library bawaan; kolom Library di 3.1 = "Komponen RN: `Pressable`, `TextInput`, `Switch`, `FlatList`, `Modal`". Kalau pakai library UI (React Native Reusables, Tamagui, Gluestack, React Native Paper), tulis default library → nilai token seperti shadcn.

**6. Jebakan.**
- Tidak ada CSS variables, `em`, `calc`, `hover`, gradien CSS, atau kelas `dark:` bawaan; light saja: `"userInterfaceStyle": "light"` di `app.json`.
- Android: `fontWeight` diabaikan untuk font kustom; `elevation` tidak punya warna/offset; `shadow*` hanya iOS.
- iOS: `overflow: 'hidden'` memotong bayangan; pisahkan view pembungkus bayangan dan view isi yang memotong.
- `lineHeight` absolut (px), bukan rasio; `letterSpacing` dalam px/dp, bukan `em`.
- Safe area: `react-native-safe-area-context` (`SafeAreaProvider`, `useSafeAreaInsets`); tulis inset untuk header, tab bar, FAB. Keyboard: `KeyboardAvoidingView` `behavior` berbeda per `Platform.OS`.
- Hex 8 digit di RN adalah `#RRGGBBAA` (alpha di akhir), berbeda dengan Android native; tulis warna transparan sebagai `rgba()`.
- `Platform.select` dan `.ios.tsx` / `.android.tsx` untuk perbedaan; tulis perbedaan visual yang disengaja (ripple Android, haptic iOS), bukan membiarkannya acak.

---

## 7. Flutter (Material 3)

**1. Token.** `ThemeData` untuk token standar, `ThemeExtension` untuk token kustom (gradien, bayangan, durasi). Material 3 aktif secara default (`useMaterial3` default true; flag ini akan dihapus pada akhirnya). Sumber: https://api.flutter.dev/flutter/material/ThemeData/useMaterial3.html

```dart
// Buat lib/theme/app_theme.dart
import 'package:flutter/material.dart';

@immutable
class AppTokens extends ThemeExtension<AppTokens> {
  const AppTokens({required this.shadow1, required this.gradientHero, required this.durBase, required this.easeOut});
  final List<BoxShadow> shadow1;
  final Gradient gradientHero;
  final Duration durBase;
  final Curve easeOut;

  @override
  AppTokens copyWith({List<BoxShadow>? shadow1, Gradient? gradientHero, Duration? durBase, Curve? easeOut}) =>
      AppTokens(shadow1: shadow1 ?? this.shadow1, gradientHero: gradientHero ?? this.gradientHero,
          durBase: durBase ?? this.durBase, easeOut: easeOut ?? this.easeOut);

  @override
  AppTokens lerp(ThemeExtension<AppTokens>? other, double t) => this; // token non-interpolasi: kembalikan this
}

final appTheme = ThemeData(
  useMaterial3: true,
  colorScheme: const ColorScheme(
    brightness: Brightness.light,
    primary: Color(0xFF0F5C4D), onPrimary: Color(0xFFFFFFFF),
    secondary: Color(0xFFB8860B), onSecondary: Color(0xFFFFFFFF),
    error: Color(0xFFB3261E), onError: Color(0xFFFFFFFF),
    surface: Color(0xFFFBF8F3), onSurface: Color(0xFF1B1A17),
  ),
  textTheme: const TextTheme(
    bodyLarge: TextStyle(fontSize: 16, height: 24 / 16, fontWeight: FontWeight.w400),
    headlineMedium: TextStyle(fontSize: 28, height: 34 / 28, fontWeight: FontWeight.w700),
  ),
  extensions: <ThemeExtension<dynamic>>[
    AppTokens(
      shadow1: [BoxShadow(color: Color(0x141B1A17), blurRadius: 2, offset: Offset(0, 1))],
      gradientHero: const RadialGradient(center: Alignment(-0.6, -1), radius: 1.2,
          colors: [Color(0xFF2FA58E), Color(0xFF0F5C4D), Color(0xFF082B24)], stops: [0, 0.45, 1]),
      durBase: Duration(milliseconds: 220),
      easeOut: Cubic(0.16, 1, 0.3, 1),
    ),
  ],
);
// Pakai: Theme.of(context).extension<AppTokens>()!.shadow1
```
`ThemeExtension<T>` mensyaratkan `copyWith` dan `lerp` (resmi). `ColorScheme.fromSeed` membuat palet tonal baru dan TIDAK menjamin hex brand tepat; untuk hex persis pakai konstruktor `ColorScheme(...)` seperti di atas atau `fromSeed(...).copyWith(primary: ...)`. Spacing/radius: kelas `abstract final class Space { static const s4 = 4.0; ... }`, `BorderRadius.circular(8)`.

**2. Font.** Paket `google_fonts`: `GoogleFonts.interTextTheme(base)` atau `GoogleFonts.inter()`. Untuk rilis, bundel file font di `assets/google_fonts/` (nama file asli, daftarkan folder di `pubspec.yaml` bagian `assets:`, BUKAN bagian `fonts:`) supaya tidak mengunduh saat runtime. Alternatif tanpa paket: `flutter: fonts:` di `pubspec.yaml` dengan `family` dan `weight`. Sumber: https://pub.dev/packages/google_fonts. Mematikan fetch runtime lewat `GoogleFonts.config.allowRuntimeFetching = false` `[?]`.

**3. Motion.** Implicit: `AnimatedContainer`, `AnimatedOpacity`, `TweenAnimationBuilder` dengan `duration` + `curve` dari token; eksplisit: `AnimationController`; spring: `SpringSimulation`/`SpringDescription` atau paket `flutter_animate` `[?]`; transisi halaman: `PageRouteBuilder` / tema `pageTransitionsTheme`. Reduced motion: `MediaQuery.disableAnimationsOf(context)` (resmi; hanya membangun ulang saat properti itu berubah); jika true, pakai `Duration.zero` atau fade pendek. `MediaQuery.accessibleNavigationOf(context)` untuk pengguna pembaca layar.
```dart
final reduce = MediaQuery.disableAnimationsOf(context);
final d = reduce ? Duration.zero : tokens.durBase;
```

**4. A11y.** `Semantics(label:, button: true, ...)`, `MergeSemantics`, `ExcludeSemantics`, `Semantics(header: true)`. Target sentuh min 48×48dp (`kMinInteractiveDimension`; tombol Material memakai `MaterialTapTargetSize`). Fokus: `ThemeData.focusColor` + `FocusableActionDetector` untuk kontrol kustom. Skala font: `MediaQuery.textScalerOf(context)` (`TextScaler`, menggantikan `textScaleFactor` yang akan dihapus); batasi dengan `MediaQuery.withClampedTextScaling(minScaleFactor:, maxScaleFactor:)` atau `TextScaler.clamp(...)` pada subpohon yang rawan rusak. Sumber: https://api.flutter.dev/flutter/painting/TextScaler-class.html

**5. Override.** Kolom Library: widget Material (`FilledButton`, `OutlinedButton`, `TextField`/`InputDecorationTheme`, `Card`, `NavigationBar`, `BottomSheet`, `SnackBar`). Override lewat tema komponen: `filledButtonTheme`, `inputDecorationTheme`, `cardTheme`, `navigationBarTheme`, `bottomSheetTheme`, `snackBarTheme`; tulis "default M3 → nilai" (mis. FilledButton tinggi 40 → 48, radius stadion → 8).

**6. Jebakan.**
- `Color(0xRRGGBB)` salah: harus `0xFFRRGGBB` (alpha di depan); `0x141B1A17` = alpha 0x14.
- `TextStyle.height` adalah pengali (lineHeight / fontSize), bukan px; 24/16 = 1.5.
- Elevasi M3 memberi tint permukaan (`surfaceTintColor`) bukan hanya bayangan; untuk meniru bayangan token set `surfaceTintColor: Colors.transparent` dan `shadowColor`, atau gambar sendiri dengan `DecoratedBox(boxShadow: ...)`.
- M3 default ripple `InkSparkle` (Android) berbeda dari `InkRipple`; tulis `splashFactory` kalau ripple harus seragam.
- `ColorScheme` M3 punya banyak peran (`surfaceContainer*`, `outlineVariant`, `onSurfaceVariant`); peran yang tidak diisi diturunkan otomatis dan bisa menyimpang dari token. Tulis peran mana yang dipakai.
- Light saja: `themeMode: ThemeMode.light` dan jangan beri `darkTheme`.
- Overflow teks di 360dp dan textScaler 1.3: gunakan `Flexible`/`Expanded`, `maxLines` + `overflow`, bukan lebar tetap. Safe area: `SafeArea` / `MediaQuery.paddingOf`.

---

## 8. SwiftUI (iOS)

**1. Token.** Warna: asset catalog (`Colors.xcassets`, Any Appearance saja untuk light saja) atau ekstensi `Color`. Ukuran: `enum` dengan `static let`.
```swift
// Buat file DesignTokens.swift
import SwiftUI

extension Color {
    init(hex: UInt32, alpha: Double = 1) {
        self.init(.sRGB, red: Double((hex >> 16) & 0xFF) / 255, green: Double((hex >> 8) & 0xFF) / 255,
                  blue: Double(hex & 0xFF) / 255, opacity: alpha)
    }
    static let appBackground = Color(hex: 0xFBF8F3)
    static let appPrimary = Color(hex: 0x0F5C4D)
}

enum Space { static let s1: CGFloat = 4, s2: CGFloat = 8, s4: CGFloat = 16 }
enum Radius { static let md: CGFloat = 8, xl: CGFloat = 28 }
enum Motion {
    static let base = 0.22
    static let easeOutExpo = Animation.timingCurve(0.16, 1, 0.3, 1, duration: 0.22)
    static let snappy = Animation.spring(duration: 0.35, bounce: 0.15) // iOS 17+
}
extension View {
    func shadow1() -> some View {
        self.shadow(color: .black.opacity(0.08), radius: 1, x: 0, y: 1)
            .shadow(color: .black.opacity(0.04), radius: 0.5, x: 0, y: 1)
    }
}
let heroGradient = RadialGradient(colors: [Color(hex: 0x2FA58E), .appPrimary, Color(hex: 0x082B24)],
                                  center: .topLeading, startRadius: 0, endRadius: 500)
```
Light saja: `.preferredColorScheme(.light)` di root, atau `UIUserInterfaceStyle = Light` di Info.plist. Sudut: `RoundedRectangle(cornerRadius: 8, style: .continuous)`. Radius `.shadow` bukan padanan 1:1 dengan `blur` CSS; kira-kira blur CSS = 2 × radius SwiftUI `[?]`, tulis nilai SwiftUI langsung di spesifikasi.

**2. Font.** Tambah file `.ttf/.otf` ke target, daftarkan di Info.plist `UIAppFonts` (Fonts provided by application), pakai nama PostScript. Untuk Dynamic Type SELALU `relativeTo`:
```swift
Text("Judul").font(.custom("Inter-Bold", size: 28, relativeTo: .title))
```
`Font.custom(_:size:relativeTo:)` menskalakan ukuran dengan Dynamic Type relatif ke text style (iOS 14+) `[?]`. Pakai `@ScaledMetric(relativeTo: .body) var icon = 24` untuk ukuran non-teks yang harus ikut membesar.

**3. Motion.** `withAnimation(.spring(duration:bounce:))` / `.animation(_, value:)` (varian tanpa `value` sudah deprecated `[?]`), `.transition(.opacity.combined(with: .move(edge: .bottom)))`, `matchedGeometryEffect` (transisi daftar → detail), `PhaseAnimator` dan `KeyframeAnimator` (iOS 17) untuk momen signature. Reduced motion (resmi): `@Environment(\.accessibilityReduceMotion) var reduceMotion`; saat true, ganti gerak dengan fade atau `nil`.
```swift
@Environment(\.accessibilityReduceMotion) private var reduceMotion
...
.animation(reduceMotion ? nil : Motion.easeOutExpo, value: isOpen)
```
Sumber: https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducemotion

**4. A11y.** `.accessibilityLabel("Tutup")`, `.accessibilityHint(...)`, `.accessibilityAddTraits(.isButton)`, `.accessibilityElement(children: .combine)` untuk baris kartu. Target sentuh: `.frame(minWidth: 44, minHeight: 44)` + `.contentShape(Rectangle())`. Fokus (keyboard eksternal/Switch Control): `@FocusState`. Batasi Dynamic Type: `.dynamicTypeSize(...DynamicTypeSize.accessibility2)` pada layar yang rusak di ukuran terbesar. Kontras tinggi: `@Environment(\.colorSchemeContrast)` `[?]`.

**5. Override.** Kolom Library: kontrol native (`Button` + `ButtonStyle`, `Toggle` + `ToggleStyle`, `List`, `NavigationStack`, `TabView`, `.sheet` dengan `.presentationDetents`, `TextField`). Tulis style kustom yang menggantikan tampilan bawaan (mis. `PrimaryButtonStyle`: tinggi 48, radius 8, warna token), dan komponen yang sengaja dibiarkan bawaan iOS.

**6. Jebakan.**
- `.font(.system(size:))` dan `Font.custom(_, fixedSize:)` TIDAK ikut Dynamic Type; pakai text style atau `relativeTo`.
- Urutan modifier mengubah hasil: `.padding()` sebelum `.background()` ≠ sesudahnya; `.clipShape` setelah `.shadow` memotong bayangan, jadi tulis urutannya.
- Nama font = nama PostScript, bukan nama file; salah nama = jatuh diam-diam ke font sistem.
- Bayangan berlapis = beberapa `.shadow` berurutan; satu `.shadow` tidak bisa multi-lapis.
- Teks angka yang berubah: `.monospacedDigit()` + `.contentTransition(.numericText())` (iOS 16/17 `[?]`) agar tidak bergoyang.
- Safe area: `.safeAreaInset(edge: .bottom)` untuk dock/CTA, `.ignoresSafeArea()` hanya untuk latar; tulis inset header/tab bar. Gesture kembali tepi kiri bentrok dengan geser horizontal kustom.
- Versi minimum (`iOS 16/17`) menentukan API (`PhaseAnimator`, `.spring(duration:bounce:)`, `MeshGradient` iOS 18): tulis target deployment di 2.8.

---

## 9. Lain / tidak diketahui

Kalau stack tidak ada di daftar (Android Jetpack Compose, Angular, Qwik, Astro polos, Laravel Blade, Unity, dsb.), tulis di 2.8:

1. **Tabel token netral** dalam format W3C Design Tokens (DTCG), sebagai sumber kebenaran:
```json
{
  "color": {
    "$type": "color",
    "bg": { "$value": "#FBF8F3" },
    "primary": { "$value": "#0F5C4D", "$description": "CTA, tautan aktif" }
  },
  "space": { "$type": "dimension", "s4": { "$value": "16px" } },
  "radius": { "$type": "dimension", "md": { "$value": "8px" } },
  "shadow": {
    "1": { "$type": "shadow", "$value": [
      { "color": "#1B1A17", "offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "0px" } ] }
  },
  "motion": {
    "duration-base": { "$type": "duration", "$value": "220ms" },
    "ease-out-expo": { "$type": "cubicBezier", "$value": [0.16, 1, 0.3, 1] }
  }
}
```
Kunci `$value`, `$type`, `$description` dan tipe `color`, `dimension`, `shadow`, `duration`, `cubicBezier` mengikuti spesifikasi DTCG; bentuk nilai (string hex vs objek ruang warna, `"220ms"` vs `{value, unit}`) berbeda antar draf dan versi stabil `[?]`. Tulis versi spesifikasi yang diacu.
2. **Catatan pemetaan** per target: satu tabel "token → API stack" (warna → apa, radius → apa, bayangan → apa, motion → apa, reduced motion → apa, skala font → apa, target sentuh).
3. **Skeleton kode minimal** untuk SATU token dari tiap kategori di stack itu, supaya agent coding punya pola. Kalau tidak bisa menulisnya, nyatakan di 1.4 Perlu Konfirmasi dan jangan mengarang API.
4. Alat konversi (mis. Style Dictionary) hanya disebut kalau PRD memintanya; default-nya tulis blok kode manual.

---

## Preview HTML untuk stack non-web

`design-preview.html` tetap HTML tunggal, apa pun stack-nya. Untuk React Native, Flutter, SwiftUI (dan Compose):

- **Token identik.** Preview memakai CSS variables dari tabel bagian 2 (hex yang sama dengan blok 2.8 stack). Jangan menggambar ulang warna dengan nilai berbeda.
- **Bingkai ponsel** sesuai platform sasaran, ditaruh di tengah dengan latar netral:
  - iOS: 393×852pt, status bar 54pt dengan Dynamic Island, indikator home 34pt di bawah, judul besar (large title) 34pt jika dipakai, tab bar 49pt + 34pt safe area, sheet dengan grabber dan sudut 38 sampai 40pt.
  - Android: 360×800dp (atau 412×915dp), status bar 24dp, bar navigasi gestur 24dp (atau 3 tombol), top app bar 64dp, navigation bar 80dp, FAB 56dp, ripple saat sentuh.
  - Kalau dua platform, sediakan toggle bingkai (iOS | Android) dan jelaskan perbedaan yang disengaja.
- **Konvensi platform di preview:** tombol kembali di kiri atas (iOS chevron + judul, Android panah), tipografi memakai font yang sama dengan aplikasi (bukan SF/Roboto kecuali memang dipakai), bayangan Android satu lapis (elevation) kalau itu yang akan dibangun, bukan bayangan CSS berlapis yang tidak bisa dibuat di native.
- **Tampilkan hanya yang bisa dibangun:** bayangan, gradien, blur, dan animasi di preview harus punya padanan di adaptor (lihat jebakan masing-masing). Efek CSS yang tidak ada padanannya di native (mis. `backdrop-filter` kompleks, `mix-blend-mode`) jangan dipakai.
- **Ukuran sentuh:** beri anotasi/outline opsional 44pt (iOS) atau 48dp (Android) pada kontrol utama.
- **Motion di preview:** token durasi dan easing sama; reduced motion lewat `@media (prefers-reduced-motion: reduce)` dan tombol "Simulasikan reduced motion" yang menambah kelas `.rm` ke `<html>`. Spring native diaproksimasi dengan `cubic-bezier`/keyframes; tulis catatan "aproksimasi" di preview dan stiffness/damping aslinya di 2.7.
- **Skala font:** sediakan kontrol 100% / 130% / 200% yang mengubah `font-size` root untuk membuktikan layout tidak pecah pada Dynamic Type / fontScale / textScaler.
- Tulis di kepala preview: "Stack: React Native (Expo)", dan catatan bahwa perbedaan render native (ripple, haptik, font sistem) tidak bisa direpresentasikan penuh di HTML.
