
def can_koa_get_to_the_island(n, k, l, depths):
    # Initialize variables
    x = 0
    t = 0
    p = [0] * (2 * k)
    for i in range(1, k):
        p[i] = 1
    for i in range(k, 2 * k):
        p[i] = -1

    # Loop through each second
    while x < n:
        # Check if Koa can swim to the next meter
        if x + 1 <= n and depths[x + 1] + p[t % (2 * k)] <= l:
            x += 1
        # Check if Koa can stay at the current meter
        elif depths[x] + p[t % (2 * k)] <= l:
            pass
        # Koa cannot swim or stay, she will drown
        else:
            return "No"
        t += 1

    # Koa has reached the island
    if x == n:
        return "Yes"
    else:
        return "No"

