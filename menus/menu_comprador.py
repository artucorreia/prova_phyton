import sqlite3
import os
from functions.product_db import searchProduct, listAllProducts, displayer, buyProduct, getProductQuantity, getProductValue

connection = sqlite3.connect('data-base')

def menuComprador():
    option = 0
    while option != 4:
        print("1 - Buscar Produto\n2 - Comprar Produto\n3 - Exibir todos os produtos\n4 - Voltar ao Início")
        option = int(input("Digite a opção: "))
        os.system("cls")
        match option:
            case 1:
                productId = int(input('Informe o ID do produto: '))
                selectedProduct = searchProduct(connection, productId)
                os.system("cls")
                if not selectedProduct:
                    print('Produto não encontrado!')
                else:
                    displayer(selectedProduct, 0)
                displayer(selectedProduct, 0)
            case 2:
                productId = int(input('Informe o ID do produto: '))
                quantity = int(input('Informe a quantidade: '))
                quantityTotal = getProductQuantity(connection, productId)
                if quantity > quantityTotal:
                    os.system("cls")
                    print('Não foi possível realizar a compra!\nInforme uma quantidade válida!')
                else:
                    productValue = getProductValue(connection, productId)
                    os.system("cls")
                    print('Subtotal: ', productValue * quantity)
                    print('Deseja confirmar a compra?\n1 - SIM\n2 - NÃO')
                    answer = int(input('Digite a opção: '))
                    match answer:
                        case 1:
                            buyProduct(connection, productId, quantityTotal, quantity)
                            os.system("cls")
                            print('Compra efetuada com sucesso!')
                        case 2: 
                            os.system("cls")
                            print('Compra Cancelada')
                menuComprador()
            case 3:
                allProducts = listAllProducts(connection)
                os.system("cls")
                displayer(allProducts, 0)