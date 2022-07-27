from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Jelena:1234@localhost/webcrawler'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class RealEstate(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(20), nullable=False)
    offer = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(200))
    quadrature = db.Column(db.Float)
    year_built = db.Column(db.String(20))
    land_area = db.Column(db.String(20))
    total_floors = db.Column(db.String(20))
    floor = db.Column(db.String(20))
    registered = db.Column(db.String(20))
    heating_type = db.Column(db.String(100))
    rooms = db.Column(db.String(20))
    toilets = db.Column(db.String(20))
    parking = db.Column(db.String(20))
    equipment = db.Column(db.String(500))


def insert_row(type, offer, location, quadrature, year_built, land_area, total_floors,
               floor, registered, heating_type, rooms, toilets, parking, equipment):
    row = RealEstate(type=type, offer=offer, location=location, quadrature=quadrature, year_built=year_built,
                     land_area=land_area, total_floors=total_floors, floor=floor, registered=registered,
                     heating_type=heating_type, rooms=rooms, toilets=toilets, parking=parking, equipment=equipment)
    db.session.add(row)
    db.session.commit()