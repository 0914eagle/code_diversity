
def solve(a, b):
    x = 1
    while True:
        if x * (x + 1) // 2 >= a:
            if x * (x + 1) // 2 == a and x * (2 * x + 1) // 2 == b:
                return x
            else:
                return -1
        x += 1

