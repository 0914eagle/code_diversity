
def shuffling_game(n, s, t, shuffling_operations):
    if s == t:
        return 0
    
    # Initialize a list to keep track of the positions of the glasses
    glasses = list(range(1, n+1))
    
    # Initialize a variable to keep track of the number of shuffling operations
    num_shuffles = 0
    
    # Loop through each shuffling operation
    for p in shuffling_operations:
        # Find the index of the glass that is being moved
        glass_index = glasses.index(s)
        
        # Move the glass to its new position
        glasses[glass_index] = p
        
        # Increment the number of shuffling operations
        num_shuffles += 1
        
        # If the marble has reached its final position, return the number of shuffling operations
        if glasses[glass_index] == t:
            return num_shuffles
    
    # If the marble has not reached its final position after all shuffling operations, return -1
    return -1

