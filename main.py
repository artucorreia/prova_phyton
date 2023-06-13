import sqlite3
import os
from functions.user_db import sign_up, sign_in, getUserId, verifyUserType
from menus.menu_fornecedor import menuFornecedor
from menus.menu_comprador import menuComprador

connection = sqlite3.connect('data-base')

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
            print('1 - Fornecedor\n2 - Comprador')
            userType = int(input("Digite a opção: "))
            os.system("cls")
            sign_up(connection, newName, newPassword, userType)
        elif option == 2:
            name = input("Usuário: ")
            password = input("Senha: ")
            verify = sign_in(connection, name, password)
            os.system("cls")
            if verify:
                verifyType = verifyUserType(connection, name, password) 
                if verifyType == 1: 
                    menuFornecedor(getUserId(connection, name))
                else:
                    menuComprador()
            else:
                print('Não foi possível conectar-se\nUsuário ou Senha incorretos')

main()