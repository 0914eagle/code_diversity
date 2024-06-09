
def solve(m, n, p, q):
    if m < n or m > 1000000 or n > 1000000 or p > 1000000 or q > 1000000:
        return "IMPOSSIBLE"
    
    num = 1
    for i in range(m):
        num *= 10
        num += i + 1
    
    for i in range(n):
        num //= 10
    
    num *= 10
    num += p
    num *= q
    
    if num % 10 != 0:
        return "IMPOSSIBLE"
    
    return str(num // 10)

