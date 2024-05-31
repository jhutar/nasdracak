#!/bin/bash

# To convert svg files, we need utility rsvg-convert from librsvg2-tools package

set -eux

source venv/bin/activate

rm -f gamebook/opustena_magova_vez.pdf
rm -f gamebook/opustena_magova_vez2.md
rm -f gamebook/opustena_magova_vez.dot
rm -f gamebook/opustena_magova_vez.dot.png

# PDF doc
pandoc --lua-filter=pagebreak/pagebreak.lua --lua-filter=pangamebook/pangamebook.lua --pdf-engine=xelatex -o gamebook/opustena_magova_vez.pdf gamebook/opustena_magova_vez.md
echo "PDF doc: gamebook/opustena_magova_vez.pdf"

# Raw PDF doc
pandoc -Mgamebook-shuffle=false -Mgamebook-pre-link="[[" -Mgamebook-post-link="]]" -Mgamebook-numbers=false --lua-filter=pangamebook/pangamebook.lua --pdf-engine=xelatex -o gamebook/opustena_magova_vez-raw.pdf gamebook/opustena_magova_vez.md
echo "Raw PDF doc: gamebook/opustena_magova_vez-raw.pdf"

# PNG graph
pandoc --lua-filter=pangamebook/pangamebook.lua -o gamebook/opustena_magova_vez2.md gamebook/opustena_magova_vez.md
pandoc --lua-filter=pangamebook/pangamebookdot.lua -t plain -o gamebook/opustena_magova_vez.dot gamebook/opustena_magova_vez2.md
dot -Tpng -O gamebook/opustena_magova_vez.dot
echo "PNG graph: gamebook/opustena_magova_vez.dot.png"
