import pymysql

connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="inven_db",
    port=3306
)

print("Connected to MySQL!")

cursor = connection.cursor()

cursor.execute("""
    INSERT INTO products (name, quantity, price)
    VALUES ('Mouse', 50, 800.00)
""")

connection.commit()

print("Product inserted!")

cursor.execute("SELECT * FROM products")

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
