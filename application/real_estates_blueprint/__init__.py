from flask import Blueprint

APP_NAME = 'real-estates'
real_estate_blueprint = \
    Blueprint(APP_NAME, __name__, url_prefix=f"/{APP_NAME}")

import application.real_estates_blueprint.api
