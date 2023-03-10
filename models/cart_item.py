from database import db


class CartItem(db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coupon_id = db.Column(db.Integer, db.ForeignKey('coupons.id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    coupon = db.relationship('Coupon', backref='cart_items')
    quantity = db.Column(db.Integer, nullable=False, default=1)
