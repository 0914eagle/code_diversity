
def can_reach_end(road, k):
    n = len(road)
    dp = [False] * (n + 1)
    dp[1] = True
    for i in range(1, n + 1):
        if dp[i]:
            for j in range(1, k + 1):
                if i + j <= n and road[i + j - 1] == ".":
                    dp[i + j] = True
    return dp[n]

