"""
 Module Name: test_api_v1.py
 Author: thibault2705
 Date: 2025-11-16
 Description: Test API v1
 """

from fastapi.testclient import TestClient
from src.main import app
from http import HTTPStatus

client = TestClient(app)

def test_greet():
    response = client.get("/api/v1/greeting/Thibault")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == "Hello, Thibault! This is a greeting from API v1."

