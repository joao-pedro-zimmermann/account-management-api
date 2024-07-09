from pydantic import BaseModel, Field, field_validator, model_validator

# ---------------------------------------------------------- #

class Transfer(BaseModel):
    amount: int
    from_: str = Field(alias="from")
    to: str

    @field_validator('amount')
    def validate_amount(cls, v):
        if v <= 0:
            raise ValueError('Transfer amount must be greater than zero.')
        return v