
def get_max_value(sequence):
    # Initialize variables
    max_value = 0
    operations = []

    # Loop through the sequence
    while len(sequence) > 1:
        # Find the maximum value in the sequence
        max_index = sequence.index(max(sequence))
        max_value = max(max_value, sequence[max_index])

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

        # Add the operation to the list of operations
        operations.append(max_index + 1)

    # Return the maximum value and the list of operations
    return max_value, operations

def main():
    # Read the input
    N = int(input())
    sequence = list(map(int, input().split()))

    # Get the maximum value and the list of operations
    max_value, operations = get_max_value(sequence)

    # Print the maximum value
    print(max_value)

    # Print the number of operations
    print(len(operations))

    # Print the indices of the elements chosen in each operation
    for operation in operations:
        print(operation)

if __name__ == '__main__':
    main()

