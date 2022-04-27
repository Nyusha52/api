import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        action="store",
        default=200,
        help="This is status code"
    )


@pytest.fixture(scope="session")
def base_params(request):
    url = request.config.getoption("--url")
    code = request.config.getoption("--status_code")
    return url, code
