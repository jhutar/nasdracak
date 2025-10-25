# Tento projekt

Tento repozitář obsahuje různé komponenty pro naši RPG stolní (ne počítačovou) hru která těžce čerpá z her "Dungeons&Dragons" nebo "Dtačí doupě", ale jejich mechaniky zjednodušuje tak aby se snadno vysvětlovaly dětem (řekněme 6 let a výše) a aby bylo jednoduché s nimi hrát.

V repozitáři jsou:

* Pravidla
* Předpřipravené příběhy
* Bestiář
* Příběh zpracovaný jako "gamebook"
* Skripty pro simulaci soubojů
* Pomocné skripty


# Použité technologie

* v adresáři `gamebook/` je gamebook který používá https://github.com/lifelike/pangamebook.git pro preprocessing gamebooku (zamíchání uzlů a poobně), Pandoc (pro převod do PDF) a GraphViz (příkaz dot) pro generování grafu gamegooku
* v adresáři `docs/` jsou pravidla a příběhy a bestiář a používá se Sphinx pro překlad do PDF a HTML
* v adresáři `tools/` jsou relevantní skripty pro různé experimenty v Pythonu


# Práce s Gitem

Hlavní branch repozitáře je "main".

Pro popisy commitů používáme "Conventional commits" a commit message jsou v češtině.

Změny vygnerované pomocí Gemini musí být commitnuty s trailerem "Generated-by:Gemini" a commit message musí také obsahovat zesumarizovaný prompt poskytnutý operátorem.
