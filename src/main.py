from fastapi import FastAPI, APIRouter
import uvicorn

from config import settings

# ---------------------------------------------------------- #

main_router = APIRouter(
    prefix="/api/v1"
)

app = FastAPI()

app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=settings.PORT)