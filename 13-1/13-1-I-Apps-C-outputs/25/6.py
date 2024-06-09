
def solve(a, b):
    x = 0
    while True:
        if (x * (x + 1)) % (2 * a) == b:
            return x
        x += 1
    return -1

