import math

continuar = 1
while continuar != 0:
    a, b, c = input().split(" ")
    a = int(a)
    b = int(b)
    c = int(c)

    if a == 0 or b == 0 or c == 0:
        continuar = 0

    else:
        area_da_casa = a * b
        lado_minimo_casa = math.sqrt(area_da_casa)
        lado_minimo_terreno =  lado_minimo_casa * 100 // c

        print(lado_minimo_terreno)
        continuar = 1