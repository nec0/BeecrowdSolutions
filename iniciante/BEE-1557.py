def CriaMatriz(linhas, colunas, valor):
    matriz = []
    for l in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz

while True:
    n = int(input())
    if n == 0:
        break

    #criando matriz com 0 e depois adicionando o que se pede
    matrizN = CriaMatriz(n, n, 0)
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                matrizN[i][j] = 1
            elif i == 0:
                matrizN[i][j] = (matrizN[i][j-1])*2
            else:
                matrizN[i][j] = (matrizN[i-1][j])*2

    #print saida; lê cada elemento e transforma-o em string, logo após
    max_caracteres = len(str(matrizN[n-1][n-1])) #numero maximo de caracteres, ultimo elemento
    for i in range(n):
        for j in range(n):
            matrizN[i][j] = str(matrizN[i][j])
            while len(matrizN[i][j]) < max_caracteres:
                matrizN[i][j] = ' ' + matrizN[i][j]

        saida = ' '.join(matrizN[i])
        print(saida)
    print()