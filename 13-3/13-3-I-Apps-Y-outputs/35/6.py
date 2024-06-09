
def solve(n, m, d, c):
    # Initialize the array a with 0s
    a = [0] * (n + 2)
    
    # Loop through each platform
    for i in range(m):
        # Get the length of the current platform
        length = c[i]
        
        # Loop through each cell in the platform
        for j in range(length):
            # Set the cell to the current platform number
            a[j + 1] = i + 1
    
    # Check if the last cell is equal to the number of platforms
    if a[n] == m:
        return "YES"
    else:
        return "NO"

