import os
import json

from flask import Flask, request
from marshmallow import ValidationError

from app.hello import greet
from app.tickets import do_something
from app.models import TicketSchema, ResultSchema


def create_app():
    app = Flask(__name__)
    return app


flask_app = create_app()


@flask_app.route('/hello', methods=['GET'])
def hello():
    who = request.args.get('word', 'world')
    greeting = greet(who)
    return greeting


@flask_app.route('/create', methods=['POST'])
def create():
    ticket_schema = TicketSchema()
    try:
        ticket = ticket_schema.load(request.json)
    except ValidationError as err:
        return json.dumps(err.messages)

    result = do_something(ticket)

    schema = ResultSchema()
    result = schema.dumps(result)
    return result


if __name__ == "__main__":
    flask_app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8080)),
    )
