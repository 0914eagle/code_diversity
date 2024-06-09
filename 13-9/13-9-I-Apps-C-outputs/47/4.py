
def solve(a, b):
    x = 0
    while True:
        if (x * (x + a)) + (b * x) == 0:
            return x
        x += 0.000000001
    return -1

