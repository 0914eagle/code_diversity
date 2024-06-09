
def solve(starting_sequence, resulting_sequence):
    # Initialize a list to store the proclamations
    proclamations = []
    
    # Loop through the resulting sequence and find the indices of the frogs that need to be swapped
    for i in range(len(resulting_sequence)):
        # If the frog at the current index in the resulting sequence is not in its correct position, find the index of the frog that needs to be swapped with it
        if resulting_sequence[i] != i+1:
            # Find the index of the frog that needs to be swapped with the frog at the current index in the resulting sequence
            swap_index = resulting_sequence.index(i+1)
            
            # Add the number of leaps needed to the proclamations list
            proclamations.append(swap_index - i)
            
            # Swap the frogs at the current index and the swap index in the resulting sequence
            resulting_sequence[i], resulting_sequence[swap_index] = resulting_sequence[swap_index], resulting_sequence[i]
    
    # Return the proclamations list
    return proclamations

