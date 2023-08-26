import os
from typing import Optional
from fastapi import APIRouter, Cookie, Depends
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
import redis
import json

router = APIRouter()


@router.put("/score", response_model=s_schema.ScoreRes)
async def update_score(
    req: UpdateScoreReq,
    sessionId: Optional[str] = Cookie(None),
    db: Session = Depends(get_db),
):
    rr = redis.Redis(
        host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_PORT")
    )
    print(sessionId)
    json_str = rr.get(sessionId).decode()
    user_dict = json.loads(json_str)
    score = readScoreByUserId(user_id=user_dict["user"]["id"], db=db)
    # score = readScoreByUserId(user_id=req.user_id, db=db)
    if req.score > score.score:
        score.score = req.score
        updateScore(score=score, db=db)
    return s_schema.ScoreRes(message="OK")
