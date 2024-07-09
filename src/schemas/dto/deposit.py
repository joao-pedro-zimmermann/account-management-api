from dataclasses import dataclass

from schemas.dto.base_dto import BaseDTO

# ---------------------------------------------------------- #

@dataclass
class DepositDTO(BaseDTO):

    amount: int | None
    account_number: str | None