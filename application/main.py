from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = "Secret key"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Abcd123$@localhost/webcrawler'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .routes import main, filter_data
    from .real_estates_blueprint import real_estate_blueprint

    app.register_blueprint(main)
    app.register_blueprint(filter_data)
    app.register_blueprint(real_estate_blueprint)

    return app
