
def get_max_value(sequence):
    # Find the maximum value in the sequence
    max_value = max(sequence)

    # Initialize the number of operations to 0
    operations = 0

    # Loop until the sequence has only one element
    while len(sequence) > 1:
        # Find the index of the maximum value in the sequence
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
            sequence.pop(max_index - 1)

        # Increment the number of operations
        operations += 1

        # Find the new maximum value in the sequence
        max_value = max(sequence)

    # Return the maximum value and the number of operations
    return max_value, operations

def get_chosen_indices(sequence, operations):
    # Initialize an empty list to store the indices of the chosen elements
    chosen_indices = []

    # Loop through the sequence and the operations
    for i in range(len(sequence)):
        # If the current element is chosen in the current operation, add its index to the list of chosen indices
        if i == operations[i]:
            chosen_indices.append(i)

    # Return the list of chosen indices
    return chosen_indices

if __name__ == '__main__':
    # Read the input sequence from stdin
    sequence = list(map(int, input().split()))

    # Get the maximum value and the number of operations
    max_value, operations = get_max_value(sequence)

    # Get the indices of the chosen elements
    chosen_indices = get_chosen_indices(sequence, operations)

    # Print the maximum value
    print(max_value)

    # Print the number of operations
    print(operations)

    # Print the indices of the chosen elements
    for i in range(len(chosen_indices)):
        print(chosen_indices[i] + 1)

