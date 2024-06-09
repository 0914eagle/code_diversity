
def solve(notes):
    n = len(notes)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 1
            elif j - i == 1:
                dp[i][j] = 2
            elif notes[i - 1] % 7 == notes[j - 1] % 7:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j] + 1)
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    return dp[1][n]

