import pydantic


class BaseModelWithId(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

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

    @pydantic.field_validator("inventory")
    @classmethod
    def check_inventory_item_ids(cls, v: list[str]) -> list[str]:
        for item_id in v:
            for model_name in ["MeleeWeapon", "RangeWeapon", "CommonItem"]:
                if item_id.startswith(model_name + ":"):
                    return v
            else:
                raise ValueError(f"Item '{item_id}' does not look like valid ID.")
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
