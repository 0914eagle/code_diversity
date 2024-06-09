
def get_max_deliciousness(x, y, a, b, c, p, q, r):
    # Initialize a 2D array to store the maximum deliciousness for each combination of apples eaten
    dp = [[0] * (x + 1) for _ in range(y + 1)]

    # Initialize the first row and column of the array with the deliciousness of the apples
    for i in range(x + 1):
        dp[0][i] = p[i]
    for j in range(y + 1):
        dp[j][0] = q[j]

    # Fill in the rest of the array using the recurrence relation
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + r[i - 1] + q[j - 1])

    # Return the maximum deliciousness
    return dp[x][y]

