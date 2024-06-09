
def get_segments(n, k, absurdity):
    # Sort the absurdity values in descending order
    absurdity.sort(reverse=True)
    
    # Initialize the segments with the first k values
    segment_1 = absurdity[:k]
    segment_2 = absurdity[k:2*k]
    
    # Initialize the total absurdity of the signed laws
    total_absurdity = sum(segment_1) + sum(segment_2)
    
    # Iterate through the remaining values
    for i in range(2*k, n):
        # Check if the current value is greater than the total absurdity
        if absurdity[i] > total_absurdity:
            # Add the current value to the first segment
            segment_1.append(absurdity[i])
            # Remove the first value from the first segment
            segment_1.pop(0)
            # Calculate the new total absurdity
            total_absurdity = sum(segment_1) + sum(segment_2)
        else:
            # Add the current value to the second segment
            segment_2.append(absurdity[i])
            # Remove the first value from the second segment
            segment_2.pop(0)
            # Calculate the new total absurdity
            total_absurdity = sum(segment_1) + sum(segment_2)
    
    # Return the segments with the minimum total absurdity
    return segment_1, segment_2

