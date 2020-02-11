import json
import pytest

from app.routes import flask_app


@pytest.fixture
def client():
    return flask_app.test_client()


def json_loader(file):
    with open(f'tests/mocks/{file}', 'r') as f:
        contents = f.read()
        return json.loads(contents)
