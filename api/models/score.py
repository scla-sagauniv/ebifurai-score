from sqlalchemy import Column, Integer, String
from api.db import Base


class Score(Base):
    __tablename__ = "scores"

    user_id = Column(String(20), primary_key=True, default="あいう")
    score = Column(Integer, default=100)
