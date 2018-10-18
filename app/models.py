from app import db

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    city = db.Column(db.String(64))

    def __repr__(self):
        return '<Shop {}>'.format(self.name)

class Donut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    topping = db.Column(db.String(64))
    price = db.Column(db.Integer)

    def __repr__(self):
        return '<Donut {}>'.format(self.name)
        
class Shop_donut(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'))
    donut_id = db.Column(db.Integer, db.ForeignKey('donut.id'))

    def __repr__(self):
        return '<Shop_donut {}>'.format(self.id)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    favorite_donut = db.Column(db.Integer, db.ForeignKey('donut.id'))
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username) 




