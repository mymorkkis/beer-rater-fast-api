import os
import databases
import sqlalchemy
from pydantic import PostgresDsn

DSN = PostgresDsn.build(
    # TODO Update this to use the "+asyncpg" driver
    scheme="postgresql",
    user=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
    host="db",  # compose db service name
    port=os.environ["POSTGRES_PORT"],
    path=f'/{os.environ["POSTGRES_DB"]}',
)

database = databases.Database(DSN)

engine = sqlalchemy.create_engine(DSN)
