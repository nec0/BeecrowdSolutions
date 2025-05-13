entrada = input()
p1, c1, p2, c2 = entrada.split(" ")

if int(p1) * int(c1) < int(p2) * int(c2):
    print(1)
elif int(p1) * int(c1) > int(p2) * int(c2):
    print(-1)
else:
    print(0)
