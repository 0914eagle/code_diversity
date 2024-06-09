
def solve(n, m, d, c):
    # Initialize the array a with 0s
    a = [0] * (n + 2)
    
    # Initialize the number of jumps made
    jumps_made = 0
    
    # Loop through each platform
    for i in range(m):
        # Get the length of the current platform
        platform_length = c[i]
        
        # Loop through each cell in the platform
        for j in range(platform_length):
            # Get the current cell number
            cell_number = j + 1
            
            # Check if the cell is not already occupied by a platform
            if a[cell_number] == 0:
                # Mark the cell as occupied by the current platform
                a[cell_number] = i + 1
                
                # Check if the cell is the last cell in the platform
                if j == platform_length - 1:
                    # Increment the number of jumps made
                    jumps_made += 1
                    
                    # Check if the number of jumps made is equal to the maximum distance of the jump
                    if jumps_made == d:
                        # Reset the number of jumps made
                        jumps_made = 0
                        
                        # Break out of the inner loop
                        break
    
    # Check if the last cell is occupied by a platform
    if a[n + 1] == 0:
        # Return NO
        return "NO"
    
    # Return YES and the array a
    return "YES\n" + " ".join(map(str, a[1:]))

