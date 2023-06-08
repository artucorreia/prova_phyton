import sqlite3

user = sqlite3.connect('User') 
userCursor = user.cursor()

userCursor.execute('''
          CREATE TABLE IF NOT EXISTS User(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name VARCHAR(50) UNIQUE,
            user_password VARCHAR(20)
          )
          ''')

user.commit()

product = sqlite3.connect('Product') 
productCursor = product.cursor()

productCursor.execute('''
          CREATE TABLE IF NOT EXISTS Product(
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR(30),
            product_value FLOAT,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES User(user_id)
          )
          ''')

product.commit()