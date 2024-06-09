
def can_koa_get_to_the_island(n, k, l, d):
    # Initialize variables
    x = 0
    t = 0
    p = [0] * (2 * k)
    for i in range(1, 2 * k):
        p[i] = p[i - 1] + 1
    for i in range(1, k):
        p[i] = p[i - 1] - 1

    # Loop through each second
    while x < n:
        # Check if Koa can swim to the next meter
        if d[x] + p[t % (2 * k)] <= l:
            x += 1
        t += 1

    # Return whether Koa reached the island
    return x == n

