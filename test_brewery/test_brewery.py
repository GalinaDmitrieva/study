import pytest
from jsonschema import validate
import requests


@pytest.mark.parametrize("per_page", [1, 3, 49])
def test_numbers_brewery_per_page(base_url, per_page):
    schema = {
        "type": "array",
        "items": {
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": ["string", "null"]},
                "address_2": {"type": ["string", "null"]},
                "address_3": {"type": ["string", "null"]},
                "city": {"type": "string"},
                "state": {"type": ["string", "null"]},
                "county_province": {"type": ["string", "null"]},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": ["string", "null"]},
                "latitude": {"type": ["string", "null"]},
                "phone": {"type": ["string", "null"]},
                "website_url": {"type": ["string", "null"]},
                "updated_at": {"type": "string"},
                "created_at": {"type": "string"}
            }
        }
    }
    response = requests.get(f"{base_url}/breweries?per_page={per_page}")
    validate(instance=response.json(), schema=schema)
    assert len(response.json()) == per_page


@pytest.mark.parametrize("by_type", ['micro', 'nano', 'brewpub'])
def test_numbers_brewery_per_page(base_url, by_type):
    schema = {
        "type": "array",
        "items": {
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": ["string", "null"]},
                "address_2": {"type": ["string", "null"]},
                "address_3": {"type": ["string", "null"]},
                "city": {"type": "string"},
                "state": {"type": ["string", "null"]},
                "county_province": {"type": ["string", "null"]},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": ["string", "null"]},
                "latitude": {"type": ["string", "null"]},
                "phone": {"type": ["string", "null"]},
                "website_url": {"type": ["string", "null"]},
                "updated_at": {"type": "string"},
                "created_at": {"type": "string"}
            }
        }
    }
    response = requests.get(f"{base_url}/breweries?by_type={by_type}")
    validate(instance=response.json(), schema=schema)
    for brew in response.json():
        assert brew['brewery_type'] == by_type


def test_default_numbers_brewery_per_page(base_url):
    schema = {
        "type": "array",
        "items": {
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": ["string", "null"]},
                "address_2": {"type": ["string", "null"]},
                "address_3": {"type": ["string", "null"]},
                "city": {"type": "string"},
                "state": {"type": ["string", "null"]},
                "county_province": {"type": ["string", "null"]},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": ["string", "null"]},
                "latitude": {"type": ["string", "null"]},
                "phone": {"type": ["string", "null"]},
                "website_url": {"type": ["string", "null"]},
                "updated_at": {"type": "string"},
                "created_at": {"type": "string"}
            }
        }
    }
    response = requests.get(f"{base_url}/breweries")
    validate(instance=response.json(), schema=schema)
    assert len(response.json()) == 20


@pytest.mark.parametrize('per_page', [50, 51, 150])
def test_max_numbers_brewery_per_page(base_url, per_page):
    schema = {
        "type": "array",
        "items": {
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": ["string", "null"]},
                "address_2": {"type": ["string", "null"]},
                "address_3": {"type": ["string", "null"]},
                "city": {"type": "string"},
                "state": {"type": ["string", "null"]},
                "county_province": {"type": ["string", "null"]},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": ["string", "null"]},
                "latitude": {"type": ["string", "null"]},
                "phone": {"type": ["string", "null"]},
                "website_url": {"type": ["string", "null"]},
                "updated_at": {"type": "string"},
                "created_at": {"type": "string"}
            }
        }
    }
    response = requests.get(f"{base_url}/breweries?per_page={per_page}")
    validate(instance=response.json(), schema=schema)
    assert len(response.json()) == 50


def test_brewery_random(base_url):
    schema = {
        "type": "array",
        "items": {
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": ["string", "null"]},
                "address_2": {"type": ["string", "null"]},
                "address_3": {"type": ["string", "null"]},
                "city": {"type": "string"},
                "state": {"type": ["string", "null"]},
                "county_province": {"type": ["string", "null"]},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": ["string", "null"]},
                "latitude": {"type": ["string", "null"]},
                "phone": {"type": ["string", "null"]},
                "website_url": {"type": ["string", "null"]},
                "updated_at": {"type": "string"},
                "created_at": {"type": "string"}
            }
        }
    }
    response = requests.get(f"{base_url}/breweries/random")
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200