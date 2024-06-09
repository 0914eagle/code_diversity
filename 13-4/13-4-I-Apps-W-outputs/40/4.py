
def get_segments(n, k, absurdity):
    # Sort the absurdity values in descending order
    absurdity.sort(reverse=True)
    
    # Initialize the segments with the first k values
    segments = absurdity[:k]
    
    # Add the remaining values to the segments
    for i in range(k, n):
        # Find the smallest segment that the current value can be added to
        smallest_segment_index = 0
        for j in range(1, k):
            if absurdity[i] > segments[j]:
                smallest_segment_index = j
                break
        segments[smallest_segment_index] += absurdity[i]
    
    # Return the segments with the minimum value of a
    return segments

