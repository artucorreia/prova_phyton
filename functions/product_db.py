def createNewProduct(productConnection, name, value):
    productCursor = productConnection.cursor()
    sql = f'INSERT INTO Product(product_name, product_value) VALUES (?, ?)'
    productCursor.execute(sql, [name, value])
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
    sql = 'SELECT * FROM Product'
    productCursor.execute(sql)
    return productCursor.fetchall()
    
