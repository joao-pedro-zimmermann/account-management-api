from fastapi import APIRouter, status, HTTPException
from pydantic import ValidationError

from schemas.validators.account import (
    Account
)

# ---------------------------------------------------------- #

router = APIRouter(
    prefix="/accounts",
    tags=["Account"],
)

##@router.post(
#    path='',
#    status_code=status.HTTP_201_CREATED,
#    response_model=Account,
#)
#def create_an_account(
#    body: Account
#):
#    return body
    