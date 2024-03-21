from app.utils.db import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, DateTime, func, ForeignKey
from datetime import datetime
from uuid import uuid4
from passlib.hash import pbkdf2_sha256


class ShopModel(db.Model):
    __tablename__ = "shop"

    id = mapped_column(String, primary_key=True)
    user_id = mapped_column(String(100), ForeignKey("user.id")) # as foreign key references to id in user table
    # Could not initialize target column for ForeignKey 'user.user_id' on table 'shop': table 'user' has no column named 'user_id'
    shopname = mapped_column(String(100), nullable=False, unique=True)
    email = mapped_column(String(100), nullable=False, unique=True)
    password = mapped_column(String(100), nullable=False)
    address = mapped_column(String(100), nullable=False)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), onupdate=datetime.now)

    def __init__(self, user_id:str, shopname:str, email:str, password:str, address:str) -> None:
        self.id = str(uuid4())
        self.user_id = user_id
        self.shopname = shopname
        self.email = email
        self.password = pbkdf2_sha256.hash(password)
        self.address = address
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)
    def check_password(self, password):
        is_password_matching = False
        try:
            is_password_matching = pbkdf2_sha256.verify(password)
        except Exception as e:
            print(e)
        return(is_password_matching)
