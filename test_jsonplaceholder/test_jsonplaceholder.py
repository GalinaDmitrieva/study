import pytest
from jsonschema import validate
import requests

NUMBER_OF_COMMENTS = 500

def test_delete_posts(base_url):
    response = requests.delete(f"{base_url}/posts/1")
    assert response.status_code == 200


def test_get_posts1(base_url):
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": 'number'},
            "id": {"type": 'number'},
            "title": {"type": "string"},
            "body": {"type": "string"}
        }
    }
    response = requests.get(f"{base_url}/posts/1")
    validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_filter_albums_by_user(base_url, user_id):
    schema = {
        "type": "array",
        "items":{
            "properties": {
                "userId": {"type": 'number'},
                "id": {"type": 'number'},
                "title": {"type": "string"},
            }
        }
    }
    response = requests.get(f"{base_url}/users/{user_id}/albums")
    validate(instance=response.json(), schema=schema)
    resp_json = response.json()
    for resp in resp_json:
        assert resp['userId'] == user_id
    assert response.status_code == 200


def test_number_of_comments(base_url):
    response = requests.get(f"{base_url}/comments")
    assert len(response.json()) == NUMBER_OF_COMMENTS
    assert response.status_code == 200


@pytest.mark.parametrize("post_id", [1, 11, 100])
def test_filter_comments_by_post_id(base_url, post_id):
    schema = {
        "type": "array",
        "items": {
            "properties": {
                "postId": {"type": 'number'},
                "id": {"type": 'number'},
                "name": {"type": "string"},
                "email": {"type": "string"},
                "body": {"type": "string"},
            }
        }
    }
    response = requests.get(f"{base_url}/comments?postId={post_id}")
    validate(instance=response.json(), schema=schema)
    resp_json = response.json()
    for resp in resp_json:
        assert resp['postId'] == post_id
    assert response.status_code == 200