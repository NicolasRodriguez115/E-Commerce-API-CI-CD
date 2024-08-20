from flask import Blueprint
from controllers.customerAccountController import create_customer_account, get_all, update_credentials, get_by_id, delete_by_id, login

customer_account_blueprint = Blueprint('customers_account_bp', __name__)
customer_account_blueprint.route('/', methods=["POST"])(create_customer_account)
customer_account_blueprint.route('/', methods=["GET"])(get_all)
customer_account_blueprint.route('/login', methods=["POST"])(login)
customer_account_blueprint.route('/<int:customer_id>', methods=["GET"])(get_by_id)
customer_account_blueprint.route('/<int:customer_id>', methods=["DELETE"])(delete_by_id)
customer_account_blueprint.route('/<int:account_id>', methods=["PATCH"])(update_credentials)