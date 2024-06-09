
def get_min_height_diff(heights, k):
    # Sort the heights in non-decreasing order
    heights.sort()
    # Initialize the minimum height difference
    min_diff = float('inf')
    # Loop through the heights and choose k trees
    for i in range(len(heights) - k + 1):
        # Get the height of the ith tree
        curr_height = heights[i]
        # Get the height of the (i+k)th tree
        next_height = heights[i + k - 1]
        # Calculate the height difference
        diff = next_height - curr_height
        # Update the minimum height difference
        min_diff = min(min_diff, diff)
    # Return the minimum height difference
    return min_diff

