from typing import List
from fastapi import APIRouter, HTTPException, Depends
from api.db import get_db
import api.schemas.ranking_row as r_schema
from api.schemas.ranking_res import RankingRes
import api.schemas.score as s_schema
import api.cruds.ranking as r_crud
import api.cruds.score as s_crud
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

# from api.db import get_db


router = APIRouter()


@router.get("/ranking", response_model=RankingRes)
# async def list_ranking(db: AsyncSession = Depends(get_db)):
async def list_ranking(db: Session = Depends(get_db)):
    res = await r_crud.get_ranking(db)
    return res
