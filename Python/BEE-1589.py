numeroTestes = 1
quantidadeTestes = int(input())

while numeroTestes < quantidadeTestes:
    try:
        x = input().split(" ")
        raioConduite = int(x[0]) + int(x[1])
        print(raioConduite)
    except EOFError:
        break