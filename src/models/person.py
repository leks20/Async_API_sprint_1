from pydantic import UUID4, Field

from models.commons.orjson import BaseOrjsonModel


class Person(BaseOrjsonModel):
    id: str = Field(default_factory=UUID4)
    name: str = Field(..., alias="full_name")
