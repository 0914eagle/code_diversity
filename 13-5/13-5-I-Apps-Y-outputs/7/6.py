
def solve(a):
    n = len(a)
    for i in range(n-1):
        if a[i] == a[i+1]:
            return "YES"
    return "NO"

