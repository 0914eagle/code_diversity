
def get_maximum_length(tube_lengths, L1, L2):
    # Sort the tube lengths in descending order
    tube_lengths.sort(reverse=True)

    # Initialize the maximum length as 0
    max_length = 0

    # Loop through all possible pairs of tubes
    for i in range(len(tube_lengths)):
        for j in range(i+1, len(tube_lengths)):
            # Check if the sum of the lengths of the first two tubes is less than or equal to L1
            if tube_lengths[i] + tube_lengths[j] <= L1:
                # Check if the sum of the lengths of the last two tubes is less than or equal to L2
                if tube_lengths[i+1] + tube_lengths[j+1] <= L2:
                    # Calculate the total length of the four tubes
                    total_length = tube_lengths[i] + tube_lengths[j] + tube_lengths[i+1] + tube_lengths[j+1]
                    # Update the maximum length if necessary
                    if total_length > max_length:
                        max_length = total_length

    # Return the maximum length or the string "Impossible" if no pair of tubes fits the criteria
    if max_length == 0:
        return "Impossible"
    else:
        return max_length

