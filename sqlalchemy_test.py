from sqlalchemy import create_engine, text

DATABASE_URL = "mysql+pymysql://root:@127.0.0.1:3306/inven_db"

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM products"))

    for row in result:
        print(row)
