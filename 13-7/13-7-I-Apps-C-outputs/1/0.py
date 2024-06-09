
def solve(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize the minimum time as 0
    min_time = 0

    # Check if the initial heights are the same
    if h1 == a1 and h2 == a2:
        return min_time

    # Check if the initial heights are not the same and the modulo is 1
    if h1 != a1 and h2 != a2 and m == 1:
        return -1

    # Initialize the current heights as the initial heights
    curr_h1 = h1
    curr_h2 = h2

    # Loop until the current heights are the same as the desired heights
    while curr_h1 != a1 or curr_h2 != a2:
        # Update the current heights
        curr_h1 = (x1 * curr_h1 + y1) % m
        curr_h2 = (x2 * curr_h2 + y2) % m

        # Increment the minimum time
        min_time += 1

    # Return the minimum time
    return min_time

