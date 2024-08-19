from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError

def create_product():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    product_saved = productService.create_product(product_data)
    return product_schema.jsonify(product_saved), 201

def get_all():
    all_products = productService.get_all()
    return products_schema.jsonify(all_products), 200

def get_by_id(product_id):
    response, status = productService.get_by_id(product_id)
    if status == 404:
        return jsonify(response), status
    return product_schema.jsonify(response), status

def update_product(product_id):
    try:
        new_data = product_schema.load(request.json, partial=True)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    response, status = productService.update_product(product_id, new_data)
    return jsonify(response), status
