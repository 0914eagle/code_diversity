
def solve(K, N):
    # Initialize a 2D array to store the results
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    # Initialize the first row and column with 1
    for i in range(K + 1):
        dp[0][i] = 1
        dp[i][0] = 1

    # Fill in the rest of the 2D array using the recurrence relation
    for i in range(1, K + 1):
        for j in range(1, K + 1):
            for k in range(1, K + 1):
                if i != j and i != k and j != k:
                    dp[i][j] += dp[i - 1][k]

    # Return the results
    return [dp[i][K] for i in range(1, 2 * K)]

