
def solve(n, m, k, p):
    p.sort()
    max_sum = 0
    for i in range(n - m * k + 1):
        sum = 0
        for j in range(k):
            sum += sum(p[i + j * m:i + (j + 1) * m])
        max_sum = max(max_sum, sum)
    return max_sum

