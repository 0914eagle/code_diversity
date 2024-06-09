
def expected_max(m, n):
    total = 0
    for i in range(1, m+1):
        total += i * combination(n, i) * (1/m)**i
    return total

def combination(n, r):
    if r == 0:
        return 1
    return fac(n) // (fac(r) * fac(n-r))

def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

