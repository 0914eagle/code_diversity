
def expected_max_dots(m, n):
    total = 0
    for i in range(1, m+1):
        total += i * combination(n, i) * (1/m) ** i * (m-1)/m ** (n-i)
    return total

def combination(n, r):
    if r == 0:
        return 1
    return factorial(n) // (factorial(r) * factorial(n-r))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

