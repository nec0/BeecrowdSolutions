x = input()
x = x.split(' ')

a = float(x[0])
b = float(x[1])

aumento = (b - a)
porcentagem = (aumento / a)*100

print(f'{porcentagem:0.2f}%')