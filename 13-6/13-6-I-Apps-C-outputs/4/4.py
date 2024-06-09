
def solve(n):
    if n == 1:
        return "YES"
    
    swaps = []
    for i in range(1, n):
        for j in range(i+1, n+1):
            swaps.append([i, j])
    
    return "YES" if len(set(swaps)) == n*(n-1)//2 else "NO"

