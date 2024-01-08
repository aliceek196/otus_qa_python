import pytest
import requests
from urls import dog_api_url


def test_list_count_of_sub_breeds_hound():
    """Counting the sub-breeds hound"""
    url_param = f"{dog_api_url}/breed/hound/list"
    response = requests.get(url_param)
    dict_hound_sub_breeds = response.json()["message"]
    assert len(dict_hound_sub_breeds) == 7


@pytest.mark.parametrize(
    "actual_breed, expected_breed",
    [("buhund", ["norwegian"]),
     ("bulldog", ["boston", "english", "french"]),
     ("bullterrier", ["staffordshire"]),
     ("cattledog", ["australian"]),
     ("chihuahua", [])]
)
def test_get_breed(actual_breed, expected_breed):
    """Checking the breeds list"""
    url_param = f"{dog_api_url}/breeds/list/all"
    response = requests.get(url_param)
    dict_breed = response.json()["message"]
    assert dict_breed.get(actual_breed) == expected_breed


def test_get_spaniel_sub_breed():
    """Checking the schema spaniel sub-breeds"""
    url_param = f"{dog_api_url}/breed/spaniel/list"
    response = requests.get(url_param)
    spaniel_sub_breeds = response.json()["message"]
    assert spaniel_sub_breeds == ["blenheim", "brittany", "cocker", "irish", "japanese", "sussex", "welsh"]


@pytest.mark.parametrize("count", [1, 12, 23, 34, 45, 50, pytest.param(51, marks=pytest.mark.xfail)])
def test_random_image_number(count):
    """Checking random image count"""
    url_param = f"{dog_api_url}/breeds/image/random/{count}"
    result = requests.get(url_param)
    assert len(result.json().get("message")) == count


def test_status_success_by_breed():
    """Check the success status in a message"""
    url_param = f"{dog_api_url}/breed/hound/images"
    response = requests.get(url_param)
    status = response.json()["status"]
    assert status == "success"
