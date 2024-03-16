"""
Unit tests for App Factory.
"""
from flaskr import create_app


def test_config():
    """
    If config is not passed, there should be some default configuration, \
      otherwise the configuration should be overridden.
    """
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    """
    The test checks that the response data matches using the example route.
    """
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
