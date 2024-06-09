
def solve(n, k, l, d):
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
        if x + 1 <= n and d[x + 1] + p[t % (2 * k)] <= l:
            x += 1
        # If not, wait a second
        else:
            x = x
        t += 1

    # Return whether Koa made it to the island
    return "Yes" if x == n else "No"

