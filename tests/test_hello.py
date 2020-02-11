import pytest

from app.hello import greet


@pytest.mark.parametrize('who, expected', [
    ['world', 'Hello world!'],
    [None, 'Hello world!'],
    ['all', 'Hello all!']
])
def test_greet(who, expected):
    assert greet(who) == expected
