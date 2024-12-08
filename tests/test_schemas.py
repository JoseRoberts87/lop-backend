import pytest
from datetime import datetime
from uuid import uuid4
from app.schemas.shared import Address
from app.schemas.account import User, Account
from app.schemas.investment import Investment
from app.schemas.asset import Property, Campaign, Asset

user_uuid = uuid4()
account_uuid = uuid4()
property_uuid = uuid4()
campaign_uuid = uuid4()


def test_address_model():
    address = Address(
        street="123 Main St", city="Anytown", state="CA", zipcode=90210, country="USA"
    )
    assert address.street == "123 Main St"
    assert address.city == "Anytown"
    assert address.state == "CA"
    assert address.zipcode == 90210
    assert address.country == "USA"


def test_address_invalid_zipcode():
    with pytest.raises(ValueError):
        Address(
            street="123 Main St",
            city="Anytown",
            state="CA",
            zipcode=600,  # Invalid zipcode, below the range
            country="USA",
        )
    with pytest.raises(ValueError):
        Address(
            street="123 Main St",
            city="Anytown",
            state="CA",
            zipcode=99930,  # Invalid zipcode, above the range
            country="USA",
        )


def test_user_model():
    address = Address(
        street="123 Main St", city="Anytown", state="CA", zipcode=90210, country="USA"
    )
    user = User(
        user_id=user_uuid,
        username="testuser",
        email="test@example.com",
        password="securepassword",
        first_name="Test",
        last_name="User",
        phone_number="123-456-7890",
        address=address,
    )
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.first_name == "Test"
    assert user.last_name == "User"
    assert user.phone_number == "123-456-7890"
    assert user.address == address


def test_account_model():
    address = Address(
        street="123 Main St", city="Anytown", state="CA", zipcode=90210, country="USA"
    )
    user = User(
        user_id=user_uuid,
        username="testuser",
        email="test@example.com",
        password="securepassword",
        first_name="Test",
        last_name="User",
        phone_number="123-456-7890",
        address=address,
    )
    account = Account(account_id=account_uuid, user=user)
    assert account.user == user
    assert account.is_active is True


def test_investment_model():
    address = Address(
        street="123 Main St", city="Anytown", state="CA", zipcode=90210, country="USA"
    )
    user = User(
        user_id=user_uuid,
        username="testuser",
        email="test@example.com",
        password="securepassword",
        first_name="Test",
        last_name="User",
        phone_number="123-456-7890",
        address=address,
    )
    account = Account(account_id=account_uuid, user=user)
    property_data = Property(
        property_id=property_uuid, address=address, value=250000.00
    )
    investment = Investment(account=account, properties=[property_data])
    assert investment.account == account
    assert investment.properties[0] == property_data


def test_property_model():
    address = Address(
        street="123 Main St", city="Anytown", state="CA", zipcode=90210, country="USA"
    )
    property_data = Property(
        property_id=property_uuid,
        address=address,
        value=250000.00,
        details={"bedrooms": 3, "bathrooms": 2},
    )
    assert property_data.value == 250000.00
    assert property_data.details["bedrooms"] == 3


def test_campaign_model():
    campaign = Campaign(
        campaign_id=campaign_uuid,
        start_date="2023-01-01T00:00:00",
        end_date="2023-12-31T00:00:00",
    )
    assert campaign.start_date == datetime.fromisoformat("2023-01-01T00:00:00")
    assert campaign.end_date == datetime.fromisoformat("2023-12-31T00:00:00")


def test_asset_model():
    address = Address(
        street="123 Main St", city="Anytown", state="CA", zipcode=90210, country="USA"
    )
    property_data = Property(
        property_id=property_uuid, address=address, value=250000.00
    )
    asset = Asset(
        name="Sample Asset",
        designation="Residential",
        rent_expected=1200.50,
        property=property_data,
        investor_count=10,
        fractions_total=100,
        fractions_available=50,
        fraction_proce=10.00,
        campaign=Campaign(
            campaign_id=campaign_uuid,
            start_date="2023-01-01T00:00:00",
            end_date="2023-12-31T00:00:00",
        ),
    )
    assert asset.name == "Sample Asset"
    assert asset.designation == "Residential"
    assert asset.rent_expected == 1200.50
    assert asset.property == property_data


# Run the test
if __name__ == "__main__":
    pytest.main()
