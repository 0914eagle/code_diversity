
def solve(a):
    n = len(a)
    if n == 1:
        return "NO"
    if n == 2:
        if a[0] + a[1] % 2 == 1:
            return "YES"
        else:
            return "NO"
    if n == 3:
        if a[0] + a[1] + a[2] % 2 == 1:
            return "YES"
        else:
            return "NO"
    if n == 4:
        if a[0] + a[1] + a[2] + a[3] % 2 == 1:
            return "YES"
        else:
            return "NO"
    return "NO"

