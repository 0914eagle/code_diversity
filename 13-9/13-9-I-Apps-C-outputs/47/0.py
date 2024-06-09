
def find_x(a, b):
    x = 0
    while True:
        if a == x and b == 0:
            return x
        if a == 2 * x and b == 0:
            return 2 * x
        if a == 3 * x and b == x:
            return 3 * x
        if a == 4 * x and b == 0:
            return 4 * x
        x += 1
    return -1

