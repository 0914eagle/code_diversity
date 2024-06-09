
def solve(sequence):
    # Initialize a set to store the average elements
    average_elements = set()

    # Iterate over the sequence
    for i in range(len(sequence)):
        # Get the current element
        current_element = sequence[i]

        # Iterate over the remaining elements
        for j in range(i+1, len(sequence)):
            # Get the next element
            next_element = sequence[j]

            # Check if the current element is the average of the current element and the next element
            if current_element == (current_element + next_element) // 2:
                # Add the current element to the set of average elements
                average_elements.add(current_element)
                break

    # Return the length of the set of average elements
    return len(average_elements)

