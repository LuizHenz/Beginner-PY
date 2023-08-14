import os

while True:
    num1 = input("Digite o primeiro numero: ")
    num2 = input("Digite o segundo numero: ")
    op = input("Digite o operador (+-/*): ")
    op_pm = '+-/*'
    num_1 = 0
    num_2 = 0
    numero = None

    os.system('clear') or None

    try:
        #Aqui ele vai tentar transformar as entradas para o tipo FLOAT.
        #Caso ocorra tudo bem, o 'numero' passara a valer TRUE.
        num_1 = float(num1)
        num_2 = float(num2)
        numero = True
    except:
        #Caso aconteça algum erro no TRY, ela vai cair aqui, então significa que
        #o que foi digitado, não era um numero, então 'numero' vai continuar como NONE.
        numero = None

    #Entao se 'numero' continuar como NONE, ele vai cair nessa primeira condição,
    #que se o valor de 'numero' ainda for none, ele não é um digito numeral, ou
    #se o operador for um caracter diferente do que foi dito na variavel 'op_pm'.
    if numero is None or op not in op_pm:
        print('Formato digitado incorreto.')
        continue
    #Aqui caso seja digitado mais de 1 operado, ele percorre o que foi digitado e 
    #verifica se foi digitado mais de 1 caracter.
    if len(op) > 1:
        print('Digite apenas UM operador.')
        continue
    
    if op == "+":
        print(num_1+num_2)
    elif op == "-":
        print(num_1-num_2)
    elif op == "/":
        print(num_1/num_2)
    elif op == "*":
        print(num_1*num_2)
    
    sair = input("Deseja sair? [s]im: ").lower().startswith('s')
    os.system('clear') or None
    if sair is True:
        os.system('clear') or None
        break