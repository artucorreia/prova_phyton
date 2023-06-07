import sqlite3

user = sqlite3.connect('User')
product = sqlite3.connect('Product')

option = 0

def main():
    global option
    print("1 - Cadastra-se\n2 - Fazer login\n3 - SAIR")
    option = int(input("Digite a opção: "))

main()