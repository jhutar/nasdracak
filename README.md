Moje poznámku k "dračáku" co občas hrajeme
==========================================

Tento text v čitelné podobě najdete na https://nasdracak.readthedocs.io/

Development
-----------

Dokumentace je v adresáři 

Nainstaluju (na Fedora Linux) si nástroj na generování PDF (Sphinx):

    dnf install python3-sphinx python3-sphinx-latex python3-sphinxcontrib-inkscapeconverter latexmk texlive-babel-czech

Sestavím PDF:

    make -C docs/ latexpdf

Výsledek je tady:

    docs/build/latex/ndrak.pdf
