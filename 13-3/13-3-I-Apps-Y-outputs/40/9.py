
def solve(p):
    n = len(p)
    a = [0] * n
    for i in range(n):
        a[i] = 1
        for j in range(i+1, n):
            if p[i] == p[j]:
                a[i] += 1
        a[i] %= n
    return a
