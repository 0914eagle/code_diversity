
def get_max_value_and_ops(sequence):
    # Initialize variables
    max_value = 0
    ops = []
    
    # Loop until the sequence has only one element
    while len(sequence) > 1:
        # Choose an element from the sequence
        element = sequence.pop()
        
        # If the element is at either end of the sequence, delete it
        if element in [sequence[0], sequence[-1]]:
            sequence.remove(element)
        # If the element is not at either end of the sequence, replace it with the sum of the two adjacent elements and delete them
        else:
            sequence[sequence.index(element)-1] += sequence[sequence.index(element)+1]
            sequence.remove(element)
            sequence.remove(sequence[sequence.index(element)-1])
        
        # Update the maximum value
        max_value = max(max_value, sequence[0])
        
        # Add the operation to the list of operations
        ops.append(sequence.index(element))
    
    # Return the maximum value and the list of operations
    return max_value, ops

def main():
    # Read the input
    n = int(input())
    sequence = list(map(int, input().split()))
    
    # Get the maximum value and the list of operations
    max_value, ops = get_max_value_and_ops(sequence)
    
    # Print the maximum value
    print(max_value)
    
    # Print the number of operations
    print(len(ops))
    
    # Print the indices of the elements chosen in each operation
    for op in ops:
        print(op+1)

if __name__ == '__main__':
    main()

