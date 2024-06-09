
def solve(m, n, p, q):
    if m < n or m > 1000000 or n > 1000000 or p > 1000000 or q > 1000000:
        return "IMPOSSIBLE"
    
    num = 10**(m-n) * p * q
    while num % 10 != 0:
        num //= 10
    
    if num % 10 == 0:
        return "IMPOSSIBLE"
    
    return str(num)

