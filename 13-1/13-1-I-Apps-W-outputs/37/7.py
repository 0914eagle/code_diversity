
def max_blocks_removed(n, m, a):
    # Initialize variables
    top_view_removed = 0
    side_view_removed = 0
    max_removed = 0

    # Iterate through each stack
    for i in range(n):
        # Check if the top view of the stack is visible
        if a[i] > m - top_view_removed:
            # If not, remove blocks from the top of the stack until it is visible
            top_view_removed += a[i] - (m - top_view_removed)

        # Check if the side view of the stack is visible
        if a[i] > m - side_view_removed:
            # If not, remove blocks from the side of the stack until it is visible
            side_view_removed += a[i] - (m - side_view_removed)

    # Return the maximum number of blocks removed
    return top_view_removed + side_view_removed

