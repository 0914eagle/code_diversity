
def solve(n, k):
    count = 0
    for i in range(1, n+1):
        j = k - i
        if j > 0 and j <= n and i != j:
            count += 1
    return count

