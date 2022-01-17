from fastapi.testclient import TestClient

from fastwalk.main import app

client = TestClient(app)


def test_determinant():
    response = client.post(
        url="/algebra/determinant",
        json={
            "row_count": 4,
            "col_count": 4,
            "values": [
                [1, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 3, 0],
                [0, 0, 0, 4]
            ]
        }
    )
    expected = 24
    determinant = float(response.text)
    assert response.status_code == 200
    assert round(determinant) == expected, f"Expected {expected}, got {determinant}"


def test_determinant_error_invalid_row_count():
    response = client.post(
        url="/algebra/determinant",
        json={
            "row_count": 5,
            "col_count": 4,
            "values": [
                [1, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 3, 0],
                [0, 0, 0, 4]
            ]
        }
    )
    message = response.json()["detail"]
    assert response.status_code == 400
    assert message == "row_count(5) does not match length of values(4)"


def test_determinant_error_null_element():
    response = client.post(
        url="/algebra/determinant",
        json={
            "row_count": 4,
            "col_count": 4,
            "values": [
                [1, 0, 0, 0],
                [0, 2, 0, 0, 1],
                [0, 0, 3, 0],
                [0, 0, 0, 4]
            ]
        }
    )
    message = response.json()["detail"]
    assert response.status_code == 400
    assert message == "Number of elements in each of rows are not same"


def test_determinant_error_non_square_matrix():
    response = client.post(
        url="/algebra/determinant",
        json={
            "row_count": 5,
            "col_count": 4,
            "values": [
                [1, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 3, 0],
                [0, 0, 0, 4],
                [0, 0, 0, 5],
            ]
        }
    )
    message = response.json()["detail"]
    assert response.status_code == 400
    assert message == f"Can't calculate determinant of non-square matrix of shape (5, 4)"
