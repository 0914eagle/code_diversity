
def solve(a):
    n = len(a)
    sum = 0
    for i in range(n):
        sum += a[i]
    if sum % 2 == 1:
        return "YES"
    else:
        return "NO"

