import os
import databases
import sqlalchemy
from pydantic import PostgresDsn

DSN = PostgresDsn.build(
    scheme="postgresql",
    user=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
    host="db",
    port=os.environ["POSTGRES_PORT"],
    path=f'/{os.environ["POSTGRES_DB"]}',
)

database = databases.Database(DSN)

metadata = sqlalchemy.MetaData()

# TODO Move to models
ratings = sqlalchemy.Table(
    "ratings",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("beer_id", sqlalchemy.Integer),
    sqlalchemy.Column("rating", sqlalchemy.Integer),
)


engine = sqlalchemy.create_engine(DSN)
metadata.create_all(engine)
