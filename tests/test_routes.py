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

@pytest.mark.parametrize('ticket_json, expected_data, expected_status', [
    [
        json_loader('create_ticket.json'), {"result": "fake result", "status": "ok"}, 201
    ],
    [
        json_loader('create_ticket_missing_title.json'), {"error":"{'title': ['Missing data for required field.']}"}, 406
    ],
])
def test_ticket_create(client, ticket_json, expected_data, expected_status):
    url = '/ticket/create'
    response = client.post(
        url,
        json=ticket_json,
        headers={'Content': 'application/json'}
    )

    assert response.content_type == 'application/json'
    assert response.status_code == expected_status
    print(response.json)
    response_data = json.loads(response.json)
    for key in response_data.keys():
        assert response_data[key] == expected_data[key]
