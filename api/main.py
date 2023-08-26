from fastapi import FastAPI
from api.routers import score, ranking
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"messae": "hello world!"}


# app = FastAPI()
app.include_router(ranking.router)
app.include_router(score.router)
