import pytest
import requests
from jsonschema import validate
from urls import jsonplaceholder_api_url


@pytest.mark.parametrize("index", range(200))
def test_todos_json_schema(index):
    """Checking todos json schema"""
    url_param = f"{jsonplaceholder_api_url}/todos"
    response = requests.get(url_param)
    schema = {
        "type": "object",
        "properties":
            {
                "userId": {"type": "number"},
                "id": {"type": "number"},
                "title": {"type": "string"},
                "completed": {"type": "boolean"},
            },
        "required": ["userId", "id", "title", "completed"]
    }
    validate(instance=response.json()[index], schema=schema)


@pytest.mark.parametrize("id", [1, 2, 249, 250, 251, 499, 500, pytest.param(501, marks=pytest.mark.xfail)])
def test_check_id(id):
    """Checking comments by id"""
    url_param = f"{jsonplaceholder_api_url}/comments/{id}"
    response = requests.get(url_param)
    assert response.json()["id"] == id


def test_delete_post():
    """Checking delete post"""
    url_param = f"{jsonplaceholder_api_url}/posts/1"
    response = requests.delete(url_param)
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_count_albums():
    """Checking count of albums"""
    url_param = f"{jsonplaceholder_api_url}/albums"
    expected_albums = 100
    response = requests.get(url_param).json()
    albums_list = []
    for element in response:
        albums_list.append(element['id'])
    assert len(albums_list) == expected_albums


def test_edit_post():
    """Checking editing a post"""
    url_param = f"{jsonplaceholder_api_url}/posts/1"
    params = {"userId": 1, "id": 1, "title": "new_title", "body": "new_body", }
    response = requests.patch(url_param, json=params)
    json_resp = response.json()
    assert json_resp["userId"] == params["userId"]
    assert json_resp["id"] == params["id"]
    assert json_resp["title"] == params["title"]
    assert json_resp["body"] == params["body"]
