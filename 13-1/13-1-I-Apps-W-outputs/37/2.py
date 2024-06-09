
def max_blocks_removable(n, m, a):
    # Initialize variables
    top_view_removable = 0
    side_view_removable = 0

    # Iterate through each stack
    for i in range(n):
        # Check if the stack is tall enough to remove blocks
        if a[i] > m:
            # Calculate the number of removable blocks for the top view
            top_view_removable += a[i] - m

            # Calculate the number of removable blocks for the side view
            side_view_removable += min(a[i], m)

    # Return the minimum number of removable blocks
    return min(top_view_removable, side_view_removable)

