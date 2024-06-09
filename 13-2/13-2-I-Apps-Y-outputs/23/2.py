
def solve(a, p):
    n = len(a)
    m = len(p)
    for i in range(m):
        for j in range(i+1, m):
            if p[i] > p[j]:
                p[i], p[j] = p[j], p[i]
    for i in range(n-1):
        if a[i] > a[i+1]:
            return "NO"
    return "YES"

