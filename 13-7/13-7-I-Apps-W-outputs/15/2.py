
def solve(k, n):
    if n < k:
        return 0
    
    count = 0
    while n > 0:
        count += 1
        n //= 10
    
    return count

