from flask import Flask
from database import db
from models.schemas import ma
from caching import cache
from flask_swagger_ui import get_swaggerui_blueprint

from models.customer import Customer
from models.customerAccount import CustomerAccount
from models.product import Product
from models.order import Order
from models.orderProductAssociation import order_product_association

from routes.customerBP import customer_blueprint
from routes.customerAccountBP import customer_account_blueprint
from routes.productBP import product_blueprint
from routes.orderBP import order_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swagger_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name':"E-commerce API"})

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app)
    
    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(customer_account_blueprint, url_prefix='/customers_account')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blueprint_config(app)

    with app.app_context():
        # db.drop_all()
        db.create_all()
    
    app.run()