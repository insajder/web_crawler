from flask import request
from application.real_estates_blueprint import real_estate_blueprint
from application.real_estates_blueprint.schemas import RealEstateRequestSchema, RealEstateResponseSchema
from application.real_estates_blueprint.services import RealEstateService

real_estate_request_schema = RealEstateRequestSchema()
real_estate_response_schema = RealEstateResponseSchema()


@real_estate_blueprint.get('/<int:id>')
def get_root_single(id):
    # data = real_estate_request_schema.load(request.args.to_dict())
    real_estate = RealEstateService.get(id)
    return real_estate_response_schema.dump(real_estate)
