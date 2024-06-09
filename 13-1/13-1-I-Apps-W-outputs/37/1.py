
def max_blocks_removed(n, m, a):
    # Initialize variables
    top_view_removed = 0
    side_view_removed = 0

    # Iterate through the stacks
    for i in range(n):
        # Check if the top view is not changed
        if a[i] - top_view_removed > m:
            top_view_removed += a[i] - m

        # Check if the side view is not changed
        if a[i] - side_view_removed > m:
            side_view_removed += a[i] - m

    # Return the maximum number of blocks that can be removed
    return top_view_removed + side_view_removed

