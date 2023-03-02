from flask import Flask, jsonify, request
from database import db, DB_URI
from models.user import User
from models.coupon import Coupon
from schemas import schema
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db.init_app(app)

user_schema = schema.UserSchema()
coupon_schema = schema.CouponSchema()
coupons_schema = schema.CouponSchema(many=True)


@app.cli.command("db-create")
def create_db():
    db.create_all()
    print("Database Created")


@app.cli.command("db-drop")
def drop_db():
    db.drop_all()
    print("Database Dropped")


@app.cli.command("db-seed")
def seed_db():
    user = User(id=1,
                first_name="trevor",
                last_name="philips",
                email="tp@example.com",
                hashed_pwd="xyz")
    coupon = Coupon(id=1,
                    name="Dominos",
                    available_quantity=10,
                    denomination=300,
                    price=200)
    db.session.add(user)
    db.session.add(coupon)
    db.session.commit()
    print("Database seeded")


@app.route('/coupons', methods=["GET"])
def get_coupons():
    coupons = Coupon.query.all()
    return jsonify(coupons_schema.dump(coupons))


@app.route('/coupons/<int:coupon_id>', methods=["GET"])
def get_coupon(coupon_id: int):
    coupon = Coupon.query.get(coupon_id)
    if coupon:
        return jsonify(coupon_schema.dump(coupon))
    else:
        return jsonify({"msg": "coupon not found"}), 404


@app.route('/coupons', methods=["POST"])
def add_coupon():
    data = request.get_json()
    name = data.get("coupon_name")
    available_quantity = data.get("available_quantity")
    denomination = data.get("denomination")
    price = data.get("price")
    if not (name or available_quantity or denomination or price):
        return jsonify({"msg": "missing required fields"}), 400
    coupon = Coupon(id=None,
                    name=name,
                    available_quantity=available_quantity,
                    denomination=denomination,
                    price=price)
    db.session.add(coupon)
    db.session.commit()
    return jsonify({'msg': 'coupon added successfully', 'coupon': coupon_schema.dump(coupon)}), 201


@app.route('/auth/user/register', methods=["POST"])
def register_user():
    data = request.get_json()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    password = data.get("password")
    if not (first_name or last_name or email or password):
        return jsonify({"msg": "missing required fields"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"msg": f"user with email {email} already exists"}), 400
    user = User(first_name=first_name,
                last_name=last_name,
                email=email,
                hashed_pwd=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'user added successfully', 'id': user.id}), 201


@app.route("/auth/user/login", methods=["POST"])
def login_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    if not (email or password):
        return jsonify({"msg": "missing required fields"}), 400
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.hashed_pwd, password):
        return jsonify({"msg": "login successful", "id": user.id})
    else:
        return jsonify({"msg": "invalid email or password"}), 401


if __name__ == '__main__':
    app.run(debug=True)

