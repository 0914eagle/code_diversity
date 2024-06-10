
def find_proclamations(starting_sequence, resulting_sequence):
    # Initialize a dictionary to store the proclamations
    proclamations = {}
    
    # Iterate through the starting sequence
    for i, fruit in enumerate(starting_sequence):
        # If the fruit is not in its desired position, add a proclamation
        if fruit != resulting_sequence[i]:
            proclamations[fruit] = resulting_sequence[i]
    
    # Return the proclamations
    return proclamations

def get_proclamation_sequence(proclamations):
    # Initialize an empty list to store the proclamation sequence
    proclamation_sequence = []
    
    # Iterate through the proclamations
    for fruit, target in proclamations.items():
        # Add the proclamation to the sequence
        proclamation_sequence.append(target)
    
    # Return the proclamation sequence
    return proclamation_sequence

if __name__ == '__main__':
    # Read the input
    num_frogs = int(input())
    starting_sequence = list(map(int, input().split()))
    resulting_sequence = list(map(int, input().split()))
    
    # Find the proclamations
    proclamations = find_proclamations(starting_sequence, resulting_sequence)
    
    # Get the proclamation sequence
    proclamation_sequence = get_proclamation_sequence(proclamations)
    
    # Print the proclamation sequence
    for proclamation in proclamation_sequence:
        print(proclamation)

