from application import db

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
