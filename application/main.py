from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .routes import main, filter_data

def create_app():
    app = Flask(__name__)
    app.secret_key = "Secret key"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Jelena:1234@localhost/webcrawler'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy()

    db.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(filter_data)

    return app
