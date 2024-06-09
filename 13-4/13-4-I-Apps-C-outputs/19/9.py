
def solve(starting_sequence, resulting_sequence):
    # Initialize a list to store the proclamations
    proclamations = []
    
    # Loop through the resulting sequence
    for i in range(len(resulting_sequence)):
        # Get the current frog ID and its position in the resulting sequence
        current_frog_id = resulting_sequence[i]
        current_frog_position = i
        
        # If the current frog ID is not in its correct position, we need to make a proclamation
        if current_frog_id != current_frog_position + 1:
            # Get the position of the frog that needs to be swapped with the current frog
            swap_position = starting_sequence.index(current_frog_id)
            
            # Add the proclamation to the list
            proclamations.append(swap_position)
            
            # Swap the positions of the current frog and the frog that needs to be swapped
            starting_sequence[current_frog_position], starting_sequence[swap_position] = starting_sequence[swap_position], starting_sequence[current_frog_position]
    
    return proclamations

