import os
from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine

# TODO Move these to config file using Pydantic Settings
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
port = os.environ["POSTGRES_PORT"]
db_name = os.environ["POSTGRES_DB"]

url = f"postgresql://{user}:{password}@db:{port}/{db_name}"

engine = create_engine(url=url)  # add echo=True to see SQL statements executed


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


DBSession = Annotated[Session, Depends(get_session)]
