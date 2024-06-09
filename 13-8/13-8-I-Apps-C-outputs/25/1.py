
def get_number_of_ways(r, w, d):
    # Initialize the number of ways to be 0
    number_of_ways = 0
    
    # Iterate over all possible combinations of red and white wine piles
    for red_piles in range(1, r + 1):
        for white_piles in range(1, w + 1):
            # Check if the current combination satisfies the conditions
            if red_piles + white_piles <= r and red_piles <= d:
                # Increment the number of ways
                number_of_ways += 1
    
    # Return the number of ways
    return number_of_ways

