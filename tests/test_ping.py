from fastwalk.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_ping():
    response = client.get("/health/ping")
    response_content = response.text.strip('"')
    expected = "pong"
    assert response.status_code == 200
    assert response_content == expected, f"Expected {expected}, got {response_content}"
