from sqlalchemy import create_engine,text

# dialect + DBapi:///:location db:
engine = create_engine("mysql+pymysql://root@127.0.0.1/corsosql?charset=utf8mb4")
with engine.connect() as conn:
    
    sql = text("SELECT cust_name, cust_email from customers")
    res = conn.execute(sql)
    print(res.all())