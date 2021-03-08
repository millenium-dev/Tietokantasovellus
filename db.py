from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv


app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://foxvipfhigsqsn:0a29a72342fbe018656388d286131ab750294f19e1d5a2af4e1a6daedcf281f5@ec2-54-163-140-104.compute-1.amazonaws.com:5432/d11bng82tkrb0c"
db = SQLAlchemy(app)
