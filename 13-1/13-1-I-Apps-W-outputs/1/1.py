
def shuffling_game(n, s, t, shuffling_operations):
    if s == t:
        return 0
    
    # Initialize a list to keep track of the positions of the glasses
    glasses = list(range(1, n+1))
    
    # Initialize a variable to keep track of the number of shuffling operations
    num_shuffles = 0
    
    # Loop through each shuffling operation
    for p in shuffling_operations:
        # Find the index of the glass that the marble is currently on
        current_glass = glasses.index(s)
        
        # Move the marble to the new glass
        glasses[current_glass] = p
        
        # Update the number of shuffling operations
        num_shuffles += 1
        
        # If the marble has reached the final position, return the number of shuffling operations
        if glasses[current_glass] == t:
            return num_shuffles
    
    # If the marble has not reached the final position after all shuffling operations, return -1
    return -1

