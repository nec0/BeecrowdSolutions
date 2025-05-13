entrada = input()
diasPeriodo, saldoInicioConta = entrada.split(" ")

saldoConta = int(saldoInicioConta)
menorSaldoConta = int(saldoInicioConta)

contador = 0
while contador < int(diasPeriodo):
    movimentacoesConta = input()
    saldoConta += int(movimentacoesConta)

    if saldoConta < menorSaldoConta:
        menorSaldoConta = saldoConta
    contador += 1

print(menorSaldoConta)
