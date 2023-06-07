from product_db import createNewProduct, deleteProduct, editProduct, searchProduct

def menu():
    option = 0
    while option != 5:
        print("1 - Cadastrar Produto\n2 - Alterar\n3 - Remover Produto\n4 - Buscar Produto\n5 - SAIR")
        option = int(input("Digite a opção: "))
        match option:
            case 1:
                createNewProduct()
            case 2:
                editProduct()
            case 3:
                deleteProduct()
            case 4:
                searchProduct()
            case 5:
                break
