
def solve(n, m, d, c):
    # Initialize the array a with 0s
    a = [0] * (n + 2)
    
    # Initialize the number of platforms on each cell
    num_platforms = [0] * (n + 2)
    
    # Loop through each platform
    for i in range(m):
        # Loop through each cell in the platform
        for j in range(c[i]):
            # Increment the number of platforms on the cell
            num_platforms[i + j] += 1
    
    # Loop through each cell
    for i in range(n + 2):
        # If the cell has at least one platform, set its value to the index of the platform
        if num_platforms[i] > 0:
            a[i] = num_platforms[i]
    
    return "YES\n" + " ".join(str(x) for x in a[1:-1])

