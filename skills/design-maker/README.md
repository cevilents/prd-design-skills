# Skill set: prd-maker · design-maker · build-from-design

Tiga skill yang dipakai berurutan: **ide → PRD.md → DESIGN.md + preview → kode UI**. Ditulis mengikuti standar terbuka [Agent Skills](https://agentskills.io/specification), jadi bisa dipakai model dan tool AI apa pun, bukan hanya Claude. Sumber: https://github.com/cevilents/prd-design-skills

| Skill | Hasil |
|---|---|
| `prd-maker` | PRD.md 7 bagian (overview sampai tech stack, dengan diagram Mermaid) |
| `design-maker` | 3 konsep visual untuk dipilih, DESIGN.md, design-preview.html |
| `build-from-design` | Kode UI di stack project + verifikasi kemiripan dengan preview |

Simpan ketiga folder **berdampingan** di folder induk yang sama, karena skill saling merujuk lewat `<SKILL_DIR>/../<nama-skill>`.

## Instalasi per tool

| Tool | Cara pasang |
|---|---|
| Claude Code | Salin/symlink ke `~/.claude/skills/` (semua project) atau `.claude/skills/` (satu project) |
| Codex (OpenAI) | `~/.agents/skills/` atau `.agents/skills/` di project |
| Cursor | `.agents/skills/` atau `.cursor/skills/` di project (juga membaca `.claude/skills/`) |
| VS Code / GitHub Copilot | `~/.agents/skills/`, `~/.copilot/skills/`, atau `.github/skills/` di project |
| Gemini CLI | `~/.gemini/skills/` atau `~/.agents/skills/` |
| Windsurf | `.windsurf/skills/` atau `~/.codeium/windsurf/skills/` |
| Roo Code, OpenCode, Goose, Cline | Umumnya `.agents/skills/` atau folder skill milik tool (Cline: aktifkan fitur skills di pengaturan) |
| Claude.ai | Zip tiap folder skill, unggah di pengaturan Skills (butuh code execution aktif) |

Cara paling praktis untuk banyak tool sekaligus: simpan satu salinan, lalu buat symlink ke `~/.agents/skills/` (dibaca Codex, Cursor, Copilot, Gemini CLI, Roo, Goose, OpenCode) dan `~/.claude/skills/` (Claude Code).

Tool tanpa dukungan skill: tambahkan petunjuk di `AGENTS.md` project, mis. "Untuk membuat PRD, baca dan ikuti `skills/prd-maker/SKILL.md`".

## Chat biasa tanpa akses file (ChatGPT web, Gemini web, dll.)

1. Unggah `SKILL.md` dan file di `references/` sebagai file project/knowledge (atau tempel isi SKILL.md di awal percakapan).
2. Minta seperti biasa, mis. "Ikuti skill design-maker untuk aplikasi ...".
3. Script tidak bisa dijalankan di sana. Skill sudah punya jalur cadangan: kontras dihitung manual dengan rumus WCAG, hasil file diberikan sebagai blok kode, pertanyaan diajukan lewat teks.

## Kebutuhan opsional

- Python 3 (+ Pillow untuk ekstraksi warna dari gambar)
- Node.js (+ `playwright-core` atau Google Chrome) untuk screenshot otomatis
- Browser untuk melihat preview

Semua kebutuhan ini opsional untuk `prd-maker` dan `design-maker`; tanpa itu skill tetap berjalan dengan langkah manual. `build-from-design` butuh lingkungan coding.
