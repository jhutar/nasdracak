Moje poznámky k "dračáku" co občas hrajeme
==========================================

Tento text v čitelné podobě najdete na https://jhutar.github.io/nasdracak/

Development
-----------

Zdrojové kódy textu jsou v adresáři `docs/source/`.

Pro lokální sestavení textu do čitelné podoby je potřeba nainstalovat potřebné nástroje (Sphinx a LaTeX). Na Fedora Linuxu to je tímto příkazem:

    # dnf install python3-sphinx python3-sphinx-latex python3-sphinxcontrib-inkscapeconverter latexmk texlive-babel-czech texlive-pict2e texlive-ellipse

Na Ubuntu pak zdá se stačí:

    # apt-get install -y fonts-dejavu fonts-freefont-otf graphviz imagemagick inkscape latexmk lmodern make python3-pip tex-gyre texlive-fonts-extra texlive-fonts-recommended texlive-lang-czechslovak texlive-latex-extra texlive-latex-recommended texlive-luatex texlive-xetex xindy
    $ pip install sphinx sphinxcontrib-svg2pdfconverter

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

Licence
-------

[Náš "dračák"](https://github.com/jhutar/nasdracak/) © 2023 od [Jan Hutař](mailto:jhutar@seznam.cz) je licencován pod licencí [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
