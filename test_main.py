import pytest

from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello_world_status(client):
    response = client.get("/")
    assert response.status_code == 200


def test_hello_world_content(client):
    response = client.get("/")
    assert response.data == b"Hello, World!"


def test_unknown_route_returns_404(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404


def test_post_not_allowed(client):
    response = client.post("/")
    assert response.status_code == 405