
def find_nearest_entrance(n, a, b):
    if b > 0:
        return (a + b - 1) % n + 1
    else:
        return (a + n + b) % n + 1

