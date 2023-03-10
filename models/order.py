from database import db


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    order_total = db.Column(db.Float(precision=2))
    order_items = db.relationship('OrderItem', backref='orders')

