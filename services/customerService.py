from database import db
from models.customer import Customer
from sqlalchemy import select

def create_customer(customer_data):
    new_customer = Customer(
        name=customer_data['name'], 
        email=customer_data['email'],  
        phone=customer_data['phone']
    )
    db.session.add(new_customer)
    db.session.commit()

    db.session.refresh(new_customer)
    return new_customer

def get_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers

def update_customer(customer_id, new_data):

    customer = db.session.query(Customer).filter_by(id=customer_id).first()

    if not customer:
        return {'error': 'Customer not found'}, 400
    
    if 'name' in new_data:
        customer.name = new_data['name']
    if 'email' in new_data:
        customer.email = new_data['email']
    if 'phone' in new_data:
        customer.phone = new_data['phone']

    try:
        db.session.commit()
        return {'message': 'Customer updated succesfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500
    
