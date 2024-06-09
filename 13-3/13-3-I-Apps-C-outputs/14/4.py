
def solve(A, K, Q):
    # Sort the input array
    A.sort()
    
    # Initialize the smallest and largest values removed
    smallest, largest = A[K-1], A[N-1]
    
    # Loop through each operation
    for i in range(Q):
        # Remove the smallest element in the current subsequence
        smallest = min(smallest, A[i+K-1])
        # Remove the largest element in the current subsequence
        largest = max(largest, A[i+N-K])
    
    # Return the difference between the smallest and largest values removed
    return largest - smallest

