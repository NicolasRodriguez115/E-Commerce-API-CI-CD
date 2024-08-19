from database import db, Base

order_product_association = db.Table(
    'order_product_association',
    Base.metadata,
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
)