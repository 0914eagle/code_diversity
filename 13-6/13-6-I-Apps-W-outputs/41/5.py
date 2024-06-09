
def can_koa_reach_island(depths, k, l):
    # Initialize variables
    x = 0
    t = 0
    p = [0] * (2 * k)
    for i in range(k):
        p[i] = 1
        p[k + i] = -1

    # Loop through each depth and check if Koa can reach the island
    for i in range(len(depths)):
        # Calculate the current depth at this position
        current_depth = depths[i] + p[t % (2 * k)]

        # Check if Koa can swim to the next position
        if x + 1 <= n and current_depth <= l:
            x += 1
            t += 1
        else:
            return "No"

    # Check if Koa has reached the island
    if x == n:
        return "Yes"
    else:
        return "No"

