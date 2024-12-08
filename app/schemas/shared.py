from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str
    city: str
    state: str
    zipcode: int = Field(..., ge=601, le=99929)
    country: str = Field(default="USA")
