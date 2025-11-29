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

def test_world_update_probabilities():
    world = models.World(DATA_DIR)
    get_location = world.get(models.Location, "vesnice")
    get_occupation = world.get(models.Occupation, "svec")
    assert get_location.probability == 1
    assert get_occupation.probability == 1
    world.update_probabilities({"Location:vesnice": 0.5})
    assert get_location.probability == 0.5
    assert get_occupation.probability == 1


def test_world_get_by_id():
    world = models.World(DATA_DIR)
    get_location = world.get_by_id("Location:vesnice")
    assert isinstance(get_location, models.Location)
    assert get_location.id == "Location:vesnice"
    assert get_location.name == "Vesnice"


def test_world_get_by_model():
    world = models.World(DATA_DIR)
    get_locations = world.get_by_model("Location")
    for i in get_locations:
        assert isinstance(i, models.Location)
