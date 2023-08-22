
palavra_secreta = 'inteligencia'
frase = ''

while True:
    substring = input('Digite uma letra que possa ter na palavra secreta: ')
    
    #Se a letra digitada estiver na palavra secreta, a letra digitada
    #vai ser adicionada a variavel frase.
    if substring in palavra_secreta:
        frase += substring
    
    palavra_formada = ''
    i = 0
    #Enquanto o código continua, ele cai nesse FOR, onde a letra
    #vai percorrrer a palavra secreta, se ela estiver na variavel frase
    #ela vai acidionada a palavra formada. Seguindo a mesma lógica anterior
    #se não, será adicionado um '*'
    for letra_secreta in palavra_secreta:
        if letra_secreta in frase:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
        
    print(palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print('Conseguiu!')
        print(f'Você tentou {len(letra_secreta)} vezes')
        break