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


    