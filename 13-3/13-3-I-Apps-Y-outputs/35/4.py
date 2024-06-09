
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
    
    # Check if the last cell is 0
    if a[-1] == 0:
        return "NO"
    
    # Initialize the maximum distance of the jump
    max_distance = d
    
    # Loop through each cell in the array
    for i in range(n + 2):
        # Check if the current cell is not 0
        if a[i] != 0:
            # Get the platform number of the current cell
            platform = a[i]
            
            # Loop through each cell in the platform
            for j in range(c[platform - 1]):
                # Check if the current cell is not 0
                if a[i + j + 1] == 0:
                    # Set the current cell to the platform number
                    a[i + j + 1] = platform
                    
                    # Decrement the maximum distance of the jump
                    max_distance -= 1
                    
                    # Check if the maximum distance of the jump is 0
                    if max_distance == 0:
                        # Break the loop
                        break
    
    # Check if the last cell is 0
    if a[-1] == 0:
        return "NO"
    
    # Return the array a
    return "YES\n" + " ".join(str(x) for x in a[1:-1])

