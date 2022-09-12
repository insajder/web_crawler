class RealEstateViewModel:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')

class RealEstateQueryParamsViewModel:
    def __init__(self, **kwargs):
        self.type = kwargs.get('type')
        self.min = kwargs.get('min')
        self.max = kwargs.get('max')
        self.parking = kwargs.get('parking')