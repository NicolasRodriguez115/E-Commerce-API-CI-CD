from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class CustomerAccount(Base):
    __tablename__ = 'customers_account'
    customer_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('Customers.id', ondelete='CASCADE'), primary_key=True)
    username: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    customer: Mapped['Customer'] = relationship('Customer', back_populates='account')