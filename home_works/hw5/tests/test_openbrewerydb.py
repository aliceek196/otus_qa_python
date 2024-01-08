import pytest
import requests
from urls import openbrew_api_url


def test_list_count_of_params():
    """Counting the number of params"""
    url_param = f"{openbrew_api_url}/v1/breweries/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
    dict_number_params = requests.get(url_param).json()
    assert len(dict_number_params) == 16


def test_status_code_success():
    """Check the success status in a message"""
    url_param = f"{openbrew_api_url}"
    response = requests.get(url_param).status_code
    assert response == 200


@pytest.mark.parametrize("city", {'norman', "austin", "san_diego", "louisville", "marseille"})
def test_get_brewery_by_city(city):
    """Checking the status code filtering by city"""
    url_param = f"{openbrew_api_url}/breweries?by_city={city}"
    response = requests.get(url_param).status_code
    assert response == 200


@pytest.mark.parametrize("page", [1, 2, 101, 199, 200, 201])
def test_get_status_number_brewery_per_page(page):
    """Checking the status code filtering per page"""
    url_param = f"{openbrew_api_url}/v1/breweries?per_page={page}"
    response = requests.get(url_param).status_code
    assert response == 200


def test_check_micro_brewery():
    """Checking json schema microbrewery"""
    url_param = f"{openbrew_api_url}/v1/breweries/meta?by_type=micro"
    expected = {"total": "4266", "page": "1", "per_page": "50"}
    response = requests.get(url_param).json()
    assert response["total"] == expected["total"]
    assert response["page"] == expected["page"]
    assert response["per_page"] == expected["per_page"]
