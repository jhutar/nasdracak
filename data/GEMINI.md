# Adresář `data/`

Tento adresář slouží k ukládání herních dat pro RPG hru, jako jsou dovednosti (Skill), bonusy (Bonus), postavy (Character), povolání (Occupation), lokace (Location) a předměty (MeleeWeapon, RangeWeapon, CommonItem), ve formátu YAML.

## Struktura dat

- **Dovednosti (Skill):** Definovány v souborech `data/skill/*.yaml`. Každá dovednost má `id`, `name`, `description`, odkaz na `bonus` a volitelný seznam `requires` jiných dovedností. Příklad: `data/skill/bojove_finty.yaml`.
- **Bonusy (Bonus):** Definovány v souborech `data/meta/bonus/*.yaml`. Každý bonus má `id`, `name` a `description`. Příklad: `data/meta/bonus/boj.yaml`.
- **Postavy (Character):** Definovány v `data/character/*.yaml`. Obsahuje `id`, `name`, `appearance`, `background`, atributy (`strength`, `dexterity`, `inteligence`, `charisma`), `level`, `health`, `magenergy`, `inventory`, `occupation` a `location`.
- **Povolání (Occupation):** Definovány v `data/meta/occupation/*.yaml`. Obsahuje `id` a `name`.
- **Lokace (Location):** Definovány v `data/meta/location/*.yaml`. Obsahuje `id` a `name`.
- **Zbraně na blízko (MeleeWeapon):** Definovány v `data/weapon/melee/*.yaml`. Obsahuje `id`, `name`, `description`, `demage` a `price`.
- **Střelné zbraně (RangeWeapon):** Definovány v `data/weapon/range/*.yaml`. Obsahuje `id`, `name`, `description`, `demage` a `price`.
- **Obyčejné předměty (CommonItem):** Definovány v `data/item/common/*.yaml`. Obsahuje `id`, `name`, `description` a `price`.

## Modely dat

Struktura dat je definována v Python souboru `tools/models.py`, který zajišťuje konzistenci a správnost datových typů pro všechny výše uvedené entity.

## Validace dat

Pro kontrolu správnosti a konzistence dat se používá linter. Linter lze spustit příkazem:
```bash
venv/bin/python tools/doit.py --data data/ lint
```

## Relevantní dokumentace

Pro širší kontext projektu a další detaily o použitých technologiích se podívejte do hlavního souboru `GEMINI.md` v kořenovém adresáři projektu.