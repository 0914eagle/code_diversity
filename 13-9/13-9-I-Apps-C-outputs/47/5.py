
def solve(a, b):
    x = 0
    while True:
        if x * (2 * x + 1) >= a and x * (x + 1) >= b:
            return x
        x += 1
    return -1

