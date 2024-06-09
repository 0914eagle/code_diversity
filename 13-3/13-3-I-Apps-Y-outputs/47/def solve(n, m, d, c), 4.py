
def solve(n, m, d, c):
    # Initialize the array a with 0s
    a = [0] * (n + 2)
    
    # Initialize the number of jumps as 0
    jumps = 0
    
    # Loop through each platform
    for i in range(m):
        # Get the length of the current platform
        length = c[i]
        
        # Loop through each cell in the platform
        for j in range(length):
            # Get the current cell number
            cell = j + 1
            
            # If the cell is not the last cell in the platform, set the next cell to 1
            if j < length - 1:
                a[cell] = 1
            
            # If the cell is the last cell in the platform, set the next cell to 2
            else:
                a[cell] = 2
            
            # Increment the number of jumps
            jumps += 1
    
    # If the number of jumps is greater than or equal to the maximum distance, return YES
    if jumps >= d:
        return "YES"
    
    # Otherwise, return NO
    else:
        return "NO"

