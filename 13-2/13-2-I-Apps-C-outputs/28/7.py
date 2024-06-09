
def get_smallest_diff(A, K, Q):
    # Sort the array in ascending order
    A.sort()
    # Initialize the smallest difference
    smallest_diff = float('inf')
    # Loop through each possible starting index
    for i in range(len(A) - K + 1):
        # Get the subsequence of length K starting from index i
        subsequence = A[i:i+K]
        # Get the minimum element in the subsequence
        min_element = min(subsequence)
        # Get the index of the minimum element in the subsequence
        min_index = subsequence.index(min_element)
        # Remove the minimum element from the array
        A.remove(min_element)
        # Update the smallest difference
        smallest_diff = min(smallest_diff, min_element - A[min_index])
    # Return the smallest difference
    return smallest_diff

