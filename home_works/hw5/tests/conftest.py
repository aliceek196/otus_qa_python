import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru"
    )

    parser.addoption(
        '--status_code',
        action='store',
        default='200',
    )


@pytest.fixture
def url_param(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")