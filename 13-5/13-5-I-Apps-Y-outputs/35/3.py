
def solve(N, K, heights):
    # Sort the heights in non-decreasing order
    heights.sort()
    # Initialize the minimum difference to a large value
    min_diff = float('inf')
    # Loop through all possible combinations of K trees
    for i in range(N - K + 1):
        # Calculate the difference between the height of the tallest and shortest tree in this combination
        diff = heights[i + K - 1] - heights[i]
        # Update the minimum difference if necessary
        min_diff = min(min_diff, diff)
    # Return the minimum difference
    return min_diff

