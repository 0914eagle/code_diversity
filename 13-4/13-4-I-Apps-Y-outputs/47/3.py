
def get_min_rolls(ell, n):
    # Initialize the minimum number of rolls to infinity
    min_rolls = float('inf')
    
    # Loop through all possible values of k
    for k in range(1, ell + 1):
        # Calculate the length of each roll
        roll_length = ell * (k - 1) + n
        
        # If the length of the roll is greater than or equal to the total length of the loo roll, we have found a solution
        if roll_length >= ell:
            min_rolls = min(min_rolls, k)
    
    # Return the smallest value of k that works
    return min_rolls

