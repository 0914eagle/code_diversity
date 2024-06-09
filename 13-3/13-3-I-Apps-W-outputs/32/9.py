
def solve(b, c):
    n = len(b) + 1
    a = [0] * n
    for i in range(n):
        a[i] = b[i] + c[i]
    return a

