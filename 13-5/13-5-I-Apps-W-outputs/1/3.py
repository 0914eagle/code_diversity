
def get_max_deliciousness(X, Y, A, B, C, p, q, r):
    # Initialize a two-dimensional array to store the maximum deliciousness for each possible combination of eaten apples
    dp = [[0] * (Y + 1) for _ in range(X + 1)]

    # Initialize the first row and column of the array with the values of the apples
    for i in range(X + 1):
        dp[i][0] = p[i - 1] if i <= A else 0
    for j in range(Y + 1):
        dp[0][j] = q[j - 1] if j <= B else 0

    # Fill in the rest of the array using the recurrence relation
    for i in range(1, X + 1):
        for j in range(1, Y + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + r[i - 1 + j - 1])

    return dp[X][Y]

