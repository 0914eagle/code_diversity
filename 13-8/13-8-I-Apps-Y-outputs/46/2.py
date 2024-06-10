
def solve(n, a):
    a.sort(reverse=True)
    b = a[:]
    for i in range(n):
        b[i] //= 2
    return sum(a), sum(b)

