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

# Single test with custom marker and parameterization
@pytest.mark.parametrize("input_value", [1,2,3])
def test_single_value(input_value):
    print(f"Testing with input value: {input_value}")
    assert input_value > 0

# Multiple parameterized tests with different inputs
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (4, 5, 9),
    (10, 15, 25)
])
def test_multiple_values(a, b, expected):
    print(f"Testing with a: {a}, b: {b}, expected: {expected}")
    assert a + b == expected


def generate_test_data():
    return [
        ("admin", "admin123", True),
        ("user", "user123", True),
        ("guest", "wrong", True)
    ]

@pytest.mark.today
@pytest.mark.parametrize("username,password,expect_success", generate_test_data())
def test_login(username, password, expect_success):
    print(f"Testing login with username: {username}, password: {password}, expect_success: {expect_success}")
    # Simulate login logic
    result = True
    # result = login(username, password)
    assert result == expect_success