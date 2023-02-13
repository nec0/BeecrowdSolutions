x = input()
x = x.split(' ')

for i in range(0, len(x)):
    if x[i] == '1':
        print(i+1)