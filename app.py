from flask import Flask, render_template, flash, request, redirect, url_for
from sqlalchemy import create_engine,text

app = Flask(__name__)
app.secret_key = "key"

URLpath = "mysql+pymysql://root@127.0.0.2/Marathon"

engine = create_engine(URLpath)


@app.route("/")
def index():
    with engine.connect() as conn:
        sql = text("SELECT id , nome , cognome , email from partecipants")
        result = conn.execute(sql)
        partecipants = result.all()
    nameSite = "Marathon";
    return render_template("home.html", nome=nameSite, partecipants=partecipants)

@app.route("/partecipants") #"/about-me"
def partecipants(): 
    engine = create_engine(URLpath)
    with engine.connect() as conn:
        sql = text("SELECT id , nome , cognome , email from partecipants")
        result = conn.execute(sql)
        partecipants = result.all()
    return render_template("partecipants.html", partecipants=partecipants)
 

@app.route('/subscribe', methods=['GET','POST']) 
def subscribe(): 
    if request.method == 'POST':
        try:
            nome = request.form.get("nome")
            cognome = request.form.get("cognome")
            email = request.form.get("email")       
            with engine.connect() as conn :
                sqlInsert = text("""
                                INSERT INTO partecipants (nome, cognome, email) 
                                VALUES (:nome, :cognome, :email)
                                """)
                conn.execute(sqlInsert, {
                    "nome":nome,
                    "cognome":cognome,
                    "email":email
                    })
                conn.commit()
            flash("Iscrizione completata con successo!")
            return redirect(url_for("partecipants"))
        except Exception as e:
            flash("Si è verificato un errore durante l'iscrizione: " + str(e))
            return redirect(url_for("subscribe"))
    return render_template("subscribe.html")


                
    