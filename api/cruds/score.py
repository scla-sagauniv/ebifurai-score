from sqlalchemy.ext.asyncio import AsyncSession

import api.models.score as s_model
import api.schemas.score as s_schema

from typing import List, Tuple, Optional

async def update_score(
    db: AsyncSession, score_create: s_schema.ScoreRow, original: s_model.Score
) -> s_model.Score:
    original.score = score_create.score
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original