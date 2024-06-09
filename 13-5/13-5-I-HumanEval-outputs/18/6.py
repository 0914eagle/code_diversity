
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize a 2D array to store the minimum path values
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]
    
    # Initialize the first row of the dp array with the values of the first row of the grid
    for i in range(len(grid[0])):
        dp[0][i] = grid[0][i]
    
    # Initialize the first column of the dp array with the values of the first column of the grid
    for i in range(len(grid)):
        dp[i][0] = grid[i][0]
    
    # Fill in the rest of the dp array using the recurrence relation
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # Find the minimum path by starting from the bottom-right corner and working backwards
    path = []
    i, j = len(grid) - 1, len(grid[0]) - 1
    while i >= 0 and j >= 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            path.append(grid[i][j])
            i -= 1
            j -= 1
    
    # Reverse the path and return it
    path.reverse()
    return path

