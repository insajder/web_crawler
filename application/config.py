from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jelena:1234@localhost/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
