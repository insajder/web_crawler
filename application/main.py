from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = "Secret key"
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jelena:1234@localhost/postgres"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)

    db.init_app(app)

    from .real_estates_blueprint import real_estate_blueprint

    app.register_blueprint(real_estate_blueprint)

    return app
