from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine

from app.config import settings


db_user = settings.postgres_user
db_password = settings.postgres_password
db_port = settings.postgres_port
db_name = settings.postgres_db

dsn = f"postgresql://{db_user}:{db_password}@db:{db_port}/{db_name}"

engine = create_engine(
    url=dsn,
    echo=settings.debug,
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


DBSession = Annotated[Session, Depends(get_session)]
