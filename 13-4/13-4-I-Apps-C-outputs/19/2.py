
def solve(starting_sequence, resulting_sequence):
    # Initialize a list to store the proclamations
    proclamations = []
    
    # Loop through the resulting sequence and check if it matches the starting sequence
    for i in range(len(resulting_sequence)):
        # If the elements are not in the same position, add the proclamation to the list
        if resulting_sequence[i] != starting_sequence[i]:
            proclamations.append(resulting_sequence[i])
    
    # Return the list of proclamations
    return proclamations

