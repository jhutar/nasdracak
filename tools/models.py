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
