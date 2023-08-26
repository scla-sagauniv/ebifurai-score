from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from api.models.user import User
from api.models.score import Score

from typing import List, Tuple, Optional


def updateScore(score: Score, db: Session):
    user_name = db.query(Score).where(Score.user_id == score.user_id).first()
    user_name.score = score.score
    db.commit()


def readScoreByUserId(db: Session, user_id: str) -> Score:
    score = db.query(Score).where(Score.user_id == user_id).first()
    return score
