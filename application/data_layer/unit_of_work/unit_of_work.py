from application.data_layer import RealEstateDAO

class UnitOfWork(object):
    def __init__(self, session):
        self.session = session

    @property
    def real_estate_dao(self):
        return RealEstateDAO(self.session)
