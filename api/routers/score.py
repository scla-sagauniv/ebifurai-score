from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

import api.cruds.score as s_crud
from api.db import get_db
from api.cruds.score import readScoreByUserId, updateScore
from api.models.user import User
from api.models.score import Score
from api.schemas.update_score_req import UpdateScoreReq

# from api.db import get_db

import api.schemas.score_res as s_schema
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()


@router.put("/score", response_model=s_schema.ScoreRes)
async def update_score(req: UpdateScoreReq, db: Session = Depends(get_db)):
    score = readScoreByUserId(user_id=req.user_id, db=db)
    if req.score > score.score:
        score.score = req.score
        updateScore(score=score, db=db)
    return s_schema.ScoreRes(message="OK")
