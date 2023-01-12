from fastapi import FastAPI
from pydantic import BaseModel

from app.db import database, ratings

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# TODO Move below to routes package
class BeerRatingCreate(BaseModel):
    beer_id: int
    rating: int


class BeerRating(BaseModel):
    id: int
    beer_id: int
    rating: int


@app.get("/", response_model=dict)
def healthcheck():
    return {"status": "OK"}


@app.get("/ratings/", response_model=list[BeerRating])
async def read_notes():
    query = ratings.select()
    return await database.fetch_all(query)


@app.get("/ratings/{rating_id}", response_model=BeerRating)
async def read_notes(rating_id: int):
    # TODO Handle noT found
    query = ratings.select().where(ratings.c.id == rating_id)
    return await database.fetch_one(query)


@app.post("/ratings/", response_model=BeerRating)
async def read_item(beer_rating: BeerRatingCreate):
    query = ratings.insert().values(
        beer_id=beer_rating.beer_id, rating=beer_rating.rating
    )
    last_record_id = await database.execute(query)
    return {**beer_rating.dict(), "id": last_record_id}
