import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from services import customerAccountService, customerService, productService
from app import create_app, blueprint_config

fake = Faker()
class TestLoginCustomer(unittest.TestCase):
    def setUp(self):
            app = create_app('DevelopmentConfig')
            blueprint_config(app)
            app.config['TESTING'] = True
            self.app = app.test_client()
            

    @patch('services.customerAccountService.login')
    def test_login_customer(self, mock_customer):
        username = fake.user_name()
        password = fake.password()
        password_hash = generate_password_hash(password)

        mock_response = {
            'status': 'success',
            'message': 'Successfully Logged in',
            'token': 'fake_token'
        }

        mock_customer.return_value = mock_response

        payload = {
            "username": username,
            "password": password
        }

        response = self.app.post('/customers_account/login', json=payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'success')
        self.assertEqual(response.json['message'], 'Successfully Logged in')
        self.assertIn('token', response.json)

    @patch('services.customerAccountService.login')
    def test_login_fail(self, mock_execute):
        mock_execute.return_value = None
        payload = {
            "username": "nonexistent_user",
            "password": "wrong_password",
        }

        response = self.app.post('/customers_account/login', json=payload)

        self.assertEqual(response.status_code, 401)

class TestCustomer(unittest.TestCase):

    def setUp(self):
        app = create_app('DevelopmentConfig')
        blueprint_config(app)
        app.config['TESTING'] = True
        self.app = app.test_client()
    @patch('services.customerService.create_customer')
    def test_case_customer(self, mock_save):
        name = fake.name()
        phone = fake.basic_phone_number()
        email = fake.email()

        mock_customer = MagicMock()
        mock_customer.name = name
        mock_customer.phone = phone
        mock_customer.email = email

        mock_save.return_value = mock_customer

        payload = {
            "name": name,
            "phone": phone,
            'email': email,
        }
        response = self.app.post('/customers/', json=payload) 

        self.assertEqual(response.status_code, 201)
        self.assertEqual(mock_save.return_value.name, name)




if __name__ == '__main__':
    unittest.main()
