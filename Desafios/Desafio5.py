
palavra_secreta = 'inteligencia'
frase = ''
limite = 0

while True:
    substring = input('Digite uma letra que possa ter na palavra secreta: ')
    
    if substring in palavra_secreta:
        frase += substring
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in frase:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print('Conseguiu!')
        break