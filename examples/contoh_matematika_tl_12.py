# -*- coding: utf-8 -*-
"""CONTOH konten lengkap: Matematika Tingkat Lanjut Kelas XII (40 soal + rangkuman 4 bab).
Dipakai sebagai acuan gaya, tingkat kesulitan, dan format. Render: python scripts/buat_pdf.py examples/contoh_matematika_tl_12.py"""

META = {
    "mapel": "Matematika Tingkat Lanjut",
    "kelas": "Kelas XII SMA",
    "subjudul": "Lingkaran · Limit · Turunan · Integral Tak Tentu",
    "slug": "Matematika_TL_Kelas12",
    "waktu": "120 menit",
    "kalkulator": False,
    "pengantar_rangkuman": "Ringkasan konsep, rumus, dan catatan penting untuk materi Lingkaran, Limit dan Kekontinuan, Turunan dan Aplikasinya, serta Integral Tak Tentu.",
}

SOAL = [
# -------------------- LINGKARAN
{
    "bab": "Lingkaran",
    "materi": "Persamaan lingkaran: titik pusat dari bentuk umum",
    "soal": r'''Titik pusat lingkaran $x^2+y^2-6x+8y-11=0$ adalah ....''',
    "opsi": [r'''$(-6,\,8)$''', r'''$(-3,\,4)$''', r'''$(3,\,4)$''', r'''$(3,\,-4)$''', r'''$(6,\,-8)$'''],
    "kunci": "D",
    "kolom": 5,
    "pembahasan": r'''Bentuk umum $x^2+y^2+Ax+By+C=0$ memiliki pusat $\left(-\tfrac{A}{2},\,-\tfrac{B}{2}\right)$.
 Di sini $A=-6$ dan $B=8$, sehingga
 $$P\left(-\tfrac{-6}{2},\,-\tfrac{8}{2}\right)=(3,\,-4).$$''',
},
{
    "bab": "Lingkaran",
    "materi": "Persamaan lingkaran: konstanta k jika jari-jari diketahui",
    "soal": r'''Lingkaran $x^2+y^2+4x-2y+k=0$ mempunyai jari-jari 3. Nilai $k$ yang memenuhi adalah ....''',
    "opsi": [r'''$-14$''', r'''$-4$''', r'''$4$''', r'''$6$''', r'''$14$'''],
    "kunci": "B",
    "kolom": 5,
    "pembahasan": r'''Pusat lingkaran $\left(-\tfrac{4}{2},\,-\tfrac{-2}{2}\right)=(-2,\,1)$. Jari-jarinya
 $$r=\sqrt{a^2+b^2-C}\;\Rightarrow\;3=\sqrt{(-2)^2+1^2-k}\;\Rightarrow\;9=5-k\;\Rightarrow\;k=-4.$$''',
},
{
    "bab": "Lingkaran",
    "materi": "Persamaan lingkaran: dari pusat dan jari-jari",
    "soal": r'''Persamaan lingkaran yang berpusat di $(2,\,-3)$ dan berjari-jari 5 adalah ....''',
    "opsi": [r'''$x^2+y^2+4x-6y-12=0$''', r'''$x^2+y^2-4x+6y+12=0$''', r'''$x^2+y^2-4x+6y-38=0$''', r'''$x^2+y^2+4x+6y-12=0$''', r'''$x^2+y^2-4x+6y-12=0$'''],
    "kunci": "E",
    "kolom": 2,
    "pembahasan": r'''$$(x-2)^2+(y+3)^2=5^2$$
 $$x^2-4x+4+y^2+6y+9-25=0$$
 $$x^2+y^2-4x+6y-12=0.$$''',
},
{
    "bab": "Lingkaran",
    "materi": "Persamaan lingkaran: berpusat di titik tertentu dan menyinggung garis",
    "soal": r'''Persamaan lingkaran yang berpusat di titik $(3,\,-1)$ dan menyinggung garis $3x-4y+12=0$ adalah ....''',
    "opsi": [r'''$x^2+y^2+6x-2y-15=0$''', r'''$x^2+y^2-6x+2y-5=0$''', r'''$x^2+y^2-6x+2y-15=0$''', r'''$x^2+y^2-6x+2y+5=0$''', r'''$x^2+y^2-6x-2y-15=0$'''],
    "kunci": "C",
    "kolom": 2,
    "pembahasan": r'''Jari-jari = jarak pusat ke garis singgung:
 $$r=\frac{|3(3)-4(-1)+12|}{\sqrt{3^2+(-4)^2}}=\frac{25}{5}=5.$$
 Persamaannya $(x-3)^2+(y+1)^2=25 \Rightarrow x^2-6x+9+y^2+2y+1-25=0$, yaitu
 $$x^2+y^2-6x+2y-15=0.$$''',
},
{
    "bab": "Lingkaran",
    "materi": "Persamaan lingkaran: titik yang terletak pada lingkaran",
    "soal": r'''Diketahui lingkaran $x^2+y^2-4x+2y-20=0$. Titik berikut yang terletak <b>pada</b> lingkaran tersebut adalah ....''',
    "opsi": [r'''$(4,\,3)$''', r'''$(6,\,3)$''', r'''$(3,\,-6)$''', r'''$(7,\,0)$''', r'''$(5,\,3)$'''],
    "kunci": "E",
    "kolom": 5,
    "pembahasan": r'''Titik terletak pada lingkaran jika hasil substitusinya ke ruas kiri bernilai $0$.
 Misalkan $K(x,y)=x^2+y^2-4x+2y-20$.
 <ul class="cek">
 <li>$K(4,3)=16+9-16+6-20=-5$</li>
 <li>$K(6,3)=36+9-24+6-20=7$</li>
 <li>$K(3,-6)=9+36-12-12-20=1$</li>
 <li>$K(7,0)=49+0-28+0-20=1$</li>
 <li>$K(5,3)=25+9-20+6-20=0$ &nbsp;&#10003;</li>
 </ul>
 Jadi titik $(5,\,3)$ terletak pada lingkaran.''',
},
{
    "bab": "Lingkaran",
    "materi": "Kedudukan titik terhadap lingkaran",
    "soal": r'''Di antara titik-titik berikut, titik yang terletak <b>di luar</b> lingkaran $x^2+y^2-2x+4y-20=0$ adalah ....''',
    "opsi": [r'''$(6,\,2)$''', r'''$(4,\,1)$''', r'''$(5,\,1)$''', r'''$(-2,\,1)$''', r'''$(0,\,-6)$'''],
    "kunci": "A",
    "kolom": 5,
    "pembahasan": r'''Misalkan $K(x,y)=x^2+y^2-2x+4y-20$. Titik di luar lingkaran jika $K\gt 0$, pada lingkaran jika $K=0$, di dalam jika $K\lt 0$.
 <ul class="cek">
 <li>$K(6,2)=36+4-12+8-20=16\gt 0$ &nbsp;(di luar) &#10003;</li>
 <li>$K(4,1)=16+1-8+4-20=-7\lt 0$ &nbsp;(di dalam)</li>
 <li>$K(5,1)=25+1-10+4-20=0$ &nbsp;(pada lingkaran)</li>
 <li>$K(-2,1)=4+1+4+4-20=-7\lt 0$ &nbsp;(di dalam)</li>
 <li>$K(0,-6)=0+36-0-24-20=-8\lt 0$ &nbsp;(di dalam)</li>
 </ul>''',
},
{
    "bab": "Lingkaran",
    "materi": "Translasi lingkaran",
    "soal": r'''Lingkaran $x^2+y^2-4x+6y-3=0$ ditranslasikan oleh $T=\begin{pmatrix}-1\\5\end{pmatrix}$. Persamaan bayangan lingkaran tersebut adalah ....''',
    "opsi": [r'''$x^2+y^2+2x+4y-11=0$''', r'''$x^2+y^2-2x-4y-11=0$''', r'''$x^2+y^2-2x-4y+11=0$''', r'''$x^2+y^2-2x+4y-11=0$''', r'''$x^2+y^2-6x+16y+57=0$'''],
    "kunci": "B",
    "kolom": 2,
    "pembahasan": r'''Pusat lingkaran awal $(2,\,-3)$ dan $r=\sqrt{4+9+3}=4$. Translasi hanya menggeser pusat, jari-jari tetap:
 $$(2,-3)\xrightarrow{T}(2-1,\,-3+5)=(1,\,2).$$
 Bayangannya $(x-1)^2+(y-2)^2=16 \Rightarrow x^2+y^2-2x-4y+1+4-16=0$, yaitu
 $$x^2+y^2-2x-4y-11=0.$$''',
},
{
    "bab": "Lingkaran",
    "materi": "Garis singgung lingkaran di titik pada lingkaran",
    "soal": r'''Persamaan garis singgung lingkaran $x^2+y^2-4x+2y-20=0$ di titik $(5,\,3)$ adalah ....''',
    "opsi": [r'''$4x+3y-29=0$''', r'''$3x-4y-3=0$''', r'''$3x+4y+27=0$''', r'''$3x+4y-27=0$''', r'''$4x-3y-11=0$'''],
    "kunci": "D",
    "kolom": 3,
    "pembahasan": r'''Titik $(5,3)$ terletak pada lingkaran (cek: $25+9-20+6-20=0$). Rumus garis singgung di titik $(x_1,y_1)$ pada $x^2+y^2+Ax+By+C=0$:
 $$x_1x+y_1y+\tfrac{A}{2}(x+x_1)+\tfrac{B}{2}(y+y_1)+C=0$$
 $$5x+3y-2(x+5)+1(y+3)-20=0$$
 $$3x+4y-27=0.$$''',
},
{
    "bab": "Lingkaran",
    "materi": "Garis singgung lingkaran dengan gradien tertentu",
    "soal": r'''Persamaan garis singgung lingkaran $x^2+y^2-2x+4y-5=0$ yang sejajar dengan garis $3x-y+2=0$ adalah ....''',
    "opsi": [r'''$y=3x+1$ dan $y=3x-11$''', r'''$y=3x+10$ dan $y=3x-10$''', r'''$y=3x+5$ dan $y=3x-15$''', r'''$y=3x-5$ dan $y=3x+15$''', r'''$y=3x+7$ dan $y=3x-13$'''],
    "kunci": "C",
    "kolom": 1,
    "pembahasan": r'''Pusat $(1,\,-2)$, $r=\sqrt{1+4+5}=\sqrt{10}$. Garis $3x-y+2=0$ bergradien $3$, jadi $m=3$.
 $$y-b=m(x-a)\pm r\sqrt{1+m^2}$$
 $$y+2=3(x-1)\pm\sqrt{10}\cdot\sqrt{10}=3x-3\pm 10$$
 $$y=3x-5\pm 10\;\Rightarrow\; y=3x+5 \;\text{ dan }\; y=3x-15.$$''',
},
{
    "bab": "Lingkaran",
    "materi": "Jarak terdekat titik ke lingkaran",
    "soal": r'''Jarak terdekat titik $P(7,\,10)$ ke lingkaran $x^2+y^2-2x-4y-20=0$ adalah ....''',
    "opsi": [r'''$3$''', r'''$5$''', r'''$8$''', r'''$10$''', r'''$15$'''],
    "kunci": "B",
    "kolom": 5,
    "pembahasan": r'''Pusat $M(1,\,2)$, $r=\sqrt{1+4+20}=5$. Jarak titik ke pusat:
 $$PM=\sqrt{(7-1)^2+(10-2)^2}=\sqrt{36+64}=10.$$
 Karena $PM\gt r$, titik $P$ di luar lingkaran, sehingga jarak terdekatnya $PM-r=10-5=5$.''',
},
{
    "bab": "Lingkaran",
    "materi": "Kedudukan garis terhadap lingkaran",
    "soal": r'''Kedudukan garis $x-y+1=0$ terhadap lingkaran $x^2+y^2-4x+2y-4=0$ adalah ....''',
    "opsi": [r'''memotong lingkaran di dua titik berbeda''', r'''menyinggung lingkaran''', r'''tidak memotong maupun menyinggung lingkaran''', r'''melalui pusat lingkaran''', r'''memotong lingkaran di satu titik dan melalui pusatnya'''],
    "kunci": "A",
    "kolom": 1,
    "pembahasan": r'''Substitusi $y=x+1$ ke persamaan lingkaran:
 $$x^2+(x+1)^2-4x+2(x+1)-4=0 \;\Rightarrow\; 2x^2-1=0.$$
 Diskriminan $D=0^2-4(2)(-1)=8\gt 0$, jadi garis memotong lingkaran di dua titik berbeda.<br>
 (Cara lain: pusat $(2,-1)$, $r=3$, jarak pusat ke garis $\frac{|2+1+1|}{\sqrt2}=2\sqrt2\lt 3$.)''',
},
# -------------------- LIMIT DAN KEKONTINUAN FUNGSI
{
    "bab": "Limit dan Kekontinuan Fungsi",
    "materi": "Limit fungsi dari grafik",
    "soal": r'''Perhatikan grafik fungsi $y=f(x)$ berikut.<div class='fig'><svg width="238" height="212" viewBox="0 0 238 212" font-family="Times New Roman"><defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#000"/></marker></defs><line x1="15" y1="197" x2="15" y2="15" stroke="#d0d0d0" stroke-width="0.7"/><line x1="41" y1="197" x2="41" y2="15" stroke="#d0d0d0" stroke-width="0.7"/><line x1="67" y1="197" x2="67" y2="15" stroke="#d0d0d0" stroke-width="0.7"/><line x1="93" y1="197" x2="93" y2="15" stroke="#d0d0d0" stroke-width="0.7"/><line x1="119" y1="197" x2="119" y2="15" stroke="#d0d0d0" stroke-width="0.7"/><line x1="145" y1="197" x2="145" y2="15" stroke="#d0d0d0" stroke-width="0.7"/><line x1="171" y1="197" x2="171" y2="15" stroke="#d0d0d0" stroke-width="0.7"/><line x1="197" y1="197" x2="197" y2="15" stroke="#d0d0d0" stroke-width="0.7"/><line x1="223" y1="197" x2="223" y2="15" stroke="#d0d0d0" stroke-width="0.7"/><line x1="15" y1="197" x2="223" y2="197" stroke="#d0d0d0" stroke-width="0.7"/><line x1="15" y1="171" x2="223" y2="171" stroke="#d0d0d0" stroke-width="0.7"/><line x1="15" y1="145" x2="223" y2="145" stroke="#d0d0d0" stroke-width="0.7"/><line x1="15" y1="119" x2="223" y2="119" stroke="#d0d0d0" stroke-width="0.7"/><line x1="15" y1="93" x2="223" y2="93" stroke="#d0d0d0" stroke-width="0.7"/><line x1="15" y1="67" x2="223" y2="67" stroke="#d0d0d0" stroke-width="0.7"/><line x1="15" y1="41" x2="223" y2="41" stroke="#d0d0d0" stroke-width="0.7"/><line x1="15" y1="15" x2="223" y2="15" stroke="#d0d0d0" stroke-width="0.7"/><line x1="15" y1="145" x2="231" y2="145" stroke="#000" stroke-width="1.2" marker-end="url(#ar)"/><line x1="67" y1="197" x2="67" y2="7" stroke="#000" stroke-width="1.2" marker-end="url(#ar)"/><text x="15" y="159" font-size="11" text-anchor="middle">&#8722;2</text><text x="41" y="159" font-size="11" text-anchor="middle">&#8722;1</text><text x="93" y="159" font-size="11" text-anchor="middle">1</text><text x="119" y="159" font-size="11" text-anchor="middle">2</text><text x="145" y="159" font-size="11" text-anchor="middle">3</text><text x="171" y="159" font-size="11" text-anchor="middle">4</text><text x="197" y="159" font-size="11" text-anchor="middle">5</text><text x="61" y="201" font-size="11" text-anchor="end">&#8722;2</text><text x="61" y="175" font-size="11" text-anchor="end">&#8722;1</text><text x="61" y="123" font-size="11" text-anchor="end">1</text><text x="61" y="97" font-size="11" text-anchor="end">2</text><text x="61" y="71" font-size="11" text-anchor="end">3</text><text x="61" y="45" font-size="11" text-anchor="end">4</text><text x="61" y="159" font-size="11" text-anchor="end">0</text><text x="227" y="139" font-size="12" font-style="italic">x</text><text x="73" y="17" font-size="12" font-style="italic">y</text><line x1="15" y1="171" x2="119" y2="67" stroke="#000" stroke-width="2"/><line x1="119" y1="67" x2="210.0" y2="158.0" stroke="#000" stroke-width="2"/><circle cx="119" cy="67" r="4" fill="#fff" stroke="#000" stroke-width="1.6"/><circle cx="119" cy="119" r="4" fill="#000"/><line x1="119" y1="145" x2="119" y2="67" stroke="#000" stroke-dasharray="3 3" stroke-width="0.8"/><text x="176.20000000000002" y="82.60000000000001" font-size="13" font-style="italic">y = f(x)</text></svg></div>Nilai $\displaystyle\lim_{x\to 2} f(x)+f(2)$ adalah ....''',
    "opsi": [r'''$1$''', r'''$2$''', r'''$3$''', r'''$4$''', r'''tidak ada'''],
    "kunci": "D",
    "kolom": 5,
    "pembahasan": r'''Dari grafik: saat $x$ mendekati $2$ dari kiri maupun kanan, nilai $f(x)$ mendekati $3$ (lingkaran kosong), sehingga
 $$\lim_{x\to2^-}f(x)=\lim_{x\to2^+}f(x)=3\;\Rightarrow\;\lim_{x\to2}f(x)=3.$$
 Nilai fungsinya ditunjukkan titik penuh, yaitu $f(2)=1$. Jadi $3+1=4$.''',
},
{
    "bab": "Limit dan Kekontinuan Fungsi",
    "materi": "Limit tak hingga fungsi pecahan (aljabar)",
    "soal": r'''Nilai $\displaystyle\lim_{x\to\infty}\frac{4x^3-2x+1}{2x^3+5x^2-3}$ adalah ....''',
    "opsi": [r'''$0$''', r'''$\tfrac{1}{2}$''', r'''$2$''', r'''$4$''', r'''$\infty$'''],
    "kunci": "C",
    "kolom": 5,
    "pembahasan": r'''Pangkat tertinggi pembilang dan penyebut sama (pangkat 3), sehingga limitnya adalah perbandingan koefisien pangkat tertinggi:
 $$\lim_{x\to\infty}\frac{4-\frac{2}{x^2}+\frac{1}{x^3}}{2+\frac{5}{x}-\frac{3}{x^3}}=\frac{4}{2}=2.$$''',
},
{
    "bab": "Limit dan Kekontinuan Fungsi",
    "materi": "Limit tak hingga bentuk akar dan pecahan",
    "soal": r'''Nilai $\displaystyle\lim_{x\to\infty}\frac{2x+\sqrt{9x^2+1}}{4x-3}$ adalah ....''',
    "opsi": [r'''$\tfrac{1}{2}$''', r'''$\tfrac{3}{4}$''', r'''$1$''', r'''$\tfrac{5}{4}$''', r'''$\tfrac{5}{2}$'''],
    "kunci": "D",
    "kolom": 5,
    "pembahasan": r'''Bagi pembilang dan penyebut dengan $x$ (untuk $x\gt 0$, $\sqrt{9x^2+1}=x\sqrt{9+\frac1{x^2}}$):
 $$\lim_{x\to\infty}\frac{2+\sqrt{9+\frac{1}{x^2}}}{4-\frac{3}{x}}=\frac{2+3}{4}=\frac{5}{4}.$$''',
},
{
    "bab": "Limit dan Kekontinuan Fungsi",
    "materi": "Limit tak hingga selisih dua bentuk akar",
    "soal": r'''Nilai $\displaystyle\lim_{x\to\infty}\left(\sqrt{4x^2+3x-1}-\sqrt{4x^2-5x+2}\right)$ adalah ....''',
    "opsi": [r'''$\tfrac{1}{2}$''', r'''$1$''', r'''$2$''', r'''$4$''', r'''$8$'''],
    "kunci": "C",
    "kolom": 5,
    "pembahasan": r'''Untuk bentuk $\displaystyle\lim_{x\to\infty}\left(\sqrt{ax^2+bx+c}-\sqrt{ax^2+qx+r}\right)=\frac{b-q}{2\sqrt a}$ (koefisien $x^2$ sama).
 $$\frac{3-(-5)}{2\sqrt4}=\frac{8}{4}=2.$$''',
},
{
    "bab": "Limit dan Kekontinuan Fungsi",
    "materi": "Limit tak hingga selisih bentuk akar dan linear",
    "soal": r'''Nilai $\displaystyle\lim_{x\to\infty}\left(\sqrt{9x^2-6x+5}-(3x+1)\right)$ adalah ....''',
    "opsi": [r'''$-3$''', r'''$-2$''', r'''$-1$''', r'''$0$''', r'''$2$'''],
    "kunci": "B",
    "kolom": 5,
    "pembahasan": r'''Ubah bentuk linear menjadi akar: $3x+1=\sqrt{(3x+1)^2}=\sqrt{9x^2+6x+1}$ (untuk $x$ besar).
 $$\lim_{x\to\infty}\left(\sqrt{9x^2-6x+5}-\sqrt{9x^2+6x+1}\right)=\frac{-6-6}{2\sqrt9}=\frac{-12}{6}=-2.$$''',
},
{
    "bab": "Limit dan Kekontinuan Fungsi",
    "materi": "Limit fungsi trigonometri",
    "soal": r'''Nilai $\displaystyle\lim_{x\to 0}\frac{\sin 4x\cdot\tan 3x}{x\sin 6x}$ adalah ....''',
    "opsi": [r'''$\tfrac{1}{3}$''', r'''$\tfrac{1}{2}$''', r'''$1$''', r'''$\tfrac{3}{2}$''', r'''$2$'''],
    "kunci": "E",
    "kolom": 5,
    "pembahasan": r'''Gunakan $\displaystyle\lim_{x\to0}\frac{\sin ax}{bx}=\lim_{x\to0}\frac{\tan ax}{bx}=\frac ab$:
 $$\lim_{x\to0}\frac{\sin4x}{x}\cdot\frac{\tan3x}{\sin6x}=4\cdot\frac{3}{6}=2.$$''',
},
{
    "bab": "Limit dan Kekontinuan Fungsi",
    "materi": "Limit fungsi trigonometri (bentuk 1 − cos)",
    "soal": r'''Nilai $\displaystyle\lim_{x\to 0}\frac{1-\cos 4x}{x\tan 2x}$ adalah ....''',
    "opsi": [r'''$\tfrac{1}{2}$''', r'''$1$''', r'''$2$''', r'''$3$''', r'''$4$'''],
    "kunci": "E",
    "kolom": 5,
    "pembahasan": r'''Gunakan identitas $1-\cos 2A=2\sin^2A$, sehingga $1-\cos4x=2\sin^2 2x$.
 $$\lim_{x\to0}\frac{2\sin2x\cdot\sin2x}{x\tan2x}=2\cdot\frac{2}{1}\cdot\frac{2}{2}=4.$$''',
},
{
    "bab": "Limit dan Kekontinuan Fungsi",
    "materi": "Limit fungsi trigonometri (selisih kosinus dan tangen)",
    "soal": r'''Nilai $\displaystyle\lim_{x\to 0}\frac{\cos 5x-\cos 3x}{x\tan 2x}$ adalah ....''',
    "opsi": [r'''$-4$''', r'''$-2$''', r'''$0$''', r'''$2$''', r'''$4$'''],
    "kunci": "A",
    "kolom": 5,
    "pembahasan": r'''Gunakan $\cos A-\cos B=-2\sin\frac{A+B}{2}\sin\frac{A-B}{2}$:
 $$\cos5x-\cos3x=-2\sin4x\sin x.$$
 $$\lim_{x\to0}\frac{-2\sin4x\sin x}{x\tan2x}=-2\cdot\frac{4\cdot1}{1\cdot2}=-4.$$''',
},
{
    "bab": "Limit dan Kekontinuan Fungsi",
    "materi": "Kekontinuan fungsi di satu titik",
    "soal": r'''Diketahui fungsi $f(x)=\begin{cases}\dfrac{x^2+x-6}{x-2}, & x\neq 2\\[6pt] 2p-1, & x=2\end{cases}$<br>Agar $f$ kontinu di $x=2$, nilai $p$ adalah ....''',
    "opsi": [r'''$3$''', r'''$4$''', r'''$5$''', r'''$6$''', r'''$9$'''],
    "kunci": "A",
    "kolom": 5,
    "pembahasan": r'''Syarat kontinu di $x=2$: $\displaystyle\lim_{x\to2}f(x)=f(2)$.
 $$\lim_{x\to2}\frac{(x+3)(x-2)}{x-2}=\lim_{x\to2}(x+3)=5.$$
 Maka $2p-1=5\Rightarrow p=3$.''',
},
{
    "bab": "Limit dan Kekontinuan Fungsi",
    "materi": "Limit bentuk eksponen (bilangan e)",
    "soal": r'''Nilai $\displaystyle\lim_{x\to\infty}\left(\frac{x+1}{x-2}\right)^{x}$ adalah ....''',
    "opsi": [r'''$e^{-3}$''', r'''$e^{-1}$''', r'''$e$''', r'''$e^{2}$''', r'''$e^{3}$'''],
    "kunci": "E",
    "kolom": 5,
    "pembahasan": r'''Tulis $\dfrac{x+1}{x-2}=1+\dfrac{3}{x-2}$. Dengan $\displaystyle\lim_{x\to\infty}\left(1+\frac{a}{x}\right)^{bx}=e^{ab}$:
 $$\lim_{x\to\infty}\left(1+\frac{3}{x-2}\right)^{x}=e^{3\cdot1}=e^{3}$$
 (pergeseran $x-2$ tidak memengaruhi nilai limit saat $x\to\infty$).''',
},
# -------------------- TURUNAN DAN APLIKASINYA
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Turunan fungsi aljabar (perkalian dan aturan rantai)",
    "soal": r'''Diketahui $f(x)=(x+1)(2x-1)^3$. Nilai $f'(1)$ adalah ....''',
    "opsi": [r'''$13$''', r'''$15$''', r'''$19$''', r'''$21$''', r'''$25$'''],
    "kunci": "A",
    "kolom": 5,
    "pembahasan": r'''Aturan perkalian $(uv)'=u'v+uv'$ dengan $u=x+1$, $v=(2x-1)^3$, dan $v'=3(2x-1)^2\cdot2=6(2x-1)^2$ (aturan rantai).
 $$f'(x)=(2x-1)^3+(x+1)\cdot6(2x-1)^2=(2x-1)^2(8x+5)$$
 $$f'(1)=(1)^2(13)=13.$$''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Turunan fungsi bentuk akar",
    "soal": r'''Turunan pertama fungsi $f(x)=\sqrt{3x^2+4x+2}$ di $x=1$ adalah ....''',
    "opsi": [r'''$\tfrac{2}{3}$''', r'''$1$''', r'''$\tfrac{4}{3}$''', r'''$\tfrac{5}{3}$''', r'''$\tfrac{10}{3}$'''],
    "kunci": "D",
    "kolom": 5,
    "pembahasan": r'''$f(x)=(3x^2+4x+2)^{1/2}\Rightarrow f'(x)=\dfrac{6x+4}{2\sqrt{3x^2+4x+2}}$.
 $$f'(1)=\frac{6+4}{2\sqrt9}=\frac{10}{6}=\frac{5}{3}.$$''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Aplikasi turunan: persamaan garis singgung kurva",
    "soal": r'''Persamaan garis singgung kurva $y=x^3-3x^2+2$ di titik yang berabsis $3$ adalah ....''',
    "opsi": [r'''$y=9x+25$''', r'''$y=9x-25$''', r'''$y=9x-27$''', r'''$y=3x-7$''', r'''$y=9x-2$'''],
    "kunci": "B",
    "kolom": 3,
    "pembahasan": r'''Ordinat: $y(3)=27-27+2=2$, titik singgung $(3,\,2)$. Gradien: $y'=3x^2-6x\Rightarrow m=27-18=9$.
 $$y-2=9(x-3)\;\Rightarrow\;y=9x-25.$$''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Aplikasi turunan: fungsi naik",
    "soal": r'''Fungsi $f(x)=x^3+3x^2-9x+5$ naik pada interval ....''',
    "opsi": [r'''$-3\lt x\lt 1$''', r'''$-1\lt x\lt 3$''', r'''$x\lt -1$ atau $x\gt 3$''', r'''$x\lt -3$ atau $x\gt 1$''', r'''$x\gt 1$'''],
    "kunci": "D",
    "kolom": 3,
    "pembahasan": r'''Fungsi naik jika $f'(x)\gt 0$:
 $$f'(x)=3x^2+6x-9=3(x+3)(x-1)\gt 0.$$
 Pembuat nol $x=-3$ dan $x=1$. Uji tanda: $+\;(-3)\;-\;(1)\;+$. Jadi $f$ naik pada $x\lt -3$ atau $x\gt 1$.''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Aplikasi turunan: nilai maksimum dan minimum (kontekstual)",
    "soal": r'''Sebuah toko sepatu menjual $x$ pasang sepatu per bulan dengan pendapatan $R(x)=(200x-x^2)$ ribu rupiah dan biaya total $C(x)=(x^2-40x+1.000)$ ribu rupiah. Keuntungan maksimum yang dapat diperoleh toko tersebut setiap bulan adalah ....''',
    "opsi": [r'''Rp5.200.000,00''', r'''Rp6.000.000,00''', r'''Rp6.200.000,00''', r'''Rp7.200.000,00''', r'''Rp8.400.000,00'''],
    "kunci": "C",
    "kolom": 3,
    "pembahasan": r'''Keuntungan $K(x)=R(x)-C(x)=200x-x^2-x^2+40x-1.000=-2x^2+240x-1.000$.<br>
 Maksimum saat $K'(x)=0$: $-4x+240=0\Rightarrow x=60$.
 $$K(60)=-2(3.600)+240(60)-1.000=-7.200+14.400-1.000=6.200\text{ (ribu)}.$$
 Keuntungan maksimum Rp6.200.000,00.''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Turunan fungsi trigonometri",
    "soal": r'''Diketahui $f(x)=3\sin x-2\cos x+\tan x$. Nilai $f'\!\left(\tfrac{\pi}{3}\right)$ adalah ....''',
    "opsi": [r'''$\tfrac{3}{2}+\sqrt3$''', r'''$\tfrac{5}{2}+\sqrt3$''', r'''$\tfrac{11}{2}-\sqrt3$''', r'''$\tfrac{7}{2}+\sqrt3$''', r'''$\tfrac{11}{2}+\sqrt3$'''],
    "kunci": "E",
    "kolom": 5,
    "pembahasan": r'''$$f'(x)=3\cos x+2\sin x+\sec^2x$$
 $$f'\!\left(\tfrac{\pi}{3}\right)=3\cdot\tfrac12+2\cdot\tfrac{\sqrt3}{2}+\frac{1}{\left(\frac12\right)^2}=\tfrac32+\sqrt3+4=\tfrac{11}{2}+\sqrt3.$$''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Turunan kedua fungsi trigonometri",
    "soal": r'''Jika $f(x)=\cos^2 2x$, nilai $f''\!\left(\tfrac{\pi}{12}\right)$ adalah ....''',
    "opsi": [r'''$-8$''', r'''$-4$''', r'''$-2$''', r'''$4$''', r'''$8$'''],
    "kunci": "B",
    "kolom": 5,
    "pembahasan": r'''$f'(x)=2\cos2x\cdot(-\sin2x)\cdot2=-2\sin4x$ (memakai $2\sin A\cos A=\sin2A$).
 $$f''(x)=-8\cos4x$$
 $$f''\!\left(\tfrac{\pi}{12}\right)=-8\cos\tfrac{\pi}{3}=-8\cdot\tfrac12=-4.$$''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Turunan perkalian fungsi aljabar dan trigonometri",
    "soal": r'''Turunan pertama fungsi $f(x)=x^2\sin x$ adalah ....''',
    "opsi": [r'''$f'(x)=2x\sin x+x^2\cos x$''', r'''$f'(x)=2x\cos x+x^2\sin x$''', r'''$f'(x)=2x\sin x-x^2\cos x$''', r'''$f'(x)=2x\cos x-x^2\sin x$''', r'''$f'(x)=2x\cos x$'''],
    "kunci": "A",
    "kolom": 2,
    "pembahasan": r'''Aturan perkalian dengan $u=x^2$ ($u'=2x$) dan $v=\sin x$ ($v'=\cos x$):
 $$f'(x)=u'v+uv'=2x\sin x+x^2\cos x.$$''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Turunan trigonometri dengan aturan rantai",
    "soal": r'''Turunan pertama fungsi $f(x)=\sin^3(2x-1)$ adalah ....''',
    "opsi": [r'''$3\sin^2(2x-1)\cos(2x-1)$''', r'''$6\sin(2x-1)\cos^2(2x-1)$''', r'''$-6\sin^2(2x-1)\cos(2x-1)$''', r'''$6\sin^2(2x-1)\cos(2x-1)$''', r'''$2\sin^2(2x-1)\cos(2x-1)$'''],
    "kunci": "D",
    "kolom": 2,
    "pembahasan": r'''Aturan rantai tiga lapis: pangkat $\to$ sinus $\to$ fungsi linear.
 $$f'(x)=3\sin^2(2x-1)\cdot\cos(2x-1)\cdot2=6\sin^2(2x-1)\cos(2x-1).$$''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Garis singgung kurva trigonometri",
    "soal": r'''Persamaan garis singgung kurva $y=2\sin x+\cos x$ di titik yang berabsis $\tfrac{\pi}{2}$ adalah ....''',
    "opsi": [r'''$y=x-\tfrac{\pi}{2}+2$''', r'''$y=-x+\tfrac{\pi}{2}-2$''', r'''$y=-x+\tfrac{\pi}{2}+2$''', r'''$y=-2x+\pi+2$''', r'''$y=x+\tfrac{\pi}{2}+2$'''],
    "kunci": "C",
    "kolom": 3,
    "pembahasan": r'''Ordinat: $y\left(\tfrac\pi2\right)=2(1)+0=2$. Gradien: $y'=2\cos x-\sin x\Rightarrow m=0-1=-1$.
 $$y-2=-1\left(x-\tfrac{\pi}{2}\right)\;\Rightarrow\;y=-x+\tfrac{\pi}{2}+2.$$''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Masalah optimasi (luas maksimum trapesium)",
    "soal": r'''Sebuah talang air dibuat dari lembaran seng selebar 30 cm. Lembaran itu dibagi menjadi tiga bagian sama lebar, lalu kedua sisinya ditekuk sehingga penampang talang berbentuk trapesium sama kaki seperti gambar. Sudut kemiringan dinding talang terhadap garis horizontal adalah $\theta$.<div class='fig'><svg width="330" height="135" viewBox="0 0 330 135" font-family="Times New Roman" font-size="13">
  <polyline points="70,20 120,110 210,110 260,20" fill="none" stroke="#000" stroke-width="2.2"/>
  <line x1="210" y1="110" x2="285" y2="110" stroke="#000" stroke-dasharray="4 3" stroke-width="0.9"/>
  <path d="M240,110 A30,30 0 0 0 225,84" fill="none" stroke="#000" stroke-width="0.9"/>
  <text x="243" y="100" font-style="italic">&#952;</text>
  <path d="M90,110 A30,30 0 0 1 105,84" fill="none" stroke="#000" stroke-width="0.9"/>
  <line x1="45" y1="110" x2="120" y2="110" stroke="#000" stroke-dasharray="4 3" stroke-width="0.9"/>
  <text x="78" y="100" font-style="italic">&#952;</text>
  <text x="148" y="127">10 cm</text>
  <text x="38" y="68">10 cm</text>
  <text x="252" y="68">10 cm</text>
</svg></div>Luas penampang maksimum talang tersebut adalah ....''',
    "opsi": [r'''$25\sqrt3$ cm²''', r'''$50$ cm²''', r'''$50\sqrt3$ cm²''', r'''$75$ cm²''', r'''$75\sqrt3$ cm²'''],
    "kunci": "E",
    "kolom": 5,
    "pembahasan": r'''Alas bawah $10$, tinggi $10\sin\theta$, alas atas $10+2\cdot10\cos\theta$.
 $$L(\theta)=\frac{10+(10+20\cos\theta)}{2}\cdot10\sin\theta=100\sin\theta\,(1+\cos\theta).$$
 $$L'(\theta)=100(\cos\theta+\cos^2\theta-\sin^2\theta)=100(2\cos\theta-1)(\cos\theta+1)=0.$$
 Untuk $0\lt \theta\lt \tfrac{\pi}{2}$ diperoleh $\cos\theta=\tfrac12$, yaitu $\theta=60^\circ$.
 $$L_{\max}=100\cdot\tfrac{\sqrt3}{2}\cdot\tfrac32=75\sqrt3\text{ cm}^2.$$''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Turunan fungsi eksponen",
    "soal": r'''Turunan pertama fungsi $f(x)=(x+1)e^{2x}$ adalah ....''',
    "opsi": [r'''$(2x+3)e^{2x}$''', r'''$(2x+1)e^{2x}$''', r'''$(x+2)e^{2x}$''', r'''$2(x+1)e^{2x}$''', r'''$(x+3)e^{2x}$'''],
    "kunci": "A",
    "kolom": 5,
    "pembahasan": r'''Dengan $\left(e^{u}\right)'=u'e^{u}$ dan aturan perkalian:
 $$f'(x)=1\cdot e^{2x}+(x+1)\cdot2e^{2x}=(1+2x+2)e^{2x}=(2x+3)e^{2x}.$$''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Turunan fungsi logaritma",
    "soal": r'''Jika $f(x)=\ln(x^2+5)$, nilai $f'(2)$ adalah ....''',
    "opsi": [r'''$\tfrac{1}{9}$''', r'''$\tfrac{2}{9}$''', r'''$\tfrac{4}{9}$''', r'''$\tfrac{4}{5}$''', r'''$\tfrac{9}{4}$'''],
    "kunci": "C",
    "kolom": 5,
    "pembahasan": r'''Dengan $\left(\ln u\right)'=\dfrac{u'}{u}$:
 $$f'(x)=\frac{2x}{x^2+5}\;\Rightarrow\;f'(2)=\frac{4}{9}.$$''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Turunan fungsi eksponen berpangkat fungsi",
    "soal": r'''Diketahui $f(x)=3^{x^2-2x}$. Nilai $f'(2)$ adalah ....''',
    "opsi": [r'''$\ln3$''', r'''$2\ln3$''', r'''$3\ln3$''', r'''$2$''', r'''$6\ln3$'''],
    "kunci": "B",
    "kolom": 5,
    "pembahasan": r'''Dengan $\left(a^{u}\right)'=u'\cdot a^{u}\ln a$:
 $$f'(x)=(2x-2)\cdot3^{x^2-2x}\ln3$$
 $$f'(2)=(2)\cdot3^{0}\ln3=2\ln3.$$''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Titik belok kurva",
    "soal": r'''Titik belok kurva $f(x)=x^3-6x^2+9x+1$ adalah ....''',
    "opsi": [r'''$(1,\,5)$''', r'''$(3,\,1)$''', r'''$(2,\,1)$''', r'''$(2,\,3)$''', r'''$(-2,\,-49)$'''],
    "kunci": "D",
    "kolom": 5,
    "pembahasan": r'''Titik belok terjadi saat $f''(x)=0$ dan tanda $f''$ berubah.
 $$f'(x)=3x^2-12x+9,\qquad f''(x)=6x-12=0\Rightarrow x=2.$$
 $f''\lt 0$ untuk $x\lt 2$ dan $f''\gt 0$ untuk $x\gt 2$ (tanda berubah). $f(2)=8-24+18+1=3$, jadi titik beloknya $(2,\,3)$.''',
},
{
    "bab": "Turunan dan Aplikasinya",
    "materi": "Kecekungan kurva",
    "soal": r'''Kurva $f(x)=x^4-6x^2+5$ cekung ke bawah pada interval ....''',
    "opsi": [r'''$x\lt -1$ atau $x\gt 1$''', r'''$-1\lt x\lt 1$''', r'''$-\sqrt3\lt x\lt \sqrt3$''', r'''$x\gt 1$''', r'''$0\lt x\lt 1$'''],
    "kunci": "B",
    "kolom": 3,
    "pembahasan": r'''Cekung ke bawah jika $f''(x)\lt 0$.
 $$f'(x)=4x^3-12x,\qquad f''(x)=12x^2-12=12(x+1)(x-1)\lt 0.$$
 Uji tanda: $+\;(-1)\;-\;(1)\;+$. Jadi kurva cekung ke bawah pada $-1\lt x\lt 1$.''',
},
# -------------------- INTEGRAL TAK TENTU
{
    "bab": "Integral Tak Tentu",
    "materi": "Integral tak tentu fungsi polinom",
    "soal": r'''Hasil dari $\displaystyle\int(3x^2-2)(x+1)\,dx$ adalah ....''',
    "opsi": [r'''$\tfrac34x^4+x^3-2x+C$''', r'''$x^4+x^3-x^2-2x+C$''', r'''$\tfrac34x^4+x^3-x^2-2x+C$''', r'''$\tfrac34x^4+x^3-x^2+2x+C$''', r'''$3x^4+3x^3-2x^2-2x+C$'''],
    "kunci": "C",
    "kolom": 2,
    "pembahasan": r'''Jabarkan dahulu: $(3x^2-2)(x+1)=3x^3+3x^2-2x-2$. Dengan $\int x^n\,dx=\frac{x^{n+1}}{n+1}+C$:
 $$\int(3x^3+3x^2-2x-2)\,dx=\tfrac34x^4+x^3-x^2-2x+C.$$''',
},
{
    "bab": "Integral Tak Tentu",
    "materi": "Integral tak tentu: menentukan fungsi dari turunan dan nilai awal",
    "soal": r'''Diketahui $f'(x)=6x^2-2x+1$ dan $f(1)=5$. Nilai $f(2)$ adalah ....''',
    "opsi": [r'''$9$''', r'''$11$''', r'''$14$''', r'''$15$''', r'''$17$'''],
    "kunci": "E",
    "kolom": 5,
    "pembahasan": r'''$$f(x)=\int(6x^2-2x+1)\,dx=2x^3-x^2+x+C.$$
 $f(1)=2-1+1+C=5\Rightarrow C=3$, sehingga $f(x)=2x^3-x^2+x+3$.
 $$f(2)=16-4+2+3=17.$$''',
},
{
    "bab": "Integral Tak Tentu",
    "materi": "Integral tak tentu dengan substitusi",
    "soal": r'''Hasil dari $\displaystyle\int 6x^2\sqrt{x^3+2}\,dx$ adalah ....''',
    "opsi": [r'''$\tfrac43(x^3+2)\sqrt{x^3+2}+C$''', r'''$\tfrac23(x^3+2)\sqrt{x^3+2}+C$''', r'''$\tfrac49(x^3+2)\sqrt{x^3+2}+C$''', r'''$2(x^3+2)\sqrt{x^3+2}+C$''', r'''$\tfrac34(x^3+2)\sqrt{x^3+2}+C$'''],
    "kunci": "A",
    "kolom": 2,
    "pembahasan": r'''Misalkan $u=x^3+2$, maka $du=3x^2\,dx$, sehingga $6x^2\,dx=2\,du$.
 $$\int2\sqrt u\,du=2\cdot\tfrac23u^{3/2}+C=\tfrac43(x^3+2)\sqrt{x^3+2}+C.$$''',
},
]

RANGKUMAN = [
{
    "bab": "I. LINGKARAN",
    "baris": [
        (r'''Persamaan lingkaran bentuk baku''',
         r'''$$x^2+y^2=r^2$$ $$(x-a)^2+(y-b)^2=r^2$$''',
         r'''Bentuk pertama berpusat di $O(0,0)$. Bentuk kedua berpusat di $P(a,b)$ dengan jari-jari $r$.'''),
        (r'''Bentuk umum dan titik pusat''',
         r'''$$x^2+y^2+Ax+By+C=0$$ $$P\left(-\tfrac{A}{2},\,-\tfrac{B}{2}\right)$$''',
         r'''Koefisien $x^2$ dan $y^2$ harus sama dengan 1. Jika belum, bagi dulu seluruh persamaan.'''),
        (r'''Jari-jari dari bentuk umum''',
         r'''$$r=\sqrt{\tfrac{A^2}{4}+\tfrac{B^2}{4}-C}=\sqrt{a^2+b^2-C}$$''',
         r'''Lingkaran nyata jika $\tfrac{A^2}{4}+\tfrac{B^2}{4}-C>0$. Rumus ini dipakai untuk mencari konstanta yang belum diketahui jika $r$ diketahui.'''),
        (r'''Menyusun persamaan dari pusat dan jari-jari''',
         r'''Substitusi $(a,b)$ dan $r$ ke $(x-a)^2+(y-b)^2=r^2$, lalu jabarkan: $$x^2+y^2-2ax-2by+(a^2+b^2-r^2)=0$$''',
         r'''Jadi $A=-2a$, $B=-2b$, $C=a^2+b^2-r^2$.'''),
        (r'''Lingkaran yang menyinggung garis''',
         r'''Jari-jari = jarak pusat $(a,b)$ ke garis $px+qy+c=0$: $$r=\frac{|pa+qb+c|}{\sqrt{p^2+q^2}}$$''',
         r'''Menyinggung sumbu $X$: $r=|b|$. Menyinggung sumbu $Y$: $r=|a|$.'''),
        (r'''Titik pada lingkaran''',
         r'''Titik $(x_1,y_1)$ terletak pada lingkaran jika $$(x_1-a)^2+(y_1-b)^2=r^2$$''',
         r'''Untuk bentuk umum: substitusi titik ke ruas kiri, hasilnya harus $0$.'''),
        (r'''Kedudukan titik terhadap lingkaran''',
         r'''Misalkan $K=x_1^2+y_1^2+Ax_1+By_1+C$. <ul class='r'><li>$K<0$: di dalam</li><li>$K=0$: pada lingkaran</li><li>$K>0$: di luar</li></ul>''',
         r'''Setara dengan membandingkan jarak titik ke pusat ($d$) dengan $r$: $d<r$, $d=r$, $d>r$.'''),
        (r'''Translasi lingkaran''',
         r'''Translasi $T=\begin{pmatrix}h\\k\end{pmatrix}$: $$(x,y)\to(x+h,\;y+k)$$ Pusat $(a,b)\to(a+h,\;b+k)$''',
         r'''Jari-jari tidak berubah. Cara cepat: ganti $x$ dengan $x-h$ dan $y$ dengan $y-k$ pada persamaan awal.'''),
        (r'''Garis singgung di titik pada lingkaran (cara bagi adil)''',
         r'''<ul class='r'><li>$x^2+y^2=r^2$: &nbsp;$x_1x+y_1y=r^2$</li><li>$(x-a)^2+(y-b)^2=r^2$:<br>$(x_1-a)(x-a)+(y_1-b)(y-b)=r^2$</li><li>Bentuk umum:<br>$x_1x+y_1y+\tfrac{A}{2}(x+x_1)+\tfrac{B}{2}(y+y_1)+C=0$</li></ul>''',
         r'''Berlaku hanya jika $(x_1,y_1)$ <b>terletak pada</b> lingkaran. Cek dulu dengan substitusi.'''),
        (r'''Garis singgung dengan gradien $m$''',
         r'''$$y=mx\pm r\sqrt{1+m^2}$$ $$y-b=m(x-a)\pm r\sqrt{1+m^2}$$''',
         r'''Selalu menghasilkan dua garis. Gradien garis $px+qy+c=0$ adalah $m=-\tfrac{p}{q}$. Sejajar: $m_1=m_2$. Tegak lurus: $m_1\cdot m_2=-1$.'''),
        (r'''Jarak titik ke lingkaran''',
         r'''$d$ = jarak titik ke pusat $=\sqrt{(x_1-a)^2+(y_1-b)^2}$ <ul class='r'><li>Jarak terdekat: $|d-r|$</li><li>Jarak terjauh: $d+r$</li></ul>''',
         r'''Panjang garis singgung dari titik di luar lingkaran: $\sqrt{d^2-r^2}$.'''),
        (r'''Kedudukan garis terhadap lingkaran''',
         r'''Substitusi persamaan garis ke persamaan lingkaran sehingga diperoleh persamaan kuadrat, lalu hitung $D=b^2-4ac$. <ul class='r'><li>$D>0$: memotong di dua titik</li><li>$D=0$: menyinggung</li><li>$D<0$: tidak memotong</li></ul>''',
         r'''Cara lain: bandingkan jarak pusat ke garis ($d$) dengan $r$. $d<r$ memotong, $d=r$ menyinggung, $d>r$ tidak memotong.'''),
    ],
},
{
    "bab": "II. LIMIT DAN KEKONTINUAN FUNGSI",
    "baris": [
        (r'''Pengertian limit dan limit sepihak''',
         r'''$$\lim_{x\to c}f(x)=L \iff \lim_{x\to c^-}f(x)=\lim_{x\to c^+}f(x)=L$$''',
         r'''Limit dikatakan <b>ada</b> jika limit kiri sama dengan limit kanan. Nilai limit tidak harus sama dengan $f(c)$.'''),
        (r'''Membaca limit dari grafik''',
         r'''<ul class='r'><li>Limit kiri/kanan: lihat nilai $y$ yang didekati kurva dari kiri/kanan $x=c$.</li><li>Nilai fungsi $f(c)$: lihat titik <b>penuh</b> (&#9679;) di $x=c$.</li><li>Titik <b>kosong</b> (&#9675;) berarti nilai itu didekati tetapi tidak dicapai.</li></ul>''',
         r'''Jika kurva melompat di $x=c$ (limit kiri $\neq$ limit kanan), limitnya tidak ada.'''),
        (r'''Sifat-sifat limit''',
         r'''$$\lim(f\pm g)=\lim f\pm\lim g$$ $$\lim(f\cdot g)=\lim f\cdot\lim g,\qquad \lim kf=k\lim f$$ $$\lim\frac{f}{g}=\frac{\lim f}{\lim g}\;\;(\lim g\neq0)$$''',
         r'''Jika substitusi langsung menghasilkan $\tfrac00$, sederhanakan dulu (faktorkan, kalikan sekawan, atau gunakan identitas).'''),
        (r'''Limit tak hingga fungsi pecahan aljabar''',
         r'''$$\lim_{x\to\infty}\frac{a x^n+\dots}{p x^m+\dots}=\begin{cases}\dfrac{a}{p}, & n=m\\[4pt] 0, & n<m\\[4pt] \pm\infty, & n>m\end{cases}$$''',
         r'''$n$ dan $m$ adalah pangkat tertinggi pembilang dan penyebut. Dasarnya: bagi semua suku dengan $x$ berpangkat tertinggi, karena $\tfrac{k}{x^n}\to0$.'''),
        (r'''Limit tak hingga bentuk akar dan pecahan''',
         r'''Bagi pembilang dan penyebut dengan $x$ berpangkat tertinggi. Gunakan $$\sqrt{ax^2+bx+c}=x\sqrt{a+\tfrac bx+\tfrac c{x^2}}\;\;(x>0)$$''',
         r'''Secara cepat, $\sqrt{ax^2+\dots}$ berperilaku seperti $\sqrt a\,x$ untuk $x\to\infty$.'''),
        (r'''Limit tak hingga selisih dua bentuk akar''',
         r'''$$\lim_{x\to\infty}\left(\sqrt{ax^2+bx+c}-\sqrt{px^2+qx+r}\right)$$ $$=\begin{cases}\infty, & a>p\\[3pt] \dfrac{b-q}{2\sqrt a}, & a=p\\[6pt] -\infty, & a<p\end{cases}$$''',
         r'''Dasarnya: kalikan dengan bentuk sekawan $\dfrac{\sqrt{\;\;}+\sqrt{\;\;}}{\sqrt{\;\;}+\sqrt{\;\;}}$.'''),
        (r'''Limit tak hingga selisih bentuk akar dan linear''',
         r'''Ubah bentuk linear menjadi akar: $$\sqrt a\,x+d=\sqrt{ax^2+2d\sqrt a\,x+d^2}$$ lalu pakai rumus selisih dua akar: $$\lim_{x\to\infty}\left(\sqrt{ax^2+bx+c}-(\sqrt a\,x+d)\right)$$ $$=\frac{b-2d\sqrt a}{2\sqrt a}$$''',
         r'''Berlaku jika koefisien $x$ pada bentuk linear sama dengan $\sqrt a$. Jika tidak sama, hasilnya $\pm\infty$.'''),
        (r'''Limit fungsi trigonometri (dasar)''',
         r'''$$\lim_{x\to0}\frac{\sin ax}{bx}=\lim_{x\to0}\frac{ax}{\sin bx}=\frac ab$$ $$\lim_{x\to0}\frac{\tan ax}{bx}=\lim_{x\to0}\frac{\sin ax}{\tan bx}=\frac ab$$''',
         r'''Untuk $x\to0$: $\sin ax$ dan $\tan ax$ boleh dianggap $\approx ax$ jika berupa faktor perkalian. Juga $\lim_{x\to0}\cos ax=1$.'''),
        (r'''Limit trigonometri bentuk $1-\cos$''',
         r'''$$1-\cos 2A=2\sin^2A$$ $$1-\cos ax=2\sin^2\tfrac{ax}{2}$$ $$\lim_{x\to0}\frac{1-\cos ax}{bx^2}=\frac{a^2}{2b}$$''',
         r'''Ubah $1-\cos$ menjadi $2\sin^2$ terlebih dahulu, kemudian gunakan limit trigonometri dasar.'''),
        (r'''Limit trigonometri: selisih kosinus dan tangen''',
         r'''$$\cos A-\cos B=-2\sin\tfrac{A+B}{2}\sin\tfrac{A-B}{2}$$ $$\sin A-\sin B=2\cos\tfrac{A+B}{2}\sin\tfrac{A-B}{2}$$ $$\tan x=\frac{\sin x}{\cos x}$$''',
         r'''Ubah selisih menjadi perkalian agar bisa disederhanakan dengan $\tan$ atau $x$ di penyebut.'''),
        (r'''Kekontinuan fungsi di satu titik''',
         r'''$f$ kontinu di $x=c$ jika: <ol class='r'><li>$f(c)$ terdefinisi</li><li>$\lim_{x\to c}f(x)$ ada</li><li>$\lim_{x\to c}f(x)=f(c)$</li></ol>''',
         r'''Untuk fungsi sepotong-sepotong: samakan limit kiri, limit kanan, dan nilai fungsinya di titik sambung.'''),
        (r'''Limit bentuk eksponen (bilangan $e$)''',
         r'''$$\lim_{x\to\infty}\left(1+\frac1x\right)^{x}=e$$ $$\lim_{x\to\infty}\left(1+\frac{a}{x}\right)^{bx}=e^{ab},\qquad \lim_{x\to0}(1+ax)^{\frac{b}{x}}=e^{ab}$$''',
         r'''$e\approx2{,}71828$. Bentuk $\left(\frac{x+m}{x+n}\right)^{x}$ diubah menjadi $\left(1+\frac{m-n}{x+n}\right)^{x}$, hasilnya $e^{m-n}$.'''),
    ],
},
{
    "bab": "III. TURUNAN DAN APLIKASINYA",
    "baris": [
        (r'''Definisi turunan''',
         r'''$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$$''',
         r'''Notasi lain: $\dfrac{dy}{dx}$, $y'$. Turunan menyatakan gradien garis singgung atau laju perubahan.'''),
        (r'''Turunan fungsi aljabar dasar''',
         r'''$$\frac{d}{dx}(k)=0,\qquad \frac{d}{dx}(ax^n)=anx^{n-1}$$ $$(u\pm v)'=u'\pm v'$$''',
         r'''Ubah bentuk akar dan pecahan ke pangkat: $\sqrt[m]{x^n}=x^{n/m}$, $\dfrac1{x^n}=x^{-n}$.'''),
        (r'''Aturan perkalian dan pembagian''',
         r'''$$(uv)'=u'v+uv'$$ $$\left(\frac uv\right)'=\frac{u'v-uv'}{v^2}$$''',
         r'''Setelah diturunkan, keluarkan faktor persekutuan agar hasilnya lebih sederhana.'''),
        (r'''Aturan rantai''',
         r'''$$y=f(g(x))\;\Rightarrow\;y'=f'(g(x))\cdot g'(x)$$ $$\left(u^n\right)'=n\,u^{n-1}\cdot u'$$''',
         r'''Turunkan dari lapisan terluar ke dalam, lalu kalikan semuanya.'''),
        (r'''Turunan fungsi bentuk akar''',
         r'''$$\frac{d}{dx}\sqrt{u}=\frac{u'}{2\sqrt u},\qquad \frac{d}{dx}\sqrt[n]{u^m}=\frac mn\,u^{\frac mn-1}\cdot u'$$''',
         r'''Kasus khusus dari aturan rantai dengan pangkat pecahan.'''),
        (r'''Persamaan garis singgung kurva''',
         r'''Di titik $(x_1,y_1)$ pada kurva $y=f(x)$: $$m=f'(x_1),\qquad y-y_1=m(x-x_1)$$''',
         r'''Jika hanya absis diketahui, hitung $y_1=f(x_1)$ dulu. Garis normal: gradien $-\tfrac1m$.'''),
        (r'''Fungsi naik, turun, dan stasioner''',
         r'''<ul class='r'><li>Naik: $f'(x)>0$</li><li>Turun: $f'(x)<0$</li><li>Stasioner: $f'(x)=0$</li></ul>''',
         r'''Cari pembuat nol $f'(x)$, gambar garis bilangan, lalu uji tanda tiap interval.'''),
        (r'''Jenis titik stasioner''',
         r'''Jika $f'(c)=0$: <ul class='r'><li>$f''(c)<0$: maksimum</li><li>$f''(c)>0$: minimum</li><li>$f''(c)=0$: perlu uji tanda $f'$</li></ul>''',
         r'''Uji tanda $f'$: $+\to-$ maksimum, $-\to+$ minimum, tanda tetap berarti titik belok horizontal.'''),
        (r'''Nilai maksimum dan minimum (soal kontekstual)''',
         r'''<ol class='r'><li>Nyatakan besaran yang dioptimalkan sebagai fungsi satu variabel.</li><li>Selesaikan $f'(x)=0$.</li><li>Pastikan jenisnya (uji $f''$ atau tanda $f'$).</li><li>Hitung nilai fungsinya.</li></ol>''',
         r'''Keuntungan = pendapatan $-$ biaya. Pada interval tertutup $[a,b]$, bandingkan juga $f(a)$ dan $f(b)$.'''),
        (r'''Turunan fungsi trigonometri''',
         r'''$$(\sin x)'=\cos x,\qquad (\cos x)'=-\sin x$$ $$(\tan x)'=\sec^2x,\qquad (\cot x)'=-\csc^2x$$ $$(\sec x)'=\sec x\tan x,\qquad (\csc x)'=-\csc x\cot x$$''',
         r'''Dengan aturan rantai: $(\sin u)'=u'\cos u$, $(\cos u)'=-u'\sin u$, $(\tan u)'=u'\sec^2u$.'''),
        (r'''Nilai sudut istimewa''',
         r'''$$\begin{array}{c|ccccc} & 0^\circ & 30^\circ & 45^\circ & 60^\circ & 90^\circ\\ \hline \sin & 0 & \tfrac12 & \tfrac12\sqrt2 & \tfrac12\sqrt3 & 1\\ \cos & 1 & \tfrac12\sqrt3 & \tfrac12\sqrt2 & \tfrac12 & 0\\ \tan & 0 & \tfrac13\sqrt3 & 1 & \sqrt3 & -\end{array}$$''',
         r'''$\pi$ rad $=180^\circ$. $\sec x=\dfrac1{\cos x}$, $\csc x=\dfrac1{\sin x}$, $\cot x=\dfrac1{\tan x}$.'''),
        (r'''Turunan kedua fungsi trigonometri''',
         r'''$$f''(x)=\frac{d}{dx}\big(f'(x)\big)$$ $$(\sin ax)''=-a^2\sin ax,\qquad (\cos ax)''=-a^2\cos ax$$''',
         r'''Identitas yang sering membantu: $2\sin A\cos A=\sin2A$, $\cos^2A=\tfrac12(1+\cos2A)$, $\sin^2A=\tfrac12(1-\cos2A)$.'''),
        (r'''Turunan perkalian fungsi aljabar dan trigonometri''',
         r'''$$\big(u\cdot v\big)'=u'v+uv'$$ dengan $u$ fungsi aljabar dan $v$ fungsi trigonometri.''',
         r'''Contoh pola: $(x^n\sin x)'=nx^{n-1}\sin x+x^n\cos x$.'''),
        (r'''Turunan trigonometri dengan aturan rantai''',
         r'''$$\big(\sin^n u\big)'=n\sin^{n-1}u\cdot\cos u\cdot u'$$ $$\big(\cos^n u\big)'=-n\cos^{n-1}u\cdot\sin u\cdot u'$$''',
         r'''Urutan: pangkat $\to$ fungsi trigonometri $\to$ sudut di dalamnya.'''),
        (r'''Garis singgung kurva trigonometri''',
         r'''$$m=f'(x_1),\qquad y-f(x_1)=m(x-x_1)$$''',
         r'''Prosedurnya sama dengan kurva aljabar. Gunakan nilai sudut istimewa untuk menghitung $f(x_1)$ dan $f'(x_1)$.'''),
        (r'''Masalah optimasi (luas bangun datar)''',
         r'''$$L_{\text{trapesium}}=\tfrac12(a+b)\,t,\qquad L_{\text{persegi panjang}}=p\,\ell$$ Nyatakan sisi-sisinya dalam satu variabel (panjang atau sudut), lalu $L'=0$.''',
         r'''Jika variabelnya sudut $\theta$, gunakan $t=s\sin\theta$ dan proyeksi $s\cos\theta$.'''),
        (r'''Turunan fungsi eksponen''',
         r'''$$(e^x)'=e^x,\qquad (e^{u})'=u'\,e^{u}$$ $$(a^x)'=a^x\ln a$$''',
         r'''Bilangan $e$ adalah basis logaritma natural, $\ln x={}^{e}\!\log x$.'''),
        (r'''Turunan fungsi logaritma''',
         r'''$$(\ln x)'=\frac1x,\qquad (\ln u)'=\frac{u'}{u}$$ $$\left({}^{a}\!\log x\right)'=\frac{1}{x\ln a},\qquad \left({}^{a}\!\log u\right)'=\frac{u'}{u\ln a}$$''',
         r'''Sifat yang membantu: $\ln(uv)=\ln u+\ln v$, $\ln\frac uv=\ln u-\ln v$, $\ln u^n=n\ln u$.'''),
        (r'''Turunan fungsi eksponen berpangkat fungsi''',
         r'''$$\big(a^{u}\big)'=u'\cdot a^{u}\ln a$$ Untuk $y=u^{v}$ (basis dan pangkat sama-sama fungsi): $$y'=u^{v}\left(v'\ln u+\frac{v\,u'}{u}\right)$$''',
         r'''Bentuk $u^v$ diselesaikan dengan menurunkan $\ln y=v\ln u$ (turunan logaritmik).'''),
        (r'''Kecekungan kurva''',
         r'''<ul class='r'><li>$f''(x)>0$: cekung ke atas ($\cup$)</li><li>$f''(x)<0$: cekung ke bawah ($\cap$)</li></ul>''',
         r'''Cari pembuat nol $f''(x)$ lalu uji tanda pada garis bilangan.'''),
        (r'''Titik belok kurva''',
         r'''Titik $(c,\,f(c))$ adalah titik belok jika $$f''(c)=0$$ dan tanda $f''$ berubah di sekitar $x=c$.''',
         r'''Titik belok adalah titik peralihan kecekungan. Untuk $f(x)=ax^3+bx^2+cx+d$: $x=-\tfrac{b}{3a}$.'''),
    ],
},
{
    "bab": "IV. INTEGRAL TAK TENTU",
    "baris": [
        (r'''Pengertian integral tak tentu''',
         r'''$$\int f(x)\,dx=F(x)+C\iff F'(x)=f(x)$$''',
         r'''Integral adalah antiturunan (kebalikan turunan). $C$ adalah konstanta integrasi.'''),
        (r'''Integral fungsi polinom''',
         r'''$$\int k\,dx=kx+C$$ $$\int ax^n\,dx=\frac{a}{n+1}x^{n+1}+C,\;\;n\neq-1$$ $$\int\frac1x\,dx=\ln|x|+C$$''',
         r'''Sifat linear: $\int(f\pm g)\,dx=\int f\,dx\pm\int g\,dx$ dan $\int kf\,dx=k\int f\,dx$. Perkalian atau pembagian polinom dijabarkan dulu.'''),
        (r'''Menentukan fungsi dari turunan dan nilai awal''',
         r'''$$f(x)=\int f'(x)\,dx=F(x)+C$$ Nilai $C$ dicari dari syarat awal $f(x_0)=y_0$.''',
         r'''Jika diketahui gradien garis singgung $m=f'(x)$ dan kurva melalui suatu titik, caranya sama. Dari $f''$, integralkan dua kali (ada $C_1$ dan $C_2$).'''),
        (r'''Integral dengan substitusi''',
         r'''Misalkan $u=g(x)$, maka $du=g'(x)\,dx$: $$\int f\big(g(x)\big)\,g'(x)\,dx=\int f(u)\,du$$''',
         r'''Pilih $u$ sebagai bagian yang turunannya muncul (sebagai faktor) di luar. Kembalikan hasil ke variabel $x$.'''),
        (r'''Rumus cepat substitusi''',
         r'''$$\int(ax+b)^n\,dx=\frac{(ax+b)^{n+1}}{a(n+1)}+C$$ $$\int u'\,u^n\,dx=\frac{u^{n+1}}{n+1}+C,\;\;n\neq-1$$''',
         r'''Bentuk akar diubah dulu menjadi pangkat pecahan: $\sqrt u=u^{1/2}$.'''),
    ],
},
]
