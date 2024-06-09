
def solve(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize the minimum time as 0
    min_time = 0

    # While the height of Xaniar is not equal to a1 or the height of Abol is not equal to a2
    while h1 != a1 or h2 != a2:
        # Increment the minimum time by 1
        min_time += 1

        # Calculate the new height of Xaniar and Abol
        h1 = (x1 * h1 + y1) % m
        h2 = (x2 * h2 + y2) % m

    # Return the minimum time
    return min_time

