
def solve(N, K, board):
    # Initialize a 2D array to store the sums of the numbers in each row
    sums = [[0] * 3 for _ in range(N)]
    for i in range(N):
        for j in range(3):
            sums[i][j] = sums[i][j-1] + board[i][j]
    
    # Initialize a 2D array to store the maximum sum possible with each domino
    dp = [[0] * (K+1) for _ in range(N)]
    
    # Base case: no dominoes placed
    for i in range(N):
        dp[i][0] = sums[i][2]
    
    # Place dominoes
    for i in range(1, K+1):
        for j in range(N):
            dp[j][i] = max(dp[j-1][i-1], dp[j][i-1], sums[j][2] + dp[j-1][i-1])
    
    # Return the maximum sum possible with K dominoes
    return dp[N-1][K]

