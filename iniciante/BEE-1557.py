def CriaMatriz(linhas, colunas, valor):
    matriz = []
    for l in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz

continuar = 1
while continuar == 1:
    n = int(input())
    if n == 0:
        continuar = 0

    matrizN = CriaMatriz(n, n, 0)
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                matrizN[i][j] = 1
            elif i == 0:
                matrizN[i][j] = (matrizN[i][j-1])*2
            else:
                matrizN[i][j] = (matrizN[i-1][j])*2
    print(matrizN)

    #formatar a saida