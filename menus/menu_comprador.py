import sqlite3
import os
from functions.product_db import searchProduct, listAllProducts, displayer, buyProducts, verifyProductsQuantity, getProductValue


connection = sqlite3.connect('data-base')

def menuComprador():
    option = 0
    while option != 4:
        print("1 - Buscar Produto\n2 - Comprar Produto\n3 - Exibir todos os produtos\n4 - Voltar ao Início")
        option = int(input("Digite a opção: "))
        # os.system("cls")
        match option:
            case 1:
                productId = int(input('Informe o ID do produto: '))
                selectedProduct = searchProduct(connection, productId)
                # os.system("cls")
                print(selectedProduct)
            case 2:
                productId = int(input('Informe o ID do produto: '))
                quantity = int(input('Informe a quantidade: '))
                quantityTotal = verifyProductsQuantity(connection, quantity)
                if quantity > quantityTotal:
                    print('Não foi possível realizar a compra!\nInforme uma quantidade válida!')
                else:
                    productValue = getProductValue(productId)
                    print('Subtotal: ', productValue * quantity)
                    print('Deseja confirmar a compra?\n1 - SIM\n2 - NÃO')
                    answer = int(input('Digite a opção: '))
                    match answer:
                        case 1:
                            buyProducts(productId, quantityTotal, quantity)
                            print('Compra efetuada com sucesso!')
                        case 2: 
                            # os.system("cls")
                            print('Compra Cancelada')
                            menuComprador()
                
            case 3:
                allProducts = listAllProducts(connection)
                # os.system("cls")
                displayer(allProducts, 0)
            case 4:
                break