
def max_sum_coverage(N, K, board):
    # Initialize a two-dimensional array to store the sums of the numbers in each row and column
    row_sums = [[0] * N for _ in range(N)]
    col_sums = [[0] * N for _ in range(N)]

    # Populate the row and column sums
    for i in range(N):
        for j in range(N):
            row_sums[i][j] = row_sums[i][j-1] + board[i][j]
            col_sums[i][j] = col_sums[i-1][j] + board[i][j]

    # Initialize a two-dimensional array to store the maximum sum possible with each domino in each position
    dp = [[0] * (N-1) for _ in range(K+1)]

    # Base case: no dominoes placed, maximum sum is 0
    dp[0][0] = 0

    # Populate the dp array using the recurrence relation
    for i in range(1, K+1):
        for j in range(N-1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + row_sums[i][j] + col_sums[i][j])

    # Return the maximum sum possible with K dominoes
    return dp[K][N-1]

