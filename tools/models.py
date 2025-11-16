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
