cartas = input()
a, b = cartas.split(" ")

if int(a) == int(b):
    print(a)
elif int(a) > int(b):
    print(a)
else:
    print(b)
