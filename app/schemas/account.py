from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from .shared import Address
from .asset import Property


class User(BaseModel):
    user_id: UUID = uuid4()
    username: str = Field(..., description="The username of the user")
    email: str = Field(..., description="The email address of the user")
    password: str = Field(..., description="The password of the user")
    first_name: str = Field(..., description="The first name of the user")
    last_name: str = Field(..., description="The last name of the user")
    phone_number: str = Field(..., description="The phone number of the user")
    address: Address
    is_active: bool = Field(default=True, description="The active status of the user")


class Account(BaseModel):
    account_id: UUID = uuid4()
    user: User
    is_active: bool = Field(
        default=True, description="The active status of the account"
    )
    properties: list[Property] = Field(
        default=None, description="List of properties owned by the user"
    )
