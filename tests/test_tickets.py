import pytest

from app.models import Ticket, Result
from app.tickets import do_something


@pytest.mark.parametrize('ticket, expected', [
    [
        Ticket(title="title", description="description"),
        Result(result="fake result", status="ok")
    ]
])
def test_do_something(ticket, expected):
    result = do_something(ticket)

    assert result == expected
