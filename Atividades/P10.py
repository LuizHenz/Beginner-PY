n1, n2, n3, n4 = map(float, input().split())

media = (n1*2)+(n2*3)+(n3*4)+(n4*1)
media = media/10

if media >= 7.0:
    print(f'Media: {media:.1f}\nAluno aprovado.')
elif media < 5.0:
    print(f'Media: {media:.1f}\nAluno reprovado.')
else:
    print(f'Media: {media:.1f}\nAluno em exame.')
    nota_exame = float(input())
    nova_nota = (nota_exame+media)/2
    if nova_nota >= 5.0:
        print(f'Nota do exame: {nota_exame:.1f}\nAluno aprovado.\nMedia final: {nova_nota:.1f}')
    else:
        print(f'Nota do exame: {nota_exame:.1f}\nAluno reprovado.\nMedia final: {nova_nota:.1f}')