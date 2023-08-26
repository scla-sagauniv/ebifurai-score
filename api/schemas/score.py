from typing import Optional

from pydantic import BaseModel, Field

class ScoreRow(BaseModel):
    user_id: str
    score: int

    class Config:
        orm_mode = True
