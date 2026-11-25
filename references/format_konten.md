# Format file konten / Content file format

> **English summary:** the content file is a Python module defining `META`, `SOAL` (questions), and `RANGKUMAN` (summary). Field names are Indonesian, but the values can be in any language: set `META["bahasa"] = "en"` for English labels and write all text in English. Key fields: `bab` = chapter, `materi` = topic, `soal` = question stem, `opsi` = 5 options, `kunci` = answer letter, `kolom` = option columns (5/3/2/1), `pembahasan` = solution. Summary rows are `(concept, formula/theory, notes)`. See `examples/example_english_short.py`.

File konten adalah **modul Python** (bukan JSON) supaya LaTeX bisa ditulis di raw string `r"..."` tanpa menggandakan backslash. Di JSON, `"\frac"` diam-diam menjadi karakter form-feed + `rac`, jadi jangan pakai JSON.

File harus mendefinisikan tiga variabel: `META`, `SOAL`, `RANGKUMAN`.

```python
# -*- coding: utf-8 -*-
META = {
    "bahasa": "id",                             # "id" (Indonesia, default) atau "en" (English): label, footer, nama file
    "mapel": "Matematika Tingkat Lanjut",       # wajib, dicetak kapital di kop
    "kelas": "Kelas XII SMA",                   # wajib
    "slug": "Matematika_TL_Kelas12",            # wajib, dipakai di nama file (tanpa spasi)
    "subjudul": "Lingkaran · Limit · Turunan",  # opsional, baris kecil di kop
    "waktu": "120 menit",                       # opsional (default "120 menit" / "120 minutes")
    "kalkulator": False,                        # False -> petunjuk "Tidak diperkenankan menggunakan kalkulator."
    "judul_soal": "LATIHAN SOAL",               # opsional, mis. "PENILAIAN AKHIR SEMESTER"
    "pengantar_rangkuman": "Ringkasan ...",     # opsional, kalimat miring di bawah kop rangkuman
}

SOAL = [
    {
        "bab": "Lingkaran",                     # judul bab; header bab muncul saat nilainya berganti
        "materi": "Persamaan lingkaran: titik pusat dari bentuk umum",  # label materi di pembahasan
        "soal": r"Titik pusat lingkaran $x^2+y^2-6x+8y-11=0$ adalah ....",
        "opsi": [r"$(-6,\,8)$", r"$(-3,\,4)$", r"$(3,\,4)$", r"$(3,\,-4)$", r"$(6,\,-8)$"],  # tepat 5
        "kunci": "D",                           # A-E
        "kolom": 5,                             # tata letak opsi: 5 (pendek), 3, 2, atau 1 (kalimat panjang)
        "pembahasan": r"""Pusat bentuk umum $\left(-\tfrac{A}{2},-\tfrac{B}{2}\right)$ ...
 $$P(3,\,-4).$$""",
    },
    # ...
]

RANGKUMAN = [
    {
        "bab": "I. LINGKARAN",
        "baris": [
            # (konsep, rumus/teori, keterangan)
            (r"Persamaan lingkaran bentuk baku",
             r"$$x^2+y^2=r^2$$ $$(x-a)^2+(y-b)^2=r^2$$",
             r"Bentuk pertama berpusat di $O(0,0)$ ..."),
        ],
    },
]
```

## Aturan penulisan

**Rumus**
- Inline `$...$`, display (baris sendiri, rata tengah) `$$...$$`. Selalu pakai raw string `r"..."` / `r"""..."""`.
- `<` dan `>` di dalam rumus aman, karena script otomatis mengubahnya ke `\lt` / `\gt`. Di luar rumus, tulis `&lt;` / `&gt;`.
- Pecahan kecil dalam teks: `\tfrac{1}{2}`. Limit/integral besar di soal: `\displaystyle\lim_{x\to\infty}`.
- Bilangan desimal gaya Indonesia di dalam rumus: `2{,}5`. Ribuan: `1.000`.
- Matriks/vektor: `\begin{pmatrix}a\\b\end{pmatrix}`. Fungsi sepotong: `\begin{cases}...\end{cases}`.

**HTML yang boleh dipakai di teks**
- `<b>...</b>` untuk penekanan (mis. "**tidak**", "**di luar**"), `<br>` untuk baris baru.
- Daftar: `<ul class='cek'><li>...</li></ul>` (pembahasan), `<ul class='r'>` / `<ol class='r'>` (rangkuman).
- Gambar: sisipkan SVG di teks soal dalam `<div class='fig'><svg ...>...</svg></div>`. Gunakan `font-family="Times New Roman"`, garis hitam, dan ukuran sekitar 250–330 px lebar. Untuk grafik fungsi, buat SVG lewat kode Python (grid, sumbu dengan panah, label angka, titik penuh `●` / titik kosong `○`), lalu tempel hasil string-nya. Lihat soal 12 dan 32 di contoh.

**Rangkuman**
- Satu blok `$$...$$` per rumus. Dua rumus yang dipisah `\qquad` otomatis dipecah ke baris berbeda, tetapi rumus tunggal yang sangat panjang harus dipecah manual (mis. pisahkan ruas kiri dan `=` ruas kanan ke dua blok `$$`).
- Kolom Rumus/Teori lebarnya kira-kira 48% halaman. Rumus yang lebih lebar dari kira-kira 55 karakter LaTeX sebaiknya dipecah.

**Penomoran bab**
- Header bab di soal/pembahasan diambil dari field `bab` setiap soal (cukup nama, mis. "Turunan dan Aplikasinya").
- Judul bab rangkuman biasanya diberi angka Romawi: "III. TURUNAN DAN APLIKASINYA".
