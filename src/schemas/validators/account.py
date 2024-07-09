import re
from pydantic import BaseModel, field_validator

# ---------------------------------------------------------- #

class Account(BaseModel):
    account_number: str

    @field_validator('account_number')
    def validate_account_number(cls, v):
        if re.search(r'[a-zA-Z]', v):
            raise ValueError('Account number can\'t contain any letters')
        return v


class Balance(BaseModel):
    current_balance: int | None = None

