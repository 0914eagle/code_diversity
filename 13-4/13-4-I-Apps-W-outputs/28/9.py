
def can_koa_get_to_island(n, k, l, depths):
    # Initialize variables
    x = 0
    t = 0
    p = [i for i in range(0, 2 * k, 1)]

    # Loop through each second
    for i in range(n):
        # Calculate the current depth at position x
        current_depth = depths[x] + p[t % 2 * k]

        # Check if Koa can swim or not
        if current_depth <= l:
            x += 1
        else:
            return "No"

        t += 1

    # Check if Koa reached the island
    if x == n:
        return "Yes"
    else:
        return "No"

