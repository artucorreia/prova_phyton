def sign_up(user, name, password):
    userCursor = user.cursor()
    sql = f'INSERT INTO User(user_name, user_password) VALUES (?, ?)'
    userCursor.execute(sql, [name, password])
    user.commit()
    
    return True

def sign_in(userConection, name, password):
    userCursor = userConection.cursor()
    sql = 'select * from User where user_name LIKE ? and user_password LIKE ?'
    userCursor.execute(sql, [name, password])
    return userCursor.fetchall()

def display_users(userConection):
    userCursor = userConection.cursor()
    sql = 'select * from User'
    userCursor.execute(sql)
    return userCursor.fetchall()
