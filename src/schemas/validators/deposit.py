from pydantic import BaseModel, field_validator

# ---------------------------------------------------------- #

class Deposit(BaseModel):
    amount: int

    @field_validator('amount')
    def validate_deposit_amount(cls, v):
        if v <= 0:
            raise ValueError('Deposit amount must be greater than zero.')
        return v
    
class DepositWithAccountResponse(BaseModel):
    account_number: str
    amount: int