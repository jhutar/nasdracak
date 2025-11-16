import typing
import pydantic


class BaseModelWithId(pydantic.BaseModel):
    id: str

    @pydantic.field_validator("id")
    @classmethod
    def check_id_format(cls, v: str) -> str:
        expected_prefix = f"{cls.__name__}:"
        if not v.startswith(expected_prefix):
            raise ValueError(f"ID must start with '{expected_prefix}'")
        return v


class TestFile(BaseModelWithId):
    name: str

class Character(BaseModelWithId):
    name: str
    appearance: str   # How does the character look like
    background: str   # What is the background story of the character, its motivation
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

    @pydantic.field_validator("inventory")
    @classmethod
    def check_inventory_item_ids(cls, v: list[str]) -> list[str]:
        for item_id in v:
            if ":" not in item_id:
                raise ValueError(f"Invalid inventory item ID format '{item_id}'. Expected 'ModelName:id_value'.")
            model_name = item_id.split(":")[0]
            if model_name not in ["MeleeWeapon", "RangeWeapon", "CommonItem"]: # Add other item types here as they are created
                raise ValueError(f"Unknown item type '{model_name}' in inventory ID '{item_id}'.")
        return v

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
