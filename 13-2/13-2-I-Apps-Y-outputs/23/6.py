
def solve(a, p):
    n = len(a)
    m = len(p)
    for i in range(m):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return "YES" if a == sorted(a) else "NO"

