from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hi, there"

def test_greet():
    response = client.get("/greeting/Thibault")
    assert response.status_code == 200
    assert response.json() == "Hello, Thibault!"


def test_gen_random_int():
    max_value = 100
    response = client.get(f"/random/{max_value}")
    assert response.status_code == 200

    data = response.json()
    assert "max_value" in data
    assert "random_number" in data

    assert data['max_value'] == max_value
    assert 1 <= data['random_number'] <= max_value

def test_gen_random_in_range():
    min_value = 1
    max_value = 100
    response = client.get(f"/random-in-range?min_value={min_value}&max_value={max_value}")
    assert response.status_code == 200

    data = response.json()
    assert "min_value" in data
    assert "max_value" in data
    assert "random_number" in data

    assert data['min_value'] == min_value
    assert data['max_value'] == max_value
    assert min_value <= data['random_number'] <= max_value

def test_gen_random_in_range_without_min_max():
    response = client.get(f"/random-in-range")
    assert response.status_code == 200

    data = response.json()
    assert "min_value" in data
    assert "max_value" in data
    assert "random_number" in data

    default_min_value = 0
    default_max_value = 100
    assert data['min_value'] == default_min_value
    assert data['max_value'] == default_max_value
    assert default_min_value <= data['random_number'] <= default_max_value

def test_gen_random_in_range_with_only_min_value():
    min_value = 5
    response = client.get(f"/random-in-range?min_value={min_value}")
    assert response.status_code == 200

    data = response.json()
    assert "min_value" in data
    assert "max_value" in data
    assert "random_number" in data

    default_max_value = 100
    assert data['min_value'] == min_value
    assert data['max_value'] == default_max_value
    assert min_value <= data['random_number'] <= default_max_value

def test_gen_random_in_range_with_only_max_value():
    max_value = 50
    response = client.get(f"/random-in-range?max_value={max_value}")
    assert response.status_code == 200

    data = response.json()
    assert "min_value" in data
    assert "max_value" in data
    assert "random_number" in data

    default_min_value = 0
    assert data['min_value'] == default_min_value
    assert data['max_value'] == max_value
    assert default_min_value <= data['random_number'] <= max_value

def test_gen_random_in_range_with_invalid_range():
    min_value = 70
    max_value = 30
    response = client.get(f"/random-in-range?min_value={min_value}&max_value={max_value}")
    assert response.status_code == 400

    data = response.json()
    assert "detail" in data
    assert data["detail"] == "min_value can't be greater than max_value"