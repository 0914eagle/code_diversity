
def get_max_length(tubes, L1, L2):
    # Sort the tubes in descending order
    tubes.sort(reverse=True)

    # Initialize the maximum length and the pairs of tubes
    max_length = 0
    pairs = []

    # Iterate over the tubes
    for i in range(len(tubes)):
        for j in range(i+1, len(tubes)):
            # Check if the sum of the lengths of the two tubes is less than or equal to L1
            if tubes[i] + tubes[j] <= L1:
                # Check if the sum of the lengths of the two tubes is less than or equal to L2
                if tubes[i] + tubes[j] <= L2:
                    # Add the pair of tubes to the list of pairs
                    pairs.append([tubes[i], tubes[j]])

    # Iterate over the pairs of tubes
    for pair in pairs:
        # Calculate the total length of the four tubes
        total_length = pair[0] + pair[1]

        # Check if the total length is greater than the current maximum length
        if total_length > max_length:
            # Update the maximum length
            max_length = total_length

    # Return the maximum length
    return max_length

