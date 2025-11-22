import pathlib
import pytest
import tempfile
import sys
import os

# Add the 'tools' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import models   # noqa: E402


DATA_DIR = pathlib.Path("tools/tests/test_lint_directory")

def test_world_loads_dir():
    world = models.World(DATA_DIR)
    assert len(world._all_models) > 0
    assert any(isinstance(m, models.Location) for m in world._all_models.values())
    assert any(isinstance(m, models.Occupation) for m in world._all_models.values())


def test_world_get_location():
    world = models.World(DATA_DIR)
    get_location = world.get(models.Location, "vesnice")
    assert isinstance(get_location, models.Location)
    assert get_location.id == "Location:vesnice"


def test_world_pick_location():
    world = models.World(DATA_DIR)
    picked_location = world.pick(models.Location)
    assert isinstance(picked_location, models.Location)
    assert picked_location.id == "Location:vesnice"


def test_world_pick_missing_model():
    world = models.World(DATA_DIR)
    world.pick(models.Location)
    with pytest.raises(models.ModelError, match="No models of type Race found."):
        world.pick(models.Race)


def test_world_pick_from_empty_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        data_dir = pathlib.Path(tmpdirname)
        world = models.World(data_dir)
        with pytest.raises(models.ModelError, match="No models of type Location found."):
            world.pick(models.Location)
