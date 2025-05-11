teste = int(input())

for i in range(0, teste):
    numero = int(input())
    if numero == 1:
        print(1)
    else:
        if (numero % 2) == 0:
            print(0)
        else:
            print(1)