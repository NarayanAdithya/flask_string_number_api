from werkzeug.wrappers import response
from server.app import app
import pytest
import json
from pathlib import Path

@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    app.config["TESTING"] = True
    yield app.test_client()  # tests run here


def test_palindrome_p(client):
    response=client.get('/check/palindrome/malayalam')
    response=json.loads(response.data)
    assert response['result']==1

def test_palindrome_f(client):
    response=client.get('/check/palindrome/adithya')
    response=json.loads(response.data)
    assert response['result']==0

def test_anagram_p(client):
    response=client.get('/check/anagram/silent/listen')
    response=json.loads(response.data)
    assert response['result']==1

def test_anagram_f(client):
    response=client.get('/check/anagram/adithya/narayan')
    response=json.loads(response.data)
    assert response['result']==0

def test_prime_p(client):
    response=client.get('/check/prime/337')
    response=json.loads(response.data)
    assert response['result']==1

def test_prime_f(client):
    response=client.get('/check/prime/1000')
    response=json.loads(response.data)
    assert response['result']==0

def test_armstrong_p(client):
    response=client.get('/check/armstrong/407')
    response=json.loads(response.data)
    assert response['result']==1

def test_armstrong_f(client):
    response=client.get('/check/armstrong/200')
    response=json.loads(response.data)
    assert response['result']==0