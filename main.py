import sqlite3
# import os
from functions.user_db import sign_up, sign_in,display_users
from menu.menu import menu

user = sqlite3.connect('User')

option = 0

def main():
    global option
    while option != 4:
        print("1 - Cadastrar-se\n2 - Fazer login\n3 - Exibir tudo\n4 - Encerrar o Código\n")
        option = int(input("Digite a opção: "))
        if option == 1:
            newName = input("Digite o novo usuário: ")
            newPassword = input("Digite a nova senha: ")
            sign_up(user, newName, newPassword)
        elif option == 2:
            name = input("Usuário: ")
            password = input("Senha: ")
            verify = sign_in(user, name, password)
            if verify:
                menu()
        elif option == 3:
            users = display_users(user)
            print(users)

main()