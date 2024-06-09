
def solve(N, K, board):
    # Initialize a two-dimensional array to store the sums of the numbers in each row
    sums = [[0] * 3 for _ in range(N)]
    
    # Calculate the sums of the numbers in each row
    for i in range(N):
        for j in range(3):
            sums[i][j] = sums[i][j-1] + board[i][j]
    
    # Initialize a two-dimensional array to store the maximum sums for each combination of two rows
    max_sums = [[0] * (K+1) for _ in range(N)]
    
    # Fill in the maximum sums for the first row
    for j in range(K+1):
        max_sums[0][j] = sums[0][j]
    
    # Fill in the maximum sums for the remaining rows
    for i in range(1, N):
        for j in range(K+1):
            max_sums[i][j] = max(max_sums[i-1][j], max_sums[i-1][j-1] + sums[i][j])
    
    # Return the maximum sum
    return max_sums[N-1][K]

