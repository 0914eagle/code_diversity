
def get_absurdity_segments(n, k, absurdity):
    # Sort the absurdity values in descending order
    absurdity.sort(reverse=True)
    
    # Initialize the segments with the first k absurdity values
    segment_1 = absurdity[:k]
    segment_2 = absurdity[k:]
    
    # Calculate the total absurdity of the signed laws
    total_absurdity = sum(segment_1) + sum(segment_2)
    
    return segment_1, segment_2, total_absurdity

def get_optimal_segments(n, k, absurdity):
    # Initialize the optimal segments and total absurdity
    optimal_segment_1 = []
    optimal_segment_2 = []
    optimal_total_absurdity = 0
    
    # Iterate over all possible segments
    for i in range(n - k + 1):
        for j in range(i + k, n + 1):
            # Get the absurdity segments and total absurdity for the current segment
            segment_1, segment_2, total_absurdity = get_absurdity_segments(n, k, absurdity[i:j])
            
            # Check if the current segment is optimal
            if total_absurdity > optimal_total_absurdity:
                optimal_segment_1 = segment_1
                optimal_segment_2 = segment_2
                optimal_total_absurdity = total_absurdity
    
    return optimal_segment_1, optimal_segment_2, optimal_total_absurdity

def main():
    n, k = map(int, input().split())
    absurdity = list(map(int, input().split()))
    
    segment_1, segment_2, total_absurdity = get_optimal_segments(n, k, absurdity)
    
    print(segment_1)
    print(segment_2)
    print(total_absurdity)

if __name__ == '__main__':
    main()

