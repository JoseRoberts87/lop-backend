from typing import Dict, Optional
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from .shared import Address
from datetime import datetime


class Pictures(BaseModel):
    picture_id: UUID = uuid4()
    picture_path: str = Field(..., description="The path to the picture")


class MediaCollection(BaseModel):
    collection_id: UUID = uuid4()
    pictures: Optional[list[Pictures]] = Field(
        default=None, description="List of pictures of the property"
    )
    videos: Optional[list[str]] = Field(
        default=None, description="List of videos of the property"
    )


class Property(BaseModel):
    property_id: UUID = uuid4()
    address: Address
    value: float
    media_collection: Optional[MediaCollection] = Field(
        default=None, description="Media collection of the property"
    )
    details: Optional[dict] = Field(
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
