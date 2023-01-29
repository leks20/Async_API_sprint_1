from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from services.genre import GenreService, get_genre_service
from models.genre import Genre
from models.commons.sort import SortOrder


router = APIRouter()


@router.get(
    "/{genre_id}",
    response_model=Genre,
    summary="Get genre by ID",
    description="Get information about genre: ID, name, description",
    tags=["Genres"],
)
async def genre_details(
    genre_id: str, genre_service: GenreService = Depends(get_genre_service)
) -> Genre:
    if genre := await genre_service.get_by_id(genre_id):
        return Genre.from_orm(genre)

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="genre not found")


@router.get(
    "",
    response_model=List[Genre],
    summary="Get list of genres",
    description="Get a list of information about genres: id, name, description",
    tags=["Genres"],
)
async def genre_search(
    query_: str,
    from_: int,
    size_: int,
    sort_order_: SortOrder,
    genre_service: GenreService = Depends(get_genre_service),
) -> List[Genre]:
    sort_by_: str = "name.keyword"
    if result := await genre_service.search_in_elastic(
        query_, from_, size_, sort_by_, sort_order_
    ):
        return result
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="genre not found")
