import os
import json

from flask import Flask, request
from marshmallow import ValidationError

from app.hello import greet
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
