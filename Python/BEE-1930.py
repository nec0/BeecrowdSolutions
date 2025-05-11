x = input()
x = x.split(' ')
tomadas = 0

for i in x:
    tomadas += int(i)

print(tomadas - 3)
