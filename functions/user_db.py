def verifyUserName(userConnection, name):
    userCursor = userConnection.cursor()
    sql = 'SELECT * FROM User WHERE user_name LIKE ?'
    userCursor.execute(sql, [name])
    return userCursor.fetchall()

def sign_up(userConnection, name, password):
    if not verifyUserName(userConnection, name):
        userCursor = userConnection.cursor()
        sql = f'INSERT INTO User(user_name, user_password) VALUES (?, ?)'
        userCursor.execute(sql, [name.upper(), password.upper()])
        userConnection.commit()
    else:
        print('Erro ao criar conta\nUsuário não disponível')
    return True

def sign_in(userConnection, name, password):
    userCursor = userConnection.cursor()
    sql = 'SELECT * FROM User WHERE user_name LIKE ? and user_password LIKE ?'
    userCursor.execute(sql, [name, password])
    return userCursor.fetchall()

def display_users(userConnection):
    userCursor = userConnection.cursor()
    sql = 'SELECT * FROM User'
    userCursor.execute(sql)
    return userCursor.fetchall()

def getUserId(userConnection, name):
    userCursor = userConnection.cursor()
    sql = 'SELECT user_id FROM User WHERE user_name LIKE ?'
    userCursor.execute(sql, [name])
    return userCursor.fetchall()[0][0]