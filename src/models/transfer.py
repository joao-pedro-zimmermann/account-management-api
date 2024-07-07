from dataclasses import dataclass

from models.base_model import BaseModel

# ---------------------------------------------------------- #

@dataclass
class TransferModel(BaseModel):
    
    amount: int
    from_: str
    to: str