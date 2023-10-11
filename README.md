Moje poznámku k "dračáku" co občas hrajeme
==========================================

Tento text v čitelné podobě najdete na https://nasdracak.readthedocs.io/

Development
-----------

Zdrojové kódy textu jsou v adresáři `docs/source/`.

Pro lokální sestavení textu do čitelné podoby je potřeba nainstalovat potřebné nástroje (Sphinx a LaTeX). Na Fedora Linuxu to je tímto příkazem:

    # dnf install python3-sphinx python3-sphinx-latex python3-sphinxcontrib-inkscapeconverter latexmk texlive-babel-czech texlive-pict2e texlive-ellipse

Sestavení kompletní PDF verze:

    $ sphinx-build -M latexpdf docs/source/ docs/build/
    $ ls docs/build/latex/ndrak.pdf

A HTML verze:

    $ make -C docs/ html
    $ firefox docs/build/html/index.html

Jednotlivé PDF soubory:

    $ sphinx-build -M latexpdf docs/source/pravidla/ docs/build/
    $ sphinx-build -M latexpdf docs/source/predmety/ docs/build/
    $ sphinx-build -M latexpdf docs/source/bestiar/ docs/build/
    $ sphinx-build -M latexpdf docs/source/dobrodruzstvi/ docs/build/
    $ sphinx-build -M latexpdf docs/source/dobrodruzstvi/opustena_magova_vez/ docs/build/
    $ sphinx-build -M latexpdf docs/source/dobrodruzstvi/duha_ve_meste/ docs/build/
