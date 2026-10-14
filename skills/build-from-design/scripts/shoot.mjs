#!/usr/bin/env node
/*
 * shoot.mjs : screenshot halaman untuk dibandingkan dengan compare-screens.py.
 *
 * Pemakaian:
 *   node shoot.mjs <url> <out.png> [--width 390] [--height 844] [--full] [--selector "#screen-x"]
 *                  [--scroll-to "#id"] [--wait 1500] [--dpr 1] [--no-reduced-motion]
 *
 * Bawaan: emulasi prefers-reduced-motion: reduce (keadaan akhir, tanpa noise timing animasi),
 * lalu menunggu font siap dan document.getAnimations() tidak ada yang 'running' (animasi berulang tak hingga diabaikan; maksimal --wait ms).
 * --reduced-motion diterima sebagai penegas (sudah bawaan).
 * --selector memotret satu elemen saja; --scroll-to menggulir elemen ke tengah sebelum memotret.
 *
 * Butuh playwright atau playwright-core (dicari dari folder kerja saat ini, lalu folder script).
 * playwright-core memakai Chrome sistem di /Applications/Google Chrome.app.
 * Kalau tidak ada, script mencetak petunjuk pasang dan perintah cadangan Chrome headless.
 */
import { createRequire } from 'node:module';
import path from 'node:path';
import fs from 'node:fs';
import { fileURLToPath } from 'node:url';

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const argv = process.argv.slice(2);
const pos = [];
const opt = { width: 390, height: 844, wait: 1500, dpr: 1, full: false, reduced: true, selector: null, scrollTo: null };
const needs = ['--width', '--height', '--wait', '--dpr', '--selector', '--scroll-to'];
if (argv.includes('--help') || argv.includes('-h')) {
  console.log('Pemakaian: node shoot.mjs <url> <out.png> [--width 390] [--height 844] [--full] [--reduced-motion|--no-reduced-motion] [--wait 1500] [--dpr 1] [--selector "#id"] [--scroll-to "#id"]');
  process.exit(0);
}
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (needs.includes(a)) {
    const v = argv[++i];
    if (v === undefined) die('Opsi ' + a + ' butuh nilai.');
    if (a === '--selector') opt.selector = v;
    else if (a === '--scroll-to') opt.scrollTo = v;
    else if (isNaN(Number(v))) die('Opsi ' + a + ' butuh angka, dapat "' + v + '".');
    else opt[a.slice(2)] = Number(v);
  } else if (a === '--full') opt.full = true;
  else if (a === '--reduced-motion') opt.reduced = true;
  else if (a === '--no-reduced-motion') opt.reduced = false;
  else if (a.startsWith('--')) die('Opsi tidak dikenal: ' + a);
  else pos.push(a);
}
if (pos.length < 2) die('Pemakaian: node shoot.mjs <url> <out.png> [--width 390] [--height 844] [--full] [--reduced-motion] [--wait 1500] [--selector "#id"] [--scroll-to "#id"]');
const [url, out] = pos;

function die(msg) { console.error(msg); process.exit(2); }

function fallback(reason) {
  console.error('Playwright tidak bisa dipakai: ' + reason);
  console.error('\nPasang di project (sekali):  npm i -D playwright-core');
  console.error('(playwright-core memakai Chrome sistem; tidak mengunduh browser)');
  console.error('\nCadangan tanpa Playwright, Chrome headless CLI (tidak mendukung --selector, --scroll-to, --full):');
  console.error('  "' + CHROME + '" --headless=new --hide-scrollbars --force-prefers-reduced-motion \\');
  console.error('    --virtual-time-budget=' + opt.wait + ' --window-size=' + opt.width + ',' + opt.height + ' \\');
  console.error('    --screenshot="' + path.resolve(out) + '" "' + url + '"');
  console.error('Catatan: Chrome headless bisa membatasi lebar jendela kecil (di bawah sekitar 500px); cek ukuran PNG hasilnya.');
  process.exit(3);
}

function load() {
  const bases = [path.join(process.cwd(), 'noop.js'), fileURLToPath(import.meta.url)];
  for (const name of ['playwright', 'playwright-core']) {
    for (const b of bases) {
      try { return { name, mod: createRequire(b)(name) }; } catch (e) { /* coba berikutnya */ }
    }
  }
  return null;
}

const pw = load();
if (!pw) fallback('paket playwright / playwright-core tidak ditemukan dari ' + process.cwd());

let browser;
try {
  const launchOpts = { headless: true };
  if (fs.existsSync(CHROME)) launchOpts.executablePath = CHROME;
  browser = await pw.mod.chromium.launch(launchOpts);
} catch (e) {
  fallback('gagal membuka browser (' + String(e.message).split('\n')[0] + ')');
}

try {
  const ctx = await browser.newContext({
    viewport: { width: opt.width, height: opt.height },
    deviceScaleFactor: opt.dpr,
    reducedMotion: opt.reduced ? 'reduce' : 'no-preference',
  });
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'load', timeout: 30000 });
  await page.evaluate(() => document.fonts && document.fonts.ready);
  await page.waitForFunction(() => document.getAnimations().every(a => a.playState !== 'running' || a.effect.getComputedTiming().iterations === Infinity),
    null, { timeout: opt.wait }).catch(() => console.error('PERINGATAN: masih ada animasi berjalan setelah ' + opt.wait + 'ms'));
  if (opt.scrollTo) {
    await page.locator(opt.scrollTo).first().scrollIntoViewIfNeeded();
    await page.evaluate(s => document.querySelector(s).scrollIntoView({ block: 'center' }), opt.scrollTo);
  }
  await page.waitForTimeout(150);
  fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
  if (opt.selector) await page.locator(opt.selector).first().screenshot({ path: out });
  else await page.screenshot({ path: out, fullPage: opt.full });
  console.log('OK: ' + out + ' (' + opt.width + 'x' + opt.height + (opt.full ? ' full' : '') + ', reduced-motion ' + (opt.reduced ? 'on' : 'off') + ')');
} catch (e) {
  console.error('Gagal memotret: ' + e.message);
  process.exitCode = 1;
} finally {
  await browser.close();
}
