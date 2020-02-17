import json
import pytest

from conftest import json_loader


@pytest.mark.parametrize('word, expected', [
    ['', 'Hello world!'],
    [None, 'Hello world!'],
    ['all', 'Hello all!'],
])
def test_hello_world(client, word, expected):
    url = f'/hello?word={word}' if word is not None else '/hello'
    response = client.get(url)
    assert expected in str(response.data)

def test_ticket_create(client):
    url = '/ticket/create'
    response = client.post(url)
    assert response.status_code is 201
    assert response.content_type == 'application/json'
