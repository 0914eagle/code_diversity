
def get_proclamations(starting_sequence, resulting_sequence):
    # Initialize a list to store the proclamations
    proclamations = []
    
    # Loop through the resulting sequence
    for i in range(len(resulting_sequence)):
        # Get the current frog in the resulting sequence
        current_frog = resulting_sequence[i]
        
        # Get the index of the current frog in the starting sequence
        starting_index = starting_sequence.index(current_frog)
        
        # Get the number of leaps needed to move the current frog to its correct position
        leaps_needed = abs(i - starting_index)
        
        # Add the number of leaps needed to the proclamations list
        proclamations.append(leaps_needed)
    
    # Return the proclamations list
    return proclamations

def main():
    # Read the input
    N = int(input())
    starting_sequence = list(map(int, input().split()))
    resulting_sequence = list(map(int, input().split()))
    
    # Get the proclamations needed
    proclamations = get_proclamations(starting_sequence, resulting_sequence)
    
    # Print the proclamations
    for proclamation in proclamations:
        print(proclamation)

if __name__ == '__main__':
    main()

