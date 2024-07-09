import logging

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


from services import transfer as transfer_service

# ---------------------------------------------------------- #

router = APIRouter(
    prefix="/transfers",
    tags=["Transfer"],
)


@router.get(
    path='',
    status_code=status.HTTP_200_OK,
    response_model=list[None] | list[TransferSchema]
)
async def get_all_transfers():
    try:
        transfers = transfer_service.get_all_transfers()
        return [TransferSchema(**transfer.to_dict(by_alias=True)) for transfer in transfers]
    except Exception as e:
        logging.error(str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An error occurred while retrieving transfers information. Please try again later.'
        )