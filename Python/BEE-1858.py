while True:
    try:
        quantidadeNomes = int(input())
        nomesAlgoz = input().split(" ")
        menorAlgoz = nomesAlgoz[0]
        posicaoAlgoz = 1

        i = 0
        while i < quantidadeNomes:
            if int(nomesAlgoz[i]) < int(menorAlgoz):
                menorAlgoz = nomesAlgoz[i]
                posicaoAlgoz = i + 1
            i += 1

        print(posicaoAlgoz)

    except EOFError:
        break