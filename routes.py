from sqlalchemy import sql
from app import app
import random
from flask import render_template, request, redirect, session, flash
import messages, users
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

@app.route("/pankkipalvelut")
def accountcheck():
  username = session['username']
  sql = "SELECT COUNT(*)  FROM accounts WHERE username=:username"
  result = db.session.execute(sql,{"username":username})
  check = result.fetchone()[0]
  print(check)
  if check == 0:
    return render_template("tilinluonti.html")
  else:
    return render_template("pankkipalvelut.html")

@app.route("/tili", methods=["POST"])
def luotili():
    username = session['username']
    account_number = random.randint(1, 100000000)
    account_balance = 0
    sql = "SELECT id  FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user_id = result.fetchone()[0]
    print(user_id)
    sql = "INSERT INTO accounts (user_id,username,account_number,account_balance) VALUES (:user_id,:username,:account_number,:account_balance)"
    db.session.execute(sql, {"user_id":user_id,"username":username,"account_number":account_number,"account_balance":account_balance})
    db.session.commit()
    return redirect("/")

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

@app.route("/tehdyttalletukset")
def tehdyttalletukset():
    username = session['username']
    sql = "SELECT user_id  FROM accounts WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user_id = result.fetchone()[0]

    sqll = "SELECT account_number,sum,account_balance,sent_at  FROM deposits  WHERE user_id=:user_id ORDER BY sent_at DESC"
    result = db.session.execute(sqll, {"user_id": user_id})
    list = result.fetchall()

    sqll = "SELECT SUM(sum)  FROM deposits  WHERE user_id=:user_id"
    res = db.session.execute(sqll, {"user_id": user_id})
    sum = res.fetchall()[0][0]

    return render_template("tehdyttalletukset.html",list=list,sum=sum)


@app.route("/tilinsaldo")
def tilinsaldo():
    username = session['username']
    sql = "SELECT account_number  FROM accounts WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    account_number = result.fetchone()[0]
    sqlq = "SELECT account_balance  FROM accounts WHERE username=:username"
    result = db.session.execute(sqlq, {"username": username})
    account_balance = result.fetchone()[0]
    return render_template("tilinsaldo.html",account_number=account_number,account_balance=account_balance)

@app.route("/talletus")
def talletus():
    username = session['username']
    sql = "SELECT account_number  FROM accounts WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    account_number = result.fetchone()[0]
    sqlq = "SELECT account_balance  FROM accounts WHERE username=:username"
    result = db.session.execute(sqlq, {"username": username})
    account_balance = result.fetchone()[0]
    return render_template("talletus.html",account_number=account_number,account_balance=account_balance)


@app.route("/talletukset", methods=["POST"])
def talletukset():
    username = session['username']
    sql = "SELECT username,account_number,account_balance  FROM accounts WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    lista = result.fetchall()
    username = lista[0][0]
    account_number = lista[0][1]
    account_balancee = lista[0][2]
    sum = request.form["summa"]
    account_balance = int(sum) + int(account_balancee)
    message = "Summa joka yritettiin tallettaa oli suurempi kuin 100 000 Japanin yeniä"
    if int(sum) > 100000:
        return render_template("error.html",message=message)
    sql = "UPDATE accounts SET account_balance = :account_balance WHERE username = :username"
    db.session.execute(sql, {"account_balance": account_balance, "username":username})
    db.session.commit()
    transaction_type = 'talletus'
    sqll = "SELECT user_id FROM accounts WHERE username=:username"
    result = db.session.execute(sqll, {"username": username})
    user_id = result.fetchone()[0]
    print(user_id)
    sql = "INSERT INTO deposits (user_id,account_number,sum,account_balance,sent_at,transaction_type) VALUES (:user_id,:account_number,:sum,:account_balance,NOW(),:transaction_type)"
    db.session.execute(sql, {"user_id": user_id, "account_number": account_number,"sum":sum,
                             "account_balance": account_balance,"transaction_type":transaction_type})
    db.session.commit()
    return render_template("onnistunuttoiminto.html")

@app.route("/nosto")
def nosto():
    username = session['username']
    sql = "SELECT account_number  FROM accounts WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    account_number = result.fetchone()[0]
    sqlq = "SELECT account_balance  FROM accounts WHERE username=:username"
    result = db.session.execute(sqlq, {"username": username})
    account_balance = result.fetchone()[0]
    return render_template("nosto.html", account_number=account_number, account_balance=account_balance)

@app.route("/nostot", methods=["POST"])
def nostot():
    username = session['username']
    sql = "SELECT username,account_number,account_balance  FROM accounts WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    lista = result.fetchall()
    username = lista[0][0]
    account_number = lista[0][1]
    account_balancee = lista[0][2]
    sum = request.form["summa"]
    account_balance = int(account_balancee) - int(sum)
    message = "Tilillä ei ole riittävästi rahaa kyseisen kyseisen nostotoiminnon suorittamiseksi"
    if account_balance < 0:
        return render_template("error.html", message=message)
    sql = "UPDATE accounts SET account_balance = :account_balance WHERE username = :username"
    db.session.execute(sql, {"account_balance": account_balance, "username":username})
    db.session.commit()
    transaction_type = 'nosto'
    sqll = "SELECT user_id FROM accounts WHERE username=:username"
    result = db.session.execute(sqll, {"username": username})
    user_id = result.fetchone()[0]
    print(user_id)
    sql = "INSERT INTO withdrawals (account_number,sum,account_balance,sent_at,transaction_type) VALUES (:account_number,:sum,:account_balance,NOW(),:transaction_type)"
    db.session.execute(sql, {"account_number": account_number,"sum":sum,
                             "account_balance": account_balance,"transaction_type":transaction_type})
    db.session.commit()
    return render_template("onnistunuttoiminto.html")

@app.route("/siirto")
def siirto():
    username = session['username']
    sql = "SELECT account_number  FROM accounts WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    account_number = result.fetchone()[0]
    sqlq = "SELECT account_balance  FROM accounts WHERE username=:username"
    result = db.session.execute(sqlq, {"username": username})
    account_balance = result.fetchone()[0]
    return render_template("siirto.html", account_number=account_number, account_balance=account_balance)

@app.route("/siirrot", methods=["POST"])
def siirrot():
    message = "Tilillä ei ole riittävästi rahaa kyseisen kyseisen toiminnon suorittamiseksi"
    message2 = "Negatiivisen summan siirtäminen ei ole mahdollista"
    message3 = "Tilinumeroa ei ole olemassa"
    sum = request.form["summa"]
    tilinumero = request.form["tilinumero"]
    account_number = tilinumero
    if int(account_number) > 1000000:
        return render_template("error.html", message=message3)
    sql = "SELECT COUNT(*) FROM accounts WHERE account_number=:tilinumero"
    res = db.session.execute(sql, {"tilinumero": account_number})
    control = res.fetchone()[0]
    if control == 0:
        return render_template("error.html", message=message3)
    if int(sum) < 0:
        return render_template("error.html", message=message2)

    username = session['username']
    sql = "SELECT username,account_number,account_balance  FROM accounts WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    lista = result.fetchall()
    username = lista[0][0]
    account_number = lista[0][1]
    tilapäinen = lista[0][1]
    account_balancee = lista[0][2]
    account_balance = int(account_balancee) - int(sum)
    if account_balance < 0:
        return render_template("error.html", message=message)


    sql = "UPDATE accounts SET account_balance = :account_balance WHERE username = :username"
    db.session.execute(sql, {"account_balance": account_balance, "username":username})
    db.session.commit()


    account_number = tilinumero
    sqlll = "SELECT account_balance FROM accounts WHERE account_number=:account_number"
    result = db.session.execute(sqlll, {"account_number": account_number})
    tilinsaldo = result.fetchone()[0]
    tilinsaldok = int(tilinsaldo) + int(sum)
    account_balance = tilinsaldok
    print(account_number)

    sqk = "UPDATE accounts SET account_balance =:account_balance WHERE account_number=:account_number"
    db.session.execute(sqk,{"account_balance":account_balance, "account_number":account_number})
    db.session.commit()
    to_account = tilinumero
    transaction_type = 'siirto'
    account_number = tilapäinen

    sql = "INSERT INTO transfers (account_number,sum,to_account,sent_at,transaction_type) VALUES (:account_number,:sum,:to_account,NOW(),:transaction_type)"
    db.session.execute(sql, {"account_number": account_number,"sum":sum,"to_account":to_account,"transaction_type":transaction_type})
    db.session.commit()


    return render_template("onnistunuttoiminto.html")

@app.route("/palaute")
def new():
    return render_template("palaute.html")


@app.route("/tilihistoria")
def tilihistoria():
    username = session['username']
    sql = "SELECT account_number  FROM accounts WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    account_number = result.fetchone()[0]

    sqll = "SELECT account_number,sum,transaction_type,sent_at FROM transfers UNION ALL SELECT account_number,sum,transaction_type,sent_at FROM deposits UNION ALL SELECT account_number,sum,transaction_type,sent_at FROM withdrawals WHERE account_number=:account_number ORDER BY sent_at DESC;"
    result = db.session.execute(sqll, {"account_number": account_number})
    list = result.fetchall()
    print(list)

    sqll = "SELECT SUM(sum)  FROM deposits  WHERE account_number=:account_number"
    res = db.session.execute(sqll, {"account_number": account_number})
    deposits = res.fetchall()[0][0]

    sqll = "SELECT SUM(sum)  FROM transfers  WHERE account_number=:account_number"
    res = db.session.execute(sqll, {"account_number": account_number})
    transfers = res.fetchall()[0][0]

    sqll = "SELECT SUM(sum)  FROM withdrawals  WHERE account_number=:account_number"
    res = db.session.execute(sqll, {"account_number": account_number})
    withdrawals = res.fetchall()[0][0]

    return render_template("tilihistoria.html", list=list, deposits=deposits,transfers=transfers,withdrawals=withdrawals)


@app.route("/")
def etusivu():
    return render_template("index.html")


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