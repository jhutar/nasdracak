# Adresář `data/`

Tento adresář slouží k ukládání herních dat pro RPG hru ve formátu YAML. Všechny datové soubory sdílejí společný základní model `BaseModelWithId` a jsou definovány v `tools/models.py`.

## Základní model: `BaseModelWithId`

Každý datový soubor v tomto adresáři obsahuje následující pole:
- `id`: Unikátní identifikátor ve formátu `ModelName:nazev_souboru`.
- `probability`: Váha pro výběr při generování postav (výchozí: 1).
- `modifiers`: Slovník, který může ovlivnit pravděpodobnost výběru jiných položek. Hodnota `0.1` znamená silné zmenšení pravděpodobnosti (váha se sníží na desetinu), zatímco hodnota `10` znamená silné zvětšení pravděpodobnosti (váha se zvýší desetkrát). Hodnota `1` nemá smysl, protože nijak nezmění váhu a navíc ji validator považuje za chybu.

## Struktura dat

### Dovednosti (Skill)
Definovány v `data/skill/*.yaml`.
- `name`, `description`, `bonus` (odkaz na `Bonus`), `requires` (seznam `Skill`).

### Bonusy (Bonus)
Definovány v `data/meta/bonus/*.yaml`.
- `name`, `description`.

### Postavy (Character)
Definovány v `data/character/*.yaml`.
- `race` (odkaz na `Race`), `name`, `appearance`, `background`, `strength`, `dexterity`, `inteligence`, `charisma`, `level`, `health`, `health_max`, `magenergy`, `magenergy_max`, `inventory` (seznam odkazů na `MeleeWeapon`, `RangeWeapon`, `CommonItem`), `occupation` (odkaz na `Occupation`), `location` (odkaz na `Location`).

### Povolání (Occupation)
Definovány v `data/meta/occupation/*.yaml`.
- `name`, `description`.

### Lokace (Location)
Definovány v `data/meta/location/*.yaml`.
- `name`.

### Rasy (Race)
Definovány v `data/meta/race/*.yaml`.
- `name`, `description`, `names` (seznam jmen), `innate_strength`, `innate_dexterity`, `innate_inteligence`, `innate_charisma`.

### Vlastnosti (Property)
Definovány v `data/meta/property/*.yaml`.
- `name`, `description`.

### Zbraně na blízko (MeleeWeapon)
Definovány v `data/weapon/melee/*.yaml`.
- `name`, `description`, `demage`, `price`.

### Střelné zbraně (RangeWeapon)
Definovány v `data/weapon/range/*.yaml`.
- `name`, `description`, `demage`, `price`.

### Obyčejné předměty (CommonItem)
Definovány v `data/item/common/*.yaml`.
- `name`, `description`, `price`.

## Modely dat

Struktura dat je definována v Python souboru `tools/models.py`, který zajišťuje konzistenci a správnost datových typů pro všechny výše uvedené entity.

## Validace dat

Pro kontrolu správnosti a konzistence dat se používá linter. Linter lze spustit příkazem:
```bash
venv/bin/python tools/doit.py --data data/ lint
```
**Důležité:** Po každé změně v adresáři `data/` je nutné před commitem ověřit data pomocí tohoto linteru.

## Relevantní dokumentace

Pro širší kontext projektu a další detaily o použitých technologiích se podívejte do hlavního souboru `GEMINI.md` v kořenovém adresáři projektu.
