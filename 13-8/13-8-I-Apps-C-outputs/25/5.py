
def get_number_of_ways(R, W, d):
    # Initialize the number of ways to be 0
    ways = 0
    
    # Loop through all possible number of red wine piles
    for r in range(1, R + 1):
        # Calculate the number of white wine piles
        w = R - r
        
        # Check if the number of red wine piles is less than or equal to d
        if r <= d:
            # Increment the number of ways
            ways += 1
    
    # Return the number of ways
    return ways

