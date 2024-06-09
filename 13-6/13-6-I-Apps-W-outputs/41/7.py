
def solve(n, k, l, d):
    # Initialize variables
    x = 0
    t = 0
    p = [0, 1]
    while x < n:
        # Check if Koa can swim to the next meter
        if x + 1 <= n and d[x] + p[t % 2] <= l:
            x += 1
        # If not, wait for one second
        else:
            x = x
        # Increment time
        t += 1
    # Check if Koa reached the island
    if x == n:
        return "Yes"
    else:
        return "No"

