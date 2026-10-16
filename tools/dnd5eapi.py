#!/usr/bin/env python3
"""Fetch one D&D 5e (2024) resource from dnd5eapi.co and emit a dndmd box.

Spec: docs/source/dobrodruzstvi/hlubinodul/docs/dnd5eapi-tool.md
Stdlib only. One resource per run, output to stdout.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib import error, request

API_BASE = "https://www.dnd5eapi.co/api/2024/"
API_VERSION = "2024"
OVERRIDES_DIR = Path(__file__).resolve().parent / "dnd5eapi-overrides"

ABILITY_ABBR = {
    "strength": "STR",
    "dexterity": "DEX",
    "constitution": "CON",
    "intelligence": "INT",
    "wisdom": "WIS",
    "charisma": "CHA",
}

CHALLENGE_FRACTIONS = {0.25: "1/4", 0.5: "1/2", 0.75: "3/4"}

MONSTER_SECTIONS = [
    ("special_abilities", None),
    ("actions", "Actions"),
    ("bonus_actions", "Bonus Actions"),
    ("reactions", "Reactions"),
    ("legendary_actions", "Legendary Actions"),
]


def fetch(collection, index, lang):
    """GET one API resource; return the parsed JSON object. Exit 1 on error."""
    url = f"{API_BASE}{collection}/{index}?lang={lang}"
    req = request.Request(url, headers={"Accept": "application/json"})
    try:
        with request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (error.HTTPError, error.URLError) as exc:
        print(f"error: fetch failed for {url}: {exc}", file=sys.stderr)
        sys.exit(1)


def override_path(lang, collection, index):
    """Override file path for a resource: <script>/dnd5eapi-overrides/<lang>/<collection>/<index>.json."""
    return OVERRIDES_DIR / lang / collection / f"{index}.json"


def write_override(path, resource):
    """Write raw resource JSON to the override path, creating parent dirs."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(resource, indent=2, ensure_ascii=False) + "\n")


def type_str(resource):
    """'Medium Beast, Unaligned' — Title-case type and each alignment word."""
    alignment = " ".join(w.title() for w in resource["alignment"].split())
    return f"{resource['size']} {resource['type'].title()}, {alignment}"


def armor_class_str(armor_classes):
    """'13' or '15 (leather armor, shield)'; multiple entries joined ' or '."""
    parts = []
    for ac in armor_classes:
        armor = [a["name"] for a in (ac.get("armor") or [])]
        if armor:
            parts.append(f"{ac['value']} ({', '.join(armor)})")
        else:
            parts.append(str(ac["value"]))
    return " or ".join(parts)


def speed_str(speed):
    """'30 ft., burrow 10 ft.' — walk unlabeled, fixed key order."""
    parts = []
    for key in ("walk", "fly", "swim", "burrow", "climb"):
        value = speed.get(key)
        if value:
            parts.append(value if key == "walk" else f"{key} {value}")
    return ", ".join(parts)


def proficiencies(resource):
    """Split proficiencies into (saving_throws, skills) display strings."""
    saves, skills = [], []
    for p in resource.get("proficiencies") or []:
        name = p["proficiency"]["name"]
        value = p.get("value") or 0
        if name.startswith("Saving Throw: "):
            saves.append(f"{ABILITY_ABBR[name[len('Saving Throw: '):].lower()]} +{value}")
        elif name.startswith("Skill: "):
            skills.append(f"{name[len('Skill: '):]} +{value}")
    return saves, skills


def senses_str(senses):
    """'darkvision 60 ft., passive Perception 13' — fixed key order."""
    parts = []
    for key in ("darkvision", "blindsight", "tremorsense", "truesight"):
        if senses.get(key):
            parts.append(f"{key} {senses[key]}")
    if senses.get("passive_perception") is not None:
        parts.append(f"passive Perception {senses['passive_perception']}")
    return ", ".join(parts)


def challenge_str(challenge):
    """1/4-style fractions; integer plain; other decimals trimmed."""
    if challenge in CHALLENGE_FRACTIONS:
        return CHALLENGE_FRACTIONS[challenge]
    if isinstance(challenge, float) and challenge.is_integer():
        challenge = int(challenge)
    if isinstance(challenge, float):
        return f"{challenge:g}"
    return str(challenge)


def styled_desc(desc):
    """Light regex styling: italicize leading attack/saving-throw phrase and 'Hit:'."""
    d = re.sub(r"^(Melee|Ranged) (Attack Roll|Weapon Attack): ?", r"*\1 \2.* ", desc)
    d = re.sub(r"^(\w+) Saving Throw: ?", r"*\1 Saving Throw.* ", d)
    d = re.sub(r"(?<!\S)Hit:", "*Hit.*", d)
    return d.strip()


def render_monster(resource):
    """Render a monster resource as a ::: dndmonster box."""
    lines = ["::: dndmonster", f"name: {resource['name']}", f"type: {type_str(resource)}"]
    if resource.get("armor_class"):
        lines.append(f"armor_class: {armor_class_str(resource['armor_class'])}")
    if resource.get("hit_points") is not None:
        roll = resource.get("hit_points_roll", "")
        lines.append(f"hit_points: {resource['hit_points']} ({roll})")
    if resource.get("speed"):
        lines.append(f"speed: {speed_str(resource['speed'])}")
    for short, key in (("str", "strength"), ("dex", "dexterity"), ("con", "constitution"),
                       ("int", "intelligence"), ("wis", "wisdom"), ("cha", "charisma")):
        lines.append(f"{short}: {resource[key]}")
    saves, skills = proficiencies(resource)
    if saves:
        lines.append(f"saving_throws: {', '.join(saves)}")
    if skills:
        lines.append(f"skills: {', '.join(skills)}")
    for key in ("damage_immunities", "damage_vulnerabilities", "damage_resistances",
                "condition_immunities"):
        values = resource.get(key)
        if values:
            lines.append(f"{key}: {', '.join(v.lower() for v in values)}")
    if resource.get("senses"):
        lines.append(f"senses: {senses_str(resource['senses'])}")
    if resource.get("languages") is not None:
        langs = resource["languages"]
        lines.append(f"languages: {'—' if langs == 'None' else langs}")
    if resource.get("challenge_rating") is not None:
        lines.append(f"challenge: {challenge_str(resource['challenge_rating'])}")

    paragraphs = ["---"]
    for field, header in MONSTER_SECTIONS:
        entries = [e for e in (resource.get(field) or [])
                   if e.get("name") and e.get("desc")]
        if not entries:
            continue
        if header:
            paragraphs.append(f"**{header}**")
        for entry in entries:
            paragraphs.append(f"**{entry['name']}.** {styled_desc(entry['desc'])}")

    return "\n".join(lines) + "\n\n" + "\n\n".join(paragraphs) + "\n:::"


def render_item(resource):
    """Render a magic-item resource as a ::: dnditem box."""
    desc = resource.get("desc") or []
    second_line = desc[0] if desc else ""
    rarity = (resource.get("rarity") or {}).get("name", "")
    second_line = f"{second_line}, {rarity.lower()}"
    if resource.get("attunement"):
        second_line += " (requires attunement)"
    lines = ["::: dnditem", resource["name"], second_line]
    return "\n".join(lines) + ("\n\n" + "\n\n".join(desc[1:]) if len(desc) > 1 else "") + "\n:::"


RENDERERS = {
    "monsters": render_monster,
    "magic-items": render_item,
}


def main(argv=None):
    """Parse CLI, load override (or fetch), render to stdout."""
    parser = argparse.ArgumentParser(
        description="Fetch one D&D 5e (2024) resource and emit a dndmd box.")
    parser.add_argument("target", help="collection/index, e.g. monsters/giant-badger")
    parser.add_argument("--dump-override", action="store_true",
                        help="fetch from API and write raw JSON to the override path")
    parser.add_argument("--output", choices=["dndmd"], default="dndmd",
                        help="output format (default: dndmd)")
    parser.add_argument("--lang", default="cs-CZ",
                        help="API lang param / override subdir (default: cs-CZ)")
    args = parser.parse_args(argv)

    try:
        collection, index = args.target.split("/", 1)
    except ValueError:
        parser.error("target must be collection/index")
    renderer = RENDERERS.get(collection)
    if renderer is None:
        parser.error(f"unknown collection: {collection}")

    opath = override_path(args.lang, collection, index)
    if args.dump_override:
        # Always re-fetch: the dump point is seeding/refreshing the override.
        resource = fetch(collection, index, args.lang)
        write_override(opath, resource)
    elif opath.exists():
        resource = json.loads(opath.read_text())
    else:
        resource = fetch(collection, index, args.lang)

    print(renderer(resource))


if __name__ == "__main__":
    main()
