tipoChah = 1
entrada = input()
acertos = 0

a, b, c, d, e = input().split(" ")
print(a, b, c, d, e)

if entrada == a:
    acertos += 1
if entrada == b:
    acertos += 1
if entrada == c:
    acertos += 1
if entrada == d:
    acertos += 1
if entrada == e:
    acertos += 1

print(acertos)
