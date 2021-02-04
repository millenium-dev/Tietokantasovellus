from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv



app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:qwerty123@localhost"
db = SQLAlchemy(app)
