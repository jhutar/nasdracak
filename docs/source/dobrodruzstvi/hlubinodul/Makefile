# Build D&D adventures (Markdown -> PDF via pandoc + DND-5e-LaTeX-Template).
# See README.md for installation, docs/repo-setup.md for the design.

TEXMF := $(CURDIR)/texmf
PANDOC := pandoc
PANDOCFLAGS = --template template/dnd.latex --lua-filter filters/boxes.lua \
            --lua-filter filters/tables.lua --toc
# TEXINPUTS: pdflatex finds our template/*.sty (trailing ':' keeps system paths)
export TEXINPUTS = $(CURDIR)/template:

DEPS = template/dnd.latex template/dndboxes.sty template/dndczech.sty filters/boxes.lua

# All top-level *.md -> output/*.pdf
MDPDFS = $(patsubst %.md,output/%.pdf,$(wildcard *.md))

all: $(MDPDFS)

output/adventure.pdf: adventure.md images/chapel-door.pdf $(DEPS)
	@echo "building $@ from $<"
	TEXMFHOME=$(TEXMF) $(PANDOC) $< $(PANDOCFLAGS) -o $@

output/adventure-cz.pdf: adventure-cz.md images/chapel-door.pdf $(DEPS)
	@echo "building $@ from $<"
	TEXMFHOME=$(TEXMF) $(PANDOC) $< $(PANDOCFLAGS) -o $@

# Generic rule for the remaining *.md files
output/%.pdf: %.md $(DEPS)
	@echo "building $@ from $<"
	TEXMFHOME=$(TEXMF) $(PANDOC) $< $(PANDOCFLAGS) -o $@

# SVG -> vector PDF (pdflatex cannot read SVG directly)
images/%.pdf: images/%.svg
	inkscape $< -o $@

en: output/adventure.pdf
cz: output/adventure-cz.pdf

# book-*.svg -> output/books/<n>.pdf (rotated 90 CW) -> merged output/books.pdf
BOOKSVGS = $(wildcard book-[0-9][0-9].svg)
BOOKPDFS = $(patsubst book-%.svg,output/books/%.pdf,$(BOOKSVGS))

output/books.pdf: $(BOOKPDFS)
	pdftk $(BOOKPDFS) cat output $@

output/books/%.pdf: book-%.svg
	@mkdir -p output/books
	inkscape --batch-process --export-area-page --export-dpi=600 \
	  --export-pdf-version=1.5 --export-overwrite --export-type=pdf \
	  --export-filename=output/books/.unrot-$*.pdf $<
	pdftk output/books/.unrot-$*.pdf cat 1right output $@
	rm -f output/books/.unrot-$*.pdf

books: output/books.pdf

# Rebuild the kpathsea index for the local texmf tree (speeds up package
# lookup; pdflatex falls back to directory walking without it)
index:
	TEXMFHOME=$(TEXMF) mktexlsr $(TEXMF)

clean:
	rm -f output/*.pdf output/books/*.pdf output/books/.unrot-*.pdf images/*.pdf

.PHONY: all en cz books index clean
