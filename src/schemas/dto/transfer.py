from dataclasses import dataclass

from schemas.dto.base_dto import BaseDTO

# ---------------------------------------------------------- #

@dataclass
class TransferDTO(BaseDTO):

    __aliases__ = {
        'from_': 'from'
    }
    
    amount: int | None
    from_: str | None
    to: str | None