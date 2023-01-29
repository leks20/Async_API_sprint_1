from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from models.person import Person
from models.commons.sort import SortOrder
from services.person import PersonService, get_person_service

router = APIRouter()


@router.get(
    "/{person_id}",
    response_model=Person,
    summary="Get person by ID",
    description="Get information about person: ID and name",
    tags=["Persons"],
)
async def person_details(
    person_id: str, person_service: PersonService = Depends(get_person_service)
) -> Person:
    if person := await person_service.get_by_id(person_id):
        return Person.from_orm(person)

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="person not found")


@router.get(
    "",
    response_model=List[Person],
    summary="Get list of persons",
    description="Get a list of information about persons: id and name",
    tags=["Persons"],
)
async def person_search(
    query_: str,
    from_: int,
    size_: int,
    sort_order_: SortOrder,
    person_service: PersonService = Depends(get_person_service),
) -> List[Person]:
    sort_by_: str = "full_name.keyword"
    if result := await person_service.search_in_elastic(
        query_, from_, size_, sort_by_, sort_order_
    ):
        return result
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="person not found")
