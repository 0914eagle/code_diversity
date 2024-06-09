
def can_koa_get_to_the_island(n, k, l, d):
    # Initialize variables
    x = 0
    t = 0
    p = [0, 1]

    # Loop through each second
    for second in range(n):
        # Calculate the current depth at Koa's position
        current_depth = d[x] + p[t % 2]

        # Check if Koa can swim or not
        if current_depth <= l:
            # Koa can swim, so she moves forward one meter
            x += 1
        else:
            # Koa can't swim, so she stays at the same position
            pass

        # Update the time and the array of depths
        t += 1
        p = [p[1], p[0]]

    # Check if Koa reached the island
    if x == n:
        return "Yes"
    else:
        return "No"

