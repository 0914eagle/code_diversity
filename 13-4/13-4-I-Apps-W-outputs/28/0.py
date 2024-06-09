
def can_koa_reach_island(n, k, l, depths):
    # Initialize variables
    x = 0
    t = 0
    p = [0, 1]
    while x < n:
        # Check if Koa can swim to the next meter
        if x + 1 <= n and depths[x + 1] + p[t % 2] <= l:
            x += 1
        # Check if Koa can stay at the current meter
        elif depths[x] + p[t % 2] <= l:
            pass
        # Koa cannot swim or stay, she will drown
        else:
            return "No"
        t += 1
    # Koa has reached the island
    return "Yes"

