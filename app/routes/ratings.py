from pydantic import BaseModel
from fastapi import APIRouter

from app.db import database


class BeerRatingCreate(BaseModel):
    user_id: int
    beer_id: int
    rating: int


class BeerRating(BaseModel):
    id: int
    user_id: int
    beer_id: int
    rating: int


router = APIRouter()


@router.get("/ratings/", response_model=list[BeerRating])
async def get_ratings():
    query = "SELECT * FROM ratings"
    return await database.fetch_all(query)


@router.get("/ratings/{rating_id}", response_model=BeerRating)
async def get_rating(rating_id: int):
    # TODO Handle not found
    query = "SELECT * FROM ratings WHERE id = :rating_id"
    values = dict(rating_id=rating_id)
    return await database.fetch_one(query, values)


@router.post("/ratings/", response_model=BeerRating)
async def set_rating(beer_rating: BeerRatingCreate):
    query = """
        INSERT INTO ratings (user_id, beer_id, rating)
        VALUES (:user_id, :beer_id, :rating)
        RETURNING id
    """
    values = beer_rating.dict()
    beer_rating_id = await database.execute(query, values)
    return {**values, "id": beer_rating_id}
