from database import db
from sqlalchemy import Column, Integer, String


class Coupon(db.Model):
    __tablename__ = "coupons"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("coupon_name", String)
    available_quantity = Column(Integer)
    denomination = Column(Integer)
    price = Column(Integer)


