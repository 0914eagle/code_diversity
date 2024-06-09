
def get_smallest_diff(A, K, Q):
    # Sort the array in ascending order
    A.sort()
    # Initialize the smallest difference and the largest and smallest elements removed
    smallest_diff = float('inf')
    largest_removed = -1
    smallest_removed = -1
    # Loop through each contiguous subsequence of length K
    for i in range(len(A) - K + 1):
        # Get the minimum element in the subsequence
        min_element = A[i]
        # Get the maximum and minimum elements removed in this operation
        max_removed = A[i + K - 1]
        min_removed = A[i]
        # Update the smallest difference, largest and smallest elements removed
        diff = max_removed - min_removed
        if diff < smallest_diff:
            smallest_diff = diff
            largest_removed = max_removed
            smallest_removed = min_removed
    # Return the smallest difference and the largest and smallest elements removed
    return smallest_diff, largest_removed, smallest_removed

def main():
    # Read the input data from stdin
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    # Get the smallest difference and the largest and smallest elements removed
    smallest_diff, largest_removed, smallest_removed = get_smallest_diff(A, K, Q)
    # Print the smallest difference
    print(smallest_diff)

if __name__ == '__main__':
    main()

