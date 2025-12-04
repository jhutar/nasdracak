import sys
import pydantic
import typing
import inspect
import yaml
import json
import pathlib
import random
import glob
import logging


logger = logging.getLogger(__name__)


class BaseModelWithId(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    _file_path: str | None = None  # From where it was loaded
    id: str
    probability: int = 1  # When generating character, this is weight for entity to pick
    modifiers: dict[str, float] = (
        {}
    )  # When generating character and this item s picked, it can change probability of other items that are about to be picked

    @pydantic.field_validator("id")
    @classmethod
    def check_id_format(cls, v: str) -> str:
        expected_prefix = f"{cls.__name__}:"
        if not v.startswith(expected_prefix):
            raise ValueError(f"ID must start with '{expected_prefix}'")
        return v

    @pydantic.field_validator("modifiers")
    @classmethod
    def check_modifier_ids(cls, v: dict[str, float]) -> dict[str, float]:
        for mod_id in v.keys():
            mod_schema = mod_id.split(":")[0]
            if mod_schema not in SCHEMA_REGISTRY:
                raise ValueError(
                    f"Modifier for '{mod_id}' does not look like valid ID."
                )
        return v


class Character(BaseModelWithId):
    race: str
    name: str
    appearance: str  # How does the character look like
    background: str  # What is the background story of the character, its motivation
    strength: int
    dexterity: int
    inteligence: int
    charisma: int
    level: int
    health: int
    health_max: int
    magenergy: int
    magenergy_max: int
    inventory: list[str] = []
    occupation: str
    location: str

    @pydantic.field_validator("inventory")
    @classmethod
    def check_inventory_item_ids(cls, v: list[str]) -> list[str]:
        for item_id in v:
            ok = False
            for model_name in ["MeleeWeapon", "RangeWeapon", "CommonItem"]:
                if item_id.startswith(model_name + ":"):
                    ok = True
            if not ok:
                raise ValueError(f"Item '{item_id}' does not look like valid ID.")
        return v

    @pydantic.field_validator("race")
    @classmethod
    def check_race(cls, v: str) -> str:
        if v.startswith("Race:"):
            return v
        else:
            raise ValueError(f"Invalid occupation '{v}'.")

    @pydantic.field_validator("occupation")
    @classmethod
    def check_occupation(cls, v: str) -> str:
        if v.startswith("Occupation:"):
            return v
        else:
            raise ValueError(f"Invalid occupation '{v}'.")

    @pydantic.field_validator("location")
    @classmethod
    def check_location(cls, v: str) -> str:
        if v.startswith("Location:"):
            return v
        else:
            raise ValueError(f"Invalid location '{v}'.")


class Occupation(BaseModelWithId):
    name: str
    description: str


class Location(BaseModelWithId):
    name: str


class MeleeWeapon(BaseModelWithId):
    name: str
    description: str
    demage: int
    price: float


class RangeWeapon(BaseModelWithId):
    name: str
    description: str
    demage: int
    price: float


class CommonItem(BaseModelWithId):
    name: str
    description: str
    price: float


class Bonus(BaseModelWithId):
    """Describes bonuses from various skills."""

    name: str
    description: str


class Skill(BaseModelWithId):
    name: str
    description: str
    bonus: str
    requires: list[str] = []

    @pydantic.field_validator("bonus")
    @classmethod
    def check_bonus_id(cls, v: str) -> str:
        if not v.startswith("Bonus:"):
            raise ValueError(f"Bonus '{v}' does not look like valid ID.")
        return v

    @pydantic.field_validator("requires")
    @classmethod
    def check_requires_ids(cls, v: list[str]) -> list[str]:
        for skill_id in v:
            if not skill_id.startswith("Skill:"):
                raise ValueError(f"Skill '{skill_id}' does not look like valid ID.")
        return v


class Race(BaseModelWithId):
    name: str
    description: str
    names: list[str] = []
    innate_strength: int
    innate_dexterity: int
    innate_inteligence: int
    innate_charisma: int


class Property(BaseModelWithId):
    name: str
    description: str


class ModelError(Exception):
    pass


SCHEMA_REGISTRY: typing.Dict[str, typing.Type[pydantic.BaseModel]] = dict(
    inspect.getmembers(
        sys.modules[__name__],
        lambda member: inspect.isclass(member)
        and member.__module__ == __name__
        and issubclass(member, pydantic.BaseModel),
    )
)


def load_file(file_path: str) -> BaseModelWithId:
    with open(file_path, "r") as f:
        if file_path.suffix == ".json":
            data = json.load(f)
        else:
            data = yaml.safe_load(f)

    if data is None:
        raise ModelError("File is empty or contains only comments.")

    if not isinstance(data, dict):
        raise ModelError("File does not contain dictionary.")

    item_id = data.get("id")
    if not item_id:
        raise ModelError("No 'id' field found.")

    schema_name = item_id.split(":")[0]
    model = SCHEMA_REGISTRY.get(schema_name)
    if not model:
        raise ModelError(
            f"No model found for schema '{schema_name}' (from id '{item_id}')."
        )

    model.model_validate(data)

    item = model(**data)
    item._file_path = file_path

    return item


def list_dir_files(data_dir: pathlib.Path) -> list[pathlib.Path]:
    return sorted(list(data_dir.rglob("*.yaml")) + list(data_dir.rglob("*.json")))


class World:
    def __init__(self, data_dir: pathlib.Path = pathlib.Path("data")) -> None:
        self._all_models: dict[str, BaseModelWithId] = {}

        for file_path in list_dir_files(data_dir):
            try:
                model_instance = load_file(file_path)
                if model_instance.id in self._all_models:
                    raise ModelError(f"Duplicate ID {model_instance.id} found")
                self._all_models[model_instance.id] = model_instance
            except Exception as e:
                logger.warning(f"Loading '{file_path}' failed, skipping. Error: {e}")

    def get(
        self, model_type: typing.Type[BaseModelWithId], name: str
    ) -> BaseModelWithId:
        return self._all_models[f"{model_type.__name__}:{name}"]

    def get_by_id(self, entid: str) -> BaseModelWithId:
        model_name = entid.split(":")[0]
        model_type = SCHEMA_REGISTRY.get(model_name)
        entity_name = entid[len(model_name) + 1 :]
        return self.get(model_type, entity_name)

    def get_by_model(self, model_name: str) -> list[BaseModelWithId]:
        model_type = SCHEMA_REGISTRY.get(model_name)
        if model_type == None:
            raise Exception(f"Unknown model '{model_name}'")
        return [m for m in self._all_models.values() if isinstance(m, model_type)]

    def pick(self, model_type: typing.Type[BaseModelWithId]) -> BaseModelWithId:
        candidates = [m for m in self._all_models.values() if isinstance(m, model_type)]
        if not candidates:
            raise ModelError(f"No models of type {model_type.__name__} found.")

        weights = [c.probability for c in candidates]
        return random.choices(candidates, weights=weights, k=1)[0]

    def update_probabilities(self, updates: dict[str, float]) -> None:
        for k, v in updates.items():
            entity = self._all_models[k]
            logging.debug(
                f"Changing probability for '{entity.id}' from {entity.probability} to {entity.probability * v}"
            )
            entity.probability = entity.probability * v
