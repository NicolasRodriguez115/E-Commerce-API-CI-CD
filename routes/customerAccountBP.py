from flask import Blueprint
from controllers.customerAccountController import create_customer_account, get_all, update_credentials

customer_account_blueprint = Blueprint('customers_account_bp', __name__)
customer_account_blueprint.route('/', methods=["POST"])(create_customer_account)
customer_account_blueprint.route('/', methods=["GET"])(get_all)
customer_account_blueprint.route('/<int:account_id>', methods=["PATCH"])(update_credentials)