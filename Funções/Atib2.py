a, b, c = map(int, input('Digite 3 multiplicadores: ').split())

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(a)
triplicar = criar_multiplicador(b)
quadruplicar = criar_multiplicador(c)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))