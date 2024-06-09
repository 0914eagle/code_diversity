
def can_koa_get_to_the_island(n, k, l, d):
    # Initialize variables
    x = 0
    t = 0
    p = [i for i in range(0, 2*k)]

    # Loop through each second
    while x < n:
        # Check if Koa can swim to the next meter
        if d[x] + p[t%(2*k)] <= l:
            x += 1
        # Koa stays at the current meter
        else:
            x = x
        # Increment time
        t += 1

    # Check if Koa reached the island
    if x == n:
        return "Yes"
    else:
        return "No"

