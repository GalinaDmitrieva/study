import pytest
from jsonschema import validate
import requests


"""тест на корректный ответ конкретного запроса"""


def test_breed_list(base_url):
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    response = requests.get(f"{base_url}/breed/hound/images")
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


"""тест на корректный ответ для существующей породы"""


@pytest.mark.parametrize('breed', ['hound', 'bullterrier', 'groenendael'])
def test_breeds(base_url, breed):
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    response = requests.get(f"{base_url}/breed/{breed}/images")
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


"""тест на ответ для несуществующей породы. для hound буква о - кириллическая"""


@pytest.mark.parametrize('breed', ['qwerty', 'hоund', 'groenedfvdgfndael'])
def test_breeds(base_url, breed):
    response = requests.get(f"{base_url}/breed/{breed}/images")
    assert response.status_code == 404


"""тест на корректный ответ конкретного запроса"""

def test_random_image(base_url):
    schema = {
        'type': 'object',
        'properties': {
            'message': {
                'type': 'string'
            },
            'status': {
                'type': 'string'
            },
        },
        "required": ['message', 'status']
    }
    response = requests.get(f"{base_url}/breeds/image/random")
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


"""тест на лимит"""


@pytest.mark.parametrize('number', [50, 51, 100])
def test_random_limit_by_all_breeds(base_url, number):
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    response = requests.get(f"{base_url}/breeds/image/random/{number}")
    validate(instance=response.json(), schema=schema)
    assert len(response.json()["message"]) == 50


"""тест на то, что кол-во фото в ответе соответствует заданному числу"""


@pytest.mark.parametrize('number', [1, 50, 150])
def test_number_photo_for_one_breed(base_url, number):
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    response = requests.get(f"{base_url}/breed/hound/images/random/{number}")
    validate(instance=response.json(), schema=schema)
    assert len(response.json()["message"]) == number
