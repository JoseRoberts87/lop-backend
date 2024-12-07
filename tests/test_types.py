import pytest
from app.schemas.Asset import Asset, Property, Address
from uuid import uuid4

# Unit tests for the Asset model
def test_asset_model():
    this_uuid = uuid4()
    address = Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zipcode=12345,
        country="USA"
    )
    property_data = Property(
        id=this_uuid,
        name="Sample Property",
        address=address,
        value=250000.00
    )
    asset = Asset(
        name="Sample Asset",
        designation="Residential",
        expected_rent=1200.50,
        property=property_data
    )
    assert asset.name == "Sample Asset"
    assert asset.designation == "Residential"
    assert asset.expected_rent == 1200.50
    assert asset.property.id == this_uuid
    assert asset.property.name == "Sample Property"
    assert asset.property.address.street == "123 Main St"


def test_asset_model_invalid_zipcode():
    with pytest.raises(ValueError):
        Address(
            street="123 Main St",
            city="Anytown",
            state="CA",
            zipcode=600,  # Invalid zipcode, below the range
            country="USA"
        )
    with pytest.raises(ValueError):
        Address(
            street="123 Main St",
            city="Anytown",
            state="CA",
            zipcode=99930,  # Invalid zipcode, above the range
            country="USA"
        )


def test_asset_model_invalid_property_id():
    address = Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zipcode=12345,
        country="USA"
    )
    with pytest.raises(ValueError):
        Asset(
            name="Sample Asset",
            designation="Residential",
            expected_rent=1200.50,
            property=Property(
                id="",  # This should raise an error for empty id
                name="Sample Property",
                address=address,
                value=250000.00
            )
        )


def test_asset_model_missing_fields():
    address = Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zipcode=12345,
        country="USA"
    )
    with pytest.raises(ValueError):
        Asset(
            designation="Residential",
            expected_rent=1200.50,
            property=Property(
                id="property_id_1",
                name="Sample Property",
                address=address,
                value=250000.00
            )
        )  # Missing 'name' should raise an error


# Run the test
if __name__ == "__main__":
    pytest.main()
