
def solve(a):
    n = len(a)
    for i in range(n - 2):
        for j in range(i + 1, n):
            if a[i] == a[j] and a[i + 1] == a[j - 1]:
                return "YES"
    return "NO"

