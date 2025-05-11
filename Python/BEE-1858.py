while True:
    try:
        quantidadeNomes = int(input())
        nomesProvavelAlgoz = input().split(" ")
        menorProvavelAlgoz = 0
        posicaoAlgoz = 0

        i = 0
        while i < quantidadeNomes:
            if int(nomesProvavelAlgoz[i]) <= int(menorChute):
                menorChute = nomesProvavelAlgoz[i]
                posicaoMenorChute = i
            i += 1

        print(posicaoMenorChute + 1)

    except EOFError:
        break