
def solve(sequence):
    # Initialize the maximum value of the final element and the number of operations
    max_value, operations = 0, 0
    
    # Loop until the length of the sequence is 1
    while len(sequence) > 1:
        # Find the index of the maximum value in the sequence
        max_index = sequence.index(max(sequence))
        
        # If the maximum value is at either end of the sequence, delete it
        if max_index == 0 or max_index == len(sequence) - 1:
            sequence.pop(max_index)
        # If the maximum value is not at either end of the sequence, replace it with the sum of the two adjacent elements and delete them
        else:
            sequence[max_index] = sequence[max_index - 1] + sequence[max_index + 1]
            sequence.pop(max_index - 1)
            sequence.pop(max_index - 1)
        
        # Update the maximum value of the final element and the number of operations
        max_value = max(sequence)
        operations += 1
    
    # Return the maximum value of the final element and the number of operations
    return max_value, operations

