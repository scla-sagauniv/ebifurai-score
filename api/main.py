from fastapi import FastAPI
from api.routers import score, ranking

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"messae": "hello world!"}


# app = FastAPI()
app.include_router(ranking.router)
app.include_router(score.router)
