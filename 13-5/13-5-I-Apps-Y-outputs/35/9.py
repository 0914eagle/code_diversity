
def get_min_height_diff(trees, k):
    # Sort the trees by height in descending order
    trees.sort(reverse=True)
    # Initialize the minimum height difference
    min_height_diff = float('inf')
    # Loop through the first k trees
    for i in range(k):
        # Get the height of the current tree
        height = trees[i]
        # Calculate the height difference between this tree and the previous tree
        if i > 0:
            height_diff = abs(height - trees[i-1])
        else:
            height_diff = 0
        # Update the minimum height difference if necessary
        if height_diff < min_height_diff:
            min_height_diff = height_diff
    return min_height_diff

