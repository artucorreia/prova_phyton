def createNewProduct(connection, name, value, quantity,foreignkeyUserId):
    cursor = connection.cursor()
    sql = 'INSERT INTO Product(product_name, product_value, product_quantity, product_user_id) VALUES (?, ?, ?, ?)'
    cursor.execute(sql, [name, value, quantity, foreignkeyUserId])
    connection.commit()
    return True

def checkPermission(connection, productId):
    cursor = connection.cursor()
    sql = 'SELECT product_user_id FROM Product WHERE product_id = ?'
    cursor.execute(sql, [productId])
    return cursor.fetchall()


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

def listUserProducts(connection):
    cursor = connection.cursor()
    sql = 'SELECT * FROM Product INNER JOIN User ON Product.product_user_id = User.user_id'
    cursor.execute(sql)
    return cursor.fetchall()

def listAllProducts(connection):
    cursor = connection.cursor()
    sql = 'SELECT * FROM Product INNER JOIN User ON Product.product_user_id = User.user_id'
    cursor.execute(sql)
    return cursor.fetchall()

def displayer(products, userId):
    for row in products:
        if userId == 0:
            print('==================')
            print('ID:', row[0])
            print('Nome:', row[1])
            print('Valor:', row[2])
            print('Quantidade:', row[3])
            print('Fornecedor:', row[6])
            print('==================')
        elif row[4] == userId:
            print('==================')
            print('ID:', row[0])
            print('Nome:', row[1])
            print('Valor:', row[2])
            print('Quantidade:', row[3])
            print('==================')

## compradores
def verifyProductsQuantity(connection):
    cursor = connection.cursor()
    sql = 'SELECT product_quantity FROM Product'
    cursor.execute(sql)
    return cursor.fetchall()

def getProductValue(connection, productId):
    cursor = connection.cursor()
    sql = 'SELECT product_value FROM Product WHERE product_id = ?'
    cursor.execute(sql, [productId])
    return cursor.fetchall()

def buyProducts(connection, productId, quantityTotal, quantity):
    cursor = connection.cursor()
    sql = 'UPDATE Product SET product_quantity = ? WHERE product_id = ?'
    cursor.execute(sql, [quantityTotal - quantity, productId])
    return cursor.fetchall()