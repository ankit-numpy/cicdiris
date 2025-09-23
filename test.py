#test fask 

import pytest

from app import app

@pytest.fixture
def clients():
    app.config['TESTING']=True
    with app.test_client() as client:
        yield client

def test_home_page(clients):
    response=clients.get('/')
    assert response.status_code==200
    assert b"Welcome to the Iris Prediction API!" in response.data

def test_compute_page(clients):
    response=clients.post('/compute', json={'features': [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code==200
    assert b'setosa' in response.data

