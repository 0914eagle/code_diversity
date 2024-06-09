
def find_n(n_factorial):
    n = 1
    while n * n <= n_factorial:
        n += 1
    return n

