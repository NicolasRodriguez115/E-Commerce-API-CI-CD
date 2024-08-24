import os
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Amoamati1.@localhost/advanced_e_commerce_db'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///app.db'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = False