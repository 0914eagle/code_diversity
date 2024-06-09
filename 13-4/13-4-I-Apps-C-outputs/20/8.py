
def solve(m, n, p, q):
    if m < n or n < 1 or p < 1 or q < 1:
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

