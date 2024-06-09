
def max_blocks_removed(n, m, a):
    # Initialize variables
    top_view_blocks = 0
    side_view_blocks = 0
    max_removed_blocks = 0

    # Iterate through each stack
    for i in range(n):
        # Check if the stack has more blocks than the height of the exhibit
        if a[i] > m:
            # If so, remove all blocks from the stack
            top_view_blocks += m
            side_view_blocks += a[i] - m
            max_removed_blocks += a[i] - m
        else:
            # If not, remove only the number of blocks that exceed the height of the exhibit
            top_view_blocks += a[i]
            side_view_blocks += a[i]
            max_removed_blocks += a[i]

    # Return the maximum number of blocks that can be removed
    return max_removed_blocks

