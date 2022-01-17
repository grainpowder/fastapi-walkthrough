from fastwalk.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_add_integers():
    a, b = 5, 6
    response = client.get(f"/arithmetic/plus-int/{a}/{b}")
    response_content = response.text.strip('"')
    expected = f"{a} + {b} = {a + b}"
    assert response.status_code == 200
    assert response_content == expected, f"Expected {expected}, got {response_content}"


def test_subtract_integers():
    a, b = 15, 29
    response = client.get(f"/arithmetic/minus/int/?a={a}&b={b}")
    response_content = response.text.strip('"')
    expected = f"{a} - {b} = {a - b}"
    assert response.status_code == 200
    assert response_content == expected, f"Expected {expected}, got {response_content}"


def test_error_different_data_type():
    a, b = 5, 1.5
    response = client.get(f"/arithmetic/minus/int/?a={a}&b={b}")
    assert response.status_code == 400


def test_error_different_operation():
    a, b = 5, 6
    response = client.get(f"/arithmetic/minus/float/?a={a}&b={b}")
    assert response.status_code == 400
