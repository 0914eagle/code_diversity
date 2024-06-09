
def get_segments(n, k, absurdity):
    # Sort the absurdity list in descending order
    absurdity.sort(reverse=True)
    
    # Initialize the segments with the first k laws
    segments = absurdity[:k]
    
    # Iterate through the remaining laws
    for i in range(k, n):
        # If the current law is more absurd than the minimum absurdity in either segment, add it to the segment with the minimum absurdity
        if absurdity[i] > min(segments):
            if absurdity[i] > segments[0]:
                segments[0] = absurdity[i]
            else:
                segments[1] = absurdity[i]
    
    # Return the segments with the minimum total absurdity
    return segments

