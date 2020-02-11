from app.models import Result


def do_something(ticket):
    print(ticket)
    return Result(result="fake result", status="ok")
