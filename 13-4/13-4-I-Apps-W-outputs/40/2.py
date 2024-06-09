
def get_segments(n, k, absurdity):
    # Sort the absurdity list in descending order
    absurdity.sort(reverse=True)
    
    # Initialize the segments with the first k elements
    segments = absurdity[:k]
    
    # Loop through the remaining elements
    for i in range(k, n):
        # If the current element is greater than the smallest element in the segment, replace it
        if absurdity[i] > segments[0]:
            segments[0] = absurdity[i]
            segments.sort(reverse=True)
    
    # Return the segments
    return segments

def get_optimal_segments(n, k, absurdity):
    # Get the optimal segments
    segments = get_segments(n, k, absurdity)
    
    # Initialize the optimal segments with the first segment
    optimal_segments = [segments[0]]
    
    # Loop through the remaining segments
    for i in range(1, len(segments)):
        # If the current segment is different from the previous segment, add it to the list of optimal segments
        if segments[i] != segments[i-1]:
            optimal_segments.append(segments[i])
    
    # Return the optimal segments
    return optimal_segments

def get_a_and_b(n, k, absurdity):
    # Get the optimal segments
    segments = get_optimal_segments(n, k, absurdity)
    
    # Initialize a and b with the first segment
    a = segments[0]
    b = segments[1]
    
    # Loop through the remaining segments
    for i in range(2, len(segments)):
        # If the current segment is different from the previous segment, update a and b
        if segments[i] != segments[i-1]:
            a = segments[i]
            b = segments[i+1]
    
    # Return a and b
    return a, b

n, k = map(int, input().split())
absurdity = list(map(int, input().split()))
a, b = get_a_and_b(n, k, absurdity)
print(a, b)

