from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI

from app.db import create_db_and_tables
from app.routes import ratings, users


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(ratings.router)
app.include_router(api_router)
