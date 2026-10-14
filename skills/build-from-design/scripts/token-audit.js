/*
 * token-audit.js : audit halaman yang sedang terbuka terhadap design tokens.
 *
 * Cara pakai (JS biasa, tanpa modul):
 *   1. Suntik token dulu:  window.__DESIGN_TOKENS = <isi tokens.json>;
 *   2. Jalankan seluruh file ini (alat "execute JavaScript" browser atau tempel di DevTools).
 *   3. Nilai ekspresi terakhir adalah string JSON ringkas (aman ditempel dua kali, tanpa global baru).
 *
 * Opsi (opsional, set sebelum menjalankan):
 *   window.__AUDIT_MODE = 'light' | 'dark' | 'both'   (default: 'light' bila token tidak punya nilai Dark; selain itu
 *                                                      deteksi dari kelas .dark, data-theme, atau prefers-color-scheme)
 *
 * Yang diperiksa: (a) warna di luar token, (b) font di luar desain, (c) font-size di luar skala token (fontSizeNotInScale)
 * dan line-height yang tidak cocok padahal ukurannya ada di token (lineHeightMismatch), (d) kontras teks WCAG, (e) target sentuh (tier < 24px AA dan tier < 44px saran), (f) overflow horizontal,
 * (g) border-radius di luar token. Batasan: pseudo-element (::before/::after), elemen SVG, dan
 * latar gradien/gambar tidak dianalisis (kontras di atasnya dilewati dan dihitung di contrast.skipped).
 */
(function () {
  'use strict';
  var T = window.__DESIGN_TOKENS;
  if (!T || typeof T !== 'object') {
    return JSON.stringify({ error: 'window.__DESIGN_TOKENS belum disuntik. Set dulu dengan isi tokens.json.' });
  }
  var TOP = 20;
  var root = document.documentElement;

  // ---------- warna ----------
  var cvs = document.createElement('canvas');
  cvs.width = cvs.height = 1;
  var ctx = cvs.getContext('2d', { willReadFrequently: true });
  var colorCache = {};
  function parseColor(str) {
    if (colorCache[str]) return colorCache[str];
    var out = null, m;
    if (str === 'transparent') out = [0, 0, 0, 0];
    else if ((m = /^rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,\/]\s*([\d.]+%?))?\s*\)$/.exec(str))) {
      var a = m[4] === undefined ? 1 : (m[4].slice(-1) === '%' ? parseFloat(m[4]) / 100 : parseFloat(m[4]));
      out = [+m[1], +m[2], +m[3], a];
    } else if (ctx) {
      ctx.clearRect(0, 0, 1, 1);
      ctx.fillStyle = '#010203';
      ctx.fillStyle = str;
      ctx.fillRect(0, 0, 1, 1);
      var d = ctx.getImageData(0, 0, 1, 1).data;
      out = [d[0], d[1], d[2], d[3] / 255];
    }
    colorCache[str] = out || [0, 0, 0, 0];
    return colorCache[str];
  }
  function hex(c) {
    return '#' + [0, 1, 2].map(function (i) {
      var v = Math.max(0, Math.min(255, Math.round(c[i]))).toString(16);
      return v.length < 2 ? '0' + v : v;
    }).join('').toUpperCase();
  }
  function hexToRgb(h) {
    var m = /^#?([0-9a-f]{6})/i.exec(h || '');
    if (!m) return null;
    var n = parseInt(m[1], 16);
    return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
  }
  function over(fg, bg) { // fg [r,g,b,a] di atas bg [r,g,b] -> [r,g,b]
    var a = fg[3];
    return [fg[0] * a + bg[0] * (1 - a), fg[1] * a + bg[1] * (1 - a), fg[2] * a + bg[2] * (1 - a)];
  }
  function lin(v) { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }
  function lum(c) { return 0.2126 * lin(c[0]) + 0.7152 * lin(c[1]) + 0.0722 * lin(c[2]); }
  function ratio(a, b) {
    var l1 = lum(a), l2 = lum(b);
    return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
  }
  function lab(c) {
    var r = lin(c[0]), g = lin(c[1]), b = lin(c[2]);
    var x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047;
    var y = (0.2126 * r + 0.7152 * g + 0.0722 * b);
    var z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883;
    function f(t) { return t > 0.008856 ? Math.cbrt(t) : 7.787 * t + 16 / 116; }
    return [116 * f(y) - 16, 500 * (f(x) - f(y)), 200 * (f(y) - f(z))];
  }
  function dE(a, b) { return Math.sqrt(Math.pow(a[0] - b[0], 2) + Math.pow(a[1] - b[1], 2) + Math.pow(a[2] - b[2], 2)); }
  function dRGB(a, b) { return dE(a, b); }

  // ---------- mode & token ----------
  var mode = window.__AUDIT_MODE;
  var anyDark = Object.keys(T.colors || {}).some(function (n) { return T.colors[n] && T.colors[n].dark; });
  if (!mode) {
    var dk = anyDark && ( root.classList.contains('dark') || /dark/.test(root.getAttribute('data-theme') || '') ||
      (!root.classList.contains('light') && !/light/.test(root.getAttribute('data-theme') || '') &&
        window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches));
    mode = dk ? 'dark' : 'light';
  }
  var tokColors = [];
  Object.keys(T.colors || {}).forEach(function (name) {
    var e = T.colors[name] || {};
    var modes = mode === 'both' ? ['light', 'dark'] : [mode];
    modes.forEach(function (md) {
      var v = e[md] || (md === 'dark' ? e.light : null);
      var rgb = hexToRgb(v);
      if (rgb) tokColors.push({ name: name, hex: hex(rgb), rgb: rgb, lab: lab(rgb) });
    });
  });
  var tokTypo = Object.keys(T.typography || {}).map(function (n) {
    var t = T.typography[n];
    return { name: n, min: t.sizePx, max: t.sizeMaxPx || t.sizePx, lhPx: t.lineHeightPx, lhRatio: t.lineHeightRatio };
  }).filter(function (t) { return typeof t.min === 'number'; });
  var tokRadius = Object.keys(T.radius || {}).map(function (n) { return T.radius[n] && T.radius[n].px; })
    .filter(function (v) { return typeof v === 'number'; });

  function normFamily(s) {
    return String(s || '').toLowerCase().replace(/["']/g, '').replace(/^_+/, '').replace(/_/g, ' ')
      .replace(/\s+[0-9a-f]{6,}$/, '').replace(/\s+fallback$/, '').replace(/\s+/g, ' ').trim();
  }
  var designFonts = (T.fonts || []).map(normFamily);
  var generic = {};
  ['serif', 'sans-serif', 'monospace', 'system-ui', 'ui-sans-serif', 'ui-serif', 'ui-monospace', 'ui-rounded',
    'cursive', 'fantasy', '-apple-system', 'blinkmacsystemfont'].forEach(function (g) { generic[g] = 1; });
  function fontOk(first) {
    var n = normFamily(first);
    for (var i = 0; i < designFonts.length; i++) {
      var d = designFonts[i];
      if (n === d || n.indexOf(d + ' ') === 0 || d.indexOf(n + ' ') === 0) return true;
    }
    return false;
  }

  // ---------- util DOM ----------
  var styleCache = new Map();
  function cs(el) {
    var s = styleCache.get(el);
    if (!s) { s = getComputedStyle(el); styleCache.set(el, s); }
    return s;
  }
  function selector(el) {
    var parts = [], n = 0;
    while (el && el.nodeType === 1 && n < 4) {
      var p = el.tagName.toLowerCase();
      if (el.id) { parts.unshift(p + '#' + el.id); break; }
      var cls = (typeof el.className === 'string' ? el.className : '').trim().split(/\s+/).filter(Boolean).slice(0, 2);
      if (cls.length) p += '.' + cls.join('.');
      else if (el.parentElement) p += ':nth-child(' + (Array.prototype.indexOf.call(el.parentElement.children, el) + 1) + ')';
      parts.unshift(p);
      el = el.parentElement;
      n++;
    }
    return parts.join(' > ').slice(0, 110);
  }
  function hasOwnText(el) {
    for (var c = el.firstChild; c; c = c.nextSibling) {
      if (c.nodeType === 3 && /\S/.test(c.nodeValue)) return true;
    }
    return false;
  }
  function ownText(el) {
    var t = '';
    for (var c = el.firstChild; c; c = c.nextSibling) if (c.nodeType === 3) t += c.nodeValue;
    return t.replace(/\s+/g, ' ').trim().slice(0, 28);
  }
  function opacityChain(el) {
    var o = 1;
    for (var e = el; e && e.nodeType === 1; e = e.parentElement) o *= parseFloat(cs(e).opacity) || 0;
    return o;
  }
  // latar efektif: [r,g,b] | null (tidak diketahui: gradien/gambar)
  var bgCache = new Map();
  function effBg(el) {
    if (!el || el.nodeType !== 1) return [255, 255, 255];
    if (bgCache.has(el)) return bgCache.get(el);
    var s = cs(el), res;
    if (s.backgroundImage && s.backgroundImage !== 'none') res = null;
    else {
      var c = parseColor(s.backgroundColor);
      if (c[3] >= 0.999) res = [c[0], c[1], c[2]];
      else {
        var below = el === root ? [255, 255, 255] : effBg(el.parentElement);
        res = c[3] <= 0 ? below : (below ? over(c, below) : null);
      }
    }
    bgCache.set(el, res);
    return res;
  }
  function clippedByAncestor(el) {
    for (var p = el.parentElement; p && p !== document.body && p !== root; p = p.parentElement) {
      var ox = cs(p).overflowX;
      if (ox !== 'visible') return true;
    }
    return false;
  }

  // ---------- agregator ----------
  function bucket() { return { map: {}, order: [] }; }
  function add(b, key, init, sel) {
    var e = b.map[key];
    if (!e) { e = b.map[key] = init; e.count = 0; e.samples = []; b.order.push(key); }
    e.count++;
    if (e.samples.length < 3 && e.samples.indexOf(sel) < 0) e.samples.push(sel);
    return e;
  }
  function top(b, extraSort) {
    return b.order.map(function (k) { return b.map[k]; })
      .sort(extraSort || function (x, y) { return y.count - x.count; }).slice(0, TOP);
  }

  var offColors = bucket(), offFonts = bucket(), offSize = bucket(), offLH = bucket(), offRadius = bucket();
  var contrastFails = [], targets = [], overflowEls = [];
  var stats = { elements: 0, textElements: 0, contrastChecked: 0, contrastSkipped: 0, interactive: 0, inlineLinksSkipped: 0, lhNormal: 0 };
  var weights = {};
  var skipTags = { SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, TEMPLATE: 1, HEAD: 1, META: 1, LINK: 1, TITLE: 1, BR: 1, WBR: 1 };

  function nearestToken(rgb) {
    var best = null, bl = lab(rgb);
    for (var i = 0; i < tokColors.length; i++) {
      var d = dE(bl, tokColors[i].lab);
      if (!best || d < best.dE) best = { name: tokColors[i].name, hex: tokColors[i].hex, dE: d, rgbDist: dRGB(rgb, tokColors[i].rgb) };
    }
    return best;
  }
  function checkColor(rgbaOrRgb, prop, el, alphaUsed) {
    if (!tokColors.length) return;
    var rgb = rgbaOrRgb;
    var ok = false;
    for (var i = 0; i < tokColors.length; i++) {
      if (dRGB(rgb, tokColors[i].rgb) <= 6 || dE(lab(rgb), tokColors[i].lab) <= 3) { ok = true; break; }
    }
    if (ok) return;
    var h = hex(rgb);
    var e = add(offColors, h, { color: h, props: {}, fromAlpha: false, nearest: null }, selector(el));
    e.props[prop] = (e.props[prop] || 0) + 1;
    if (alphaUsed) e.fromAlpha = true;
    if (!e.nearest) {
      var n = nearestToken(rgb);
      e.nearest = n ? { token: n.name, hex: n.hex, dE: Math.round(n.dE * 10) / 10 } : null;
    }
  }

  var all = document.body ? document.body.getElementsByTagName('*') : [];
  var vw = root.clientWidth, vh = window.innerHeight;
  var interactiveSel = 'a, button, input:not([type=hidden]), select, textarea, [role=button], [role=link], [role=tab], [role=switch], summary';

  for (var i = 0; i < all.length; i++) {
    var el = all[i];
    if (skipTags[el.tagName] || !(el instanceof HTMLElement)) continue;
    var s = cs(el);
    if (s.display === 'none' || s.visibility === 'hidden' || s.visibility === 'collapse') continue;
    var r = el.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) continue;
    if (r.width <= 1 && r.height <= 1) continue; // sr-only
    stats.elements++;
    var sel = null;
    function S() { return sel || (sel = selector(el)); }

    // --- warna latar & border ---
    var bg = parseColor(s.backgroundColor);
    var hasBg = bg[3] > 0 && s.backgroundImage === 'none';
    if (hasBg) {
      var below = effBg(el.parentElement);
      var shown = bg[3] >= 0.999 ? [bg[0], bg[1], bg[2]] : (below ? over(bg, below) : [bg[0], bg[1], bg[2]]);
      checkColor(shown, 'background', el, bg[3] < 0.999);
    }
    var sides = ['Top', 'Right', 'Bottom', 'Left'], hasBorder = false, seen = {};
    for (var k = 0; k < 4; k++) {
      var sd = sides[k];
      if (parseFloat(s['border' + sd + 'Width']) > 0 && s['border' + sd + 'Style'] !== 'none') {
        hasBorder = true;
        var bc = parseColor(s['border' + sd + 'Color']);
        if (bc[3] > 0 && !seen[s['border' + sd + 'Color']]) {
          seen[s['border' + sd + 'Color']] = 1;
          var bb = effBg(el);
          checkColor(bc[3] >= 0.999 || !bb ? [bc[0], bc[1], bc[2]] : over(bc, bb), 'border', el, bc[3] < 0.999);
        }
      }
    }

    // --- radius ---
    if ((hasBg || hasBorder) && tokRadius.length) {
      var rr = s.borderTopLeftRadius;
      if (rr && rr !== '0px') {
        var pxv = parseFloat(rr), pill = /%/.test(rr) || pxv >= Math.min(r.width, r.height) / 2 - 0.5;
        if (!pill) {
          var okR = false;
          for (var q = 0; q < tokRadius.length; q++) if (Math.abs(tokRadius[q] - pxv) <= 0.5) { okR = true; break; }
          if (!okR) add(offRadius, rr, { radius: rr }, S());
        }
      }
    }

    // --- teks ---
    var tag = el.tagName;
    var isField = (tag === 'INPUT' && !/^(checkbox|radio|range|file|color|image|button|submit|reset)$/.test(el.type)) || tag === 'TEXTAREA' || tag === 'SELECT';
    var isText = hasOwnText(el) || isField;
    if (isText) {
      stats.textElements++;
      var fs = parseFloat(s.fontSize), fw = parseInt(s.fontWeight, 10) || 400;
      weights[fw] = (weights[fw] || 0) + 1;
      var tc = parseColor(s.color), op = opacityChain(el);
      var bgE = effBg(el);

      // warna teks
      if (tc[3] > 0 && op > 0) {
        var eff = bgE ? over([tc[0], tc[1], tc[2], tc[3] * op], bgE) : [tc[0], tc[1], tc[2]];
        checkColor(eff, 'color', el, tc[3] * op < 0.999);
        // kontras
        var disabled = el.disabled || el.getAttribute('aria-disabled') === 'true';
        if (!disabled) {
          if (!bgE) stats.contrastSkipped++;
          else {
            stats.contrastChecked++;
            var cr = ratio(eff, bgE);
            var large = fs >= 24 || (fs >= 18.66 && fw >= 700);
            var need = large ? 3 : 4.5;
            if (cr < need) {
              contrastFails.push({
                sel: S(), text: ownText(el) || (isField ? '(field)' : ''), fg: hex(eff), bg: hex(bgE),
                ratio: Math.round(cr * 100) / 100, need: need, size: fs, weight: fw
              });
              if (op < 0.999) contrastFails[contrastFails.length - 1].opacity = Math.round(op * 100) / 100;
            }
          }
        }
      }

      // font family
      var fam = s.fontFamily.split(',')[0].trim().replace(/^["']|["']$/g, '');
      if (designFonts.length && !fontOk(fam)) {
        add(offFonts, fam, { family: fam, stack: s.fontFamily.slice(0, 90), generic: !!generic[fam.toLowerCase()] }, S());
      }

      // ukuran / line-height
      if (tokTypo.length) {
        var lh = s.lineHeight, lhPx = lh === 'normal' ? null : parseFloat(lh);
        if (lhPx === null) stats.lhNormal++;
        var sizeMatched = false, fullMatched = false, expect = [];
        for (var t = 0; t < tokTypo.length && !fullMatched; t++) {
          var tk = tokTypo[t];
          if (fs < tk.min - 0.5 || fs > tk.max + 0.5) continue;
          sizeMatched = true;
          var want = tk.lhPx != null ? tk.lhPx : tk.lhRatio != null ? tk.lhRatio * fs : null;
          if (lhPx === null || want === null) fullMatched = true;
          else if (Math.abs(lhPx - want) <= 0.5 + (tk.lhRatio != null ? 0.01 * fs : 0)) fullMatched = true;
          else expect.push(tk.name + ' ' + (Math.round(want * 10) / 10) + 'px');
        }
        var fsr = Math.round(fs * 100) / 100;
        if (!sizeMatched) {
          var nt = null;
          tokTypo.forEach(function (tk) {
            var dd = fs < tk.min ? tk.min - fs : fs > tk.max ? fs - tk.max : 0;
            if (!nt || dd < nt.d) nt = { d: dd, name: tk.name, px: dd === 0 ? fs : (fs < tk.min ? tk.min : tk.max) };
          });
          add(offSize, fsr + 'px', { size: fsr + 'px', nearest: nt ? nt.name + ' ' + nt.px + 'px' : null }, S());
        } else if (!fullMatched) {
          var key = fsr + 'px/' + (Math.round(lhPx * 100) / 100) + 'px';
          add(offLH, key, { pair: key, expected: expect.slice(0, 3) }, S());
        }
      }
    }

    // --- target sentuh ---
    if (el.matches(interactiveSel) && !el.closest('[aria-hidden="true"]')) {
      var isInline = tag === 'A' && s.display === 'inline' && el.parentElement && (function () {
        for (var c = el.parentElement.firstChild; c; c = c.nextSibling) {
          if (c !== el && c.nodeType === 3 && /\S/.test(c.nodeValue)) return true;
        }
        return false;
      })();
      if (isInline) stats.inlineLinksSkipped++;
      else {
        var box = r;
        if (tag === 'INPUT' && /^(checkbox|radio)$/.test(el.type)) {
          var lbl = el.closest('label') || (el.id && document.querySelector('label[for="' + el.id + '"]'));
          if (lbl) box = lbl.getBoundingClientRect();
        }
        stats.interactive++;
        targets.push({ sel: S(), text: ownText(el) || el.getAttribute('aria-label') || '', l: box.left, t: box.top, r: box.right, b: box.bottom, w: box.width, h: box.height });
      }
    }

    // --- overflow ---
    if ((r.right > vw + 1 || r.left < -1) && s.position !== 'fixed' && !clippedByAncestor(el)) {
      overflowEls.push({ sel: S(), left: Math.round(r.left), right: Math.round(r.right), w: Math.round(r.width) });
    }
  }

  // ---------- ringkasan ----------
  var docOverflow = root.scrollWidth > root.clientWidth;
  // target sentuh: tier AA (WCAG 2.2 SC 2.5.8, < 24px kecuali pengecualian jarak) dan tier saran 44px
  function circleHitsOther(t, idx) {
    var cx = (t.l + t.r) / 2, cy = (t.t + t.b) / 2;
    for (var j = 0; j < targets.length; j++) {
      if (j === idx) continue;
      var o = targets[j];
      if (o.l >= t.l - 0.5 && o.r <= t.r + 0.5 && o.t >= t.t - 0.5 && o.b <= t.b + 0.5) continue; // di dalam target yang sama
      var dx = Math.max(o.l - cx, 0, cx - o.r), dy = Math.max(o.t - cy, 0, cy - o.b);
      if (dx * dx + dy * dy < 144) return true;
    }
    return false;
  }
  var below24 = [], below44 = [];
  targets.forEach(function (t, idx) {
    var item = { sel: t.sel, text: t.text, w: Math.round(t.w * 10) / 10, h: Math.round(t.h * 10) / 10 };
    function failing(min) { return t.w < min && t.h < min ? 'both' : t.w < min ? 'width' : 'height'; }
    if ((t.w < 23.5 || t.h < 23.5) && circleHitsOther(t, idx)) { item.fails = failing(23.5); below24.push(item); }
    else if (t.w < 43.5 || t.h < 43.5) { item.fails = failing(43.5); below44.push(item); }
  });
  function bySize(x, y) { return (x.w * x.h) - (y.w * y.h); }
  below24.sort(bySize); below44.sort(bySize);
  contrastFails.sort(function (a, b) { return (a.ratio / a.need) - (b.ratio / b.need); });
  overflowEls.sort(function (a, b) { return (b.right - vw) - (a.right - vw); });

  var out = {
    meta: {
      url: location.href, title: document.title, mode: mode,
      viewport: { w: vw, h: vh, dpr: window.devicePixelRatio || 1 },
      scanned: stats.elements, textElements: stats.textElements,
      tokens: { colors: tokColors.length, typography: tokTypo.length, fonts: designFonts.length, radius: tokRadius.length }
    },
    colorsOffToken: { distinct: offColors.order.length, top: top(offColors) },
    fontsOffDesign: { distinct: offFonts.order.length, top: top(offFonts) },
    fontSizeNotInScale: { distinct: offSize.order.length, top: top(offSize) },
    lineHeightMismatch: { distinct: offLH.order.length, lineHeightNormalSkipped: stats.lhNormal, top: top(offLH) },
    contrast: {
      checked: stats.contrastChecked, skippedUnknownBg: stats.contrastSkipped,
      failCount: contrastFails.length, top: contrastFails.slice(0, TOP)
    },
    touchTargets: {
      checked: stats.interactive, inlineLinksSkipped: stats.inlineLinksSkipped,
      targetsBelow24: { count: below24.length, top: below24.slice(0, TOP) },
      targetsBelow44: { count: below44.length, top: below44.slice(0, TOP) }
    },
    overflowX: {
      documentOverflow: docOverflow, scrollWidth: root.scrollWidth, clientWidth: root.clientWidth,
      offenderCount: overflowEls.length, top: overflowEls.slice(0, TOP)
    },
    radiusOffToken: { distinct: offRadius.order.length, top: top(offRadius) },
    fontWeightsUsed: weights
  };
  out.summary = {
    colorsOffToken: offColors.order.length, fontsOffDesign: offFonts.order.length,
    fontSizeNotInScale: offSize.order.length, lineHeightMismatch: offLH.order.length, contrastFail: contrastFails.length,
    targetsBelow24: below24.length, targetsBelow44: below44.length, overflowX: docOverflow || overflowEls.length > 0,
    radiusOffToken: offRadius.order.length
  };
  return JSON.stringify(out);
})();
