
def get_maximum_value(sequence):
    # Find the maximum value in the sequence
    max_value = max(sequence)
    
    # Initialize a variable to store the number of operations
    operations = 0
    
    # While the length of the sequence is greater than 1
    while len(sequence) > 1:
        # Find the index of the maximum value in the sequence
        max_index = sequence.index(max_value)
        
        # If the maximum value is at the end of the sequence
        if max_index == len(sequence) - 1:
            # Delete the maximum value
            sequence.pop()
        # If the maximum value is at the beginning of the sequence
        elif max_index == 0:
            # Delete the maximum value
            sequence.pop(0)
        # If the maximum value is in the middle of the sequence
        else:
            # Add the values of the two elements adjacent to the maximum value
            sum_adjacent = sequence[max_index - 1] + sequence[max_index + 1]
            # Replace the maximum value with the sum of the adjacent elements
            sequence[max_index] = sum_adjacent
            # Delete the two elements adjacent to the maximum value
            sequence.pop(max_index - 1)
            sequence.pop(max_index)
        
        # Increment the number of operations
        operations += 1
    
    # Return the maximum value and the number of operations
    return max_value, operations

def get_chosen_elements(sequence, operations):
    # Initialize a list to store the indices of the elements chosen in each operation
    chosen_elements = []
    
    # For each operation
    for i in range(operations):
        # Find the index of the maximum value in the sequence
        max_index = sequence.index(max(sequence))
        
        # Add the index of the maximum value to the list of chosen elements
        chosen_elements.append(max_index)
        
        # Delete the maximum value
        sequence.pop(max_index)
    
    # Return the list of chosen elements
    return chosen_elements

if __name__ == '__main__':
    # Read the input from stdin
    N = int(input())
    sequence = list(map(int, input().split()))
    
    # Get the maximum value and the number of operations
    max_value, operations = get_maximum_value(sequence)
    
    # Get the indices of the elements chosen in each operation
    chosen_elements = get_chosen_elements(sequence, operations)
    
    # Print the maximum value
    print(max_value)
    # Print the number of operations
    print(operations)
    # Print the indices of the elements chosen in each operation
    for i in range(operations):
        print(chosen_elements[i] + 1)

