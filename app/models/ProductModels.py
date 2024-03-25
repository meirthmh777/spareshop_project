from app.utils.db import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, DECIMAL, DateTime, func
from datetime import datetime
from uuid import uuid4


class ProductModel (db.Model):
    __tablename__ = "product"

    id = mapped_column(String(100), primary_key=True)
    name = mapped_column(String(100), nullable=False)
    price = mapped_column(DECIMAL(20,2), nullable=False)
    stock = mapped_column(DECIMAL(10,2), nullable=False)
    description = mapped_column(String(100))
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), onupdate=datetime.now)

    def __init__(self, name:str, price:float, stock:int, description:str) -> None:
        self.id = str(uuid4())
        self.name = name
        self.price = price
        self.stock = stock
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


