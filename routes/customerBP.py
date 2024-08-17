from flask import Blueprint
from controllers.customerController import create_customer, get_all, update_customer

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=["POST"])(create_customer)
customer_blueprint.route('/', methods=["GET"])(get_all)
customer_blueprint.route('/<int:customer_id>', methods=["PATCH"])(update_customer)