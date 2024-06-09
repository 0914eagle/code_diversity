
def solve(p):
    n = len(p)
    a = [0] * n
    for i in range(n):
        a[i] = 1
        for j in range(i):
            if p[j] == i + 1:
                a[i] += 1
    return a

