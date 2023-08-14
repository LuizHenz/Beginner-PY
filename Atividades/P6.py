a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a > b and a > c :
    print(f'{a} eh maior')
elif b > a and b > c:
    print(f'{b} eh maior')
else:
    print(f'{c} eh maior')