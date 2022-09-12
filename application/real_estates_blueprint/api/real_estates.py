from flask import request, jsonify
from application.real_estates_blueprint import real_estate_blueprint
from application.real_estates_blueprint.schemas import RealEstateRequestSchema, RealEstateRequestQueryParamsSchema, RealEstateResponseSchema
from application.real_estates_blueprint.services import RealEstateService

real_estate_request_schema = RealEstateRequestSchema()
real_estate_response_schema = RealEstateResponseSchema()
real_estates_request_schema = RealEstateRequestQueryParamsSchema()
real_estates_response_schema = RealEstateResponseSchema(many=True)

@real_estate_blueprint.get('/<int:id>')
def get_root_single(id):
    data = real_estate_request_schema.load(request.view_args).__dict__
    real_estate = RealEstateService.get(data['id'])
    return real_estate_response_schema.dump(real_estate)

@real_estate_blueprint.get('')
def get_filter():
    data = real_estates_request_schema.load(request.args).__dict__
    real_estates = RealEstateService.get_filter(data)
    return jsonify(real_estates_response_schema.dump(real_estates))
