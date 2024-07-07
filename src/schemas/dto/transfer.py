from dataclasses import dataclass

from schemas.dto.base_dto import BaseDTO

# ---------------------------------------------------------- #

@dataclass
class TransferDTO(BaseDTO):
    amount: int | None
    from_: str | None
    to: str | None