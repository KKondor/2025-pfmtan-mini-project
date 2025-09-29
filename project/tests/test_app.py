import pytest
from project import app
from unittest.mock import patch, MagicMock

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

# POST /joke/<id>/rate endpoint test (like)
@patch('project.services.JokeService.rate_joke')
def test_rate_joke_like(mock_rate, client):
    response = client.post('/joke/1/rate', json={'value': 1})
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    mock_rate.assert_called_once_with(1, 1)

# POST /joke/<id>/rate endpoint test (dislike)
@patch('project.services.JokeService.rate_joke')
def test_rate_joke_dislike(mock_rate, client):
    response = client.post('/joke/1/rate', json={'value': -1})
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
    mock_rate.assert_called_once_with(1, -1)

# POST /joke/<id>/rate endpoint test (invalid value)
def test_rate_joke_invalid_value(client):
    response = client.post('/joke/1/rate', json={'value': 0})
    assert response.status_code == 500

