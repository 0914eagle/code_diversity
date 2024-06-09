
def solve(n, k):
    # Initialize a list to store the colors of the costumes
    colors = [0] * n
    
    # Loop through each pair
    for i in range(n):
        # If this is an even pair, the man's color is the previous woman's color plus 1
        if i % 2 == 0:
            colors[i] = (colors[i-1] + 1) % k
        # If this is an odd pair, the man's color is the previous man's color plus 1
        else:
            colors[i] = (colors[i-1] + 1) % k
    
    # Loop through each pair again to check for conflicts
    for i in range(n):
        # If the man's color is the same as the previous woman's color, or the woman's color is the same as the previous man's color, it's a conflict
        if (colors[i] == colors[i-1] and i % 2 == 0) or (colors[i] == colors[(i-1)] and i % 2 == 1):
            return "NO"
    
    # If we reach this point, there are no conflicts, so we can return the colors
    return "YES\n" + "\n".join([str(colors[i]) + " " + str(colors[(i+1) % n]) for i in range(n)])

