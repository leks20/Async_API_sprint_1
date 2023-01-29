from pydantic import UUID4, Field

from models.commons.orjson import BaseOrjsonModel


class Genre(BaseOrjsonModel):
    id: str = Field(default_factory=UUID4)
    name: str
    description: str | None = None
