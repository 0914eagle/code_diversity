
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize a 2D array to store the minimum path values
    dp = [[float('inf') for _ in range(k+1)] for _ in range(len(grid))]
    # Initialize the first row of the DP array with the values of the first row of the grid
    for i in range(len(grid[0])):
        dp[0][i] = grid[0][i]
    # Loop through each row of the grid
    for i in range(1, len(grid)):
        # Loop through each column of the current row
        for j in range(len(grid[i])):
            # Find the minimum path value from the previous row
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])
            # Add the current value to the minimum path value
            dp[i][j] += grid[i][j]
    # Return the minimum path values
    return dp[-1]

