
def solve(sequence):
    # Initialize variables
    max_value = 0
    operations = 0
    chosen_elements = []

    # Loop through the sequence
    while len(sequence) > 1:
        # Find the maximum value in the sequence
        max_index = sequence.index(max(sequence))
        max_value = max(max_value, sequence[max_index])

        # Choose the element at the maximum index
        chosen_element = sequence[max_index]
        chosen_elements.append(chosen_elements)

        # If the chosen element is at the end of the sequence, delete it
        if max_index == len(sequence) - 1:
            sequence.pop()
        # If the chosen element is at the beginning of the sequence, delete it
        elif max_index == 0:
            sequence.pop(0)
        # If the chosen element is in the middle of the sequence, replace it with the sum of the two adjacent elements and delete them
        else:
            sequence[max_index] = sequence[max_index - 1] + sequence[max_index + 1]
            sequence.pop(max_index - 1)
            sequence.pop(max_index - 1)

        # Increment the number of operations
        operations += 1

    # Return the maximum value and the number of operations
    return max_value, operations, chosen_elements

