from auto_app import db
from marshmallow import Schema, fields


class Auto(db.Model):
    __tablename__ = 'autos'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__}>: {self.brand} {self.model}'


class AutoSchema(Schema):
    id = fields.Integer()
    brand = fields.String()
    model = fields.String()
    year = fields.Integer()


auto_schema = AutoSchema()