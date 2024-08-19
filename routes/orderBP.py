from flask import Blueprint
from controllers.orderController import create_order, get_by_id

order_blueprint = Blueprint('order_bp', __name__)
order_blueprint.route('/', methods=['POST'])(create_order)
order_blueprint.route('/<int:order_id>', methods=['GET'])(get_by_id)
