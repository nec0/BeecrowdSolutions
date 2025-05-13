while True:
    try:
        entrada = input()
        if entrada == "0 0":
            break
        else:
            x, m = entrada.split(" ")

            experiencia = int(x) * int(m)
            print(experiencia)

    except EOFError:
        break