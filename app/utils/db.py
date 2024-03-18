from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base

class Base(declarative_base):
    pass

db = SQLAlchemy(model_class=Base)
