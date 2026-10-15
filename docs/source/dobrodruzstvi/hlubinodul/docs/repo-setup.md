# Repo setup — D&D adventure Markdown → PDF pipeline

Pandoc → pdflatex pipeline for D&D 5e adventures, English + Czech, using
[rpgtex/DND-5e-LaTeX-Template](https://github.com/rpgtex/DND-5e-LaTeX-Template)
**as-is** (unmodified, no vendored copy).

## Layout

```
hlubinodul/
├── README.md               # terse: install (dnf + pandoc), usage, attribution
├── Makefile                # svg→pdf (inkscape), pandoc per language
├── texmf/tex/latex/dnd -> ../../../tools/DND-5e-LaTeX-Template   # SYMLINK, repo used as-is
├── template/dnd.latex      # pandoc template (preamble: babel, dnd package, our boxes)
├── template/dndboxes.sty   # squarebox (tcolorbox) + dnditem env (our code)
├── template/dndczech.sty   # \addto\captionsczech{...} ~60 strings (our code)
├── filters/boxes.lua       # single Lua filter, all 4 divs
├── images/*.svg            # sample SVG (converted to PDF via inkscape)
├── adventure.md            # en sample (lang: english)
├── adventure-cz.md         # cz sample, same content (lang: czech)
└── output/adventure.pdf, adventure-cz.pdf
```

The `dnd` package is never copied: `texmf/tex/latex/dnd` is a symlink to the
clone at `tools/DND-5e-LaTeX-Template`. Makefile runs pdflatex with
`TEXMFHOME=$(PWD)/texmf`. `git pull` in the clone → build picks up changes.
Package moves → fix one symlink.

## Borrowed from where (attribution)

| From | What | License |
|---|---|---|
| [rpgtex/DND-5e-LaTeX-Template](https://github.com/rpgtex/DND-5e-LaTeX-Template) | Entire visual theme: `dnd` package (fonts, colors, `DndMonster` env, `DndReadAloud`, section styling, tables). **Used as-is, unmodified, via symlink.** | MIT |
| dnd-tools (fork of rightbrace's fork of the same template) | `dnd.latex` pandoc template *structure* (hyperref setup, image auto-scaling, `dnditem` env idea) — rewritten on top of the fresh package API, not copied | MIT |
| daggerheart-template | `::: div` → LaTeX-env workflow + `squarebox` concept (tcolorbox with colored rules); box visuals re-themed for 5e, not copied | repo's license |
| dnd-tools `monsterdata.py` | **Not used in v1** (hand-written `DndMonster` block instead) | — |

Our original code: `template/dnd.latex` (rewritten), `dndboxes.sty`,
`dndczech.sty`, `filters/boxes.lua`, Makefile, sample adventures.

## Pandoc template (`template/dnd.latex`)

- `\documentclass[10pt,twoside]{article}` + `\usepackage[bg=full,justified]{dnd}`
- babel: `\usepackage[main=$lang$,english,czech]{babel}` — main language from
  pandoc `lang:` metadata; both language groups always loaded so the Czech
  strings can be registered
- `\usepackage{dndboxes}` (our boxes), `\usepackage{dndczech}` (Czech strings)
- hyperref + image auto-scaling (dnd-tools pattern)
- title page from metadata, TOC when `--toc`

## Div boxes (single Lua filter, `filters/boxes.lua`)

- `::: squarebox` → tcolorbox, 5e styling (titlered rules, parchment tint);
  first line fully bold → box title
- `::: readaloud` → package `DndReadAloud` env
- `::: dnditem` → `dnditem` env: line 1 = name, line 2 = type/rarity, rest = description
- `::: dndmonster` → parse `key: value` lines from the first text block:
  `name` (required), `type`, `armor_class`, `hit_points`, `speed`,
  `str/dex/con/int/wis/cha`, `saving_throws`, `skills`,
  `damage_immunities`, `damage_vulnerabilities`, `damage_resistances`,
  `condition_immunities`, `senses`, `languages`, `challenge`.
  Emits `DndMonster` env with `\DndMonsterType`, `\DndMonsterBasics`,
  `\DndMonsterAbilityScores`, `\DndMonsterDetails`. Everything after the key
  block (actions, senses notes, …) passes through as normal markdown.

## i18n

- `lang: english` / `lang: czech` in frontmatter
- `dndczech.sty`: full string set (Třída brnění, Bodky života, Rychlost,
  Vyznání, ZP, hody odvahy, …), mirrors upstream `lib/languages/_template.sty`
- Mechanism: the package only loads its language files when babel is present,
  via `\addto\captions<lang>` — so Czech lives entirely in our
  `dndczech.sty`; **the package itself stays untouched** (keeps it mergeable
  for future upstream PRs)

## Build (Makefile)

```
make            # builds both en + cz PDFs
make en         # just output/adventure.pdf
1. inkscape images/*.svg → images/*.pdf (vector, skip if up to date)
2. TEXMFHOME=$(PWD)/texmf pandoc adventure.md -o output/adventure.pdf \
     --template template/dnd.latex --lua-filter filters/boxes.lua --toc
```

## README.md (no filler)

- Install: `dnf install` texlive set (latexextra, latexrecommended,
  fontsrecommended, fontsextra, langczech) + `inkscape` + pandoc static binary
  from GitHub releases
- Usage: `make`, `make en`
- Box syntax reference with all four examples
- Attribution table (above)
- Caveats: build not machine-verified here; first `make` may need an extra
  texlive package; `lib/languages/japanese` is loaded by the package whenever
  babel is present (harmless under pdflatex as long as no Japanese strings
  are used)

## Not doing

- No toolchain install, no build test
- No `monsterdata.py`, no `pandoc-latex-environment`, no xelatex, no global texmf install
