from flask_marshmallow import Schema


class UserSchema(Schema):
    class Meta:
        fields = ["id", "first_name", "last_name", "email", "hashed_pwd"]


class CouponSchema(Schema):
    class Meta:
        fields = ["id", "name", "available_quantity", "denomination", "price"]