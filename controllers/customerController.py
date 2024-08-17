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
    