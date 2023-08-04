Moje poznámku k "dračáku" co občas hrajeme
==========================================

Tento text v čitelné podobě najdete na https://nasdracak.readthedocs.io/

Development
-----------

Zdrojové kódy textu jsou v adresáři `docs/source/`.

Pro lokální sestavení textu do čitelné podoby je potřeba nainstalovat potřebné nástroje (Sphinx a LaTeX). Na Fedora Linuxu to je tímto příkazem:

    # dnf install python3-sphinx python3-sphinx-latex python3-sphinxcontrib-inkscapeconverter latexmk texlive-babel-czech

Sestavení PDF verze:

    $ make -C docs/ latexpdf
    $ ls docs/build/latex/ndrak.pdf

A HTML verze:

    $ make -C docs/ html
    $ firefox docs/build/html/index.html
