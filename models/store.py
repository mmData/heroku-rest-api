from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    #with lazy = 'dynamics, items is no longer a list of itemes, it's just a query builder. This avoids performing expensive operations when not needed
    items = db.relationship('ItemModel', lazy ='dynamic') #This will be a list of ItemsModel, because for each store there are many items

    def __init__(self, name):
        self.name = name
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()] }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #This is an SQL query This returns an ItemModel objet

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()