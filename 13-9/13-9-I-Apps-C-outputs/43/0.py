
def solve(a, b, p):
    n = len(a)
    m = len(b)
    count = 0
    for i in range(n - m + 1):
        if a[i:i+m] == b:
            count += 1
    return count

