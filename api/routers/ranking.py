from typing import List
from fastapi import APIRouter, HTTPException, Depends
import api.schemas.ranking as r_schema
import api.schemas.score as s_schema
import api.cruds.ranking as r_crud
import api.cruds.score as s_crud
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db



router = APIRouter()

@router.get("/ranking", response_model=List[s_schema.ScoreRow])
async def list_ranking(db: AsyncSession = Depends(get_db)):
    return await r_crud.get_ranking(db)

