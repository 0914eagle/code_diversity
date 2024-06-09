
def solve(N, K, board):
    # Initialize a 2D array to store the sums of the numbers in each row
    sums = [[0] * 3 for _ in range(N)]
    
    # Calculate the sums of the numbers in each row
    for i in range(N):
        for j in range(3):
            sums[i][j] = sums[i][j-1] + board[i][j]
    
    # Initialize a 2D array to store the maximum sums for each combination of dominoes
    dp = [[0] * (K+1) for _ in range(N)]
    
    # Base case: no dominoes placed, the maximum sum is 0
    for i in range(N):
        dp[i][0] = 0
    
    # Base case: one domino placed, the maximum sum is the sum of the numbers in the first row
    for i in range(N):
        dp[i][1] = sums[i][2]
    
    # Dynamic programming
    for i in range(2, K+1):
        for j in range(N):
            # Try placing the domino in each possible position (left or right)
            dp[j][i] = max(dp[j-1][i-1] + sums[j][2], dp[j][i-1] + sums[j][0])
    
    # Return the maximum sum possible
    return dp[N-1][K]

