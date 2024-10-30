from sqlalchemy import create_engine,text

# dialect + DBapi:///:location db:
engine = create_engine("mysql+pymysql://root@127.0.0.2/Marathon")
with engine.connect() as conn:
    
    sql = text("SELECT id , nome , cognome , email from partecipants")
    res = conn.execute(sql)
    print(res.all())