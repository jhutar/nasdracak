# Prompt: úprava adventury do Hlubinodul syntaxe

Reusable prompt for converting an adventure file to the syntax described in
`docs/source/dobrodruzstvi/hlubinodul/README.md`. Substitute `{SOUBOR}` with
the target file path.

---

Please convert @docs/source/dobrodruzstvi/hlubinodul/{SOUBOR} to use the
syntax described in @docs/source/dobrodruzstvi/hlubinodul/README.md.
Improve the Markdown syntax and clean the file up:

1. **Frontmatter**: ensure the file starts with `lang: czech` (or `english`)
   and `title: "<file_title>"` frontmatter, since the Pandoc build requires it.

2. **Headings**:
   - remove bold from headings (`## **Titulek**` → `## Titulek`)
   - remove unnecessary role labels that are not real headings
     ("**Popis pro hráče:**", "**Informace pro DM:**", "Popis monster pro
     hráče:") — replace them with the proper box syntax below or with a
     normal short heading

3. **Backslash cleanup**: remove pandoc escape artifacts throughout the text:
   `\.`, `\+`, `\-`, `\!`, `\- 1\.` etc. (e.g. `4d10 \+ 4\)` → `4d10 + 4)`,
   `1\. patře` → `1. patře`, `Zůstanu\!` → `Zůstanu!`). Do NOT touch real
   Markdown backticks or intentional escapes.

4. **Boxes** (see README "Box syntax"):
   - player-readable descriptions (usually italic paragraphs under
     "Popis pro hráče") → `::: readaloud` ... `:::`
   - DM-only callouts (secret doors, DCs, treasure) → `::: squarebox` with a
     bold title line
   - text the ghost/NPC says to players → nested/`readaloud` boxes

5. **Stat blocks**: convert any hand-written stat block (bullet lists like
   "Třída zbroje (AC): 14" or plain text blocks with `---` separators and
   STR/DEX/CON lines) into `::: dndmonster` key: value syntax using the keys
   from the README (`name`, `type`, `armor_class`, `hit_points`, `speed`,
   `str`...`cha`, `saving_throws`, `skills`, `senses`, `languages`,
   `challenge`). Section headers inside the block (Akce, Vlastnosti) become
   fully bold lines; abilities/actions become `**Name.** *Type.* ...` lines.
   Czech/English dual names may go into `name` / keep English canonical.

6. **Whitespace/typography**: collapse double spaces, fix trailing double
   spaces at line ends of non-list paragraphs, ensure blank lines around
   headings and lists.

7. **Keep content verbatim**: do not translate, rewrite or "improve" the
   fiction or game mechanics — only structure and syntax. Keep all `TODO`
   markers as-is.

Result must build with:
`TEXINPUTS="$PWD/template:" TEXMFHOME="$PWD/texmf" pandoc {SOUBOR} --template template/dnd.latex --lua-filter filters/boxes.lua --lua-filter filters/tables.lua --toc -o output/{SOUBOR}.pdf`
from the hlubinodul directory.
