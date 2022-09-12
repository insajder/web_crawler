from application.data_layer import RealEstate
from application import db

class RealEstateDAO(object):
    def __init__(self, session):
        self.session = session

    def get(self, id):
        real_estate = self.session.query(
            RealEstate
        ).filter(
            RealEstate.id == id
        ).one_or_none()
        return real_estate

    def get_filter(self, data):
        real_estates = self.session.query(RealEstate)
        if 'type' in data.keys() and data['type'] is not None:
            real_estates = real_estates.\
                filter(
                    RealEstate.type == data['type']
                )
        if 'min' in data.keys() and data['min'] is not None:
            real_estates = real_estates.\
                filter(
                    RealEstate.quadrature > float(data['min'])
                )
        if 'max' in data.keys() and data['max'] is not None:
            real_estates = real_estates.\
                filter(
                    RealEstate.quadrature < float(data['max'])
                )
        if 'parking' in data.keys():
            if data['parking'] == 'Da':
                real_estates = real_estates.\
                    filter(
                        RealEstate.parking == 'Da'
                    )
            elif data['parking'] == 'Ne':
                real_estates = real_estates.\
                    filter(
                        RealEstate.parking == 'Ne'
                    )
        return real_estates.all()

    def drop_real_estate(self):
        RealEstate.__table__.drop(db.engine)

    def create_real_estate(self):
        RealEstate.__table__.create(db.engine)

    def insert_row_real_estate(self, type, offer, location, quadrature, year_built, land_area, total_floors,
                   floor, registered, heating_type, rooms, toilets, parking, equipment):
        row = RealEstate(type=type, offer=offer, location=location, quadrature=quadrature, year_built=year_built,
                         land_area=land_area, total_floors=total_floors, floor=floor, registered=registered,
                         heating_type=heating_type, rooms=rooms, toilets=toilets, parking=parking, equipment=equipment)
        self.session.add(row)
        self.session.commit()
