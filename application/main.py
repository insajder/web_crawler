from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import app, db

def create_app():
    db.init_app(app)

    # from .routes import main, filter_data
    from .real_estates_blueprint import real_estate_blueprint

    # app.register_blueprint(main)
    # app.register_blueprint(filter_data)
    app.register_blueprint(real_estate_blueprint)

    return app
