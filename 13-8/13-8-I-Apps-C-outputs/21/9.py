
def max_sum_coverage(N, K, board):
    # Initialize a 2D array to store the sums of the numbers in each row
    sums = [[0] * 3 for _ in range(N)]
    for i in range(N):
        for j in range(3):
            sums[i][j] = sums[i][j-1] + board[i][j]
    
    # Initialize a 2D array to store the maximum sum possible with K dominoes
    dp = [[0] * (K+1) for _ in range(N+1)]
    
    # Base case: no dominoes can be placed on the first row
    for i in range(1, K+1):
        dp[1][i] = dp[0][i-1]
    
    # Populate the dp array
    for i in range(2, N+1):
        for j in range(1, K+1):
            # Case 1: place the domino on the current row
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j] + sums[i-1][2])
            # Case 2: do not place the domino on the current row
            dp[i][j] = max(dp[i][j], dp[i-1][j])
    
    # Return the maximum sum possible with K dominoes
    return dp[N][K]

