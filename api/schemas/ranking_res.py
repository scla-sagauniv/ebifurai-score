from typing import Optional, List
from pydantic import BaseModel, Field

from api.schemas.ranking_row import RankingRow


class RankingRes(BaseModel):
    ranking: List[RankingRow]
