from sqlalchemy import Column, Integer, String
from api.db import Base


class User(Base):
    __tablename__ = "Users"

    id = Column(String(128), primary_key=True)
    name = Column(String(64))
    password = Column(String(128))
    line_uid = Column(String(64))
