import sqlite3

connection = sqlite3.connect('data-base') 
cursor = connection.cursor()

cursor.execute('''
          CREATE TABLE IF NOT EXISTS User(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name VARCHAR(50) UNIQUE NOT NULL,
            user_password VARCHAR(20) NOT NULL
          )
          ''')

cursor.execute('''
          CREATE TABLE IF NOT EXISTS Product(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR(30) NOT NULL,
            product_value FLOAT NOT NULL,
            product_user_id INTEGER NOT NULL,
            FOREIGN KEY (product_user_id) REFERENCES User(user_id)
          )
          ''')

cursor.commit()