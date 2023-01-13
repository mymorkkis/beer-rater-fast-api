from pydantic import BaseModel
from fastapi import APIRouter

from app.db import database


class UserCreate(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int
    email: str


router = APIRouter()


@router.get("/users/", response_model=list[User])
async def users():
    query = "SELECT * FROM users"
    return await database.fetch_all(query)


@router.post("/users/", response_model=User)
async def set_rating(user: UserCreate):
    query = (
        "INSERT INTO users (email, password) VALUES (:email, :password) RETURNING id"
    )
    values = user.dict()
    user_id = await database.execute(query, values)
    return {"email": user.email, "id": user_id}
