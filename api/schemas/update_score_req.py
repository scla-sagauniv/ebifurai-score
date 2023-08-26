from typing import Optional

from pydantic import BaseModel, Field


class UpdateScoreReq(BaseModel):
    # user_id: str
    score: int
