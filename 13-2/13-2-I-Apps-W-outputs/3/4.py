
def solve(a):
    n = len(a)
    if n == 1:
        return 1
    if a[0] == a[1]:
        return 2
    if a[n-1] == a[n-2]:
        return 2
    return 1

