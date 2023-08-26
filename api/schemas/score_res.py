from typing import Optional

from pydantic import BaseModel, Field


class ScoreRes(BaseModel):
    message: str
