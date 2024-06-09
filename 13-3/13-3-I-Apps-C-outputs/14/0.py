
def solve(A, K, Q):
    # Sort the input array
    A.sort()
    
    # Initialize the smallest and largest values removed
    smallest, largest = A[K-1], A[N-K]
    
    # Loop through each contiguous subsequence of length K
    for i in range(N-K+1):
        # Remove the smallest element in the subsequence
        current_smallest = A[i]
        A.remove(current_smallest)
        
        # Update the largest and smallest values removed
        if current_smallest < smallest:
            smallest = current_smallest
        if A[i+K-1] > largest:
            largest = A[i+K-1]
        
        # Add the removed element back to the array
        A.insert(i, current_smallest)
    
    # Return the difference between the largest and smallest values removed
    return largest - smallest

