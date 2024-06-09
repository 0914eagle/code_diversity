
def get_smallest_diff(A, K, Q):
    # Sort the array in non-decreasing order
    A.sort()
    # Initialize the smallest difference and the largest and smallest elements removed
    smallest_diff = float('inf')
    largest_removed = -1
    smallest_removed = float('inf')
    # Loop through each contiguous subsequence of length K
    for i in range(len(A) - K + 1):
        # Get the minimum element in the subsequence
        min_elem = A[i]
        # Get the maximum and minimum elements removed in this operation
        max_removed = max(A[i + K - 1], largest_removed)
        min_removed = min(A[i], smallest_removed)
        # Update the smallest difference
        smallest_diff = min(smallest_diff, max_removed - min_removed)
        # Update the largest and smallest elements removed
        largest_removed = max_removed
        smallest_removed = min_removed
    return smallest_diff

