
def solve(sequence):
    # Find the maximum element in the sequence
    max_element = max(sequence)

    # Initialize the number of operations to 0
    operations = 0

    # While the length of the sequence is greater than 1
    while len(sequence) > 1:
        # Find the index of the maximum element in the sequence
        max_index = sequence.index(max_element)

        # If the maximum element is at the end of the sequence
        if max_index == len(sequence) - 1:
            # Delete the maximum element
            sequence.pop()
        # If the maximum element is at the beginning of the sequence
        elif max_index == 0:
            # Delete the maximum element
            sequence.pop(0)
        # If the maximum element is in the middle of the sequence
        else:
            # Find the sum of the two elements adjacent to the maximum element
            sum = sequence[max_index - 1] + sequence[max_index + 1]

            # Replace the maximum element with the sum
            sequence[max_index] = sum

            # Delete the two elements adjacent to the maximum element
            sequence.pop(max_index - 1)
            sequence.pop(max_index - 1)

        # Increment the number of operations
        operations += 1

    # Return the maximum possible value of the final element and the number of operations
    return max_element, operations

