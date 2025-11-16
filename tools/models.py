import typing
import pydantic


class TestFile(pydantic.BaseModel):
    schema_name: typing.Literal["TestFile"] = pydantic.Field(alias="$schema")
    name: str

class Character(pydantic.BaseModel):
    schema_name: typing.Literal["Character"] = pydantic.Field(alias="$schema")
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

class MeleeWeapon(pydantic.BaseModel):
    schema_name: typing.Literal["MeleeWeapon"] = pydantic.Field(alias="$schema")
    name: str
    description: str
    demage: int
    price: float

class RangeWeapon(pydantic.BaseModel):
    schema_name: typing.Literal["RangeWeapon"] = pydantic.Field(alias="$schema")
    name: str
    description: str
    demage: int
    price: float

class CommonItem(pydantic.BaseModel):
    schema_name: typing.Literal["CommonItem"] = pydantic.Field(alias="$schema")
    name: str
    description: str
