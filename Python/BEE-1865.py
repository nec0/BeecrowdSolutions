c = int(input())
contador = 0

while contador < c:
    tentativa = input().split(" ")
    nome = tentativa[0]
    forca = tentativa[1]

    if nome == "Thor":
        print("Y")
    else:
        print("N")
    contador += 1
