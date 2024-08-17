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

