a, b, c, d = [int(x) for x in input().strip().split(" ")]

def ehPossivel(a, b, c):
    return ((abs(b - c) < a < (b + c)) and (abs(a - c) < b < (a + c)) and (abs(a - b) < c < (a + b)))

teste = (ehPossivel(a, b, c) or
         ehPossivel(a, b, d) or
         ehPossivel(a, c, d) or
         ehPossivel(b, c, d))

print("S" if teste else "N")