
def solve(N, K, heights):
    # Sort the heights in non-decreasing order
    heights.sort()
    # Initialize the minimum difference to a large value
    min_diff = float('inf')
    # Iterate over the possible starting indices for the K decorated trees
    for i in range(N - K + 1):
        # Calculate the difference between the height of the Kth decorated tree and the height of the ith decorated tree
        diff = heights[i + K - 1] - heights[i]
        # Update the minimum difference if necessary
        min_diff = min(min_diff, diff)
    # Return the minimum difference
    return min_diff

