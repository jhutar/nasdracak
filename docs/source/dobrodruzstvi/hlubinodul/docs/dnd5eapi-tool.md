# dnd5eapi tool — D&D 5e (2024) API → stat-block Markdown

Generator for `::: dndmonster :::` / `::: dnditem :::` blocks. Fetches one
resource from the [D&D 5e SRD API](https://www.dnd5eapi.co) (2024 edition) and
emits Markdown matching `filters/boxes.lua`, ready to paste into an adventure.
Written so a monster/item can be **translated by hand** via an override file.

**Status:** plan only. Not yet implemented (`tools/dnd5eapi.py`).

## Goals

- stdlib only (`argparse`, `urllib.request`, `json`, `pathlib`) — no deps.
- One resource per run.
- Output the box to **stdout** (paste into `.md`). `--output dndmd` is the
  format selector; `dndmd` is the only choice and the default.
- PHB-2024 formatting, not the first-draft style in `adventure.md`.

## CLI

Path-style target, split on the first `/` → `collection` + `index`:

```
dnd5eapi.py monsters/giant-badger            [--dump-override] [--output dndmd] [--lang cs-CZ]
dnd5eapi.py magic-items/vorpal-sword         [--dump-override] [--output dndmd] [--lang cs-CZ]
```

- `collection` aligns with the API resource group (`monsters`, `magic-items`);
  it also selects the renderer.
- `index` is the API index (canonical; matches the override filename).
- Renderer chosen from a small **registry** `{collection: render_fn}` so
  "more" later = add an entry (`spells`, …). Unknown collection → error.
- `--dump-override` writes the fetched JSON to the override path (see below).
- `--lang` default `cs-CZ` (API has no `cs-CZ` yet → falls back to `en`; the
  point is to translate that dump by hand, possibly contribute back later).

## API (2024)

- Base URL `https://www.dnd5eapi.co/api/2024/` (version fixed constant `2024`).
- `GET {base}{collection}/{index}?lang={lang}`, `Accept: application/json`.
- Open API, no auth. `orc` 404s in 2024 (different roster); real indices are
  e.g. `giant-badger`, `adult-black-dragon`.

## Overrides (the translation workflow)

Full-replace: the override file **is** the resource object in the exact shape
the API would return. Rendered identically to a live fetch.

- Path: `tools/dnd5eapi-overrides/<lang>/<collection>/<index>.json`
  (lang lives in the path; default run → `…/cs-CZ/monsters/giant-badger.json`).
- **Anchored to the script**: `Path(__file__).resolve().parent /
  "dnd5eapi-overrides"`. Same dir no matter the CWD
  (`../../../../tools/dnd5eapi.py …` still hits it).
- Repo structure mirrors the API (`monsters/`, `magic-items/`, …) under the
  lang dir; add subdirs freely.

Read/write rules:

- Every run checks the override first. Present → load + render, **no network**.
  Absent → fetch from API.
- `--dump-override` → write the **raw fetched JSON** to the override path
  (create parent dirs). Overwrites an existing file silently.
- So: `--dump-override` once to seed a file, edit/translate it, and every later
  run of that index reads the edited copy.

## Output: `dndmd`

### `dnditem` (`magic-items/*`)

- line 1 = `name`
- line 2 = `desc[0]` + `", " + rarity.name.lower()` + ` (requires attunement)`
  if `attunement` is true. In 2024 rarity and attunement are **separate
  fields**, not baked into `desc[0]`.
- rest = `desc[1:]`, each element its own paragraph (blank line between).

### `dndmonster` (`monsters/*`)

Emits the key block (one paragraph, no blank lines between keys), a `---`
separator, then the body. Only present keys are emitted; all six abilities are
always emitted. Key order below (render order in `boxes.lua` is fixed anyway).

Key mapping from the 2024 JSON:

| key | source / rule |
|---|---|
| `name` | `name` |
| `type` | `f"{size} {Type}, {Alignment}"` — Title-case `type` and each alignment word. **No subtype** in 2024. e.g. `Medium Beast, Unaligned`, `Huge Dragon, Chaotic Evil` |
| `armor_class` | single: `value` if `armor` empty else `f"{value} ({', '.join(armor names)})"`. Multiple `armor_class` entries joined ` or `. e.g. `13`, `15 (leather armor, shield)` |
| `hit_points` | `f"{hit_points} ({hit_points_roll})"` — 2024 roll already spaced (`2d8 + 6`); if roll has no modifier, `f"{hit_points} ({hit_points_roll})"` still fine |
| `speed` | order walk/fly/swim/burrow/climb; `walk` unlabeled, others `f"{k} {v}"`, joined `", "`. e.g. `30 ft., burrow 10 ft.` |
| `str`…`cha` | `strength/dexterity/constitution/intelligence/wisdom/charisma` raw scores |
| `saving_throws` | from `proficiencies` where `proficiency.name` starts `Saving Throw: ` → `f"{ABBR} +{value}"`, joined `", "`. e.g. `DEX +7, CON +10` |
| `skills` | from `proficiencies` where name starts `Skill: ` → `f"{name} +{value}"`, joined `", "`. e.g. `Perception +3` |
| `damage_immunities` / `damage_vulnerabilities` / `damage_resistances` / `condition_immunities` | list joined `", "` (lowercase) |
| `senses` | order darkvision/blindsight/tremorsense/truesight/passive_perception; `passive_perception` → `passive Perception N`; others `f"{k} {v}"`; joined `", "`. e.g. `darkvision 60 ft., passive Perception 13` |
| `languages` | `languages` verbatim, but exact string `None` → `—` (em dash) |
| `challenge` | fraction: `0.25→1/4`, `0.5→1/2`, `0.75→3/4`, integer → `n` (`14`, `1`, `0`); other decimals → fall back to trimmed decimal |

Ability abbreviations for `saving_throws`: `str dex con int wis cha` →
`STR DEX CON INT WIS CHA`.

### Body + auto-style

Section order (PHB), a `**Header**` paragraph only for non-empty sections:

1. `special_abilities` — **no header**, each `**Name.** <styled desc>`
2. `**Actions**` → `actions`
3. `**Bonus Actions**` → `bonus_actions`
4. `**Reactions**` → `reactions`
5. `**Legendary Actions**` → `legendary_actions`

`boxes.lua` turns any fully-bold paragraph into a `\DndMonsterSection` header,
so section titles are bare `**…**` lines; trait/action lines carry trailing
text and stay normal paragraphs.

Each entry = `**{name}.** {styled_desc}`. `styled_desc` (light, regex-based):

- leading attack phrase → italic, trailing `:` → `.`:
  `Melee Attack Roll`, `Ranged Attack Roll`, `Melee Weapon Attack`,
  `Ranged Weapon Attack`
- leading saving-throw phrase → italic, trailing `:` → `.`:
  `<Abil> Saving Throw` (e.g. `Dexterity Saving Throw`)
- `Hit` (word, at start or after whitespace, `:` → `.`) → **italic** `*Hit.*`

Nested `actions[].actions` / `attacks` / `action_options` are data-only refs —
**not** rendered. Only top-level entries with a name + desc.

## Samples (expected output)

`dnd5eapi.py monsters/giant-badger`

```
::: dndmonster
name: Giant Badger
type: Medium Beast, Unaligned
armor_class: 13
hit_points: 15 (2d8 + 6)
speed: 30 ft., burrow 10 ft.
str: 13
dex: 10
con: 17
int: 2
wis: 12
cha: 5
skills: Perception +3
damage_resistances: poison
senses: darkvision 60 ft., passive Perception 13
languages: —
challenge: 1/4

---

**Actions**

**Bite.** *Melee Attack Roll.* +3, reach 5 ft. *Hit.* 6 (2d4 + 1) Piercing damage.
:::
```

`dnd5eapi.py magic-items/vorpal-sword`

```
::: dnditem
Vorpal Sword
Weapon (Glaive, Greatsword, Longsword, or Scimitar), legendary (requires attunement)
You gain a +3 bonus to attack rolls and damage rolls made with this magic weapon. In addition, the weapon ignores Resistance to Slashing damage.

When you use this weapon to attack a creature that has at least one head and roll a 20 on the d20 for the attack roll, you cut off one of the creature's heads. …
:::
```

## 2024 schema notes (vs 2014)

- `armor_class` = `[{value, armor: []}]`, **no `type` field** → cannot tell
  natural/unarmored vs armor from the API; when `armor` is empty emit just the
  number (PHB "natural armor" detail, if wanted, is an override edit).
- **no `subtype`** field at all.
- `hit_points_roll` already spaced (`2d8 + 6`).
- Attack phrasing is `Melee/Ranged Attack Roll:` (2014 was `…Weapon Attack:
  to hit`).
- New top-level `bonus_actions`.
- Items: `rarity` + `attunement` are separate fields; `desc[0]` is only the
  type descriptor.

## Not doing (yet)

- No GraphQL, no batch/multi-index, no name→index resolution, no `--version`
  flag (2024 hardcoded), no other collections beyond `monsters` +
  `magic-items`.
- Output to stdout only (no `--file`).
- Auto-style is intentionally light; anything the regex misses is fixed by
  editing the override.
