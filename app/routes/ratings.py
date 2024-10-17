from fastapi import APIRouter
from sqlmodel import Field, SQLModel, select

from app.db import DBSession


class BeerRating(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    beer_id: int  # will be from Brewdog's Punk API
    rating: int  # TODO limit this to 1-10


router = APIRouter()


@router.get("/ratings/", response_model=list[BeerRating])
async def get_ratings(session: DBSession):
    return session.exec(select(BeerRating)).all()


@router.get("/ratings/{rating_id}", response_model=BeerRating)
async def get_rating(rating_id: int, session: DBSession):
    rating = session.get(BeerRating, rating_id)
    # TODO Handle not found
    return rating


@router.post("/ratings/", response_model=BeerRating)
async def set_rating(beer_rating: BeerRating, session: DBSession):
    # TODO filter by user and add pagination
    session.add(beer_rating)
    session.commit()
    session.refresh(beer_rating)
    return beer_rating
