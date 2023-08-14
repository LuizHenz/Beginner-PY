frase = 'aaaaaooooooooooo'

quantidade_letras = 0
letra_vez = ''
i = 0
while i < len(frase):
    letra = frase[i]
    
    qtd = frase.count(letra)
    #.count É um metodo que retorna o número de elementos com o valor
    #especificado, aqui ele está contando quantas 'letra' tem na frase.

    if quantidade_letras < qtd:
        quantidade_letras = qtd
        letra_vez = letra
    #Esse IF basicamente é uma verificação de uma letra, na primeira
    #rodada do loop, ele vai cair no no IF pois a 'quantidade_letras'
    #é 0, então ele vai substituir ela já pela primeira letra que encontrar
    #então só vai cair no IF novamente quando a próxima letra tiver mais
    #quantidade que a que ocupou o 'quantidade_letras'
    
    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_vez}"')