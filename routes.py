from sqlalchemy import sql

from app import app
from flask import render_template, request, redirect, session
import messages, users
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

@app.route("/pankkipalvelut")
def accountcheck():
  username = session["username"]
  sql = "SELECT COUNT(*)  FROM accounts WHERE username=:username"
  result = db.session.execute(sql,{"username":username})
  check = result.fetchone()[0]
  print(check)
  if check == 0:
    return render_template("error.html")
  else:
    return render_template("pankkipalvelut.html")

@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", count=len(list), messages=list)

@app.route("/financial")
def finance():
    return render_template("financial.html")

@app.route("/restaurant")
def restaurant():
    return render_template("restaurant.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/asiakaspalvelu")
def asiakaspalvelu():
    return render_template("asiakaspalvelu.html")

@app.route("/palaute")
def new():
    return render_template("palaute.html")


@app.route("/lähetys", methods=["post"])
def send():
    palaute = request.form["palautesisältö"]
    if messages.send(palaute):
        return redirect("/")
    else:
        return render_template("error.html",message="Viestin lähetys ei onnistunut")

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")

@app.route("/testing")
def test():
    sql = "SELECT content FROM feedback"
    result = db.session.execute(sql)
    data = result.fetchall()
    return render_template("test.html", result=data)