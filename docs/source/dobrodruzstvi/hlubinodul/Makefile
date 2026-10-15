# Build D&D adventures (Markdown -> PDF via pandoc + DND-5e-LaTeX-Template).
# See README.md for installation, docs/repo-setup.md for the design.

TEXMF := $(CURDIR)/texmf
PANDOC := pandoc
PANDOCFLAGS = --template template/dnd.latex --lua-filter filters/boxes.lua --toc
# TEXINPUTS: pdflatex finds our template/*.sty (trailing ':' keeps system paths)
export TEXINPUTS = $(CURDIR)/template:

DEPS = template/dnd.latex template/dndboxes.sty template/dndczech.sty filters/boxes.lua

all: output/adventure.pdf output/adventure-cz.pdf

output/adventure.pdf: adventure.md images/chapel-door.pdf $(DEPS)
	TEXMFHOME=$(TEXMF) $(PANDOC) $< $(PANDOCFLAGS) -o $@

output/adventure-cz.pdf: adventure-cz.md images/chapel-door.pdf $(DEPS)
	TEXMFHOME=$(TEXMF) $(PANDOC) $< $(PANDOCFLAGS) -o $@

# SVG -> vector PDF (pdflatex cannot read SVG directly)
images/%.pdf: images/%.svg
	inkscape $< -o $@

en: output/adventure.pdf
cz: output/adventure-cz.pdf

# Rebuild the kpathsea index for the local texmf tree (speeds up package
# lookup; pdflatex falls back to directory walking without it)
index:
	TEXMFHOME=$(TEXMF) mktexlsr $(TEXMF)

clean:
	rm -f output/*.pdf images/*.pdf

.PHONY: all en cz index clean
