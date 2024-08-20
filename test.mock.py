import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from services import customerAccountService, customerService, productService

class TestLoginCustomer(unittest.TestCase):

    @patch('services.customerAccountService.db.session.execute')
    def test_login_customer(self, mock_customer):
        faker = Faker()
        mock_user = MagicMock() 
        mock_user.username = faker.user_name()
        mock_user.password = generate_password_hash(faker.password())
        mock_user.customer_id = 1
        mock_user.role = 'user'
        mock_customer.return_value.scalar_one_or_none.return_value = mock_user

        response = customerAccountService.login(mock_user.username, mock_user.password)

        self.assertEqual(response['status'], 'success')
        self.assertIn('token', response)

    @patch('services.customerAccountService.db.session.execute')
    def test_login_fail(self, mock_execute):
        mock_execute.return_value.scalar_one_or_none.return_value = None

        response = customerAccountService.login('wronguser', 'wrongpassword')

        self.assertEqual(response['status'], 'fail')
        self.assertEqual(response['message'], 'invalid username or password')

class TestCreateCustomer(unittest.TestCase):

    # This should work but it seems like the problem is that it wants me to import the models for Order and customerAccount to the Customer model. I was told not to do this.
    @patch('services.customerService.db.session.execute')
    def test_create_customer(self, mock_session):
        faker = Faker()
        mock_customer_data = {
            'name': faker.name(),
            'email': faker.email(),
            'phone': faker.phone_number(),
            'role': 'admin'
        }
        mock_customer = MagicMock()
        mock_session.add.return_value = None
        mock_session.commit.return_value = None
        mock_session.refresh.return_value = None

        response = customerService.create_customer(mock_customer_data)
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once()
        self.assertEqual(response.name, mock_customer_data['name'])
        self.assertEqual(response.name, mock_customer_data['email'])
        self.assertEqual(response.name, mock_customer_data['phone'])
        self.assertEqual(response.name, mock_customer_data['role'])

class TestCreateProduct(unittest.TestCase):
    # Same problem as before
    @patch('services.productService.db.session')
    def test_create_product(self, mock_session):
        faker = Faker()        
        mock_product_data = {
            'name': faker.name(),
            'price': faker.pyfloat(positive=True),
            'details': faker.pystr()
        }
        
        mock_product = MagicMock()
        mock_session.add.return_value = None
        mock_session.commit.return_value = None
        mock_session.refresh.return_value = None

        result = productService.create_product(mock_product_data)

        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once()
        self.assertEqual(result.name, mock_product_data['name'])
        self.assertEqual(result.price, mock_product_data['price'])
        self.assertEqual(result.details, mock_product_data['details'])


if __name__ == '__main__':
    unittest.main()
