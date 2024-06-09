
def solve(n, m):
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i**2 + j**2) % m == 0:
                count += 1
    return count

