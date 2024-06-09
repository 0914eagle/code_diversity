
def solve(a):
    n = len(a)
    if n < 2:
        return "Yes"
    for i in range(n-1):
        if a[i] * a[i+1] % 4 != 0:
            return "No"
    return "Yes"

