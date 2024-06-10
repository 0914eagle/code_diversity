
def get_max_value(sequence):
    # Initialize variables
    max_value = 0
    max_sequence = []
    length = len(sequence)
    
    # Loop through each element in the sequence
    for i in range(length):
        # Check if the element is at either end of the sequence
        if i == 0 or i == length - 1:
            # If it is, delete the element
            sequence.pop(i)
            length -= 1
        else:
            # If it is not, replace the element with the sum of the two elements that are adjacent to it
            sequence[i] = sequence[i - 1] + sequence[i + 1]
            # Then, delete those two elements
            sequence.pop(i - 1)
            sequence.pop(i - 1)
            length -= 2
        
        # Check if the current sequence is the maximum sequence seen so far
        if sum(sequence) > max_value:
            max_value = sum(sequence)
            max_sequence = sequence[:]
    
    # Return the maximum value and the sequence
    return max_value, max_sequence

def get_operations(sequence):
    # Initialize variables
    operations = []
    length = len(sequence)
    
    # Loop through each element in the sequence
    for i in range(length):
        # Check if the element is at either end of the sequence
        if i == 0 or i == length - 1:
            # If it is, delete the element
            sequence.pop(i)
            length -= 1
        else:
            # If it is not, replace the element with the sum of the two elements that are adjacent to it
            sequence[i] = sequence[i - 1] + sequence[i + 1]
            # Then, delete those two elements
            sequence.pop(i - 1)
            sequence.pop(i - 1)
            length -= 2
        
        # Add the index of the element chosen to the operations list
        operations.append(i)
    
    # Return the operations list
    return operations

if __name__ == '__main__':
    # Get the input sequence
    sequence = list(map(int, input().split()))
    
    # Get the maximum value and the sequence
    max_value, max_sequence = get_max_value(sequence)
    
    # Get the operations
    operations = get_operations(sequence)
    
    # Print the maximum value and the number of operations
    print(max_value)
    print(len(operations))
    
    # Print the indices of the elements chosen in each operation
    for operation in operations:
        print(operation + 1)

