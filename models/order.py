from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from typing import List

class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.utcnow, nullable=False)
    customer_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('Customers.id'), nullable=False)
    customer: Mapped['Customer'] = db.relationship(back_populates='orders')
    products: Mapped[List['Product']] = db.relationship(secondary='order_product_association', back_populates='orders')