
def get_segments(n, k, absurdity):
    # Sort the absurdity values in descending order
    absurdity.sort(reverse=True)
    
    # Initialize the segments with the first k values
    segment_1 = absurdity[:k]
    segment_2 = absurdity[k:]
    
    # Initialize the total absurdity of the signed laws
    total_absurdity = sum(segment_1) + sum(segment_2)
    
    # Iterate through the remaining values
    for i in range(k, n):
        # Check if the current value is greater than the total absurdity
        if absurdity[i] > total_absurdity:
            # Add the current value to the first segment
            segment_1.append(absurdity[i])
            # Remove the first value from the second segment
            segment_2.pop(0)
            # Update the total absurdity
            total_absurdity += absurdity[i] - segment_2[0]
    
    return segment_1, segment_2

