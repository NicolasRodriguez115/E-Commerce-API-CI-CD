from flask import Blueprint
from controllers.productController import create_product

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(create_product)