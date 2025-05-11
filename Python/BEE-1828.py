entradas = int(input())

i = 1
while not i == (entradas + 1):
    escolhas = input()
    sheldon, raj = escolhas.split(" ")

    if sheldon == raj:
        print(f"Caso #{i}: De novo!")

    elif sheldon == "pedra":
        if raj == "lagarto":
            print(f"Caso #{i}: Bazinga!")
        elif raj == "tesoura":
            print(f"Caso #{i}: Bazinga!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    elif sheldon == "papel":
        if raj == "pedra":
            print(f"Caso #{i}: Bazinga!")
        elif raj == "Spock":
            print(f"Caso #{i}: Bazinga!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    elif sheldon == "tesoura":
        if raj == "papel":
            print(f"Caso #{i}: Bazinga!")
        elif raj == "lagarto":
            print(f"Caso #{i}: Bazinga!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    elif sheldon == "lagarto":
        if raj == "Spock":
            print(f"Caso #{i}: Bazinga!")
        elif raj == "papel":
            print(f"Caso #{i}: Bazinga!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    elif sheldon == "Spock":
        if raj == "tesoura":
            print(f"Caso #{i}: Bazinga!")
        elif raj == "pedra":
            print(f"Caso #{i}: Bazinga!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")

    i += 1