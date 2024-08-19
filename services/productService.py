from database import db
from models.product import Product
from sqlalchemy import select

def create_product(product_data):
    new_product = Product(
        name=product_data['name'], 
        price=product_data['price'],
        details=product_data['details']
    )
    db.session.add(new_product)
    db.session.commit()

    db.session.refresh(new_product)
    return new_product

def get_all():
    pass