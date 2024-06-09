
def solve(a, p):
    n = len(a)
    m = len(p)
    for i in range(m):
        for j in range(n-1):
            if a[p[i]+j] > a[p[i]+j+1]:
                return "NO"
    return "YES"

