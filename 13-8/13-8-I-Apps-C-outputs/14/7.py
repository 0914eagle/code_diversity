
def solve(K, N):
    # Initialize a 2D array to store the results
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    # Initialize the first row and column of the array
    for i in range(K + 1):
        dp[0][i] = 1
    for i in range(N + 1):
        dp[i][0] = 1

    # Fill in the rest of the array using the recurrence relation
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            for k in range(1, j + 1):
                dp[i][j] += dp[i - 1][k - 1] * dp[i - 1][j - k]

    # Return the result modulo 998244353
    return [dp[N][i] % 998244353 for i in range(1, K + 1)]

