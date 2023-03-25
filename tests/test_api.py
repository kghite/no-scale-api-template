import os

import pytest
from typing import Dict

from api.app import app
from api.exceptions import CustomError


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    assert client.get("/").status_code == 200


def test_health(client):
    assert client.get("/v1/health").status_code == 200


def test_validation(client):
    test_payload: Dict[str, str] = dict(data="test")

    response = client.post(
        "/v1/test-endpoint",
        json=test_payload,
        headers={"Content-Type": "application/json", "X-Api-Key": os.getenv("USER_API_KEY")},
    )

    assert response.status_code == 200

    bad_payload = None

    response = client.post(
        "v1/test-endpoint",
        json=bad_payload,
        headers={"Content-Type": "application/json", "X-Api-Key": os.getenv("USER_API_KEY")},
    )

    assert response.status_code == 400


def test_custom_exception():
    with pytest.raises(CustomError) as exc_info:

        def test_raise():
            raise CustomError("Test CustomError")

        test_raise()

    exception_raised = exc_info.value
    assert exception_raised.status_code == 500
    assert exception_raised.message == "Test CustomError"
