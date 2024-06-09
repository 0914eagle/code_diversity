
def solve(A, K, Q):
    # Sort the input array
    A.sort()
    
    # Initialize the smallest and largest values removed
    smallest, largest = A[K-1], A[N-1]
    
    # Loop through each operation
    for i in range(Q):
        # Find the smallest element in the current subsequence
        smallest_element = A[i]
        for j in range(1, K):
            if A[i+j] < smallest_element:
                smallest_element = A[i+j]
        # Remove the smallest element from the array
        A.remove(smallest_element)
        # Update the smallest and largest values removed
        smallest = min(smallest, smallest_element)
        largest = max(largest, A[N-1])
    
    # Return the difference between the smallest and largest values removed
    return largest - smallest

