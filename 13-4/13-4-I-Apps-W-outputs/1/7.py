
def get_absurdity_value(n, k, x):
    # Calculate the total absurdity value for each segment
    total_absurdity = [0] * (n - k + 1)
    for i in range(n):
        total_absurdity[i] += x[i]
        if i + k < n:
            total_absurdity[i + 1] -= x[i]
    
    # Find the maximum total absurdity value
    max_absurdity = max(total_absurdity)
    
    # Find the segments with the maximum total absurdity value
    segments = []
    for i in range(n - k + 1):
        if total_absurdity[i] == max_absurdity:
            segments.append(i)
    
    # Return the segments with the maximum total absurdity value
    return segments

def get_optimal_segments(n, k, x):
    # Get the absurdity value for each law
    absurdity = [0] * n
    for i in range(n):
        absurdity[i] = x[i]
    
    # Sort the laws by absurdity value in descending order
    sorted_laws = sorted(range(n), key=lambda i: absurdity[i], reverse=True)
    
    # Initialize the optimal segments
    optimal_segments = []
    
    # Loop through the sorted laws and add them to the optimal segments
    for i in range(n):
        # If the current law is not already in an optimal segment, add it to a new segment
        if not any(sorted_laws[i] in segment for segment in optimal_segments):
            optimal_segments.append([sorted_laws[i]])
        # Otherwise, add the current law to the existing optimal segment with the minimum number of laws
        else:
            min_segment = min(optimal_segments, key=len)
            min_segment.append(sorted_laws[i])
    
    # Return the optimal segments
    return optimal_segments

def get_optimal_signature(n, k, x):
    # Get the absurdity value for each law
    absurdity = [0] * n
    for i in range(n):
        absurdity[i] = x[i]
    
    # Sort the laws by absurdity value in descending order
    sorted_laws = sorted(range(n), key=lambda i: absurdity[i], reverse=True)
    
    # Initialize the optimal signature
    optimal_signature = []
    
    # Loop through the sorted laws and add them to the optimal signature
    for i in range(n):
        # If the current law is not already in the optimal signature, add it
        if not any(sorted_laws[i] in signature for signature in optimal_signature):
            optimal_signature.append(sorted_laws[i])
        # Otherwise, stop adding laws to the optimal signature
        else:
            break
    
    # Return the optimal signature
    return optimal_signature

def main():
    # Read the input
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    
    # Get the optimal segments
    segments = get_optimal_segments(n, k, x)
    
    # Get the optimal signature
    signature = get_optimal_signature(n, k, x)
    
    # Print the optimal segments
    print(segments)
    
    # Print the optimal signature
    print(signature)

if __name__ == '__main__':
    main()

