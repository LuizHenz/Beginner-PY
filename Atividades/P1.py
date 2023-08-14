num = 1
while num == 1:
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite o segundo numero: '))
    operador = input('Agora escolha um operador matematico: ')
    if operador == '+':
        print(numero1+numero2)
    elif operador == '-':
        print(numero1-numero2)
    elif operador == '*':
        print(numero1*numero2)
    elif operador == '/':
        print(numero1/numero2)
    else:
        print('Operador inexistente.')
    cont = input('Deseja continuar S/N?: ')
    if cont.upper() == 'N':
        break
