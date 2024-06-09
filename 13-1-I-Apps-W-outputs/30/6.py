
def find_end_entrance(n, a, b):
    if b == 0:
        return a
    elif b > 0:
        return (a + b - 1) % n + 1
    else:
        return (a - b + n - 1) % n + 1

