from fastapi import FastAPI, APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn

from config import settings

from controllers import account

# ---------------------------------------------------------- #

main_router = APIRouter(
    prefix="/api/v1"
)

main_router.include_router(account.router)

app = FastAPI()

app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=settings.PORT, reload=True)