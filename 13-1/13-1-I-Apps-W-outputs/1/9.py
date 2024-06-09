
def shuffling_game(n, s, t, shuffling_operations):
    if s == t:
        return 0
    
    # Initialize a list to keep track of the positions of the glasses
    glasses = list(range(1, n+1))
    
    # Initialize a set to keep track of the positions that the marble has visited
    visited = set()
    
    # Initialize a variable to keep track of the number of shuffling operations
    num_shuffles = 0
    
    # Loop through each shuffling operation
    for p in shuffling_operations:
        # Check if the marble has visited this position before
        if p in visited:
            return -1
        
        # Add the current position to the set of visited positions
        visited.add(p)
        
        # Swap the current position with the position in the glasses list
        glasses[s-1], glasses[p-1] = glasses[p-1], glasses[s-1]
        
        # Increment the number of shuffling operations
        num_shuffles += 1
        
        # Check if the marble has reached the final position
        if glasses[s-1] == t:
            return num_shuffles
    
    # If the marble has not reached the final position, return -1
    return -1

