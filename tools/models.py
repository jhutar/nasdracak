import typing
import pydantic


class TestFile(pydantic.BaseModel):
    schema_name: typing.Literal["TestFile"] = pydantic.Field(alias="$schema")
    name: str
