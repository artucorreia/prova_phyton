import sqlite3
from functions.product_db import createNewProduct, deleteProduct, editProduct, searchProduct, listAllProducts

product = sqlite3.connect('Product')

def menu():
    option = 0
    while option != 6:
        print("1 - Cadastrar Produto\n2 - Editar Produto\n3 - Remover Produto\n4 - Buscar Produto\n5 - Exibir todos os produtos\n6 - Voltar ao Início\n")
        option = int(input("Digite a opção: "))
        match option:
            case 1:
                productName = input("Digite o nome do produto: ")
                productValue = float(input("Digite o valor do produto: "))
                createNewProduct(product, productName, productValue)
                
            case 2:
                productId = int(input('Insira o ID do produto: '))
                opc = 0
                while(opc != 3):
                    print('1 - Mudar o nome do produto')
                    print('2 - Mudar o valor do produto')
                    print('3 - Voltar ao Menu\n')
                    opc = int(input('Digite a opção: '))
                    match opc:
                        case 1:
                            newName = input('Insira o novo nome: ')
                            editProduct(product, newName, productId, opc)
                        case 2:
                            newValue = float(input('Insira o novo valor: ')) 
                            editProduct(product, newValue, productId, opc)
                            
            case 3:
                productId = int(input('Informe o ID do produto: '))
                deleteProduct(product, productId)
            case 4:
                productId = int(input('Informe o ID do produto: '))
                selectedProduct = searchProduct(product, productId)
                print(selectedProduct)
                
            case 5:
                allProducts = listAllProducts(product)
                print(allProducts)
            case 6:
                break
