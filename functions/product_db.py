def createNewProduct(connection, name, value, foreignkeyUserId):
    cursor = connection.cursor()
    sql = 'INSERT INTO Product(product_name, product_value, product_user_id) VALUES (?, ?, ?)'
    cursor.execute(sql, [name, value, foreignkeyUserId])
    connection.commit()
    return True

def editProduct(connection, changes, productId, opc):    
    cursor = connection.cursor()
    match opc:
        case 1: 
            sql = 'UPDATE Product SET product_name = ? WHERE product_id= ?'
            cursor.execute(sql, [changes, productId])
        case 2: 
            sql = 'UPDATE Product SET product_value = ? WHERE product_id = ?'
            cursor.execute(sql, [changes, productId])
    connection.commit()

def deleteProduct(connection, productId):
    sql = 'DELETE FROM Product WHERE product_id = ?'
    cursor = connection.cursor()
    cursor.execute(sql, [productId])
    connection.commit()

def searchProduct(connection, productId):
    cursor = connection.cursor()
    sql = 'SELECT * FROM Product WHERE product_id = ?'
    cursor.execute(sql, [productId])
    return cursor.fetchall()

def listAllProducts(connection):
    cursor = connection.cursor()
    sql = 'SELECT * FROM Product INNER JOIN User ON Product.product_user_id = User.user_id'
    cursor.execute(sql)
    return cursor.fetchall()

def displayer(products, userId):
    for row in products:
        if row[3] == userId:
            print('==================')
            print('ID:', row[0])
            print('Nome:', row[1])
            print('Valor:', row[2])
            print('==================')