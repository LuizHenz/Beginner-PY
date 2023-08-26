import os

lista = []

while True:
    opcao = input('Lista de compra, escolha uma opção\n1-Inserir\n2-Listar\n3-Deletar\n')
    os.system('clear')
    match int(opcao): #Usado para fazer um swich case em python, att da 3.11
        case 1:
            item = input('Inserir: ')
            if item.isdigit():
                print('Isso não é um item de compra.')
            else:
                lista.append(item)
        case 2:
            print('Itens na lista:')
            if len(lista) == 0:
                print('Lista vazia.')
            else:
                for indice, nome in enumerate(lista):
                    print(indice, nome)
        case 3:
            deletar = input('Intem para deletar: ')
            if deletar in lista:
                lista.remove(deletar)
                print(f'{deletar} deletado.')
            else:
                print('Item não existe.')
        case _:
            print('Opção inválida.')