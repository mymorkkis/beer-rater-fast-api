from fastapi import APIRouter, FastAPI

from app.db import create_db_and_tables
from app.routes import ratings, users

app = FastAPI()


@app.on_event("startup")
async def startup():
    create_db_and_tables()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(ratings.router)
app.include_router(api_router)
