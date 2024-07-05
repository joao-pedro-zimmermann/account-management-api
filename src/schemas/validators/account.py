from pydantic import BaseModel, Field

# ---------------------------------------------------------- #

class Account(BaseModel):
    account_number: str | None

class Balance(BaseModel):
    balance: str | None

class Deposit(BaseModel):
    amount: int | None

class Transfer(BaseModel):
    amount: int | None
    from_: str | None = Field(alias="from")
    to: str | None
