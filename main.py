import sqlite3
from functions.user_db import sign_up, sign_in,display_users
from functions.menu import menu

user = sqlite3.connect('User')
product = sqlite3.connect('Product')

option = 0

def main():
    global option
    while option != 4:
        print("1 - Cadastra-se\n2 - Fazer login\n3 - exibir tudo\n4 - SAIR")
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