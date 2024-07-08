from fastapi import APIRouter, status, HTTPException

from schemas.validators.account import (
    Account as AccountSchema,
    Balance as BalanceSchema,
)
from schemas.validators.transfer import Transfer as TransferSchema
from schemas.validators.deposit import Deposit as DepositSchema

from schemas.dto.account import AccountDTO
from schemas.dto.transfer import TransferDTO
from schemas.dto.deposit import DepositDTO

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
    

@router.post(
    path='/transfer',
    status_code=status.HTTP_200_OK,
    response_model=None
)
async def make_a_peer_to_peer_transfer(
    body: TransferSchema
):
    try:
        transfer_to_make = TransferDTO(**body.dict())
        account_service.make_a_peer_to_peer_transfer(transfer_to_make)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )
    

@router.post(
    path='/{account_number}/deposit',
    status_code=status.HTTP_200_OK,
    response_model=None
)
async def deposit_into_an_account(
    account_number: str,
    body: DepositSchema
):
    try:
        deposit = DepositDTO(**body.dict())
        return account_service.deposit_into_an_account(account_number, deposit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    

@router.get(
    path='/{account_number}/balance',
    status_code=status.HTTP_200_OK,
    response_model=BalanceSchema
)
async def get_account_balance(
    account_number: str
):
    try:
        return account_service.get_valid_account(account_number)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )