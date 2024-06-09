
def solve(street, patterns):
    n = len(street)
    m = len(patterns)
    dp = [0] * (n + 1)
    for i in range(m):
        for j in range(n - len(patterns[i]) + 1):
            if street[j:j+len(patterns[i])] == patterns[i]:
                dp[j+len(patterns[i])] = max(dp[j+len(patterns[i])], dp[j] + 1)
    return n - dp[n]

