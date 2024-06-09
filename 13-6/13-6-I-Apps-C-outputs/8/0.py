
def get_smallest_difference(A, K, Q):
    # Sort the array in non-decreasing order
    A.sort()
    
    # Initialize the smallest difference
    smallest_difference = float('inf')
    
    # Loop through each possible starting index for the contiguous subsequence
    for i in range(len(A) - K + 1):
        # Get the contiguous subsequence
        subsequence = A[i:i+K]
        
        # Get the minimum element in the subsequence
        minimum = min(subsequence)
        
        # Get the index of the minimum element in the subsequence
        minimum_index = subsequence.index(minimum)
        
        # Get the largest element in the subsequence
        largest = max(subsequence)
        
        # Get the index of the largest element in the subsequence
        largest_index = subsequence.index(largest)
        
        # Calculate the difference between the largest and smallest elements
        difference = largest - minimum
        
        # If the difference is smaller than the current smallest difference, update the smallest difference
        if difference < smallest_difference:
            smallest_difference = difference
    
    # Return the smallest difference
    return smallest_difference

def main():
    # Read the input
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Get the smallest difference
    smallest_difference = get_smallest_difference(A, K, Q)
    
    # Print the smallest difference
    print(smallest_difference)

if __name__ == '__main__':
    main()

