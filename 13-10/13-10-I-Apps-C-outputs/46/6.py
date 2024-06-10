
def get_frog_proclamations(starting_sequence, resulting_sequence):
    # Initialize a list to store the proclamations
    proclamations = []
    
    # Loop through the resulting sequence
    for i in range(len(resulting_sequence)):
        # Get the current frog in the resulting sequence
        current_frog = resulting_sequence[i]
        
        # Get the index of the current frog in the starting sequence
        current_index = starting_sequence.index(current_frog)
        
        # Get the number of proclamations needed to move the current frog to its correct position
        num_proclamations = abs(i - current_index)
        
        # Add the proclamations to the list
        proclamations += [num_proclamations] * num_proclamations
    
    # Return the list of proclamations
    return proclamations

def main():
    # Read the input
    num_frogs = int(input())
    starting_sequence = list(map(int, input().split()))
    resulting_sequence = list(map(int, input().split()))
    
    # Get the proclamations needed to rearrange the frogs
    proclamations = get_frog_proclamations(starting_sequence, resulting_sequence)
    
    # Print the proclamations
    print(*proclamations, sep='\n')

if __name__ == '__main__':
    main()

