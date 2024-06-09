
def solve(n, k, l, d):
    # Initialize variables
    x = 0
    t = 0
    p = [0, 1]
    while x < n:
        # Calculate current depth
        depth = d[x] + p[t % 2]
        # Check if Koa can swim or not
        if depth <= l:
            x += 1
            t += 1
        else:
            t += 1
    # Check if Koa reached the island
    if x == n:
        return "Yes"
    else:
        return "No"

