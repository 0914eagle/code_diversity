
def solve(K, N):
    # Initialize a 2D array to store the number of combinations for each i and j
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    # Initialize the base cases
    for i in range(1, K + 1):
        dp[i][i] = 1

    # Fill in the rest of the 2D array using the recurrence relation
    for i in range(2, K + 1):
        for j in range(1, K + 1):
            if i == j:
                continue
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    # Return the answer modulo 998244353
    return [dp[i][i] % 998244353 for i in range(1, 2 * K)]

