import mysql.connector

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "crochetology"
}

# Create a connection
connection = mysql.connector.connect(**db_config)

# Example query
cursor = connection.cursor(dictionary=True)
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()
print(products)

cursor.close()
connection.close()
