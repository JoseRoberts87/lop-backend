from pydantic import BaseModel, Field, conint
from uuid import UUID, uuid4


class Address(BaseModel):
    street: str
    city: str
    state: str
    zipcode: int = Field(..., ge=601, le=99929)
    country: str = Field(default="USA")

class Property(BaseModel):
    id: UUID = uuid4()
    name: str = Field(default=None, description="Common name of property")
    address: Address
    value: float


class Asset(BaseModel):
    name: str = Field(default=None, description="unique name of asset")
    designation: str = Field(
        default=None,
        description="The property designation",
        examples=["Single Family", "Apartment", "Small Office", "Large Office"],
    )
    expected_rent: float
    property: Property
