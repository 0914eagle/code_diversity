
def solve(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize the minimum time as 0
    min_time = 0

    # Initialize the current heights of Xaniar and Abol as h1 and h2 respectively
    current_h1 = h1
    current_h2 = h2

    # Loop until the heights of Xaniar and Abol are equal to a1 and a2 respectively
    while current_h1 != a1 or current_h2 != a2:
        # Increment the minimum time by 1
        min_time += 1

        # Update the current heights of Xaniar and Abol using the given equations
        current_h1 = (x1 * current_h1 + y1) % m
        current_h2 = (x2 * current_h2 + y2) % m

    # Return the minimum time required
    return min_time

