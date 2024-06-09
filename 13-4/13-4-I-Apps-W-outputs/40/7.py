
def get_segments(n, k, absurdity):
    # Sort the absurdity list in descending order
    absurdity.sort(reverse=True)
    
    # Initialize the segments with the first k elements
    segments = absurdity[:k]
    
    # Iterate through the remaining elements
    for i in range(k, n):
        # If the current element is greater than the sum of the segments, add it to the segments
        if absurdity[i] > sum(segments):
            segments.append(absurdity[i])
    
    # Return the segments with the minimum first element
    return segments

