n = int(input())
listaNumeros = input().split(" ")
multiplo2 = 0
multiplo4 = 0
multiplo3 = 0
multiplo5 = 0

for i in listaNumeros:
    if (int(i) % 2) == 0:
        multiplo2 += 1
    if (int(i) % 3) == 0:
        multiplo3 += 1
    if (int(i) % 4) == 0:
        multiplo4 += 1
    if (int(i) % 5) == 0:
        multiplo5 += 1

print(f"{multiplo2} Multiplo(s) de 2")
print(f"{multiplo3} Multiplo(s) de 3")
print(f"{multiplo4} Multiplo(s) de 4")
print(f"{multiplo5} Multiplo(s) de 5")
