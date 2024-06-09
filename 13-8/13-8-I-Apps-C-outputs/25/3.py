
def get_num_ways(R, W, d):
    # Initialize the number of ways to be 0
    num_ways = 0
    
    # Loop through all possible number of red piles
    for r in range(1, R + 1):
        # Get the number of white piles
        w = W - r
        
        # Check if the number of red piles is valid
        if r <= d:
            # Increment the number of ways
            num_ways += 1
    
    # Return the number of ways modulo 10^9 + 7
    return num_ways % (10**9 + 7)

