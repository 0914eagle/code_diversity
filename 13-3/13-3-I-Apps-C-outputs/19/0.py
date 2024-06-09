
def longest_common_subsequence(s1, s2, virus):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j] and s1[i] not in virus:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return "".join(s1[i - 1] for i in range(m, 0, -1) if dp[i][n] > 0)

