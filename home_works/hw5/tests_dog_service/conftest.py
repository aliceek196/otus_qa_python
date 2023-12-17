from urllib import response
import pytest


@pytest.fixture
def base_url():
    return 'https://dog.ceo/api/breeds'


@pytest.fixture()
def status_code_and_json():
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.headers["Content-Type"] == "application/json", "Response is not in JSON format"
