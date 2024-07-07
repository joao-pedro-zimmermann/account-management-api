from fastapi import APIRouter, status, HTTPException
from pydantic import ValidationError

from schemas.validators.account import (
    Account as AccountSchema
)

from schemas.dto.account import (
    AccountDTO
)

from services import account as account_service

# ---------------------------------------------------------- #

router = APIRouter(
    prefix="/accounts",
    tags=["Account"],
)

@router.post(
    path='',
    status_code=status.HTTP_201_CREATED,
    response_model=AccountSchema
)
async def create_an_account(
    body: AccountSchema
):
    try:
        account_to_create = AccountDTO(**body.dict())
        return account_service.create_an_account(account_to_create)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )