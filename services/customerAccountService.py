from database import db
from models.customerAccount import CustomerAccount
from sqlalchemy import select

def create_customer_account(customer_credentials):
    new_account = CustomerAccount(
        customer_id=customer_credentials['customer_id'],
        username=customer_credentials['username'],
        password=customer_credentials['password']
    ) 
    db.session.add(new_account)
    db.session.commit()

    db.session.refresh(new_account)
    return new_account

def get_all():
    query = select(CustomerAccount)
    all_customers_accounts = db.session.execute(query).scalars().all()
    return all_customers_accounts
