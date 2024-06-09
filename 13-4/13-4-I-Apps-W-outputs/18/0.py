
def solve(a, b, w, x, c):
    # Initialize variables
    arthur_time = 0
    alexander_time = 0
    arthur_ahead = False

    # Loop until Alexander gets ahead of Arthur
    while not arthur_ahead:
        # Arthur's operation
        if b >= x:
            b -= x
        else:
            a -= 1
            b = w - (x - b)

        # Alexander's operation
        c -= 1

        # Check if Alexander is ahead of Arthur
        if c <= a:
            arthur_ahead = True

        # Increment time
        arthur_time += 1
        alexander_time += 1

    # Return the minimum time Alexander needs to get ahead of Arthur
    return alexander_time

