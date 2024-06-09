
def solve(p):
    n = len(p)
    a = [0] * n
    for i in range(n):
        a[i] = p.index(i) + 1
    return a

