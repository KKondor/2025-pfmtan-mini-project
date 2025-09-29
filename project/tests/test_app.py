import pytest
from project import app

@pytest.fixture
def client():
    with app.test_client() as client: # create test client
        yield client

# GET /joke endpoint test
def test_get_joke(client):
    response = client.get('/joke')
    assert response.status_code == 200
    data = response.get_json()
    assert 'id' in data
    assert 'setup' in data
    assert 'punchline' in data
    assert 'rating' in data

# GET /leaderboard endpoint test
def test_get_leaderboard(client):
    response = client.get('/leaderboard')
    assert response.status_code == 200
    data = response.get_json()
    for joke in data:
        assert 'id' in joke
        assert 'setup' in joke
        assert 'punchline' in joke
        assert 'rating' in joke