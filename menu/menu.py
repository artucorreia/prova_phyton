import sqlite3
from functions.product_db import createNewProduct, deleteProduct, editProduct, searchProduct, listAllProducts, displayer, checkPermission
import os

connection = sqlite3.connect('data-base')

def menu(userId):
    option = 0
    while option != 6:
        print("1 - Cadastrar Produto\n2 - Editar Produto\n3 - Remover Produto\n4 - Buscar Produto\n5 - Exibir todos os produtos\n6 - Voltar ao Início\n")
        option = int(input("Digite a opção: "))
        os.system("cls")
        match option:
            case 1:
                productName = input("Digite o nome do produto: ")
                productValue = float(input("Digite o valor do produto: "))
                createNewProduct(connection, productName, productValue, userId)
                os.system("cls")
            case 2:
                productId = int(input('Insira o ID do produto: '))
                opc = 0
                permission = (checkPermission(connection, productId)[0][0] == userId)
                if permission:
                    while(opc != 3):
                        os.system("cls")
                        displayer(searchProduct(connection, productId), userId)
                        print('1 - Mudar o nome do produto')
                        print('2 - Mudar o valor do produto')
                        print('3 - Voltar ao Menu\n')
                        opc = int(input('Digite a opção: '))
                        match opc:
                            case 1:
                                newName = input('Insira o novo nome: ')
                                editProduct(connection, newName, productId, opc)
                            case 2:
                                newValue = float(input('Insira o novo valor: ')) 
                                editProduct(connection, newValue, productId, opc)
                        os.system("cls")
                else:
                    os.system("cls")
                    print('Você não tem permissão para editar o produto de outro usuário')
            case 3:
                productId = int(input('Informe o ID do produto: '))
                permission = (checkPermission(connection, productId)[0][0] == userId)
                if permission:
                    deleteProduct(connection, productId)
                    os.system("cls")
                    print('Produto deletado com sucesso!')
                else:
                    os.system("cls")
                    print('Você não tem permissão para deletar o produto de outro usuário')
            case 4:
                productId = int(input('Informe o ID do produto: '))
                selectedProduct = searchProduct(connection, productId)
                os.system("cls")
                print(selectedProduct)
            case 5:
                allProducts = listAllProducts(connection)
                os.system("cls")
                displayer(allProducts, userId)
            case 6:
                break
