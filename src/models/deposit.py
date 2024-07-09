from dataclasses import dataclass

from models.base_model import BaseModel

# ---------------------------------------------------------- #

@dataclass
class DepositModel(BaseModel):
    
    amount: int
    account_number: str