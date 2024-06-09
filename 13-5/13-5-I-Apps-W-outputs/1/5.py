
def get_max_deliciousness(x, y, a, b, c, p, q, r):
    # Initialize a 2D array to store the maximum deliciousness for each combination of apples eaten
    dp = [[0] * (a + 1) for _ in range(b + 1)]

    # Initialize the first row and column of the array with the deliciousness of the apples
    for i in range(a + 1):
        dp[0][i] = p[i - 1]
    for j in range(b + 1):
        dp[j][0] = q[j - 1]

    # Fill in the rest of the array using the recurrence relation
    for i in range(1, b + 1):
        for j in range(1, a + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + r[j - 1])

    # Return the maximum deliciousness for the given number of red and green apples
    return dp[b][a]

