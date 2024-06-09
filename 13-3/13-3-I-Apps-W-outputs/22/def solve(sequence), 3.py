
def solve(sequence):
    # Initialize a set to store the average elements
    average_elements = set()

    # Iterate over the sequence
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            # Check if the current element is the average of two other elements
            if sequence[i] == (sequence[j] + sequence[i-1]) // 2:
                # Add the current element to the set of average elements
                average_elements.add(sequence[i])
                break

    # Return the length of the set of average elements
    return len(average_elements)

