
def get_max_length(tubes, L1, L2):
    # Sort the tubes in descending order
    tubes.sort(reverse=True)

    # Initialize the maximum length as 0
    max_length = 0

    # Loop through all possible pairs of tubes
    for i in range(len(tubes)):
        for j in range(i+1, len(tubes)):
            # Check if the sum of the lengths of the first two tubes is less than or equal to L1
            if tubes[i] + tubes[j] <= L1:
                # Check if the sum of the lengths of the last two tubes is less than or equal to L2
                if tubes[i+1] + tubes[j+1] <= L2:
                    # Calculate the total length of the four tubes
                    total_length = tubes[i] + tubes[j] + tubes[i+1] + tubes[j+1]

                    # Update the maximum length if the current total length is greater than the previous maximum length
                    if total_length > max_length:
                        max_length = total_length

    # Return the maximum length or the string "Impossible" if no pair of tubes fits the criteria
    if max_length == 0:
        return "Impossible"
    else:
        return max_length

