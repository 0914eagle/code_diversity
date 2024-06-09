
def solve(T, n, a):
    b = []
    for i in range(n):
        b.append(a[i] // gcd(a[i], -a[0]))
    return b

