
def solve(a):
    n = len(a)
    if n == 1:
        return "YES"
    if n == 2:
        if a[0] == a[1]:
            return "YES"
        else:
            return "NO"
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(a[i] - a[j]) <= 1:
                return "YES"
    return "NO"

