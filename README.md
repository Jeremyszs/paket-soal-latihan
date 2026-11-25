# paket-soal-latihan

An agent skill (Claude Code, Codex, Gemini CLI, OpenCode, Kiro, and other tools that read `SKILL.md`) that turns **a list of topic titles** into a print-ready exam practice pack of **3 PDFs**, in **Indonesian or English**:

1. **Practice test**: multiple-choice questions with 5 options (A–E), grouped by chapter, with a student-ID header and instructions
2. **Answer key + solutions**: key grid plus a step-by-step solution for every question
3. **Theory & formula summary**: one table per chapter (Concept · Formula/Theory · Notes)

Math is typeset with KaTeX, graphs and diagrams are drawn as SVG, and the layout mimics a real school test sheet (Times New Roman 12 pt, A4).

👉 See [`samples/`](samples/) for finished output: a 40-question Indonesian Grade 12 math pack and a short English sample.

> **Bahasa Indonesia:** Skill untuk AI agent yang membuat paket latihan dari daftar judul materi saja. Hasilnya 3 PDF siap cetak: soal pilihan ganda A–E, kunci jawaban + pembahasan, dan rangkuman teori & rumus dalam bentuk tabel. Bisa dalam bahasa Indonesia atau Inggris. Kirim saja daftar materi (teks, tabel, atau foto), misalnya: *"Buatkan soal latihan dari materi ini, 1 soal per materi."*

## Install

Clone into your agent's skills folder:

```bash
# Claude Code (all projects)
git clone https://github.com/Jeremyszs/paket-soal-latihan ~/.claude/skills/paket-soal-latihan

# Shared agents folder (Codex and others that read ~/.agents/skills)
git clone https://github.com/Jeremyszs/paket-soal-latihan ~/.agents/skills/paket-soal-latihan
```

Other locations: `~/.codex/skills/`, `~/.gemini/skills/`, `~/.config/opencode/skills/`, `~/.kiro/skills/`, or `.claude/skills/` inside a single project.

Requirements for rendering:

```bash
pip install playwright        # uses installed Chrome/Edge, or: python -m playwright install chromium
pip install pymupdf           # optional, for page previews
```

An internet connection is needed while rendering, because KaTeX is loaded from a CDN.

## Usage

Just ask your agent, for example:

- *"Make a 30-question practice test on quadratic functions, trigonometry and vectors for Grade 10, with solutions and a formula sheet."*
- *"Buatkan soal latihan dari materi ini (foto tabel materi), nomor soal sesuai materinya."*

The agent writes a content file (`konten_<slug>.py`), checks the answers, renders the PDFs, and inspects them visually.

You can also render a content file yourself:

```bash
python scripts/buat_pdf.py examples/example_english_short.py --preview
```

## Layout

```
SKILL.md                      instructions for the agent
scripts/buat_pdf.py           content file -> 3 PDFs (validation, i18n labels, KaTeX, Chrome print)
references/format_konten.md   content file format
examples/                     full Indonesian pack + short English pack
samples/                      rendered PDFs of both examples
```

The language is set with `META["bahasa"]`: `"id"` (default) or `"en"`. It switches the titles, instructions, table headers, footer, and file names.
