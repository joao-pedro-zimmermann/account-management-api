from pydantic import BaseModel, Field

# ---------------------------------------------------------- #

class Account(BaseModel):
    account_number: str | None

