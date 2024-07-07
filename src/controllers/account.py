from fastapi import APIRouter, status, HTTPException

from schemas.validators.account import Account as AccountSchema
from schemas.validators.transfer import Transfer as TransferSchema

from schemas.dto.account import AccountDTO
from schemas.dto.transfer import TransferDTO

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