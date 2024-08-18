from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError

def create_customer():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer_saved = customerService.create_customer(customer_data)
    return customer_schema.jsonify(customer_saved), 201

def get_all():
    all_customers = customerService.get_all()
    return customers_schema.jsonify(all_customers), 200

def get_by_id(customer_id):
    response, status = customerService.get_by_id(customer_id)
    if status == 404:
        return jsonify(response), status
    return customer_schema.jsonify(response), status

def delete_by_id(customer_id):
    response, status = customerService.delete_by_id(customer_id)
    if status == 404:
        return jsonify(response), status
    return jsonify(response), status

def update_customer(customer_id):
    try:
        new_data = customer_schema.load(request.json, partial=True)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    response, status = customerService.update_customer(customer_id, new_data)
    return jsonify(response), status


