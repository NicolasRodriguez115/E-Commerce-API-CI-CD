from . import ma
from marshmallow import fields, post_dump

class CustomerAccountSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    customer_id = fields.Integer(required=True)
    customer = fields.Nested('CustomerSchema', dump_only=True)

    @post_dump
    def remove_customer_id(self, data, **kwargs):
        data.pop('customer_id', None)
        return data

customer_account_schema = CustomerAccountSchema()
customers_account_schema = CustomerAccountSchema(many=True)