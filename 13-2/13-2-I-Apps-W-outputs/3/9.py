
def solve(a):
    n = len(a)
    if n == 1:
        return 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            return 1
    return 2

