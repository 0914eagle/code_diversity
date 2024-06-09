
def solve(street, patterns):
    n = len(street)
    m = len(patterns)
    dp = [0] * (n + 1)
    for i in range(n):
        for j in range(m):
            if street[i] == patterns[j][0]:
                dp[i + 1] += 1
    for i in range(1, n + 1):
        for j in range(m):
            if i - len(patterns[j]) >= 0 and street[i - len(patterns[j])] == patterns[j][0]:
                dp[i] = max(dp[i], dp[i - len(patterns[j])] + 1)
    return n - dp[n]

