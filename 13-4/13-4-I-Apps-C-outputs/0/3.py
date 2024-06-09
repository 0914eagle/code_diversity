
def solve(starting_sequence, resulting_sequence):
    # Initialize a list to store the proclamations
    proclamations = []
    
    # Loop through the resulting sequence
    for i in range(len(resulting_sequence)):
        # Get the current frog ID and its position in the resulting sequence
        current_frog = resulting_sequence[i]
        current_position = i
        
        # Find the position of the current frog in the starting sequence
        starting_position = starting_sequence.index(current_frog)
        
        # Calculate the number of leaps needed to move the current frog to its correct position
        leaps_needed = abs(current_position - starting_position)
        
        # Add the leaps needed to the proclamations list
        proclamations.extend([leaps_needed] * leaps_needed)
    
    # Return the proclamations list
    return proclamations

