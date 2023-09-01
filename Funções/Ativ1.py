lista_de_numeros = []
while True:
    numeros = input('Digite alguns numeros(ou "parar" para encerrar): ')
    
    if numeros.lower() == 'parar':    
        break
    lista_de_numeros.append(numeros)
    
lista_de_numeros = list(map(int, lista_de_numeros))

def multiplicacao(*args):
    resultado = 1
    for numeros in range(len(args)):
        resultado *= args[numeros]
        
    return resultado

resultado = multiplicacao(*lista_de_numeros)
print(resultado)

def imparPar(x):
    if x % 2 == 0:
        #print(f'{x} é par')
        return 'par'
    else:
        #print(f'{x} é impar')
        return 'impar'

ativ = imparPar(resultado)
print(ativ)