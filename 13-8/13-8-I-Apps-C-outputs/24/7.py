
def get_max_value(sequence):
    # Initialize the maximum value and the number of operations
    max_value = 0
    num_operations = 0
    
    # Loop through the sequence and perform the operations
    while len(sequence) > 1:
        # Find the maximum value in the sequence
        max_index = sequence.index(max(sequence))
        
        # If the maximum value is at either end of the sequence, delete it
        if max_index == 0 or max_index == len(sequence) - 1:
            sequence.pop(max_index)
        # If the maximum value is not at either end of the sequence, replace it with the sum of the two adjacent elements and delete them
        else:
            sequence[max_index] = sequence[max_index - 1] + sequence[max_index + 1]
            sequence.pop(max_index - 1)
            sequence.pop(max_index - 1)
        
        # Update the maximum value and the number of operations
        max_value = max(sequence)
        num_operations += 1
    
    # Return the maximum value and the number of operations
    return max_value, num_operations

def get_operations(sequence):
    # Initialize the maximum value and the number of operations
    max_value = 0
    num_operations = 0
    
    # Loop through the sequence and perform the operations
    while len(sequence) > 1:
        # Find the maximum value in the sequence
        max_index = sequence.index(max(sequence))
        
        # If the maximum value is at either end of the sequence, delete it
        if max_index == 0 or max_index == len(sequence) - 1:
            sequence.pop(max_index)
        # If the maximum value is not at either end of the sequence, replace it with the sum of the two adjacent elements and delete them
        else:
            sequence[max_index] = sequence[max_index - 1] + sequence[max_index + 1]
            sequence.pop(max_index - 1)
            sequence.pop(max_index - 1)
        
        # Update the maximum value and the number of operations
        max_value = max(sequence)
        num_operations += 1
    
    # Return the maximum value and the number of operations
    return max_value, num_operations

if __name__ == '__main__':
    # Read the input sequence from stdin
    N = int(input())
    sequence = list(map(int, input().split()))
    
    # Get the maximum value and the number of operations
    max_value, num_operations = get_max_value(sequence)
    
    # Print the maximum value and the number of operations
    print(max_value)
    print(num_operations)
    
    # Get the operations
    operations = get_operations(sequence)
    
    # Print the operations
    for i in range(num_operations):
        print(operations[i])

