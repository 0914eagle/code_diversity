
def solve(n, k, l, d):
    # Initialize variables
    x = 0
    t = 0
    p = [0] * (2 * k)
    for i in range(1, 2 * k):
        p[i] = p[i - 1] + 1
    for i in range(1, k):
        p[i] = p[i - 1] - 1

    # Check if Koa can reach the island
    while x < n:
        # Check if Koa can swim to the next meter
        if d[x] + p[t % (2 * k)] <= l:
            x += 1
            t += 1
        else:
            t += 1

    # Return result
    if x == n:
        return "Yes"
    else:
        return "No"

