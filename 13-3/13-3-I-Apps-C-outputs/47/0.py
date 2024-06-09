
def get_max_length(tube_lengths, L1, L2):
    # Sort the tube lengths in descending order
    tube_lengths.sort(reverse=True)

    # Initialize the maximum total length and the pairs of tubes
    max_length = 0
    pairs = []

    # Iterate over the tube lengths
    for i in range(len(tube_lengths)):
        for j in range(i+1, len(tube_lengths)):
            # Check if the sum of the lengths of the two tubes is less than or equal to L1 and L2
            if tube_lengths[i] + tube_lengths[j] <= L1 and tube_lengths[i] + tube_lengths[j] <= L2:
                # Add the pair of tubes to the list of pairs
                pairs.append([tube_lengths[i], tube_lengths[j]])

                # Check if the sum of the lengths of the four tubes is greater than the current maximum total length
                if tube_lengths[i] + tube_lengths[j] > max_length:
                    max_length = tube_lengths[i] + tube_lengths[j]

    # Check if at least two pairs of tubes can be found
    if len(pairs) < 2:
        return "Impossible"

    # Return the maximum total length
    return max_length

