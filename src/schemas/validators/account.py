from pydantic import BaseModel, Field

# ---------------------------------------------------------- #

class Account(BaseModel):
    account_number: str | None


class Balance(BaseModel):
    current_balance: int | None

