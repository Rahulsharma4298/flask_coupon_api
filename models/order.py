from database import db


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    order_total = db.Column(db.Float(precision=2))

    # many-to-many relation
    order_coupon_association = db.Table('order_coupon_association', db.Model.metadata,
                                        db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
                                        db.Column('coupon_id', db.Integer, db.ForeignKey('coupons.id'))
                                        )
    coupons = db.relationship('Coupon', secondary=order_coupon_association, backref='orders')


