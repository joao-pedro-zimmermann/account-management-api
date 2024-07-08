from pydantic import BaseModel

# ---------------------------------------------------------- #

class Account(BaseModel):
    account_number: str | None = None


class Balance(BaseModel):
    current_balance: int | None = None

