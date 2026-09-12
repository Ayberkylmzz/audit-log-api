from fastapi.testclient import TestClient

from app.core.config import API_KEY
from app.main import app

client = TestClient(app)
headers = {"X-API-Key": API_KEY}


def test_create_log_without_api_key_fails():
    response = client.post(
        "/logs",
        json={"actor": "test", "action": "test", "resource": "test"},
    )
    assert response.status_code == 401


def test_create_and_get_log():
    response = client.post(
        "/logs",
        json={"actor": "tester", "action": "unit_test", "resource": "pytest"},
        headers=headers,
    )
    assert response.status_code == 201
    data = response.json()
    assert data["actor"] == "tester"
    assert "id" in data

    log_id = data["id"]
    response = client.get(f"/logs/{log_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == log_id


def test_get_nonexistent_log_returns_404():
    response = client.get("/logs/999999", headers=headers)
    assert response.status_code == 404
