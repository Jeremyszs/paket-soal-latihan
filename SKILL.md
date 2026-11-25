---
name: paket-soal-latihan
description: Generate a print-ready school exam practice pack as 3 PDFs — (1) multiple-choice questions with 5 options (A–E), (2) answer key + step-by-step solutions, (3) theory & formula summary in tables — from nothing more than a list of topic titles, in Indonesian or English. Use when the user asks for practice questions, exam/test questions, quizzes, "soal latihan", "soal ulangan", "soal PG", "kisi-kisi jadi soal", worked solutions/"pembahasan", a formula sheet/"rangkuman rumus", or sends a list, table, or photo of topics and wants questions, solutions, or a summary made from it. Handles math (LaTeX/KaTeX), SVG diagrams/graphs, and any subject.
---

# Paket Soal Latihan / Exam Practice Pack

The user only provides **topic titles** (text, table, or a photo of a topic list). The result is 3 A4 PDFs styled like a school test sheet (Times New Roman 12 pt, double-ruled header, KaTeX math):

| `bahasa: "id"` | `bahasa: "en"` | Contents |
|---|---|---|
| `Latihan_Soal_<slug>.pdf` | `Practice_Test_<slug>.pdf` | Header, student ID fields, instructions, A–E multiple-choice questions grouped by chapter |
| `Kunci_Pembahasan_<slug>.pdf` | `Answer_Key_Solutions_<slug>.pdf` | Answer-key grid, then each question + topic label + step-by-step solution + answer |
| `Rangkuman_<slug>.pdf` | `Summary_<slug>.pdf` | One table per chapter: No, Concept, Formula/Theory, Notes |

## Language
- **Match the user's language**: Indonesian request → `META["bahasa"] = "id"` and all content in Indonesian; English request → `"en"` and all content in English. If the user asks for a specific language, use that. All fixed labels (titles, instructions, footer, file names) switch automatically. Everything you write (questions, options, solutions, summary) must be in the same language.
- Indonesian style: formal *bahasa baku*, stems end with "adalah ....". English style: stems end with "is ...." or "=" ...., British/American spelling used consistently.

## Workflow

### 1. Understand the input
- Read the topic list. If it is a numbered photo/table, **one topic row = one question with the same number**. If it is an unnumbered list of topics, ask how many questions (default 1–2 per topic, 20–40 total).
- Infer subject, grade level, and curriculum from context (default for Indonesian: Kurikulum Merdeka). Ask only if it truly cannot be inferred.
- Group topics into **chapters** (colour groups in the user's table usually mark chapters).

### 2. Write the content file
Create one Python file, e.g. `<work_dir>/konten_<slug>.py`, following **[references/format_konten.md](references/format_konten.md)** (read it first). Use the examples as the quality bar for tone, difficulty, solution length, and summary depth:
- **[examples/contoh_matematika_tl_12.py](examples/contoh_matematika_tl_12.py)**: full Indonesian pack (40 questions, 4 chapters, graph and diagram SVGs).
- **[examples/example_english_short.py](examples/example_english_short.py)**: short English pack.

Question rules:
- **Difficulty** matches the level: school tests / end-of-semester / university-entrance style. Mix direct computation, conceptual, and contextual (word) problems.
- **Exactly one correct answer.** Recompute every answer; for numeric questions verify with Python (`sympy` if available) before writing the key.
- **Plausible distractors** built from typical student mistakes (sign errors, forgotten chain rule, swapped formulas, wrong coefficient). No duplicate or mathematically equivalent options.
- **Numeric options sorted ascending**. Algebraic-expression options may be in any order.
- **Even key distribution** across A–E (difference at most 1–2), controlled by where you place the correct option.
- Do not copy questions verbatim from copyrighted sources. Researching question types/patterns is fine; write your own numbers and contexts.

Solution rules: step by step, name the formula used, show key calculations with `$$...$$`, end with the final result.

Summary rules: **pure topic material, independent of the questions** (never reuse numbers from the questions). Each chapter covers every sub-topic in the user's list, plus genuinely needed supporting formulas (identities, special-value tables, properties). The Notes column holds conditions, tips, and common mistakes.

### 3. Render
```bash
python <skill_dir>/scripts/buat_pdf.py <work_dir>/konten_<slug>.py --preview
```
- The script validates first (5 options, key A–E, balanced `$`, key distribution). Fix every `[ERROR]`.
- PDFs are written next to the content file (or `--out FOLDER`). `--preview` saves a PNG per page into `_preview/`.
- Requirements: `pip install playwright` (+ Chrome/Edge installed, or `python -m playwright install chromium`), internet access (KaTeX from CDN). `pymupdf` is optional, for previews.

### 4. Visual check (mandatory)
Open the preview PNGs and check:
- No raw math leaking as text (`$`, `\frac`), no missing or clipped options.
- Options not cramped: if long options look tight, lower `kolom` (5 → 3 → 2 → 1).
- In the summary, formulas do not spill into the Notes column: split long formulas into several `$$...$$` blocks.
- Figures/graphs are readable and labels do not overlap lines.
Fix the content, re-render, and check again until clean. Delete `_preview/` afterwards unless the user wants it.

### 5. Hand over
Report the location of the three PDFs, number of questions, page counts, key distribution, and that answers were verified. Keep the content file so the user can edit and re-render.
