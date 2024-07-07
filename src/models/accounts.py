from dataclasses import dataclass

from models.base_model import BaseModel

# ---------------------------------------------------------- #

@dataclass
class AccountModel(BaseModel):
    
    account_number: str