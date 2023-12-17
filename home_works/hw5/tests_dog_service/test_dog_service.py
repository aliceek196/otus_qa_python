import pytest
import requests
from jsonschema import validate


def test_get_all_breeds(base_url):
    """Checks the response code 200 and schema in JSON format"""
    response = requests.get(f"{base_url}/list/all")

    def assert_status_code_and_json(status_code_and_json)

    assert response.headers["Content-Type"] == "application/json", "Response is not in JSON format"
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"},
        },
        "required": ["message", "status"]
    }
    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize("number", [1, 12, 23, 34, 49, 50])
def test_get_number_of_images(number, base_url):
    """Check if the number of requested images matches"""
    response = requests.get(f"{base_url}/image/random/{number}")
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert len(response.json().get("message")) == number
