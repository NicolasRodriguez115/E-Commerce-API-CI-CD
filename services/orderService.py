from database import db
from models.order import Order
from models.customer import Customer
from models.product import Product
from sqlalchemy import select
from datetime import datetime

def create_order(order_data):
    customer = db.session.query(Customer).filter_by(id = order_data['customer_id']).first()
    if not customer:
        return {'error': 'Customer not found'}, 404
    
    new_order = Order(
        date=datetime.utcnow(),
        customer_id=order_data['customer_id']
    )

    if not order_data.get('products'):
        return {'error': 'No products provided'}, 400
    
    for product_data in order_data['products']:
        product_id = product_data['id']
        query = select(Product).filter(Product.id == product_id)
        product = db.session.execute(query).scalar()
        if not product:
            db.session.rollback()
            return {'error': f'Product with id {product_id} not found'}, 404
        new_order.products.append(product)
        
    try:
        db.session.add(new_order)
        db.session.commit()
        db.session.refresh(new_order)
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500

    return new_order

def get_by_id(order_id):
    query = select(Order).where(Order.id == order_id)
    order = db.session.execute(query).scalars().first()
    if order is None:
        return {'message': 'Order not found'}, 404
    return order, 200
