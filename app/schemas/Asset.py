from typing import Dict
from pydantic import BaseModel, Field, conint
from uuid import UUID, uuid4
from .shared import Address
from datetime import datetime


class Property(BaseModel):
    property_id: UUID = uuid4()
    address: Address
    value: float
    details: dict = Field(
        default=None,
        description="Additional details about the property",
        examples=[
            {
                "bedrooms": 3,
                "bathrooms": 2,
                "sqft": 1500,
                "year_built": 2000,
                "hoa": 0,
                "taxes": 2000,
                "insurance": 1000,
            }
        ],
    )


class Campaign(BaseModel):
    campaign_id: UUID = uuid4()
    start_date: datetime = Field()
    end_date: datetime


class Asset(BaseModel):
    name: str = Field(default=None, description="unique name of asset")
    designation: str = Field(
        default=None,
        description="The property designation",
        examples=[
            "Single Family",
            "Multi Family",
            "Apartment",
            "Commercial",
            "Industrial",
            "Retail",
            "Office",
        ],
    )
    rent_expected: float = Field(
        default=None, description="Expected rental income of the asset"
    )
    rent_current: float = Field(
        default=None, description="Current rent of the property"
    )
    property: Property
    investor_count: int = Field(..., description="Number of investors in the asset")
    fractions_total: int = Field(..., description="Total number of fractions")
    fractions_available: int = Field(..., description="Number of available fractions")
    fraction_proce: float = Field(..., description="Price per fraction")
    campaign: Campaign
