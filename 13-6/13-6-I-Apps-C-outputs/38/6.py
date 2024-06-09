
import math

def place_obstacles(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    num_ways = 0
    
    # Loop through all possible positions for the obstacles
    for i in range(n):
        for j in range(m):
            # Check if the current position is valid (i.e., it is not on the border of the grid)
            if i > 0 and i < n-1 and j > 0 and j < m-1:
                # Count the number of ways to place the obstacle in the current position
                num_ways += 1
    
    # Return the result modulo p
    return num_ways % p

