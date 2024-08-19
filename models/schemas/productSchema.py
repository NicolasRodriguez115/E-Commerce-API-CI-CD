from . import ma
from marshmallow import fields

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    price = fields.Float(required=True)
    details = fields.String(required=False)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)