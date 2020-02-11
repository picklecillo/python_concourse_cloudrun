import datetime as dt

from marshmallow import Schema, fields, post_load, validate


class Ticket:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return f'<Ticket(name={self.title})>'


class TicketSchema(Schema):
    title = fields.String(required=True)
    description = fields.String()
    created_at = fields.DateTime()

    @post_load
    def make_ticket(self, data, **kwargs):
        return Ticket(**data)


class Result:
    def __init__(self, result, status):
        self.result = result
        self.status = status

    def __repr__(self):
        return f'<Result(status={self.status}>'

    def __eq__(self, other):
        if isinstance(other, Result):
            return self.result == other.result and \
                self.status == other.status
        return False


class ResultSchema(Schema):
    result = fields.String()
    status = fields.String(
        required=True,
        validate=validate.OneOf(['ok', 'fail']),
    )
