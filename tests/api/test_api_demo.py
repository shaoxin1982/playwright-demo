import pytest
import requests
import json

BASE_URL = "https://httpbin.org"

@pytest.mark.api
def test_anything_post():
    url = f"{BASE_URL}/anything"
    payload = {
        "username": "testuser",
        "password": "testpass"
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["json"]["username"] == "testuser"
    assert response_data["json"]["password"] == "testpass"

@pytest.mark.api
def test_anything_get():
    url = f"{BASE_URL}/get"
    params = {
        "name": "john",
        "age": 30
    }

    response = requests.get(url, params=params)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["args"]["name"] == "john"
    assert response_data["args"]["age"] == "30"