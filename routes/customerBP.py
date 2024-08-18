from flask import Blueprint
from controllers.customerController import create_customer, get_all, update_customer, get_by_id, delete_by_id

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=["POST"])(create_customer)
customer_blueprint.route('/', methods=["GET"])(get_all)
customer_blueprint.route('/<int:customer_id>', methods=["GET"])(get_by_id)
customer_blueprint.route('/<int:customer_id>', methods=["DELETE"])(delete_by_id)
customer_blueprint.route('/<int:customer_id>', methods=["PATCH"])(update_customer)