nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

nnome = len(nome.replace(" ",""))

if nome and idade:
    print(f'Seu nome e: {nome}')
    print(f'Seu nome invertido e: {nome[::-1]}')

    if " " in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome NÃO contem espaços')

    print(f'Seu nome tem: {nnome}')
    print(f'A primeira letra do seu nome: {nome[0]}')
    print(f'A primeira letra do seu nome: {nome[-1]}')
else:
    print('Voce deixou algum campo vazio')
