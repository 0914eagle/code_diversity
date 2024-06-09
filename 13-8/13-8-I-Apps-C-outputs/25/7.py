
def get_number_of_ways(r, w, d):
    # Initialize the number of ways to be 0
    ways = 0
    
    # Loop through all possible number of red wine piles
    for red_piles in range(1, r + 1):
        # Calculate the number of white wine piles
        white_piles = r - red_piles
        
        # Check if the number of white wine piles is valid
        if white_piles >= 0 and red_piles <= d:
            # Increment the number of ways
            ways += 1
    
    # Return the number of ways modulo 10^9 + 7
    return ways % (10**9 + 7)

