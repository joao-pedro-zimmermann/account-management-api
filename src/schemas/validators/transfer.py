from pydantic import BaseModel, Field

# ---------------------------------------------------------- #

class Transfer(BaseModel):
    amount: int | None = None
    from_: str | None = Field(alias="from", default=None)
    to: str | None = None