def createNewProduct(productConnection, name, value, foreignkeyUserId):
    productCursor = productConnection.cursor()
    sql = f'INSERT INTO Product(product_name, product_value, user_id) VALUES (?, ?, ?)'
    productCursor.execute(sql, [name, value, foreignkeyUserId])
    productConnection.commit()
    return True

def editProduct(productConnection, changes, productId, opc):    
    productCursor = productConnection.cursor()
    match opc:
        case 1: 
            sql = 'UPDATE product SET product_name = ? WHERE product_id= ?'
            productCursor.execute(sql, [changes, productId])
        case 2: 
            sql = 'UPDATE product SET product_value = ? WHERE product_id = ?'
            productCursor.execute(sql, [changes, productId])
    productConnection.commit()

def deleteProduct(productConnection, productId):
    sql = 'DELETE FROM Product WHERE product_id = ?'
    productCursor = productConnection.cursor()
    productCursor.execute(sql, [productId])
    productConnection.commit()

def searchProduct(productConnection, productId):
    productCursor = productConnection.cursor()
    sql = 'SELECT * FROM Product WHERE product_id = ?'
    productCursor.execute(sql, [productId])
    return productCursor.fetchall()

def listAllProducts(productConnection):
    productCursor = productConnection.cursor()
    # userConnection = userConnection.cursor()
    # sql = 'SELECT * FROM User INNER JOIN Product ON User.user_id = Product.user_id'
    sql = 'SELECT product_id, product_name, product_name, user_name FROM Product INNER JOIN User ON Product.user_id = User.user_id'
    productCursor.execute(sql)
    return productCursor.fetchall()