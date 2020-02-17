import os
import json

from flask import Flask, request, jsonify
from marshmallow import ValidationError

from app.hello import greet
from app.models import TicketSchema, ResultSchema, Result


def create_app():
    app = Flask(__name__)
    return app


flask_app = create_app()


@flask_app.route('/hello', methods=['GET'])
def hello():
    who = request.args.get('word', 'world')
    greeting = greet(who)
    return greeting

@flask_app.route('/ticket/create', methods=['POST'])
def ticket_create():
    ticket_schema = TicketSchema()
    try:
        ticket = Result(result="fake result", status="ok")
    except ValidationError as err:
        return json.dumps(err.messages)
    return jsonify('{}'), 201
