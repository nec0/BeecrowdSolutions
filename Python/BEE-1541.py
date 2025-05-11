while True:
    x = input()
    try:
        if x == "0":
            break
        else:
            a, b, c = x.split(" ")

            areaCasa = int(a) * int(b)
            areaTotalTerreno = (areaCasa * 100) / int(c)
            ladoTerreno = int(areaTotalTerreno ** (1/2))

            print(ladoTerreno)
    except EOFError:
        break