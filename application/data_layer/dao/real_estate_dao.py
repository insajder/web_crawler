from application.data_layer import RealEstate


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
