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
    query = select(Product)
    all_products = db.session.execute(query).scalars().all()
    return all_products

def get_by_id(product_id):
    query = select(Product).where(Product.id == product_id)
    product = db.session.execute(query).scalars().first()
    if product is None:
        return {'message': 'Product not found'}, 404
    return product, 200