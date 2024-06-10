
def get_proclamations(starting_sequence, resulting_sequence):
    # Initialize a list to store the proclamations
    proclamations = []
    
    # Loop through the resulting sequence
    for i in range(len(resulting_sequence)):
        # Get the current frog ID and its position in the resulting sequence
        curr_frog_id = resulting_sequence[i]
        curr_frog_pos = i
        
        # Find the position of the current frog ID in the starting sequence
        start_frog_pos = starting_sequence.index(curr_frog_id)
        
        # Calculate the number of leaps needed to move the current frog to its final position
        num_leaps = abs(start_frog_pos - curr_frog_pos)
        
        # Add the number of leaps to the list of proclamations
        proclamations.append(num_leaps)
    
    # Return the list of proclamations
    return proclamations

def main():
    # Read the input data
    num_frogs = int(input())
    starting_sequence = list(map(int, input().split()))
    resulting_sequence = list(map(int, input().split()))
    
    # Get the proclamations needed to rearrange the frogs
    proclamations = get_proclamations(starting_sequence, resulting_sequence)
    
    # Print the proclamations
    for proclamation in proclamations:
        print(proclamation)

if __name__ == '__main__':
    main()

