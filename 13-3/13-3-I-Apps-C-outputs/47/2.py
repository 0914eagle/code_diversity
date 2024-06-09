
def get_max_length(tubes, L1, L2):
    # Sort the tubes in descending order
    tubes.sort(reverse=True)

    # Initialize the maximum length and the pairs of tubes
    max_length = 0
    pairs = []

    # Iterate over the tubes
    for i in range(len(tubes)):
        for j in range(i+1, len(tubes)):
            # Check if the sum of the lengths of the two tubes is less than or equal to L1 and L2
            if tubes[i] + tubes[j] <= L1 and tubes[i] + tubes[j] <= L2:
                # Add the pair of tubes to the list of pairs
                pairs.append([tubes[i], tubes[j]])

                # Update the maximum length
                max_length = max(max_length, tubes[i] + tubes[j])

    # If no pairs of tubes can be found, return "Impossible"
    if not pairs:
        return "Impossible"

    # Return the maximum length
    return max_length

