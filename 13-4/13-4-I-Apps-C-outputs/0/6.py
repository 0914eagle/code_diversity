
def solve(starting_sequence, resulting_sequence):
    # Initialize a list to store the proclamations
    proclamations = []
    
    # Loop through the resulting sequence
    for i in range(len(resulting_sequence)):
        # Get the current frog ID and its position in the resulting sequence
        current_frog_id = resulting_sequence[i]
        current_frog_position = i
        
        # Find the position of the current frog ID in the starting sequence
        starting_frog_position = starting_sequence.index(current_frog_id)
        
        # Calculate the number of leaps needed to move the current frog to its desired position
        num_leaps = abs(current_frog_position - starting_frog_position)
        
        # Add the number of leaps to the list of proclamations
        proclamations.append(num_leaps)
    
    # Return the list of proclamations
    return proclamations

