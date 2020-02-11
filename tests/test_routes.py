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


@pytest.mark.parametrize('ticket_json, expected', [
    [
        json_loader('create_ticket.json'),
        {"result": "fake result", "status": "ok"}
    ],
    [
        json_loader('create_ticket_missing_title.json'),
        {"title": ["Missing data for required field."]}
    ],
])
def test_create_ticket(client, ticket_json, expected):
    url = '/create'
    response = client.post(
        url,
        json=ticket_json,
        headers={'Content': 'application/json'},
    )

    response_data = json.loads(response.data)

    for key in response_data.keys():
        assert response_data[key] == expected[key]
