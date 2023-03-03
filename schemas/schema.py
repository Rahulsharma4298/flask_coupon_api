from flask_marshmallow import Schema, Marshmallow
from app import app
from models.order import Order

ma = Marshmallow(app=app)


class UserSchema(Schema):
    class Meta:
        fields = ["id", "first_name", "last_name", "email"]


class CouponSchema(Schema):
    class Meta:
        fields = ["id", "name", "available_quantity", "denomination", "price"]


class OrderSchema(ma.SQLAlchemyAutoSchema):
    user = ma.Nested(UserSchema)
    coupons = ma.Nested(CouponSchema(many=True))
    class Meta:
        model = Order
