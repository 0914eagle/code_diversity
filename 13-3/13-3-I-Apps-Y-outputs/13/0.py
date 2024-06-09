
def solve(a, b):
    n = len(a)
    c = [0] * n
    for i in range(n):
        c[i] = (a[i] + b[i]) % n
    return c

