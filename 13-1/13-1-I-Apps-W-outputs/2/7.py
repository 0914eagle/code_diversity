
def get_minimum_moves(s, t):
    n = len(s)
    if n != len(t):
        return -1
    
    # Initialize a matrix to store the results of subproblems
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Fill in the base cases
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill in the rest of the matrix
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][n]

