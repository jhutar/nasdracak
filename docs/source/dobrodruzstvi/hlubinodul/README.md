# Hlubinodul — D&D 5e adventures, Markdown → PDF

Write adventures in Markdown, build D&D 5e-styled PDFs with Pandoc + the
[rpgtex/DND-5e-LaTeX-Template](https://github.com/rpgtex/DND-5e-LaTeX-Template)
package. English and Czech supported (`lang:` frontmatter).

## Install dependencies (Fedora)

```sh
sudo dnf install inkscape pandoc-cli \
  texlive-collection-latexrecommended \
  texlive-collection-latexextra \
  texlive-collection-fontsrecommended \
  texlive-collection-fontsextra \
  texlive-collection-langczechslovak
```

## Build

```sh
make        # output/adventure.pdf + output/adventure-cz.pdf
make en     # english only
make cz     # czech only
make index  # rebuild kpathsea index for the local texmf (once, speeds builds)
```

Requires the `dnd` package clone at `tools/DND-5e-LaTeX-Template`
(`texmf/tex/latex/dnd` is a symlink to it — update the clone with `git
pull`, the build picks it up).

## Box syntax

```markdown
::: squarebox
**Box title**          <- first line fully bold = title
Visually distinct callout text.
:::

::: readaloud
Text the game master reads aloud.
:::

::: dnditem
Item Name              <- block 1 = name
Wondrous item, rare    <- block 2 = type/rarity
Description text.
:::

::: dndmonster         <- stat block from key: value lines
name: Skeleton Bellkeeper
type: Medium undead, neutral evil
armor_class: 12 (bone plating)
hit_points: 13 (2d8 + 2)
speed: 30 ft.
str: 10
dex: 12
con: 10
int: 6
wis: 8
cha: 5
saving_throws: Wisdom +1
skills: Perception +3
senses: darkvision 60 ft., passive Perception 9
languages: understands Common, but cannot speak
challenge: 1/4

---                        <- optional separator (blank lines around it)
**Actions**                <- fully bold line = statblock section header

**Rusty Scythe.** *Melee Weapon Attack.* +3 to hit.
:::
```

`dndmonster` keys: `name` (required), `type`, `armor_class`, `hit_points`,
`speed`, `str`, `dex`, `con`, `int`, `wis`, `cha`, `saving_throws`, `skills`,
`damage_immunities`, `damage_vulnerabilities`, `damage_resistances`,
`condition_immunities`, `senses`, `languages`, `challenge`.

## Images

Put SVGs in `images/`. The Makefile converts them to vector PDF with
inkscape before building (pdflatex cannot read SVG). Reference the `.pdf`
path in Markdown.

## Languages

`lang: english` or `lang: czech` in frontmatter. Czech stat-block strings
live in `template/dndczech.sty` (standard Czech 5e terminology: Třída brnění,
Bodky života, Vyznání, ZP, hody odvahy…). Review the file if you translate
adventures — strings not listed there fall back to English.

## Attribution

Not all of this is original:

| Source | What is used | License |
|---|---|---|
| [rpgtex/DND-5e-LaTeX-Template](https://github.com/rpgtex/DND-5e-LaTeX-Template) | the entire visual theme (`dnd` package: fonts, colors, `DndMonster`, `DndReadAloud`, tables). | MIT |
| [dnd-tools](https://github.com/samuelbasweiler/dnd-tools) (fork lineage of the same template) | pandoc template structure (hyperref, image auto-scaling, `dnditem` idea) — rewritten, not copied | MIT |
| [daggerheart-template](https://github.com/jonathanlambertx/daggerheart-template) | `::: div` → box workflow, `squarebox` concept — re-themed for 5e | repo's license |
