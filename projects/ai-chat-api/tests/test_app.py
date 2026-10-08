# Simple test file to validate the basic FastAPI behavior.
# This helps practice writing tests for API endpoints.

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_chat_requires_api_key() -> None:
    response = client.post("/api/v1/chat/", json={"message": "hello"})
    assert response.status_code == 401


def test_chat_with_valid_api_key() -> None:
    response = client.post(
        "/api/v1/chat/",
        json={"message": "hello there"},
        headers={"x-api-key": "secret123"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert "answer" in payload
    assert payload["confidence"] == 0.92
