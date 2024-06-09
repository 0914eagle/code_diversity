
def solve(n, a):
    a = list(a)
    a[0] -= 1
    for i in range(1, n):
        if a[0] < a[i]:
            a[0] += 1
            a[i] -= 1
    return a[0]

