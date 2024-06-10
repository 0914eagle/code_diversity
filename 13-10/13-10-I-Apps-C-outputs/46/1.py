
def get_proclamations(starting_sequence, resulting_sequence):
    # Initialize a dictionary to store the proclamations
    proclamations = {}
    
    # Iterate through the starting sequence
    for i in range(len(starting_sequence)):
        # Get the current frog's ID and its position in the sequence
        frog_id = starting_sequence[i]
        frog_pos = i
        
        # If the frog is not in its desired position, add a proclamation to move it
        if frog_id != resulting_sequence[frog_pos]:
            # Get the position of the frog in the resulting sequence
            desired_pos = resulting_sequence.index(frog_id)
            
            # Add a proclamation to move the frog to its desired position
            proclamations[frog_id] = desired_pos - frog_pos
    
    # Return the proclamations dictionary
    return proclamations

def get_proclamation_sequence(proclamations):
    # Initialize an empty list to store the proclamation sequence
    sequence = []
    
    # Iterate through the proclamations dictionary
    for frog_id, proclamation in proclamations.items():
        # Add the proclamation to the sequence
        sequence.append(proclamation)
    
    # Return the proclamation sequence
    return sequence

def main():
    # Read the input
    num_frogs = int(input())
    starting_sequence = list(map(int, input().split()))
    resulting_sequence = list(map(int, input().split()))
    
    # Get the proclamations dictionary
    proclamations = get_proclamations(starting_sequence, resulting_sequence)
    
    # Get the proclamation sequence
    sequence = get_proclamation_sequence(proclamations)
    
    # Print the proclamation sequence
    print(*sequence, sep='\n')

if __name__ == '__main__':
    main()

