from flask import Flask, render_template, url_for
from sqlalchemy import create_engine,text
import random

app = Flask(__name__)

@app.route("/")
def index():

    engine = create_engine("mysql+pymysql://root@127.0.0.1/corsosql?charset=utf8mb4")
    with engine.connect() as conn:
        sql = text("SELECT cust_name, cust_email from customers")
        result = conn.execute(sql)
        clienti = result.all()

    rng = random.choice(["beppe","lorenzo", "mattia", "luca","ernesto"])
    return render_template("home.html", nome=rng, clienti=clienti)

@app.route("/about-me")
def about():
    return render_template("about-me.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")