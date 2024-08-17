from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class Customer(Base):
    __tablename__ = 'Customers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(db.String(20), nullable=False)
    # orders: Mapped[List["Order"]] = db.relationship(back_populates="customer")
    account: Mapped["CustomerAccount"] = relationship("CustomerAccount", back_populates="customer", uselist=False)

    