
def get_segments(n, k, absurdity):
    # Sort the absurdity list in descending order
    absurdity.sort(reverse=True)
    
    # Initialize the segments with the first k elements
    segments = absurdity[:k]
    
    # Iterate through the remaining elements
    for i in range(k, n):
        # If the current element is greater than the smallest element in the segment, replace it
        if absurdity[i] > segments[0]:
            segments[0] = absurdity[i]
            segments.sort(reverse=True)
    
    # Return the segments with the maximum total absurdity
    return segments[:k]

