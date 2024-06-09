
def solve(n, m, p):
    # Initialize the number of ways to place the minimum number of obstacles
    ways = 0
    
    # Loop through all possible positions of the obstacle
    for i in range(n - 1):
        for j in range(m - 1):
            # Check if the current position forms a valid 2x2 subgrid with at least one obstacle
            if (i == 0 or j == 0 or i == n - 2 or j == m - 2) and (i != n - 1 or j != m - 1):
                ways += 1
    
    # Return the number of ways modulo p
    return ways % p

