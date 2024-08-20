from database import db
from models.customerAccount import CustomerAccount
from models.customer import Customer
from sqlalchemy import select
# from sqlalchemy.orm import joinedload
from utils.util import generate_token

def login(username, password):
    query = select(CustomerAccount).where(CustomerAccount.username == username)
    customer_account = db.session.execute(query).scalar_one_or_none()

    if customer_account and customer_account.password == password:
        token = generate_token(customer_account.customer_id, customer_account.role)

        response = {
            'status': 'success',
            'message': 'Succesfully Logged in',
            'token': token
        }
        return response
    else:
        response = {
            'status': 'fail',
            'message': 'invalid username or password'
        }
        return response

def create_customer_account(customer_credentials):
    query = select(Customer).where(Customer.id == customer_credentials['customer_id'])
    associated_customer = db.session.execute(query).scalar_one_or_none()

    if associated_customer is None:
        return {'message': "There isn't a customer with that id in the database"}, 404
    new_account = CustomerAccount(
        customer_id=customer_credentials['customer_id'],
        username=customer_credentials['username'],
        password=customer_credentials['password'],
        role=customer_credentials.get('role', 'user')
    ) 
    db.session.add(new_account)
    db.session.commit()

    db.session.refresh(new_account)
    return new_account, 201

def get_all():
    query = select(CustomerAccount)
    all_customers_accounts = db.session.execute(query).scalars().all()
    return all_customers_accounts

def get_by_id(customer_id):
    query = select(CustomerAccount).where(CustomerAccount.customer_id == customer_id).options(db.joinedload(CustomerAccount.customer))
    account = db.session.execute(query).scalars().first()
    if account is None:
        return {'message': 'Account not found'}, 404
    return account, 200

def delete_by_id(customer_id):
    query = select(CustomerAccount).where(CustomerAccount.customer_id == customer_id)
    account = db.session.execute(query).scalars().first()
    if account is None:
        return {'message': 'Account not found'}, 404

    db.session.delete(account)
    db.session.commit()
    return {'message': 'Account deleted succesfully'}, 200

def update_credentials(account_id, new_data):
    account = db.session.query(CustomerAccount).filter_by(customer_id=account_id).first()

    if not account:
        return {'error': 'Account not found'}, 404
    
    if 'username' in new_data:
        account.username = new_data['username']
    if 'password' in new_data:
        account.password = new_data['password']

    try:
        db.session.commit()
        return {'message': 'Account credentials updated succesfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500
    