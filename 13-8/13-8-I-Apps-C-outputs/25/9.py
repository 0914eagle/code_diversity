
def get_number_of_ways(r, w, d):
    # Initialize the number of ways to be 0
    number_of_ways = 0
    
    # Iterate over all possible number of red wine piles
    for red_piles in range(1, r + 1):
        # Get the number of white wine piles
        white_piles = r - red_piles
        
        # Check if the number of red wine piles is valid
        if red_piles <= d:
            # Increment the number of ways
            number_of_ways += 1
    
    # Return the number of ways modulo 10^9 + 7
    return number_of_ways % (10**9 + 7)

