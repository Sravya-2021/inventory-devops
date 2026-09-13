import pymysql

connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="inven_db",
    port=3306
)

cursor = connection.cursor()

# CREATE
cursor.execute("""
    INSERT INTO products (name, quantity, price)
    VALUES ('Monitor', 10, 15000.00)
""")
connection.commit()

print("After INSERT:")
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)

# UPDATE
cursor.execute("""
    UPDATE products
    SET quantity = 20
    WHERE name = 'Monitor'
""")
connection.commit()

print("\nAfter UPDATE:")
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
