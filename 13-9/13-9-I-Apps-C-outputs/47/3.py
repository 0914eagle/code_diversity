
def solve(a, b):
    x = 0
    while True:
        if a * x ** 2 + b * x - x ** 3 == 0:
            return x
        x += 1
    return -1

