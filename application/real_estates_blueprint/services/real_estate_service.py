from application.data_layer import uow

class RealEstateService(object):
    @staticmethod
    def get(id):
        return uow.real_estate_dao.get(id)

    @staticmethod
    def get_filter(data):
        return uow.real_estate_dao.get_filter(data)
