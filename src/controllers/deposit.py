import logging

from fastapi import APIRouter, status, HTTPException

from schemas.validators.deposit import DepositWithAccountResponse

from services import deposit as deposit_service

# ---------------------------------------------------------- #

router = APIRouter(
    prefix="/deposits",
    tags=["Deposit"],
)


@router.get(
    path='',
    status_code=status.HTTP_200_OK,
    response_model=list[None] | list[DepositWithAccountResponse]
)
async def get_all_deposits():
    try:
        deposits = deposit_service.get_all_deposits()
        return [DepositWithAccountResponse(**deposit.to_dict(by_alias=True)) for deposit in deposits]
    except Exception as e:
        logging.error(str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='An error occurred while retrieving deposits information. Please try again later.'
        )