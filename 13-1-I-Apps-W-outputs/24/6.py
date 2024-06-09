
def knight_moves(X, Y):
    # Initialize a 2D array to store the number of ways to reach each square
    dp = [[0] * (Y+1) for _ in range(X+1)]
    
    # Initialize the number of ways to reach the origin as 1
    dp[0][0] = 1
    
    # Fill in the table
    for i in range(1, X+1):
        for j in range(1, Y+1):
            # The knight can only move to (i+1, j+2) or (i+2, j+1)
            dp[i][j] = dp[i-1][j-1] + dp[i-2][j-2]
    
    # Return the number of ways to reach (X, Y) modulo 10^9 + 7
    return dp[X][Y] % 1000000007

