# Tento projekt

Tento repozitář obsahuje různé komponenty pro naši RPG stolní (ne počítačovou) hru která těžce čerpá z her "Dungeons&Dragons" nebo "Dračí doupě", ale jejich mechaniky zjednodušuje tak aby se snadno vysvětlovaly dětem (řekněme 6 let a výše) a aby bylo jednoduché s nimi hrát.

V repozitáři jsou:

* Pravidla v souboru `docs/source/pravidla/index.rst` jsou zásadní pro všechny ostatní texty
  * ve formátu reStructuredText
  * psaná jednoduše a srozumitelně, krátce a rovnou k věci
  * hráči v textu konzistentně tykáme (například píšeme "Vytvoř si postavu tak a tak" a ne "Vytvořte si postavu tak a tak" ani "Postavu si vytvoříme tak a tak")
  * text ladíme ve fantasy stylu
  * zachováváme konzistntní terminologii (například síla je vždy SÍL, magická energie je vždy magenergie, zdraví je vždy životy)
  * príklady formátovány pomocí `.. admonition:: Příklad:` s odsazením textu příklau
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

Pro popisy commitů používáme "Conventional commits" a commit message jsou v češtině bez diakritiky.

Změny vygnerované pomocí Gemini musí být commitnuty s trailerem "Generated-by:Gemini" (použij `--trailer Generated-by:Gemini`) a commit message musí také obsahovat zesumarizovaný prompt poskytnutý operátorem.


# Zdrojový kod skriptů

Kód je formátován pomocí nástroje `black` a nehlásí chyby při kontrole pomocí `flake8`.

Vývoj skriptů v adresáři `tools/` používá virtuální environment v `venv/`, takže se vše pouští v tomto venv.

Testy se pouští pomocí `venv/bin/pytest tools/tests/`.
