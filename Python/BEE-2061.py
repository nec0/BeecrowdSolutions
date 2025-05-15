abasInicial, numeroAcoes = input().split()
abasAbertas = int(abasInicial)

i = 0
while i < int(numeroAcoes):
    acao = input()
    if acao == "fechou":
        abasAbertas += 1
    elif acao == "clicou":
        abasAbertas -= 1
    i += 1

    if abasAbertas < 0:
        break

print(int(abasAbertas))
