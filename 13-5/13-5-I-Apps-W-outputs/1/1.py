
def get_max_deliciousness(x, y, a, b, c, p, q, r):
    # Initialize a 2D array to store the maximum deliciousness for each possible combination of red and green apples
    dp = [[0] * (b + 1) for _ in range(a + 1)]

    # Initialize the first row and column of the array with the deliciousness of the colorless apples
    for i in range(c + 1):
        dp[0][i] = r[i]
        dp[i][0] = 0

    # Fill in the rest of the array using the recurrence relation
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + p[i - 1] + q[j - 1])

    # Return the maximum deliciousness for the given combination of red and green apples
    return dp[x][y]

