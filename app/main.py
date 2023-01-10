from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BeerRating(BaseModel):
    rating: int


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, query: str = None):
    return {"item_id": item_id, "q": query}
