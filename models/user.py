from database import db
from sqlalchemy import Column, Integer, String


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    hashed_pwd = Column(String)
    orders = db.relationship('Order', backref="user", lazy=True)


