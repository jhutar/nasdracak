import sys
import os
import argparse
import tempfile
from pathlib import Path

# Add the 'tools' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from doit import format_entity  # noqa: E402


def test_format_entity_single_entity():
    """Tests the format_entity function for a single entity using minimal data."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Setup data directory with minimal valid data
        test_data_dir = Path(tmpdir) / "data"
        test_melee_weapon_dir = test_data_dir / "weapon" / "melee"
        test_melee_weapon_dir.mkdir(parents=True)

        melee_weapon_file = test_melee_weapon_dir / "mec-rezavy.yaml"
        melee_weapon_content = """
id: MeleeWeapon:mec-rezavy
name: Meč po dědovi
description: Rezavý meč.
demage: +1
price: 2.5
"""
        melee_weapon_file.write_text(melee_weapon_content)

        template_file = Path("tools/tests/test_templates/single_weapon.yaml.j2")
        output_dir = Path(tmpdir) / "output"
        output_dir.mkdir()

        args = argparse.Namespace(
            data=str(test_data_dir),
            entity="MeleeWeapon:mec-rezavy",
            model=None,
            template=str(template_file),
            output_dir=str(output_dir),
            all_in_one=False,
        )

        format_entity(args)

        expected_output_file = output_dir / "Meč po dědovi.yaml"
        assert expected_output_file.exists()
        output_content = expected_output_file.read_text()
        expected_content = """
Name: Meč po dědovi
Description: Rezavý meč.
Demage: 1
"""
        assert output_content.strip() == expected_content.strip()


def test_format_entity_all_in_one():
    """Tests the format_entity function with --all-in-one option using minimal data."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Setup data directory with minimal valid data
        test_data_dir = Path(tmpdir) / "data"
        test_melee_weapon_dir = test_data_dir / "weapon" / "melee"
        test_melee_weapon_dir.mkdir(parents=True)

        melee_weapon_file1 = test_melee_weapon_dir / "mec-rezavy.yaml"
        melee_weapon_content1 = """
id: MeleeWeapon:mec-rezavy
name: Meč po dědovi
description: Rezavý meč.
demage: +1
price: 2.5
"""
        melee_weapon_file1.write_text(melee_weapon_content1)

        melee_weapon_file2 = test_melee_weapon_dir / "sekera.yaml"
        melee_weapon_content2 = """
id: MeleeWeapon:sekera
name: Sekera válečná
description: Těžká sekera.
demage: +2
price: 5.0
"""
        melee_weapon_file2.write_text(melee_weapon_content2)

        template_file = Path("tools/tests/test_templates/all_weapons.yaml.j2")
        output_dir = Path(tmpdir) / "output"
        output_dir.mkdir()

        args = argparse.Namespace(
            data=str(test_data_dir),
            entity=None,
            model="MeleeWeapon",
            template=str(template_file),
            output_dir=str(output_dir),
            all_in_one=True,
        )

        format_entity(args)

        expected_output_file = output_dir / "all.yaml"
        assert expected_output_file.exists()
        output_content = expected_output_file.read_text().strip()

        expected_content = """
Name: Meč po dědovi
Demage: 1
---

Name: Sekera válečná
Demage: 2
---
"""
        assert output_content.strip() == expected_content.strip()
