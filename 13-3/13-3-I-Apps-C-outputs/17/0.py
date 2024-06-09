
def f1(n, m, p):
    # Initialize the number of ways to place the minimum number of obstacles
    num_ways = 0
    
    # Loop over all possible positions of the obstacle
    for i in range(n - 1):
        for j in range(m - 1):
            # Check if the current position forms a valid subgrid
            if (i + 1) * (j + 1) <= n * m:
                # Increment the number of ways to place the minimum number of obstacles
                num_ways += 1
    
    # Return the number of ways modulo p
    return num_ways % p

