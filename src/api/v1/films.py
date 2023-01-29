from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from services.film import FilmService, get_film_service
from models.film import Film, FilmSortBy
from models.commons.sort import SortOrder

router = APIRouter()


@router.get(
    "/{film_id}",
    response_model=Film,
    summary="Get film by ID",
    description="Get information about film: ID, title, description, imdb_rating, genre, director, actors, writers",
    tags=["Films"],
)
async def film_details(
    film_id: str, film_service: FilmService = Depends(get_film_service)
) -> Film:
    if film := await film_service.get_by_id(film_id):
        return Film.from_orm(film)
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="film not found")


@router.get(
    "",
    response_model=List[Film],
    summary="Get list of films",
    description="Get a list of information about films: ID, title, description, imdb_rating, genre, director, actors, writers",
    tags=["Films"],
)
async def film_search(
    query_: str,
    from_: int,
    size_: int,
    sort_by_: FilmSortBy,
    sort_order_: SortOrder,
    film_service: FilmService = Depends(get_film_service),
) -> List[Film]:
    if sort_by_ == "title":
        sort_by_ += ".keyword"
    if result := await film_service.search_in_elastic(
        query_, from_, size_, sort_by_, sort_order_
    ):
        return result
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="film not found")
