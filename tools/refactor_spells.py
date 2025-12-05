import os
import pathlib
import yaml

# Mapping from bonus ID to spell directory name
MAGIC_TYPES = {
    "Bonus:magie-vzduchu": "air",
    "Bonus:magie-vody": "water",
    "Bonus:magie-zeme": "earth",
    "Bonus:magie-ohne": "fire",
    "Bonus:magie-zivota": "life",
    "Bonus:magie-smrti": "death",
    "Bonus:magie-ducha": "spirit",
}

SKILL_DIR = pathlib.Path("data/skill")
SPELL_DIR = pathlib.Path("data/spells")


def main():
    """
    Converts magic-related Skill files into Spell files, moving them to a new directory structure
    and deleting the original files.
    """
    SPELL_DIR.mkdir(exist_ok=True)
    for magic_type in MAGIC_TYPES.values():
        (SPELL_DIR / magic_type).mkdir(exist_ok=True)

    for skill_file in SKILL_DIR.glob("*.yaml"):
        with open(skill_file, "r") as f:
            data = yaml.safe_load(f)

        if data.get("bonus") in MAGIC_TYPES:
            print(f"Converting skill: {skill_file.name}")

            # Prepare new spell data
            spell_data = {
                "id": data["id"].replace("Skill:", "Spell:").replace("-", "_"),
                "name": data["name"],
                "description": data["description"],
                "rule": "TODO",
            }

            # Determine new path
            magic_type = MAGIC_TYPES[data["bonus"]]
            spell_filename = skill_file.name.replace("-", "_")
            new_spell_path = SPELL_DIR / magic_type / spell_filename

            # Write new spell file
            with open(new_spell_path, "w") as f:
                yaml.dump(spell_data, f, allow_unicode=True)
            print(f"  -> Created spell: {new_spell_path}")

            # Delete old skill file
            os.remove(skill_file)
            print(f"  -> Deleted skill file: {skill_file}")


if __name__ == "__main__":
    main()
