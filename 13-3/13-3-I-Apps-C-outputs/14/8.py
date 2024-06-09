
def solve(A, K, Q):
    # Sort the array in ascending order
    A.sort()
    
    # Initialize the smallest and largest elements removed
    smallest, largest = float('inf'), -float('inf')
    
    # Loop through each contiguous subsequence of length K
    for i in range(len(A) - K + 1):
        # Find the smallest and largest elements in the subsequence
        smallest_subsequence = min(A[i:i+K])
        largest_subsequence = max(A[i:i+K])
        
        # Update the smallest and largest elements removed
        smallest = min(smallest, smallest_subsequence)
        largest = max(largest, largest_subsequence)
    
    # Return the difference between the smallest and largest elements removed
    return largest - smallest

