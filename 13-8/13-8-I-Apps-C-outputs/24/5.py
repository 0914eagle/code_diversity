
def get_max_value(sequence):
    # Initialize variables
    max_value = 0
    operations = 0
    current_sequence = sequence
    
    # Loop until the sequence has only one element
    while len(current_sequence) > 1:
        # Find the maximum value in the sequence
        max_value = max(current_sequence)
        
        # Find the index of the maximum value
        max_index = current_sequence.index(max_value)
        
        # If the maximum value is at the end of the sequence, delete it
        if max_index == len(current_sequence) - 1:
            current_sequence.pop()
        # If the maximum value is at the beginning of the sequence, delete it
        elif max_index == 0:
            current_sequence.pop(0)
        # If the maximum value is in the middle of the sequence, replace it with the sum of the two adjacent elements and delete them
        else:
            current_sequence[max_index] = current_sequence[max_index - 1] + current_sequence[max_index + 1]
            current_sequence.pop(max_index - 1)
            current_sequence.pop(max_index - 1)
        
        # Increment the number of operations
        operations += 1
    
    # Return the maximum value and the number of operations
    return max_value, operations

def get_chosen_elements(sequence, operations):
    # Initialize a list to store the chosen elements
    chosen_elements = []
    
    # Loop through the operations
    for i in range(operations):
        # Find the maximum value in the sequence
        max_value = max(sequence)
        
        # Find the index of the maximum value
        max_index = sequence.index(max_value)
        
        # If the maximum value is at the end of the sequence, delete it
        if max_index == len(sequence) - 1:
            sequence.pop()
        # If the maximum value is at the beginning of the sequence, delete it
        elif max_index == 0:
            sequence.pop(0)
        # If the maximum value is in the middle of the sequence, replace it with the sum of the two adjacent elements and delete them
        else:
            sequence[max_index] = sequence[max_index - 1] + sequence[max_index + 1]
            sequence.pop(max_index - 1)
        
        # Add the maximum value to the list of chosen elements
        chosen_elements.append(max_value)
    
    # Return the list of chosen elements
    return chosen_elements

if __name__ == '__main__':
    # Read the input
    N = int(input())
    sequence = list(map(int, input().split()))
    
    # Get the maximum value and the number of operations
    max_value, operations = get_max_value(sequence)
    
    # Get the list of chosen elements
    chosen_elements = get_chosen_elements(sequence, operations)
    
    # Print the maximum value and the number of operations
    print(max_value)
    print(operations)
    
    # Print the chosen elements
    for i in range(operations):
        print(chosen_elements[i])

