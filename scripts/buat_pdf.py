# -*- coding: utf-8 -*-
"""
Render paket latihan menjadi 3 PDF dari satu file konten (.py).
Render a practice pack into 3 PDFs from one content file (.py).

  META["bahasa"] = "id" (default)          META["bahasa"] = "en"
  1. Latihan_Soal_<slug>.pdf               Practice_Test_<slug>.pdf
  2. Kunci_Pembahasan_<slug>.pdf           Answer_Key_Solutions_<slug>.pdf
  3. Rangkuman_<slug>.pdf                  Summary_<slug>.pdf

Pemakaian / usage:
  python buat_pdf.py path/to/konten.py [--out FOLDER] [--preview]

File konten adalah modul Python yang mendefinisikan META, SOAL, RANGKUMAN
(lihat references/format_konten.md). Rumus ditulis LaTeX di dalam $...$ / $$...$$
dan dirender dengan KaTeX (butuh internet saat render).
"""
import argparse, importlib.util, pathlib, re, sys
from collections import Counter

HURUF = "ABCDE"

# Teks tetap per bahasa / fixed labels per language.
STR = {
    "id": dict(
        judul_soal="LATIHAN SOAL", judul_bahas="KUNCI JAWABAN DAN PEMBAHASAN", judul_rk="RANGKUMAN TEORI DAN RUMUS",
        nama="Nama", kelas="Kelas", absen="No. Absen", waktu="Waktu", waktu_def="120 menit",
        petunjuk="Petunjuk Umum",
        p1="Tulislah nama, kelas, dan nomor absen pada tempat yang tersedia.",
        p2="Soal terdiri atas {n} butir pilihan ganda dengan lima pilihan jawaban (A, B, C, D, E).",
        p3="Pilihlah satu jawaban yang paling tepat dengan memberi tanda silang (X) pada lembar jawaban.",
        p4="Kerjakan soal yang dianggap mudah terlebih dahulu.", nokalk=" Tidak diperkenankan menggunakan kalkulator.",
        penutup="— Selamat mengerjakan —", kunci="Kunci Jawaban", materi="Materi", bahas="Pembahasan", jawaban="Jawaban",
        th=("No", "Konsep", "Rumus / Teori", "Keterangan"),
        f_soal="Latihan Soal", f_bahas="Kunci Jawaban &amp; Pembahasan", f_rk="Rangkuman Teori dan Rumus",
        hal="Halaman", dari="dari",
        file_soal="Latihan_Soal", file_bahas="Kunci_Pembahasan", file_rk="Rangkuman"),
    "en": dict(
        judul_soal="PRACTICE TEST", judul_bahas="ANSWER KEY AND SOLUTIONS", judul_rk="THEORY AND FORMULA SUMMARY",
        nama="Name", kelas="Class", absen="Student No.", waktu="Time", waktu_def="120 minutes",
        petunjuk="General Instructions",
        p1="Write your name, class, and student number in the spaces provided.",
        p2="This test consists of {n} multiple-choice questions with five answer choices (A, B, C, D, E).",
        p3="Choose the one best answer and mark it with a cross (X) on the answer sheet.",
        p4="Answer the questions you find easiest first.", nokalk=" Calculators are not allowed.",
        penutup="— Good luck —", kunci="Answer Key", materi="Topic", bahas="Solution", jawaban="Answer",
        th=("No", "Concept", "Formula / Theory", "Notes"),
        f_soal="Practice Test", f_bahas="Answer Key &amp; Solutions", f_rk="Theory and Formula Summary",
        hal="Page", dari="of",
        file_soal="Practice_Test", file_bahas="Answer_Key_Solutions", file_rk="Summary"),
}


def T(meta):
    b = meta.get("bahasa", "id")
    if b not in STR:
        sys.exit(f"[ERROR] META['bahasa'] must be 'id' or 'en', not {b!r}")
    return STR[b]


# ------------------------------------------------------------------ util
def esc_math(t):
    """Ubah < dan > di dalam $...$ menjadi \\lt / \\gt agar tidak dibaca sebagai tag HTML."""
    return re.sub(r"\$\$.+?\$\$|\$.+?\$",
                  lambda m: m.group(0).replace("<", r"\lt ").replace(">", r"\gt "), t, flags=re.S)


def split_wide(t):
    """Di blok $$...$$, pecah rumus yang dipisah \\qquad atau \\iff menjadi baris terpisah."""
    def fix(m):
        s = re.sub(r",?\\qquad\s*", "$$ $$", m.group(0))
        return s.replace(r"\iff", r"$$ $$\iff")
    return re.sub(r"\$\$.+?\$\$", fix, t, flags=re.S)


def load_konten(path):
    spec = importlib.util.spec_from_file_location("konten", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for nama in ("META", "SOAL", "RANGKUMAN"):
        if not hasattr(mod, nama):
            sys.exit(f"[ERROR] {path} does not define {nama}")
    return mod.META, mod.SOAL, mod.RANGKUMAN


def validasi(meta, soal, rangkuman):
    err = []
    T(meta)
    for k in ("mapel", "kelas", "slug"):
        if not meta.get(k):
            err.append(f"META['{k}'] is required")
    for i, s in enumerate(soal, 1):
        for k in ("bab", "materi", "soal", "opsi", "kunci", "pembahasan"):
            if k not in s:
                err.append(f"Q{i}: missing field '{k}'")
        if len(s.get("opsi", [])) != 5:
            err.append(f"Q{i}: 'opsi' must have exactly 5 options (has {len(s.get('opsi', []))})")
        if s.get("kunci") not in list(HURUF):
            err.append(f"Q{i}: 'kunci' must be one of A-E")
        if s.get("kolom", 1) not in (1, 2, 3, 5):
            err.append(f"Q{i}: 'kolom' must be 1, 2, 3, or 5")
        if len(set(s.get("opsi", []))) != len(s.get("opsi", [])):
            err.append(f"Q{i}: duplicate options")
        for teks in [s.get("soal", ""), s.get("pembahasan", "")] + list(s.get("opsi", [])):
            if teks.count("$") % 2:
                err.append(f"Q{i}: odd number of $ (unclosed math): {teks[:50]}...")
                break
    for b in rangkuman:
        for j, r in enumerate(b.get("baris", []), 1):
            if len(r) != 3:
                err.append(f"Summary '{b.get('bab')}' row {j}: must be (concept, formula, notes)")
    if err:
        print("\n".join("[ERROR] " + e for e in err))
        sys.exit(1)
    sebaran = Counter(s["kunci"] for s in soal)
    print(f"{len(soal)} questions | key distribution: " + ", ".join(f"{h}={sebaran.get(h, 0)}" for h in HURUF))
    if soal and max(sebaran.values()) - min(sebaran.get(h, 0) for h in HURUF) > max(2, len(soal) // 8):
        print("[WARNING] answer keys are unevenly distributed; consider reordering options.")


# ------------------------------------------------------------------ HTML
KATEX = "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist"
CSS = """
@page { size: A4; margin: 18mm 18mm 20mm 20mm; }
* { box-sizing: border-box; }
body { font-family: "Times New Roman", Times, serif; font-size: 12pt; line-height: 1.45; color: #000; margin: 0; }
.katex { font-size: 1.08em; }
.katex-display { margin: .35em 0; }
.kop { text-align: center; border-bottom: 3px double #000; padding-bottom: 6px; margin-bottom: 10px; }
.kop h1 { font-size: 15pt; margin: 0; letter-spacing: .5px; }
.kop h2 { font-size: 13pt; margin: 2px 0 0; }
.kop p { margin: 2px 0 0; font-size: 11.5pt; }
table.id { width: 100%; border-collapse: collapse; margin: 6px 0 10px; }
table.id td { padding: 2px 4px; }
.petunjuk { border: 1px solid #000; padding: 6px 10px; margin-bottom: 12px; font-size: 11.5pt; }
.petunjuk b { display: block; margin-bottom: 2px; }
.petunjuk ol { margin: 0; padding-left: 18px; }
.bab { font-weight: bold; margin: 20px 0 12px; padding: 2px 6px; border-left: 4px solid #000; background: #eee;
       -webkit-print-color-adjust: exact; print-color-adjust: exact; break-after: avoid; }
.soal { display: grid; grid-template-columns: 30px 1fr; align-items: baseline; margin-bottom: 24px; break-inside: avoid; }
.opsi { display: grid; gap: 5px 10px; margin-top: 7px; }
.opsi.c5 { grid-template-columns: repeat(5, 1fr); }
.opsi.c3 { grid-template-columns: repeat(3, 1fr); }
.opsi.c2 { grid-template-columns: repeat(2, 1fr); }
.opsi.c1 { grid-template-columns: 1fr; }
.opsi div { display: grid; grid-template-columns: 22px 1fr; }
.fig { margin: 6px 0; }
ul.cek, ul.r, ol.r { margin: 4px 0; padding-left: 20px; }
ul.r li, ol.r li { margin: 2px 0; }
.kunci { width: 100%; border-collapse: collapse; margin: 6px 0 14px; text-align: center; }
.kunci td { border: 1px solid #000; padding: 3px 0; width: 10%; }
.bahas { margin-bottom: 18px; break-inside: avoid; border-bottom: 1px solid #bbb; padding-bottom: 12px; }
.bahas .q { display: grid; grid-template-columns: 30px 1fr; align-items: baseline; }
.bahas .ans, .bahas .jaw, .tag { margin: 4px 0 0 30px; }
.bahas .jaw { font-weight: bold; }
.tag { font-size: 10.5pt; font-style: italic; color: #333; }
.bagian { margin: 0 0 34px; }
.bagian h3 { font-size: 13pt; margin: 0 0 10px; padding: 4px 8px; border-left: 5px solid #000; background: #eee;
             -webkit-print-color-adjust: exact; print-color-adjust: exact; break-after: avoid; }
table.rk { width: 100%; border-collapse: collapse; font-size: 11.5pt; table-layout: fixed; }
table.rk th { border: 1px solid #000; background: #d9d9d9; padding: 6px 8px; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
table.rk td { border: 1px solid #000; padding: 8px 9px; vertical-align: top; }
table.rk tr { break-inside: avoid; }
table.rk thead { display: table-header-group; }
table.rk td.no { text-align: center; }
table.rk td.k { font-weight: bold; }
table.rk td.f { overflow-wrap: anywhere; }
table.rk td.ket { font-size: 11pt; }
table.rk .katex-display { margin: .25em 0; }
table.rk .katex { font-size: 1.02em; }
"""

TAIL = """<script>
document.addEventListener("DOMContentLoaded", function () {
  renderMathInElement(document.body, {delimiters: [
    {left: "$$", right: "$$", display: true}, {left: "$", right: "$", display: false}], throwOnError: false});
  document.fonts.ready.then(function () { window.__done = true; });
});
</script></body></html>"""


def head(meta):
    return (f'<!doctype html><html lang="{meta.get("bahasa", "id")}"><head><meta charset="utf-8">'
            f'<link rel="stylesheet" href="{KATEX}/katex.min.css">'
            f'<script src="{KATEX}/katex.min.js"></script>'
            f'<script src="{KATEX}/contrib/auto-render.min.js"></script>'
            f'<style>{CSS}</style></head><body>')


def kop(meta, judul):
    sub = meta.get("subjudul", "")
    return (f'<div class="kop"><h1>{judul}</h1><h2>{meta["mapel"].upper()}</h2>'
            f'<p>{meta["kelas"]}{" &nbsp;|&nbsp; " + sub if sub else ""}</p></div>')


def opsi_html(ops, cols):
    return f'<div class="opsi c{cols}">' + "".join(
        f"<div><span>{h}.</span><span>{esc_math(o)}</span></div>" for h, o in zip(HURUF, ops)) + "</div>"


def html_soal(meta, soal):
    t = T(meta)
    b = [head(meta), kop(meta, meta.get("judul_soal", t["judul_soal"]))]
    kalk = "" if meta.get("kalkulator", False) else t["nokalk"]
    b.append(f"""<table class="id"><tr><td style="width:16%">{t["nama"]}</td><td style="width:42%">: ..................................................</td>
<td style="width:14%">{t["kelas"]}</td><td>: ..................</td></tr>
<tr><td>{t["absen"]}</td><td>: ..........</td><td>{t["waktu"]}</td><td>: {meta.get("waktu", t["waktu_def"])}</td></tr></table>
<div class="petunjuk"><b>{t["petunjuk"]}</b><ol>
<li>{t["p1"]}</li>
<li>{t["p2"].format(n=len(soal))}</li>
<li>{t["p3"]}</li>
<li>{t["p4"]}{kalk}</li></ol></div>""")
    bab = None
    for i, s in enumerate(soal, 1):
        if s["bab"] != bab:
            bab = s["bab"]
            b.append(f'<div class="bab">{bab}</div>')
        b.append(f'<div class="soal"><div>{i}.</div><div>{esc_math(s["soal"])}'
                 f'{opsi_html(s["opsi"], s.get("kolom", 1))}</div></div>')
    b.append(f'<p style="text-align:center;margin-top:18px;font-style:italic">{t["penutup"]}</p>')
    b.append(TAIL)
    return "".join(b)


def html_bahas(meta, soal):
    t = T(meta)
    b = [head(meta), kop(meta, t["judul_bahas"])]
    b.append(f'<p style="font-weight:bold;margin:4px 0 2px">{t["kunci"]}</p><table class="kunci">')
    for r in range(0, len(soal), 10):
        sel = "".join(f"<td>{j+1}. <b>{soal[j]['kunci']}</b></td>" if j < len(soal) else "<td></td>"
                      for j in range(r, r + 10))
        b.append(f"<tr>{sel}</tr>")
    b.append("</table>")
    bab = None
    for i, s in enumerate(soal, 1):
        if s["bab"] != bab:
            bab = s["bab"]
            b.append(f'<div class="bab">{bab}</div>')
        jaw = s["opsi"][HURUF.index(s["kunci"])]
        b.append(f'<div class="bahas"><div class="q"><div>{i}.</div><div>{esc_math(s["soal"])}'
                 f'{opsi_html(s["opsi"], s.get("kolom", 1))}</div></div>'
                 f'<div class="tag">{t["materi"]}: {esc_math(s["materi"])}</div>'
                 f'<div class="ans"><b>{t["bahas"]}:</b><br>{esc_math(s["pembahasan"])}</div>'
                 f'<div class="jaw">{t["jawaban"]}: {s["kunci"]}. &nbsp;{esc_math(jaw)}</div></div>')
    b.append(TAIL)
    return "".join(b)


def html_rangkuman(meta, rangkuman):
    t = T(meta)
    b = [head(meta), kop(meta, t["judul_rk"])]
    if meta.get("pengantar_rangkuman"):
        b.append(f'<p style="margin:2px 0 18px;font-size:11.5pt;text-align:center;font-style:italic">'
                 f'{meta["pengantar_rangkuman"]}</p>')
    w = ("5%", "19%", "48%", "28%")
    for bagian in rangkuman:
        b.append(f'<div class="bagian"><h3>{bagian["bab"]}</h3><table class="rk"><thead><tr>'
                 + "".join(f'<th style="width:{x}">{h}</th>' for x, h in zip(w, t["th"]))
                 + "</tr></thead><tbody>")
        for i, (k, f, ket) in enumerate(bagian["baris"], 1):
            b.append(f'<tr><td class="no">{i}</td><td class="k">{esc_math(k)}</td>'
                     f'<td class="f">{esc_math(split_wide(f))}</td><td class="ket">{esc_math(ket)}</td></tr>')
        b.append("</tbody></table></div>")
    b.append(TAIL)
    return "".join(b)


# ------------------------------------------------------------------ render
def launch(p):
    for ch in ("chrome", "msedge", None):
        try:
            return p.chromium.launch(channel=ch) if ch else p.chromium.launch()
        except Exception:
            continue
    sys.exit("[ERROR] No Chromium browser found. Install Chrome/Edge or run: python -m playwright install chromium")


def render(page, html_str, pdf_path, label, t):
    tmp = pdf_path.with_suffix(".tmp.html")
    tmp.write_text(html_str, encoding="utf-8")
    try:
        page.goto(tmp.as_uri())
        page.wait_for_function("window.__done === true", timeout=60000)
        page.wait_for_timeout(300)
        page.pdf(path=str(pdf_path), format="A4", print_background=True, prefer_css_page_size=True,
                 display_header_footer=True, header_template="<div></div>",
                 footer_template=('<div style="font-family:Times New Roman;font-size:9pt;width:100%;text-align:center;color:#444">'
                                  f'{label} — {t["hal"]} <span class="pageNumber"></span> {t["dari"]} '
                                  '<span class="totalPages"></span></div>'))
    finally:
        tmp.unlink(missing_ok=True)
    print("OK ->", pdf_path)


def preview(pdf_path, out_dir):
    try:
        import pymupdf
    except ImportError:
        print("[INFO] pymupdf not installed, skipping PNG preview (pip install pymupdf).")
        return
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    for i, pg in enumerate(doc, 1):
        pg.get_pixmap(dpi=70).save(out_dir / f"{pdf_path.stem}_{i:02d}.png")
    print(f"   preview {doc.page_count} pages -> {out_dir}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("konten")
    ap.add_argument("--out", default=None, help="output folder (default: folder of the content file)")
    ap.add_argument("--preview", action="store_true", help="save a PNG per page to <out>/_preview")
    a = ap.parse_args()

    path = pathlib.Path(a.konten).resolve()
    meta, soal, rangkuman = load_konten(path)
    validasi(meta, soal, rangkuman)
    out = pathlib.Path(a.out).resolve() if a.out else path.parent
    out.mkdir(parents=True, exist_ok=True)
    t, slug, label = T(meta), meta["slug"], f'{meta["mapel"].title()} {meta["kelas"]}'

    from playwright.sync_api import sync_playwright
    jobs = [(html_soal(meta, soal), out / f'{t["file_soal"]}_{slug}.pdf', f'{t["f_soal"]} {label}'),
            (html_bahas(meta, soal), out / f'{t["file_bahas"]}_{slug}.pdf', f'{t["f_bahas"]} {label}'),
            (html_rangkuman(meta, rangkuman), out / f'{t["file_rk"]}_{slug}.pdf', f'{t["f_rk"]} {label}')]
    with sync_playwright() as p:
        br = launch(p)
        pg = br.new_page()
        for h, pdf, lab in jobs:
            render(pg, h, pdf, lab, t)
            if a.preview:
                preview(pdf, out / "_preview")
        br.close()


if __name__ == "__main__":
    main()
