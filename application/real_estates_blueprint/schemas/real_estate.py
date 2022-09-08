from marshmallow import Schema, fields, post_load
from application.real_estates_blueprint.view_models import RealEstate


class RealEstateRequestSchema(Schema):
    id = fields.Int(required=True)

    @post_load()
    def post_load(self, data, **kwargs):
        return RealEstate(**data)


class RealEstateResponseSchema(Schema):
    id = fields.Int()
    type = fields.Str()
    location = fields.Str()
