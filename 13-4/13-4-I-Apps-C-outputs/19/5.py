
def solve(starting_sequence, resulting_sequence):
    # Initialize a list to store the proclamations
    proclamations = []
    
    # Loop through the resulting sequence
    for i in range(len(resulting_sequence)):
        # Get the current frog ID in the resulting sequence
        current_frog = resulting_sequence[i]
        
        # Get the index of the current frog ID in the starting sequence
        current_index = starting_sequence.index(current_frog)
        
        # Get the number of leaps needed to move the current frog to its correct position
        leaps_needed = abs(i - current_index)
        
        # Add the leaps needed to the proclamations list
        proclamations.extend([leaps_needed] * leaps_needed)
    
    return proclamations

