from pydantic import BaseModel, Field
from .account import Account
from .asset import Property


class Investment(BaseModel):
    account: Account
    properties: list[Property] = Field(
        default=None, description="List of properties owned by the user"
    )
