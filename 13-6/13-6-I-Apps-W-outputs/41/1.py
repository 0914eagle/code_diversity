
def solve(n, k, l, d):
    # Initialize variables
    x = 0
    t = 0
    p = [i for i in range(0, 2*k)]

    # Loop through each second
    for i in range(0, n):
        # Calculate the current depth at position x
        depth = d[x] + p[t % 2*k]

        # Check if Koa can swim or not
        if depth <= l:
            x += 1
        t += 1

    # Check if Koa reached the island
    if x == n:
        return "Yes"
    else:
        return "No"

