import requests


def test_create_add_get(base_params):

    response = requests.get(base_params[0])
    assert response.status_code == int(base_params[1])
