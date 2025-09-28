import pytest
from project import app

@pytest.fixture
def client():
    with app.test_client() as client: # create test client
        yield client