a,b,c,d = map(int, input().split())

if b > c and d > a and c+d > a+b:
    a %= 2
    if c > 0 and d > 0 and a == 0:
        print('Valores aceitos')
else:
    print('Valores nao aceitos')