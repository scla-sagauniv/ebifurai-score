from typing import List, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.score as s_model
import api.schemas.ranking as r_schemas
import api.schemas.score as s_schemas


async def get_ranking(db: AsyncSession) -> List[Tuple[str,int]]:
    result: Result = await(
        db.execute(
            select(
                s_model.Score.userid,
                s_model.Score.score,
            )
        )   
    )
    res = result.all()
    
    print("result:")
    print(res[0][0])
    return res