import os
import json

from flask import Flask, request, jsonify, Response
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
        ticket = ticket_schema.load(request.json)
    except ValidationError as err:
        error_messages = err.messages
        return Response(json.dumps('{"error":"%s"}'%(error_messages)), status=406, mimetype='application/json')

    schema = ResultSchema()
    result = Result(result="fake result", status="ok")
    result = schema.dumps(result)

    resp = Response(json.dumps(result), status=201, mimetype='application/json')
    return resp
