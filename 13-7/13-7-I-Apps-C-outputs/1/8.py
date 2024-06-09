
def solve(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize the minimum time as 0
    min_time = 0
    # Initialize the current heights of Xaniar and Abol as their initial values
    curr_h1, curr_h2 = h1, h2
    # Loop until the conditions are met or the minimum time exceeds 10^9
    while curr_h1 != a1 or curr_h2 != a2:
        # Increment the minimum time by 1
        min_time += 1
        # Calculate the new heights of Xaniar and Abol
        curr_h1 = (x1 * curr_h1 + y1) % m
        curr_h2 = (x2 * curr_h2 + y2) % m
        # If the minimum time exceeds 10^9, return -1
        if min_time > 10**9:
            return -1
    # Return the minimum time
    return min_time

