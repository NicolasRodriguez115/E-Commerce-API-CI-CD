## Overview

This app sets up a Flask application for an e-commerce API. It configures the application, initializes extensions, and registers blueprints for different parts of the application.

## Imports
```
from  flask  import  Flask
from database import  db
from models.schemas import  ma
from caching import  cache
from  flask_swagger_ui  import  get_swaggerui_blueprint
from models.customer import  Customer
from models.customerAccount import  CustomerAccount
from models.product import  Product
from models.order import  Order
from models.orderProductAssociation import  order_product_association
from routes.customerBP import  customer_blueprint
from routes.customerAccountBP import  customer_account_blueprint
from routes.productBP import  product_blueprint
from routes.orderBP import  order_blueprint
```
-   **Flask**: The main framework for creating the web application.
-   **db**: The database instance.
-   **ma**: Marshmallow instance for serialization/deserialization.
-   **cache**: Caching instance.
-   **get_swaggerui_blueprint**: Function to set up Swagger UI for API documentation.
-   **Models**: Importing various models used in the application.
-   **Blueprints**: Importing blueprints for different routes.

## Swagger Configuration
```
SWAGGER_URL  =  '/api/docs'
API_URL  =  '/static/swagger.yaml'
swagger_blueprint  =  get_swaggerui_blueprint(SWAGGER_URL,  API_URL,  config={'app_name':"E-commerce API"})
```
-   **SWAGGER_URL**: URL for accessing Swagger UI.
-   **API_URL**: Path to the Swagger YAML file.
-   **swagger_blueprint**: Blueprint for integrating Swagger UI into the application.

## `create_app`  Function
```
def  create_app(config_name):
app  =  Flask(__name__)
app.config.from_object(f'config.{config_name}')
db.init_app(app)
ma.init_app(app)
cache.init_app(app)
return  app
```
-   **create_app(config_name)**: Factory function to create and configure the Flask application.
    -   **config_name**: The configuration to use (e.g., 'DevelopmentConfig').
    -   **app**: The Flask application instance.
    -   **db.init_app(app)**: Initialize the database with the app.
    -   **ma.init_app(app)**: Initialize Marshmallow with the app.
    -   **cache.init_app(app)**: Initialize caching with the app.

## `blueprint_config`  Function
```
def  blueprint_config(app):
app.register_blueprint(customer_blueprint,  url_prefix='/customers')
app.register_blueprint(customer_account_blueprint,  url_prefix='/customers_account')
app.register_blueprint(product_blueprint,  url_prefix='/products')
app.register_blueprint(order_blueprint,  url_prefix='/orders')
```
-   **blueprint_config(app)**: Function to register blueprints with the application.
    -   **app**: The Flask application instance.
    -   **customer_blueprint**: Blueprint for customer-related routes.
    -   **customer_account_blueprint**: Blueprint for customer account-related routes.
    -   **product_blueprint**: Blueprint for product-related routes.
    -   **order_blueprint**: Blueprint for order-related routes.

## Main Execution
```
if  __name__  ==  '__main__':
app  =  create_app('DevelopmentConfig')
blueprint_config(app)
with  app.app_context():
```
# db.drop_all()

db.create_all()

app.run()

-   **Main Execution Block**: This block runs when the script is executed directly.
    -   **create_app('DevelopmentConfig')**: Create the app with the 'DevelopmentConfig' configuration.
    -   **blueprint_config(app)**: Register blueprints with the app.
    -   **app.app_context()**: Create an application context for database operations.
        -   **db.create_all()**: Create all database tables.
    -   **app.run()**: Run the Flask application.

## Summary

This file sets up and configures a Flask application for an e-commerce API. It initializes the database, Marshmallow, and caching, registers blueprints for different routes, and integrates Swagger UI for API documentation. The application is configured to run with the 'DevelopmentConfig' configuration when executed directly.

# API Documentation

## Customer Account Controller

### Endpoints

#### `POST /login`

-   **Description**: Authenticates a user and returns a token.
-   **Request Body**:
```
    {
	    "username":  "string", 
	    "password":  "string"
    }
   ``` 
-   **Responses**:
    -   `200 OK`: Returns the token.
    -   `401 Unauthorized`: Invalid payload or invalid username/password.

#### `POST /customer-account`

-   **Description**: Creates a new customer account.
-   **Request Body**:
    ```
    {
	    // Customer account data
    }
    
-   **Responses**:
    -   `201 Created`: Returns the created customer account.
    -   `400 Bad Request`: Validation error.
    -   `404 Not Found`: Resource not found.

#### `GET /customer-accounts`

-   **Description**: Retrieves all customer accounts.
-   **Responses**:
    -   `200 OK`: Returns a list of customer accounts.

#### `GET /customer-account/<customer_id>`

-   **Description**: Retrieves a customer account by ID.
-   **Parameters**:
    -   `customer_id`: ID of the customer account.
-   **Responses**:
    -   `200 OK`: Returns the customer account.
    -   `404 Not Found`: Customer account not found.

#### `DELETE /customer-account/<customer_id>`

-   **Description**: Deletes a customer account by ID.
-   **Parameters**:
    -   `customer_id`: ID of the customer account.
-   **Responses**:
    -   `200 OK`: Customer account deleted.
    -   `404 Not Found`: Customer account not found.

#### `PUT /customer-account/<account_id>`

-   **Description**: Updates customer account credentials.
-   **Parameters**:
    -   `account_id`: ID of the customer account.
-   **Request Body**:
    ```
    {    
	    // Partial customer account data    
    }
    
-   **Responses**:
    -   `200 OK`: Customer account updated.
    -   `400 Bad Request`: Validation error.

## Customer Controller

### Endpoints

#### `POST /customer`

-   **Description**: Creates a new customer.
-   **Request Body**:
   ``` 
    {    
	    // Customer data    
    }
   ```
-   **Responses**:
    -   `201 Created`: Returns the created customer.
    -   `400 Bad Request`: Validation error.

#### `GET /customers`

-   **Description**: Retrieves all customers.
-   **Responses**:
    -   `200 OK`: Returns a list of customers.

#### `GET /customer/<customer_id>`

-   **Description**: Retrieves a customer by ID.
-   **Parameters**:
    -   `customer_id`: ID of the customer.
-   **Responses**:
    -   `200 OK`: Returns the customer.
    -   `404 Not Found`: Customer not found.

#### `DELETE /customer/<customer_id>`

-   **Description**: Deletes a customer by ID.
-   **Parameters**:
    -   `customer_id`: ID of the customer.
-   **Responses**:
    -   `200 OK`: Customer deleted.
    -   `404 Not Found`: Customer not found.

#### `PUT /customer/<customer_id>`

-   **Description**: Updates a customer.
-   **Parameters**:
    -   `customer_id`: ID of the customer.
-   **Request Body**:
  ```  
    {    
	    // Partial customer data    
    }
  ```  
-   **Responses**:
    -   `200 OK`: Customer updated.
    -   `400 Bad Request`: Validation error.

## Order Controller

### Endpoints

#### `POST /order`

-   **Description**: Creates a new order.
-   **Request Body**:
```    
    {    
	    // Order data   
    }
```    
-   **Responses**:
    -   `201 Created`: Returns the created order.
    -   `400 Bad Request`: Validation error.

#### `GET /order/<order_id>`

-   **Description**: Retrieves an order by ID.
-   **Parameters**:
    -   `order_id`: ID of the order.
-   **Responses**:
    -   `200 OK`: Returns the order.
    -   `404 Not Found`: Order not found.

## Product Controller

### Endpoints

#### `POST /product`

-   **Description**: Creates a new product.
-   **Request Body**:
```    
    {    
	    // Product data    
    }
```    
-   **Responses**:
    -   `201 Created`: Returns the created product.
    -   `400 Bad Request`: Validation error.

#### `GET /products`

-   **Description**: Retrieves all products.
-   **Responses**:
    -   `200 OK`: Returns a list of products.

#### `GET /product/<product_id>`

-   **Description**: Retrieves a product by ID.
-   **Parameters**:
    -   `product_id`: ID of the product.
-   **Responses**:
    -   `200 OK`: Returns the product.
    -   `404 Not Found`: Product not found.

#### `PUT /product/<product_id>`

-   **Description**: Updates a product.
-   **Parameters**:
    -   `product_id`: ID of the product.
-   **Request Body**:
```    
    {    
	    // Partial product data    
    }
```    
-   **Responses**:
    -   `200 OK`: Product updated.
    -   `400 Bad Request`: Validation error.

#### `DELETE /product/<product_id>`

-   **Description**: Deletes a product by ID.
-   **Parameters**:
    -   `product_id`: ID of the product.
-   **Responses**:
    -   `200 OK`: Product deleted.
    -   `404 Not Found`: Product not found.

# ProductService Documentation

## Functions

### `create_product(product_data)`

Creates a new product.

-   **Parameters:**
    -   `product_data`  (dict): A dictionary containing product details (`name`,  `price`,  `details`).
-   **Returns:**
    -   `Product`: The newly created product.

### `get_all()`

Retrieves all products.

-   **Returns:**
    -   `list[Product]`: A list of all products.

### `get_by_id(product_id)`

Retrieves a product by its ID.

-   **Parameters:**
    -   `product_id`  (int): The ID of the product.
-   **Returns:**
    -   `tuple`: A tuple containing the product and status code 200, or an error message and status code 404 if not found.

### `update_product(product_id, new_data)`

Updates an existing product.

-   **Parameters:**
    -   `product_id`  (int): The ID of the product.
    -   `new_data`  (dict): A dictionary containing updated product details (`name`,  `price`,  `details`).
-   **Returns:**
    -   `dict`: A success message and status code 200, or an error message and status code 404/500.

### `delete_by_id(product_id)`

Deletes a product by its ID.

-   **Parameters:**
    -   `product_id`  (int): The ID of the product.
-   **Returns:**
    -   `dict`: A success message and status code 200, or an error message and status code 404.

# OrderService Documentation

## Functions

### `create_order(order_data)`

Creates a new order.

-   **Parameters:**
    -   `order_data`  (dict): A dictionary containing order details (`customer_id`,  `products`).
-   **Returns:**
    -   `Order`: The newly created order, or an error message and status code 404/400/500.

### `get_by_id(order_id)`

Retrieves an order by its ID.

-   **Parameters:**
    -   `order_id`  (int): The ID of the order.
-   **Returns:**
    -   `tuple`: A tuple containing the order and status code 200, or an error message and status code 404 if not found.

# CustomerService Documentation

## Functions

### `create_customer(customer_data)`

Creates a new customer.

-   **Parameters:**
    -   `customer_data`  (dict): A dictionary containing customer details (`name`,  `email`,  `phone`).
-   **Returns:**
    -   `Customer`: The newly created customer.

### `get_all()`

Retrieves all customers.

-   **Returns:**
    -   `list[Customer]`: A list of all customers.

### `get_by_id(customer_id)`

Retrieves a customer by its ID.

-   **Parameters:**
    -   `customer_id`  (int): The ID of the customer.
-   **Returns:**
    -   `tuple`: A tuple containing the customer and status code 200, or an error message and status code 404 if not found.

### `delete_by_id(customer_id)`

Deletes a customer by its ID.

-   **Parameters:**
    -   `customer_id`  (int): The ID of the customer.
-   **Returns:**
    -   `dict`: A success message and status code 200, or an error message and status code 404.

### `update_customer(customer_id, new_data)`

Updates an existing customer.

-   **Parameters:**
    -   `customer_id`  (int): The ID of the customer.
    -   `new_data`  (dict): A dictionary containing updated customer details (`name`,  `email`,  `phone`).
-   **Returns:**
    -   `dict`: A success message and status code 200, or an error message and status code 400/500.


# CustomerAccount Service Documentation

## Overview

The  `customerAccountService.py`  module provides functionalities to manage customer accounts, including creating, retrieving, updating, and deleting accounts. It also includes a login function to authenticate users.

## Functions

### `login(username, password)`

Authenticates a user based on the provided username and password.

-   **Parameters:**
    
    -   `username`  (str): The username of the customer.
    -   `password`  (str): The password of the customer.
-   **Returns:**
    
    -   `dict`: A response containing the status and message of the login attempt. If successful, it also includes a token.

### `create_customer_account(customer_credentials)`

Creates a new customer account.

-   **Parameters:**
    
    -   `customer_credentials`  (dict): A dictionary containing the customer's credentials. Must include  `customer_id`,  `username`, and  `password`. Optionally includes  `role`.
-   **Returns:**
    
    -   `tuple`: A tuple containing the newly created account and the HTTP status code. If the customer ID is not found, returns an error message and a 404 status code.

### `get_all()`

Retrieves all customer accounts.

-   **Returns:**
    -   `list`: A list of all customer accounts.

### `get_by_id(customer_id)`

Retrieves a customer account by its ID.

-   **Parameters:**
    
    -   `customer_id`  (int): The ID of the customer.
-   **Returns:**
    
    -   `tuple`: A tuple containing the account and the HTTP status code. If the account is not found, returns an error message and a 404 status code.

### `delete_by_id(customer_id)`

Deletes a customer account by its ID.

-   **Parameters:**
    
    -   `customer_id`  (int): The ID of the customer.
-   **Returns:**
    
    -   `tuple`: A tuple containing a success message and the HTTP status code. If the account is not found, returns an error message and a 404 status code.

### `update_credentials(account_id, new_data)`

Updates the credentials of a customer account.

-   **Parameters:**
    
    -   `account_id`  (int): The ID of the customer account.
    -   `new_data`  (dict): A dictionary containing the new credentials. Can include  `username`  and/or  `password`.
-   **Returns:**
    
    -   `tuple`: A tuple containing a success message and the HTTP status code. If the account is not found, returns an error message and a 404 status code. If there is an error during the update, returns an error message and a 500 status code.

## Dependencies

-   `database`: Module to handle database connections.
-   `models.customerAccount`: Model for the customer account.
-   `models.customer`: Model for the customer.
-   `sqlalchemy`: SQL toolkit and Object-Relational Mapping (ORM) library.
-   `utils.util`: Utility functions, including token generation.

## Example Usage
```
from customerAccountService import create_customer_account, get_all

# Create a new customer account
customer_credentials  =  {
	'customer_id':  1,
	'username':  'john_doe',
	'password':  'securepassword',
	'role':  'user'
}
response  =  create_customer_account(customer_credentials)
print(response)

# Get all customer accounts
accounts  =  get_all()
print(accounts)
```
## Error Handling

-   The service returns appropriate HTTP status codes and error messages for various failure scenarios, such as account not found (404) and internal server errors (500).

# Database Models Documentation

## Product Model

Represents a product in the database.

### Table Name

`products`

### Columns

-   **id**:  `int`  - Primary key.
-   **name**:  `str`  - Name of the product. Cannot be null.
-   **price**:  `float`  - Price of the product. Cannot be null.
-   **details**:  `str`  - Additional details about the product. Can be null.
-   **orders**:  `List[Order]`  - Relationship to the  `Order`  model through the  `order_product_association`  table.

### Relationships

-   **orders**: Many-to-many relationship with the  `Order`  model.

## OrderProductAssociation Model

Association table for the many-to-many relationship between  `Order`  and  `Product`.

### Table Name

`order_product_association`

### Columns

-   **order_id**:  `int`  - Foreign key referencing  `orders.id`. Primary key.
-   **product_id**:  `int`  - Foreign key referencing  `products.id`. Primary key.

## Order Model

Represents an order in the database.

### Table Name

`orders`

### Columns

-   **id**:  `int`  - Primary key.
-   **date**:  `datetime`  - Date of the order. Defaults to the current date and time. Cannot be null.
-   **customer_id**:  `int`  - Foreign key referencing  `Customers.id`. Cannot be null.
-   **customer**:  `Customer`  - Relationship to the  `Customer`  model.
-   **products**:  `List[Product]`  - Relationship to the  `Product`  model through the  `order_product_association`  table.

### Relationships

-   **customer**: Many-to-one relationship with the  `Customer`  model.
-   **products**: Many-to-many relationship with the  `Product`  model.

# Customer Model Documentation

## Overview

The  `Customer`  model represents a customer in the database. It includes fields for storing customer details such as name, email, phone number, and relationships to other models like  `CustomerAccount`  and  `Order`.

## Table Name

`Customers`

## Fields

-   **id**:
    
    -   Type:  `int`
    -   Description: Primary key for the customer.
    -   Attributes:  `primary_key=True`
-   **name**:
    
    -   Type:  `str`
    -   Description: Name of the customer.
    -   Attributes:  `db.String(255)`,  `nullable=False`
-   **email**:
    
    -   Type:  `str`
    -   Description: Email address of the customer.
    -   Attributes:  `db.String(255)`,  `unique=True`,  `nullable=False`
-   **phone**:
    
    -   Type:  `str`
    -   Description: Phone number of the customer.
    -   Attributes:  `db.String(20)`,  `nullable=False`

## Relationships

-   **account**:
    
    -   Type:  `CustomerAccount`
    -   Description: One-to-one relationship with the  `CustomerAccount`  model.
    -   Attributes:  `relationship("CustomerAccount", back_populates="customer", cascade='all, delete-orphan', uselist=False)`
-   **orders**:
    
    -   Type:  `List[Order]`
    -   Description: One-to-many relationship with the  `Order`  model.
    -   Attributes:  `db.relationship(back_populates="customer", lazy='dynamic')`
## Notes

-   The  `email`  field must be unique for each customer.
-   The  `account`  relationship uses  `cascade='all, delete-orphan'`  to ensure that related  `CustomerAccount`  entries are deleted when the customer is deleted.
-   The  `orders`  relationship is lazy-loaded dynamically.


## Schemas Documentation

### ProductSchema

**ProductSchema**  is used to serialize and deserialize product data.

-   **id**: Integer (optional)
-   **name**: String (required)
-   **price**: Float (required)
-   **details**: String (optional)

**Example:**
```
{
	"id":  1,
	"name":  "Product Name",
	"price":  99.99,
	"details":  "Product details"
}
```
### ProductOrderSchema

**ProductOrderSchema**  is used to serialize and deserialize product order data.

-   **id**: Integer (required)
-   **name**: String (optional)
-   **price**: Float (optional)
-   **quantity**: Integer (required)

**Example:**
```
{
	"id":  1,
	"name":  "Product Name",
	"price":  99.99,
	"quantity":  2
}
```
### OrderSchema

**OrderSchema**  is used to serialize and deserialize order data.

-   **id**: Integer (optional)
-   **date**: DateTime (optional)
-   **customer_id**: Integer (required)
-   **customer**: Nested  `CustomerOrderSchema`
-   **products**: Nested  `ProductOrderSchema`  (many=True)

**Example:**
```
{
	"id":  1,
	"date":  "2023-10-01T12:00:00",
	"customer_id":  1,
	"customer":  {
		"name":  "Customer Name",
		"email":  "customer@example.com",
		"phone":  "123-456-7890"
	},
	"products":  [
		{
		"id":  1,
		"name":  "Product Name",
		"price":  99.99,
		"quantity":  2
		}
	]
}
```
### CustomerSchema

**CustomerSchema**  is used to serialize and deserialize customer data.

-   **id**: Integer (optional)
-   **name**: String (required)
-   **email**: Email (required)
-   **phone**: String (required)

**Example:**
```
{
"id":  1,
"name":  "Customer Name",
"email":  "customer@example.com",
"phone":  "123-456-7890"
}
```
### CustomerOrderSchema

**CustomerOrderSchema**  is used to serialize and deserialize customer order data.

-   **name**: String (required)
-   **email**: Email (required)
-   **phone**: String (required)

**Example:**
```
{
"name":  "Customer Name",
"email":  "customer@example.com",
"phone":  "123-456-7890"
}
```
### CustomerAccountSchema

**CustomerAccountSchema**  is used to serialize and deserialize customer account data.

-   **id**: Integer (dump only)
-   **username**: String (required)
-   **password**: String (required)
-   **customer_id**: Integer (required)
-   **customer**: Nested  `CustomerSchema`  (dump only)
-   **role**: String (optional)

**Example:**
```
{
"id":  1,
"username":  "customer_username",
"password":  "hashed_password",
"customer_id":  1,
"customer":  {
	"id":  1,
	"name":  "Customer Name",
	"email":  "customer@example.com",
	"phone":  "123-456-7890"
	},
"role":  "user"
}
```
**Note:**  The  `customer_id`  field is removed from the output after serialization using the  `@post_dump`  method.