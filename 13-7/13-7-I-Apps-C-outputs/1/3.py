
def solve(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize the minimum time and the current heights
    min_time = 0
    curr_h1 = h1
    curr_h2 = h2

    # Loop until the heights of Xaniar and Abol are equal to a1 and a2 respectively
    while curr_h1 != a1 or curr_h2 != a2:
        # Calculate the next heights of Xaniar and Abol
        next_h1 = (x1 * curr_h1 + y1) % m
        next_h2 = (x2 * curr_h2 + y2) % m

        # Update the current heights
        curr_h1 = next_h1
        curr_h2 = next_h2

        # Increment the minimum time
        min_time += 1

    # Return the minimum time if the heights are equal, otherwise return -1
    return min_time if curr_h1 == a1 and curr_h2 == a2 else -1

