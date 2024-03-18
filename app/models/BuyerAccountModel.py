from app.utils.db import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime, func
from datetime import datetime
from uuid import uuid4
from passlib.hash import pbkdf2_sha256


class BuyerModel(db.Model):
    __tablename__ = "buyer"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(100), nullable=False, unique=True)
    email = mapped_column(String(100), nullable=False, unique=True)
    password = mapped_column(String(100), nullable=False)
    address = mapped_column(String(100), nullable=False, unique=True)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), onupdate=datetime.now)

    def __init__(self, username:str, email:str, password:str, address:str) -> None:
        self.id = str(uuid4())
        self.username = username
        self.email = email
        self.password = pbkdf2_sha256.hash(password)
        self.address = address
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


