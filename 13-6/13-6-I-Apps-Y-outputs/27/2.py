
def solve(n, k, d, a):
    snukes = [0] * (n + 1)
    for i in range(k):
        for j in range(d[i]):
            snukes[a[i][j]] += 1
    return sum(1 for i in range(1, n + 1) if snukes[i] == 0)

