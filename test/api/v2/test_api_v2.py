"""
 Module Name: test_api_v2.py
 Author: thibault2705
 Date: 2025-11-16
 Description: Test API v2
 """

from fastapi.testclient import TestClient
from src.main import app
from http import HTTPStatus

client = TestClient(app)

def test_gen_random_int(log_capture_fixture):
    max_value = 100
    response = client.get(f"/api/v2/random/{max_value}")
    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert "max_value" in data
    assert "random_number" in data

    assert data['max_value'] == max_value
    assert 1 <= data['random_number'] <= max_value

    logs = log_capture_fixture.getvalue()
    expected_log = get_expected_log(data['random_number'], 1, max_value)
    assert expected_log in logs

def test_gen_random_in_range(log_capture_fixture):
    min_value = 1
    max_value = 100
    response = client.get(f"/api/v2/random-in-range?min_value={min_value}&max_value={max_value}")
    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert "min_value" in data
    assert "max_value" in data
    assert "random_number" in data

    assert data['min_value'] == min_value
    assert data['max_value'] == max_value
    assert min_value <= data['random_number'] <= max_value

    logs = log_capture_fixture.getvalue()
    expected_log = get_expected_log(data['random_number'], min_value, max_value)
    assert expected_log in logs

def test_gen_random_in_range_without_min_max(log_capture_fixture):
    response = client.get(f"/api/v2/random-in-range")
    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert "min_value" in data
    assert "max_value" in data
    assert "random_number" in data

    default_min_value = 0
    default_max_value = 100
    assert data['min_value'] == default_min_value
    assert data['max_value'] == default_max_value
    assert default_min_value <= data['random_number'] <= default_max_value

    logs = log_capture_fixture.getvalue()
    expected_log = get_expected_log(data['random_number'], default_min_value, default_max_value)
    assert expected_log in logs

def test_gen_random_in_range_with_only_min_value(log_capture_fixture):
    min_value = 5
    response = client.get(f"/api/v2/random-in-range?min_value={min_value}")
    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert "min_value" in data
    assert "max_value" in data
    assert "random_number" in data

    default_max_value = 100
    assert data['min_value'] == min_value
    assert data['max_value'] == default_max_value
    assert min_value <= data['random_number'] <= default_max_value

    logs = log_capture_fixture.getvalue()
    expected_log = get_expected_log(data['random_number'], min_value, default_max_value)
    assert expected_log in logs

def test_gen_random_in_range_with_only_max_value(log_capture_fixture):
    max_value = 50
    response = client.get(f"/api/v2/random-in-range?max_value={max_value}")
    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert "min_value" in data
    assert "max_value" in data
    assert "random_number" in data

    default_min_value = 0
    assert data['min_value'] == default_min_value
    assert data['max_value'] == max_value
    assert default_min_value <= data['random_number'] <= max_value

    logs = log_capture_fixture.getvalue()
    expected_log = get_expected_log(data['random_number'], default_min_value, max_value)
    assert expected_log in logs

def test_gen_random_in_range_with_invalid_range(log_capture_fixture):
    min_value = 70
    max_value = 30
    response = client.get(f"/api/v2/random-in-range?min_value={min_value}&max_value={max_value}")
    assert response.status_code == HTTPStatus.BAD_REQUEST

    data = response.json()
    assert "detail" in data
    assert data["detail"] == "min_value can't be greater than max_value"

    logs = log_capture_fixture.getvalue()
    expected_log = f"min_value {min_value} is greater max_value {max_value}"
    assert expected_log in logs

def test_gen_random_in_range_with_invalid_min_type(log_capture_fixture):
    invalid_param = "abcd"
    response = client.get(f"/api/v2/random-in-range?min_value={invalid_param}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_CONTENT

    data = response.json()
    assert data == {
      "detail": [
        {
          "type": "int_parsing",
          "loc": [
            "query",
            "min_value"
          ],
          "msg": "Input should be a valid integer, unable to parse string as an integer",
          "input": "abcd"
        }
      ]
    }

def test_gen_random_in_range_with_invalid_max_type(log_capture_fixture):
    invalid_param = "xyz"
    response = client.get(f"/api/v2/random-in-range?max_value={invalid_param}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_CONTENT

    data = response.json()
    assert data == {
      "detail": [
        {
          "type": "int_parsing",
          "loc": [
            "query",
            "max_value"
          ],
          "msg": "Input should be a valid integer, unable to parse string as an integer",
          "input": "xyz"
        }
      ]
    }

def get_expected_log(value, min_value, max_value):
    return f"Random value {value} generated, min_value = {min_value}, max_value = {max_value}"