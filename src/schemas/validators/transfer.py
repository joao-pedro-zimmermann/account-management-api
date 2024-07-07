from pydantic import BaseModel, Field

# ---------------------------------------------------------- #

class Transfer(BaseModel):
    amount: int | None
    from_: str | None = Field(alias="from")
    to: str | None