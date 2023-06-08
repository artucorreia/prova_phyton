def sign_up(user, name, password):
    userCursor = user.cursor()
    sql = f'INSERT INTO User(user_name, user_password) VALUES (?, ?)'
    userCursor.execute(sql, [name, password])
    user.commit()
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
