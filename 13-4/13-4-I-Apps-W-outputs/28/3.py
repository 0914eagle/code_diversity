
def solve(n, k, l, d):
    # Initialize variables
    x = 0
    t = 0
    p = [0, 1]
    
    # Loop through each second
    for i in range(n):
        # Calculate the current depth
        depth = d[i] + p[t % 2]
        
        # Check if Koa can swim or not
        if depth <= l:
            x += 1
        else:
            x = x
        
        # Update the time and p
        t += 1
        p = [p[1], p[0]]
    
    # Check if Koa reached the island
    if x == n:
        return "Yes"
    else:
        return "No"

