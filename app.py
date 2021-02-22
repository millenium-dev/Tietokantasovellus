from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'redsfsfsfsfis'



import routes

