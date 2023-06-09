def verifyUserName(connection, name):
    cursor = connection.cursor()
    sql = 'SELECT * FROM User WHERE user_name LIKE ?'
    cursor.execute(sql, [name])
    return cursor.fetchall()

def sign_up(connection, name, password):
    if not verifyUserName(connection, name):
        cursor = connection.cursor()
        sql = f'INSERT INTO User(user_name, user_password) VALUES (?, ?)'
        cursor.execute(sql, [name.upper(), password.upper()])
        connection.commit()
    else:
        print('Erro ao criar conta\nUsuário não disponível')
    return True

def sign_in(connection, name, password):
    cursor = connection.cursor()
    sql = 'SELECT * FROM User WHERE user_name LIKE ? and user_password LIKE ?'
    cursor.execute(sql, [name, password])
    return cursor.fetchall()

def display_users(connection):
    cursor = connection.cursor()
    sql = 'SELECT * FROM User'
    cursor.execute(sql)
    return cursor.fetchall()

def getUserId(connection, name):
    cursor = connection.cursor()
    sql = 'SELECT user_id FROM User WHERE user_name LIKE ?'
    cursor.execute(sql, [name])
    return cursor.fetchall()[0][0]