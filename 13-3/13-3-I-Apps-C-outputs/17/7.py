
def f1(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    num_ways = 0
    
    # Iterate over each possible position of the obstacle
    for i in range(n - 1):
        for j in range(m - 1):
            # Check if the current position forms a valid obstacle
            if (i + 1) * (j + 1) % p != 0:
                num_ways += 1
    
    return num_ways % p

