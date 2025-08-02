a, b = [int(x) for x in input().split(" ")]

# A beleza do Python é que seus operadores // e %
# já foram projetados para funcionar de uma forma que
# satisfaz a definição de divisão euclidiana onde o
# resto é não-negativo, desde que o divisor seja positivo.

if b < 0:
    b = -b

    q = a // b
    r = a % b

    q = -q
else:
    q = a // b
    r = a % b

print(q, r)
