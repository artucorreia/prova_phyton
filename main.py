import sqlite3
import os
from functions.user_db import sign_up, sign_in, getUserId
from menu.menu import menu

user = sqlite3.connect('User')

option = 0

def main():
    global option
    while option != 3:
        print("1 - Cadastrar-se\n2 - Fazer login\n3 - Encerrar o Código\n")
        option = int(input("Digite a opção: "))
        os.system("cls")
        if option == 1:
            newName = input("Digite o novo usuário: ")
            newPassword = input("Digite a nova senha: ")
            os.system("cls")
            sign_up(user, newName, newPassword)
        elif option == 2:
            name = input("Usuário: ")
            password = input("Senha: ")
            verify = sign_in(user, name, password)
            if verify:
                os.system("cls")
                menu(getUserId(user, name))
            else:
                print('Não foi possível conectar-se\nUsuário ou Senha incorretos')

main()