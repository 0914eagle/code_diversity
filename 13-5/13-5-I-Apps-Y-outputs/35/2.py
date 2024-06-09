
def get_min_height_difference(trees, k):
    # Sort the trees by height in descending order
    trees.sort(reverse=True)
    # Initialize the minimum height difference
    min_height_diff = float('inf')
    # Loop through the first k trees
    for i in range(k):
        # Get the height of the current tree
        curr_height = trees[i]
        # Loop through the remaining trees
        for j in range(i+1, k):
            # Get the height of the current tree
            next_height = trees[j]
            # Calculate the height difference
            height_diff = abs(curr_height - next_height)
            # Update the minimum height difference
            min_height_diff = min(min_height_diff, height_diff)
    # Return the minimum height difference
    return min_height_diff

