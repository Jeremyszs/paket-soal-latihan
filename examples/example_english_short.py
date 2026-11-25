# -*- coding: utf-8 -*-
"""SHORT English example (5 questions + 2 summary sections). Shows META["bahasa"] = "en".
Render: python scripts/buat_pdf.py examples/example_english_short.py"""

META = {
    "bahasa": "en",
    "mapel": "Advanced Mathematics",
    "kelas": "Grade 12",
    "subjudul": "Circles · Limits · Derivatives · Integrals",
    "slug": "Advanced_Math_Grade12_Sample",
    "waktu": "20 minutes",
    "kalkulator": False,
    "pengantar_rangkuman": "Key concepts, formulas, and notes for the topics covered in this pack.",
}

SOAL = [
{
    "bab": "Circles",
    "materi": "Centre of a circle from its general equation",
    "soal": r"The centre of the circle $x^2+y^2+4x-10y+20=0$ is ....",
    "opsi": [r"$(-2,\,5)$", r"$(2,\,-5)$", r"$(-4,\,10)$", r"$(4,\,-10)$", r"$(-2,\,-5)$"],
    "kunci": "A",
    "kolom": 5,
    "pembahasan": r"""For $x^2+y^2+Ax+By+C=0$ the centre is $\left(-\tfrac{A}{2},\,-\tfrac{B}{2}\right)$. With $A=4$ and $B=-10$:
 $$\left(-\tfrac{4}{2},\,-\tfrac{-10}{2}\right)=(-2,\,5).$$""",
},
{
    "bab": "Limits",
    "materi": "Limits at infinity of rational functions",
    "soal": r"The value of $\displaystyle\lim_{x\to\infty}\frac{5x^2+1}{2x^2-x}$ is ....",
    "opsi": [r"$0$", r"$\tfrac{1}{2}$", r"$2$", r"$\tfrac{5}{2}$", r"$\infty$"],
    "kunci": "D",
    "kolom": 5,
    "pembahasan": r"""The numerator and denominator have the same highest power, so the limit is the ratio of the leading coefficients:
 $$\lim_{x\to\infty}\frac{5+\frac{1}{x^2}}{2-\frac{1}{x}}=\frac{5}{2}.$$""",
},
{
    "bab": "Derivatives and Their Applications",
    "materi": "Derivative of a polynomial",
    "soal": r"If $f(x)=3x^4-2x^2+5$, then $f'(1)=$ ....",
    "opsi": [r"$4$", r"$6$", r"$8$", r"$10$", r"$12$"],
    "kunci": "C",
    "kolom": 5,
    "pembahasan": r"""Using $\frac{d}{dx}(ax^n)=anx^{n-1}$:
 $$f'(x)=12x^3-4x\;\Rightarrow\;f'(1)=12-4=8.$$""",
},
{
    "bab": "Derivatives and Their Applications",
    "materi": "Optimisation (maximum area)",
    "soal": r"A farmer has 80 m of fencing to enclose a rectangular pen against a long wall, so only three sides need fencing. The maximum area of the pen is ....",
    "opsi": [r"200 m²", r"400 m²", r"600 m²", r"640 m²", r"800 m²"],
    "kunci": "E",
    "kolom": 5,
    "pembahasan": r"""Let the two sides perpendicular to the wall be $x$, so the side parallel to the wall is $80-2x$.
 $$L(x)=x(80-2x)=80x-2x^2,\qquad L'(x)=80-4x=0\Rightarrow x=20.$$
 $L''(x)=-4<0$, so this is a maximum: $L(20)=20\cdot40=800$ m².""",
},
{
    "bab": "Indefinite Integrals",
    "materi": "Indefinite integral of a polynomial",
    "soal": r"$\displaystyle\int(4x^3-6x)\,dx=$ ....",
    "opsi": [r"$4x^4-6x^2+C$", r"$x^4-3x^2+C$", r"$12x^2-6+C$", r"$x^4-6x^2+C$", r"$\tfrac{1}{4}x^4-3x^2+C$"],
    "kunci": "B",
    "kolom": 3,
    "pembahasan": r"""Using $\int ax^n\,dx=\frac{a}{n+1}x^{n+1}+C$:
 $$\int(4x^3-6x)\,dx=\tfrac{4}{4}x^4-\tfrac{6}{2}x^2+C=x^4-3x^2+C.$$""",
},
]

RANGKUMAN = [
{
    "bab": "I. LIMITS",
    "baris": [
        (r"Limits at infinity of rational functions",
         r"$$\lim_{x\to\infty}\frac{ax^n+\dots}{px^m+\dots}=\begin{cases}\dfrac{a}{p}, & n=m\\[4pt] 0, & n<m\\[4pt] \pm\infty, & n>m\end{cases}$$",
         r"$n$ and $m$ are the highest powers of the numerator and denominator."),
        (r"Existence of a limit",
         r"$$\lim_{x\to c}f(x)=L\iff\lim_{x\to c^-}f(x)=\lim_{x\to c^+}f(x)=L$$",
         r"The limit need not equal $f(c)$."),
    ],
},
{
    "bab": "II. DERIVATIVES",
    "baris": [
        (r"Power rule",
         r"$$\frac{d}{dx}(ax^n)=anx^{n-1}$$",
         r"Rewrite roots and fractions as powers first: $\sqrt{x}=x^{1/2}$, $\tfrac{1}{x}=x^{-1}$."),
        (r"Product and chain rules",
         r"$$(uv)'=u'v+uv'$$ $$\big(f(g(x))\big)'=f'(g(x))\,g'(x)$$",
         r"Differentiate from the outermost layer inwards."),
        (r"Stationary points",
         r"$f'(c)=0$ <ul class='r'><li>$f''(c)<0$: maximum</li><li>$f''(c)>0$: minimum</li></ul>",
         r"For word problems, express the quantity in one variable before differentiating."),
    ],
},
]
