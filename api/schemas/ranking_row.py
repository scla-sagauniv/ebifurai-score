from typing import Optional, List

from pydantic import BaseModel, Field


class RankingRow(BaseModel):
    rank: int
    user_id: str
    name: str
    score: int
