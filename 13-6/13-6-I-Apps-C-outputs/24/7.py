
def solve(sequence):
    # Initialize variables
    max_value = 0
    operations = 0
    choice = 0
    sequence_length = len(sequence)

    # Loop until the sequence has only one element
    while sequence_length > 1:
        # Find the maximum value in the sequence
        max_value = max(sequence)

        # Choose an element of the sequence
        choice = sequence.index(max_value)

        # If the chosen element is at either end of the sequence, delete it
        if choice == 0 or choice == sequence_length - 1:
            sequence.pop(choice)
            sequence_length -= 1
        else:
            # If the chosen element is not at either end of the sequence, replace it with the sum of the two elements that are adjacent to it
            sequence[choice] = sequence[choice - 1] + sequence[choice + 1]

            # Delete the two elements that are adjacent to the chosen element
            sequence.pop(choice - 1)
            sequence.pop(choice)
            sequence_length -= 2

        # Increment the number of operations
        operations += 1

    # Return the maximum value of the final element and the number of operations
    return max_value, operations, choice + 1

