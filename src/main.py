import json
import uvicorn

from fastapi import FastAPI, APIRouter, Path
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.openapi.utils import get_openapi

from config import settings

from controllers import (
    account,
    transfer,
    deposit,
)

# ---------------------------------------------------------- #

main_router = APIRouter(
    prefix="/api/v1"
)

main_router.include_router(account.router)
main_router.include_router(transfer.router)
main_router.include_router(deposit.router)

app = FastAPI(openapi_url='/custom_openapi.json')

app.include_router(main_router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(content={"detail": str(exc)}, status_code=400)

def custom_openapi():
    with open('src/openapi.json', 'r') as file:
        custom_openapi_schema = json.load(file)

    if app.openapi_schema:
        return app.openapi_schema
    
    app.openapi_schema = custom_openapi_schema
    return app.openapi_schema

app.openai = custom_openapi()
 

if __name__ == "__main__":
    uvicorn.run("main:app", port=settings.PORT)