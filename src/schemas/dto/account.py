from dataclasses import dataclass

from schemas.dto.base_dto import BaseDTO

# ---------------------------------------------------------- #

@dataclass
class AccountDTO(BaseDTO):

    account_number: str | None
    current_balance: int = 0