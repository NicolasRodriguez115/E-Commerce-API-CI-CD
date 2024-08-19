from . import ma
from marshmallow import fields

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.DateTime(required=False)
    customer_id = fields.Integer(required=True)
    customer = fields.Nested('CustomerOrderSchema')
    products = fields.Nested('ProductOrderSchema', many=True)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)