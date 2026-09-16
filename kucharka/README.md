# Kuchařka z monster

Texty a obrázky vygenerovány pomocí Gemini, idea je ze seriálu [Labužníci v kobce](https://www.csfd.cz/film/1453888-labuznici-v-kobce/prehled/).

Převedení MarkDown file do PDF:

```bash
pandoc \
    kucharka-z-monster.md \
    -V documentclass=scrartcl \
    -V geometry:a5paper \
    -V geometry:margin=14mm \
    -V mainfont="SendFlowers-Regular.ttf" \
    -V mainfontoptions="Path=$( pwd )/fonts/, AutoFakeBold=2.5" \
    -V fontsize=20pt \
    -V header-includes="
        \usepackage{eso-pic,graphicx,tikz}
        \usepackage{sectsty}
        \newfontfamily\headingfont[Path=$( pwd )/fonts/, AutoFakeBold=2.5]{SendFlowers-Regular.ttf}
        \allsectionsfont{\headingfont\bfseries}
        \special{pdf:option D 0}
        \AddToShipoutPictureFG{
            \AtPageLowerLeft{
                \tikz\node[inner sep=0,outer sep=0,opacity=0.3]{
                    \includegraphics[width=\paperwidth,height=\paperheight]{
                        $( pwd )/stains.png
                    }
                };
            }
        }" \
    --pdf-engine=xelatex \
    -o out.pdf
```

Rozdeleni na casti o 16 stranach:

```bash
pdftk out.pdf cat 1-16 output out-part-1.pdf
pdftk out.pdf cat 17-32 output out-part-2.pdf
pdftk out.pdf cat 33-48 output out-part-3.pdf
pdftk out.pdf cat 49-64 output out-part-4.pdf
```

```bash
a6-booklet-on-a4/booklet_a6_on_a4 -in out-part-1.pdf -out out-part-1-reordered.pdf -pages 16
```

```bash
pdftk A=out-part-1.pdf cat A2 A15 A6 A11 A16 A1 A12 A5 A4 A13 A8 A9 A14 A3 A10 A7 output out-part-1-reordered.pdf
pdftk A=out-part-2.pdf cat A2 A15 A6 A11 A16 A1 A12 A5 A4 A13 A8 A9 A14 A3 A10 A7 output out-part-2-reordered.pdf
pdftk A=out-part-3.pdf cat A2 A15 A6 A11 A16 A1 A12 A5 A4 A13 A8 A9 A14 A3 A10 A7 output out-part-3-reordered.pdf
pdftk A=out-part-4.pdf cat A2 A15 A6 A11 A16 A1 A12 A5 A4 A13 A8 A9 A14 A3 A10 A7 output out-part-4-reordered.pdf
```

python extrahuj.py

mogrify -transparent white ~/Downloads/monstra/*.png


pdftk A=/home/jhutar/Downloads/pokus-a6-brozura.pdf cat A2 A15 A6 A11 A16 A1 A12 A5 A4 A13 A8 A9 A14 A3 A10 A7 output /home/jhutar/Downloads/pokus-a6-brozura-out.pdf

cd /home/jhutar/Checkouts/tmp/a6-booklet-on-a4
./booklet_a6_on_a4 -in ~/Downloads/pokus-a6-brozura.pdf -out ~/Downloads/pokus-a6-brozura-out.pdf -pages 16
pdftk A=/home/jhutar/Downloads/pokus-a6-brozura.pdf cat A2 A15 A6 A11 A16 A1 A12 A5 A4 A13 A8 A9 A14 A3 A10 A7 output /home/jhutar/Downloads/pokus-a6-brozura-out.pdf


https://learnbyexample.github.io/customizing-pandoc/
https://fonts.google.com/
https://github.com/ERnsTL/a6-booklet-on-a4
