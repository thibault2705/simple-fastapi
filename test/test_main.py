"""
 Module Name: router.py
 Author: thibault2705
 Date: 2025-11-16
 Description: Main Test
 """

from fastapi.testclient import TestClient
from src.main import app
from http import HTTPStatus

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == "Hi, there. This is the homepage."

