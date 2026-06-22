from fastapi.testclient import TestClient

# app import from the original file
from main import app

# create client test
client = TestClient(app)


def test_read_root():
    # 1. client make internal request(without uvicorn)
    response = client.get("/")

    # verify 200 status
    assert response.status_code == 200

    # verify json responds
    data = response.json()
    assert data["message"] == "Hey,universe! This is my first API REST"
    assert data["status"] == "running"


def test_get_profile():
    response = client.get("/profile")
    assert response.status_code == 200

    data = response.json()
    # verify name is correct
    assert data["name"] == "hitman"
    assert "FastAPI" in data["learning_stack"]
