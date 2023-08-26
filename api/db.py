from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DB_URL = f"mysql://{os.environ.get('MYSQL_USER')}:{os.environ.get('MYSQL_PASSWORD')}@{os.environ.get('MYSQL_HOST')}/{os.environ.get('MYSQL_DATABASE')}?charset=utf8"

# async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
# async_session = sessionmaker(
#     autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
# )

engine = create_engine(DB_URL)
SessionClass = sessionmaker(engine)
session = SessionClass()

Base = declarative_base()


# async def get_db():
#     async with async_session() as session:
#         yield session
def get_db():
    db = SessionClass()
    try:
        yield db
    finally:
        db.close()
