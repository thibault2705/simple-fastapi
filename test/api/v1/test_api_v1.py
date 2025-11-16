from fastapi.testclient import TestClient
from src.main import app
from http import HTTPStatus

client = TestClient(app)

def test_greet():
    response = client.get("/api/v1/greeting/Thibault")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == "Hello, Thibault! This is a greeting from API v1."

