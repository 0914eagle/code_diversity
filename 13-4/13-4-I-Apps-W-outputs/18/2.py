
def solve(a, b, w, x, c):
    # Initialize variables
    arthur_time = 0
    alan_time = 0
    arthur_ahead = False

    # Loop until Alan gets ahead of Arthur
    while not arthur_ahead:
        # Update Arthur's time
        if b >= x:
            b -= x
        else:
            a -= 1
            b = w - (x - b)
        arthur_time += 1

        # Update Alan's time
        c -= 1
        alan_time += 1

        # Check if Alan is ahead of Arthur
        if c <= a:
            arthur_ahead = True

    # Return the minimum time needed for Alan to get ahead of Arthur
    return alan_time

