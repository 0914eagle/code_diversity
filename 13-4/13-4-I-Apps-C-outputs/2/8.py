
def get_number_of_ways(R, W, d):
    # Initialize the number of ways to be 0
    number_of_ways = 0
    
    # Loop through all possible combinations of red and white wine piles
    for i in range(1, R + 1):
        for j in range(1, W + 1):
            # Check if the current combination satisfies the conditions
            if i + j <= R and i <= d:
                # Increment the number of ways
                number_of_ways += 1
    
    # Return the number of ways modulo 10^9 + 7
    return number_of_ways % (10**9 + 7)

