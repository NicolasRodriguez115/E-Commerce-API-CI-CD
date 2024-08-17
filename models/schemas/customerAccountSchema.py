from . import ma
from marshmallow import fields

class CustomerAccountSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    customer_id = fields.Integer(required=True)

customer_account_schema = CustomerAccountSchema()
customers_account_schema = CustomerAccountSchema(many=True)