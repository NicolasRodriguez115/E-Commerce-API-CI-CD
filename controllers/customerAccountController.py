from flask import request, jsonify
from models.schemas.customerAccountSchema import customer_account_schema, customers_account_schema
from services import customerAccountService
from marshmallow import ValidationError

def create_customer_account():
    try:
        account_data = customer_account_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    account_saved = customerAccountService.create_customer_account(account_data)
    return customer_account_schema.jsonify(account_saved), 201


def get_all():
    all_customers_accounts = customerAccountService.get_all()
    return customers_account_schema.jsonify(all_customers_accounts), 200

def get_by_id(customer_id):
    response, status = customerAccountService.get_by_id(customer_id)
    if status == 404:
        return jsonify(response), status
    return customer_account_schema.jsonify(response), status

def delete_by_id(customer_id):
    response, status = customerAccountService.delete_by_id(customer_id)
    if status == 404:
        return jsonify(response), status
    return jsonify(response), status

def update_credentials(account_id):
    try:
        new_data = customer_account_schema.load(request.json, partial=True)
    except ValidationError as e:
        return jsonify(e.messages), 400

    response, status = customerAccountService.update_credentials(account_id, new_data)
    return jsonify(response), status