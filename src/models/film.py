from typing import Any, List

from enum import Enum
from pydantic import Field, UUID4

from models.commons.orjson import BaseOrjsonModel
from models.person import Person


class Film(BaseOrjsonModel):
    id: str = Field(default_factory=UUID4)
    title: str | None = None
    description: str | None = None
    imdb_rating: float
    genre: List[str] = []
    director: List[str] | str | None = None
    actors: List[Person] = []
    writers: List[Person] = []


class FilmSortBy(str, Enum):
    title = "title"
    imdb_rating = "imdb_rating"
