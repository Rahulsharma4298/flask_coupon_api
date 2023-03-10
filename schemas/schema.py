from flask_marshmallow import Schema, Marshmallow
import app
from models.cart_item import CartItem
from models.order import Order
from models.cart import Cart
from models.order_item import OrderItem

ma = Marshmallow(app=app)


class UserSchema(Schema):
    class Meta:
        fields = ["id", "first_name", "last_name", "email"]


class CouponSchema(Schema):
    class Meta:
        fields = ["id", "name", "available_quantity", "denomination", "price"]


class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    coupon = ma.Nested(CouponSchema())

    class Meta:
        model = OrderItem


class OrderSchema(ma.SQLAlchemyAutoSchema):
    user = ma.Nested(UserSchema)
    order_items = ma.Nested(OrderItemSchema(many=True))

    class Meta:
        model = Order


class CartItemSchema(ma.SQLAlchemyAutoSchema):
    coupon = ma.Nested(CouponSchema())

    class Meta:
        model = CartItem


class CartSchema(ma.SQLAlchemyAutoSchema):
    cart_items = ma.Nested(CartItemSchema(many=True))

    class Meta:
        model = Cart



