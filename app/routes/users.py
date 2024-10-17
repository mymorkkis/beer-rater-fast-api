from fastapi import APIRouter
from sqlmodel import Field, SQLModel, select

from app.db import DBSession

# TODO Create proper flow for user authentication


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True)


router = APIRouter()


@router.get("/users/", response_model=list[User])
async def users(session: DBSession):
    return session.exec(select(User)).all()


@router.post("/users/", response_model=User)
async def set_rating(user: User, session: DBSession):
    # TODO Handle unique constraint
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
