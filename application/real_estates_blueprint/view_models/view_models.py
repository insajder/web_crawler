class RealEstateViewModel:
    def __init__(self, **kwargs):
        if kwargs.get('id'):
            self.id = kwargs.get('id')
        else:
            self.type = kwargs.get('type')
            self.min = kwargs.get('min')
            self.max = kwargs.get('max')
            self.parking = kwargs.get('parking')
