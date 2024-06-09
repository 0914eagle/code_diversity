
def max_air_replacement(L1, L2, N, tubes):
    # Sort the tubes in non-decreasing order
    tubes.sort()
    # Initialize the maximum total length to 0
    max_length = 0
    # Loop through all possible pairs of tubes
    for i in range(N-1):
        for j in range(i+1, N):
            # Check if the sum of the lengths of the two tubes is less than or equal to L1
            if tubes[i] + tubes[j] <= L1:
                # Check if the sum of the lengths of the two tubes is less than or equal to L2
                if tubes[i] + tubes[j] <= L2:
                    # Calculate the total length of the four tubes
                    total_length = tubes[i] + tubes[j] + tubes[N-1] + tubes[N-2]
                    # Update the maximum total length if necessary
                    max_length = max(max_length, total_length)
    # Return the maximum total length or the word "Impossible" if no pair of tubes fits the setup
    if max_length == 0:
        return "Impossible"
    else:
        return max_length

