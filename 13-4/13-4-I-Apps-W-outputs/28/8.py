
def can_koa_reach_the_island(n, k, l, d):
    # Initialize variables
    x = 0
    t = 0
    p = [0, 1]

    # Loop through each second
    for i in range(n):
        # Calculate the current depth at position x
        depth = d[x] + p[t % 2]

        # Check if Koa can swim or not
        if depth <= l:
            x += 1
        else:
            return "No"

        # Update the time and position
        t += 1

    # Check if Koa has reached the island
    if x == n:
        return "Yes"
    else:
        return "No"

