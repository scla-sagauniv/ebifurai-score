from typing import List, Tuple

from sqlalchemy import desc, select
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result


from api.models.score import Score
from api.models.user import User
from api.schemas.ranking_res import RankingRes
from api.schemas.ranking_row import RankingRow
import api.schemas.score as s_schemas


async def get_ranking(db: Session) -> RankingRes:
    # result: Result = await(
    #     db.execute(
    #         select(
    #             s_model.Score.userid,
    #             s_model.Score.score,
    #         )
    #     )
    # )
    # res = result.all()
    scores = (
        db.query(User.id, User.name, Score.score)
        .join(User, User.id == Score.user_id)
        .order_by(desc(Score.score))
        .limit(10)
        .all()
    )

    res = []
    for idx, score in enumerate(scores):
        res.append(
            RankingRow(rank=idx, user_id=score.id, name=score.name, score=score.score)
        )
    return RankingRes(ranking=res)
