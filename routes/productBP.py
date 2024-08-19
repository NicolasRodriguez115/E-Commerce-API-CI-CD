from flask import Blueprint
from controllers.productController import create_product, get_all, get_by_id

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(create_product)
product_blueprint.route('/', methods=['GET'])(get_all)
product_blueprint.route('/<int:product_id>', methods=['GET'])(get_by_id)
