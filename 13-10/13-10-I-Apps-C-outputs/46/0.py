
def get_proclamations(starting_sequence, resulting_sequence):
    # Initialize a dictionary to store the proclamations
    proclamations = {}
    
    # Iterate through the starting sequence
    for i in range(len(starting_sequence)):
        # Get the current frog's ID and the ID of the frog in front of it
        current_frog = starting_sequence[i]
        next_frog = starting_sequence[(i + 1) % len(starting_sequence)]
        
        # If the current frog is not in its desired position, add a proclamation
        if current_frog != resulting_sequence[i]:
            # Get the number of leaps needed to move the current frog to its desired position
            leaps = resulting_sequence.index(current_frog) - i
            
            # Add the proclamation to the dictionary
            proclamations[current_frog] = leaps
    
    # Return the proclamations dictionary
    return proclamations

def get_proclamation_sequence(proclamations):
    # Initialize an empty list to store the proclamation sequence
    sequence = []
    
    # Iterate through the proclamations dictionary
    for frog, leaps in proclamations.items():
        # Add the proclamation to the sequence
        sequence += [frog] * leaps
    
    # Return the proclamation sequence
    return sequence

if __name__ == '__main__':
    # Read the input
    N = int(input())
    starting_sequence = list(map(int, input().split()))
    resulting_sequence = list(map(int, input().split()))
    
    # Get the proclamations dictionary
    proclamations = get_proclamations(starting_sequence, resulting_sequence)
    
    # Get the proclamation sequence
    sequence = get_proclamation_sequence(proclamations)
    
    # Print the proclamation sequence
    print(*sequence, sep='\n')

