
def get_min_edits(s):
    # Initialize variables
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j

    # Fill in the table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == "L" or s[i - 1] == "R":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
            elif s[i - 1] == "U" or s[i - 1] == "D":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    # Return the result
    return dp[n][n]

