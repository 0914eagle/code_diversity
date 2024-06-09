
def solve(starting_sequence, resulting_sequence):
    # Initialize a list to store the proclamations
    proclamations = []
    
    # Loop through the resulting sequence
    for i in range(len(resulting_sequence)):
        # Check if the current element in the resulting sequence is not in its correct position
        if resulting_sequence[i] != starting_sequence[i]:
            # Find the index of the element in the starting sequence
            index = starting_sequence.index(resulting_sequence[i])
            # Add the number of leaps needed to the proclamations list
            proclamations.append(index - i)
    
    # Return the proclamations list
    return proclamations

