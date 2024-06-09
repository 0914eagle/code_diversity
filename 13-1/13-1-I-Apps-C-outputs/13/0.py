
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
        A.pop(i + min_index)
        # Update the smallest difference
        smallest_diff = min(smallest_diff, A[-1] - A[0])
        # Add the minimum element back to the array
        A.insert(i + min_index, min_element)
    return smallest_diff

