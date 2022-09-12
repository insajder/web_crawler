from marshmallow import Schema, fields, post_load, validates
from application.real_estates_blueprint.view_models import RealEstateViewModel


class RealEstateRequestSchema(Schema):
    id = fields.Int(required=True)

    @post_load()
    def post_load(self, data, **kwargs):
        return RealEstateViewModel(**data)

class RealEstateRequestQueryParamsSchema(Schema):
    type = fields.Str()
    min = fields.Float()
    max = fields.Float()
    parking = fields.Str()

    @post_load()
    def post_load(self, data, **kwargs):
        return RealEstateViewModel(**data)

class RealEstateResponseSchema(Schema):
    id = fields.Int()
    type = fields.Str()
    offer = fields.Str()
    location = fields.Str()
    quadrature = fields.Str()
    year_built = fields.Float()
    land_area = fields.Str()
    total_floors = fields.Str()
    floor = fields.Str()
    registered = fields.Str()
    heating_type = fields.Str()
    rooms = fields.Str()
    toilets = fields.Str()
    parking = fields.Str()
    equipment = fields.Str()
