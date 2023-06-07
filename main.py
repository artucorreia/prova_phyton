import sqlite3
from func.user_db import sign_up, sign_in,display_users

user = sqlite3.connect('User')
product = sqlite3.connect('Product')

option = 0

def main():
    global option
    print("1 - Cadastra-se\n2 - Fazer login\n3 - exibir tudo")
    option = int(input("Digite a opção: "))
    if option == 1:
        newName = input("Digite o novo usuário: ")
        newPassword = input("Digite a nova senha: ")
        sign_up(user, newName, newPassword)
        main()
    elif option == 2:
        name = input("Usuário: ")
        password = input("Senha: ")
        test = sign_in(user, name, password)
        print(test)
    elif option == 3:
        users = display_users(user)
        print(users)
        main()

main()