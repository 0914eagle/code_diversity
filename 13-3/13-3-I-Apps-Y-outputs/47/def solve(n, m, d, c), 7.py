
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
            
            # Check if the cell is already occupied by a platform
            if a[cell_number] != 0:
                # If the cell is occupied, return NO
                return "NO"
            
            # Assign the current platform to the cell
            a[cell_number] = i + 1
            
            # Check if the cell is within the maximum jump distance
            if cell_number - jumps_made <= d:
                # If the cell is within the maximum jump distance, increment the number of jumps made
                jumps_made += 1
    
    # Check if the final cell is reachable
    if a[n + 1] == 0:
        # If the final cell is not reachable, return NO
        return "NO"
    
    # Return YES and the array a
    return "YES\n" + " ".join(str(x) for x in a)

