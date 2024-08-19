from flask import Blueprint
from controllers.productController import create_product, get_all, get_by_id, update_product, delete_by_id

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(create_product)
product_blueprint.route('/', methods=['GET'])(get_all)
product_blueprint.route('/<int:product_id>', methods=['GET'])(get_by_id)
product_blueprint.route('/<int:product_id>', methods=['PATCH'])(update_product)
product_blueprint.route('/<int:product_id>', methods=['DELETE'])(delete_by_id)
