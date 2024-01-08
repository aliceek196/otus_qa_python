import requests


def test_url_and_status_code(url_param, status_code):
    """Checking status_code"""
    response_code = requests.get(url_param).status_code
    assert response_code == 200
