import random

nove_validos = ''

for i in range(9):
    nove_validos = str(random.randint(0, 9))

print(nove_validos)
contador = 10
resultado = 0
for digito in nove_validos:
    resultado += int(digito)*contador
    contador -= 1
result = (resultado * 10) % 11
primeiro_digito = 0 if result > 9 else result


dez_validos = nove_validos + str(primeiro_digito)
contador_dois = 11
resultado_dois = 0
for digito in dez_validos:
    resultado_dois += int(digito)*contador_dois
    contador_dois -= 1
result_dois = (resultado_dois * 10) % 11
segundo_digito = 0 if result_dois > 9 else result_dois

cpf_validado = f'{nove_validos}{primeiro_digito}{segundo_digito}'
print(cpf_validado)

# if cpf_validado == cpf:
#     print(f'{cpf_validado} é valido.')
# else:
#     print('CPF inválido.')