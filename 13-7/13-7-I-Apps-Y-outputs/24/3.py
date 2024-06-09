
def shortest_ladder(vault):
    # Initialize variables
    m, n = len(vault), len(vault[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Populate the first row and column of the dp table
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + vault[i - 1][0]
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + vault[0][j - 1]
    
    # Fill in the rest of the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + vault[i - 1][j - 1]
    
    # Return the shortest ladder length
    return dp[m][n]

