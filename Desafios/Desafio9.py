cpf = '09701739973'
nove_digitos = cpf[:9]
contador = 10

result = 0
for digito in nove_digitos:
    result += int(digito)*contador
    contador -= 1
primeiro_digito = (result * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(primeiro_digito)