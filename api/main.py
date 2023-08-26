from fastapi import FastAPI, APIRouter
from api.routers import score, ranking
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


app = FastAPI()

router = APIRouter(prefix="/python", tags=["article"])
# app = FastAPI()
router.include_router(ranking.router)
router.include_router(score.router)

app.include_router(router)


@app.get("/hello")
async def hello():
    return {"messae": "hello world!"}
