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
