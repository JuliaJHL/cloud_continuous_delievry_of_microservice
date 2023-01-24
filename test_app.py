from app import *


def test_login_success():
    client = app.test_client()
    url = '/login'

    mock_request_data = {
        "user_name": "IDS721",
        "user_pwd": "DUKE2023"
    }

    response = client.post(url, data=mock_request_data)
    assert response.get_data() == b'Login successful!'


def test_login_name():
    client = app.test_client()
    url = '/login'

    mock_request_data = {
        "user_name": "hello_world",
        "user_pwd": "DUKE2023"
    }

    response = client.post(url, data=mock_request_data)
    assert response.get_data() == b'Login failed!'


def test_login_pwd():
    client = app.test_client()
    url = '/login'

    mock_request_data = {
        "user_name": "IDS721",
        "user_pwd": "BlueDevil"
    }

    response = client.post(url, data=mock_request_data)
    assert response.get_data() == b'Login failed!'


