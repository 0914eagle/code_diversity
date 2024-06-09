
def solve(n, p):
    # Initialize a list to store the number of apples in each inflorescence
    apples = [0] * (n + 1)
    
    # Initialize a set to store the indices of inflorescences with at least one apple
    active_inflorescences = set()
    
    # Initialize a variable to store the number of apples collected
    collected_apples = 0
    
    # Iterate over the input sequence
    for i in range(n - 1):
        # Get the current and next inflorescence indices
        curr_inflorescence = i + 1
        next_inflorescence = p[i]
        
        # Check if the current inflorescence has at least one apple
        if apples[curr_inflorescence] > 0:
            # Add the current inflorescence to the set of active inflorescences
            active_inflorescences.add(curr_inflorescence)
        
        # Check if the next inflorescence has at least one apple
        if apples[next_inflorescence] > 0:
            # Add the next inflorescence to the set of active inflorescences
            active_inflorescences.add(next_inflorescence)
        
        # Check if the current inflorescence and the next inflorescence have at least two apples
        if apples[curr_inflorescence] + apples[next_inflorescence] >= 2:
            # Annihilate the apples in the current and next inflorescences
            apples[curr_inflorescence] = 0
            apples[next_inflorescence] = 0
            
            # Remove the current and next inflorescences from the set of active inflorescences
            active_inflorescences.remove(curr_inflorescence)
            active_inflorescences.remove(next_inflorescence)
            
            # Increment the number of collected apples
            collected_apples += 1
    
    # Return the number of collected apples
    return collected_apples

