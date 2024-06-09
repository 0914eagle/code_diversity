
def can_koa_reach_island(n, k, l, d):
    # Initialize variables
    x = 0
    t = 0
    p = [i for i in range(0, 2*k)]

    # Loop through each second
    while x < n:
        # Check if Koa can swim to the next meter
        if d[x] + p[t%(2*k)] <= l:
            x += 1
        t += 1

    # Return whether Koa reached the island
    return x == n

