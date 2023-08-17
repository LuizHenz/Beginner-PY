a,b,c = map(float, input().split())


try:
    delta = (b ** 2) -4 * a * c
    if delta < 0:
        print("Impossivel calcular")
    else:
        r1 = (-b + delta ** (1 / 2)) / (2 * a)
        r2 = (-b - delta ** (1 / 2)) / (2 * a)

        print(f"R1 = {r1:.5f}\nR2 = {r2:.5f}")
except:
    print("Impossivel calcular")