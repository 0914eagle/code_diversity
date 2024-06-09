
def longest_common_subsequence(s1, s2, virus):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1] and s1[i - 1] not in virus:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return "".join(s1[i - 1] for i in range(m, 0, -1) if dp[i][n] > 0)

