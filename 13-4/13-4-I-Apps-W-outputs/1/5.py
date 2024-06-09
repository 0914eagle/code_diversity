
def get_absurdity_segments(n, k, absurdity):
    # Sort the absurdity list in descending order
    absurdity.sort(reverse=True)
    
    # Initialize the segments with the first k laws
    segment_1 = absurdity[:k]
    segment_2 = absurdity[k:]
    
    # Initialize the total absurdity of the signed laws
    total_absurdity = sum(segment_1) + sum(segment_2)
    
    # Loop through the remaining laws
    for i in range(k, n):
        # Check if the current law is more absurd than the current total absurdity
        if absurdity[i] > total_absurdity:
            # Add the current law to the first segment
            segment_1.append(absurdity[i])
            # Remove the current law from the second segment
            segment_2.remove(absurdity[i])
            # Update the total absurdity
            total_absurdity += absurdity[i]
    
    return segment_1, segment_2

def get_optimal_segments(n, k, absurdity):
    # Initialize the optimal segments
    optimal_segment_1 = []
    optimal_segment_2 = []
    
    # Loop through all possible segments
    for i in range(n - k + 1):
        for j in range(i + k, n + 1):
            # Get the absurdity segments for the current segment
            segment_1, segment_2 = get_absurdity_segments(n, k, absurdity[i:j])
            # Check if the current segment is more absurd than the current optimal segment
            if sum(segment_1) + sum(segment_2) > sum(optimal_segment_1) + sum(optimal_segment_2):
                # Update the optimal segments
                optimal_segment_1 = segment_1
                optimal_segment_2 = segment_2
    
    return optimal_segment_1, optimal_segment_2

def main():
    # Read the input
    n, k = map(int, input().split())
    absurdity = list(map(int, input().split()))
    
    # Get the optimal segments
    segment_1, segment_2 = get_optimal_segments(n, k, absurdity)
    
    # Print the optimal segments
    print(segment_1)
    print(segment_2)

if __name__ == '__main__':
    main()

