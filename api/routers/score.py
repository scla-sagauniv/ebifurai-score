from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.score as s_crud

# from api.db import get_db

import api.schemas.score as s_schema
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()


@router.put("/scores/{score_id}", response_model=s_schema.ScoreRow)
async def update_score():
    return
