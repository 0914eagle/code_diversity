
def solve(m, n, p, q):
    if m < n or n <= 0 or p <= 0 or q <= 0:
        return "IMPOSSIBLE"
    
    num = 10 ** (m - n) * p
    while num % 10 != 0:
        num *= 10
    num //= 10
    
    if num % (10 ** n) == 0:
        return str(num)
    else:
        return "IMPOSSIBLE"

