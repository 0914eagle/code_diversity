
def solve(a, b):
    while a > 0 and b > 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a == 0 and b == 0

