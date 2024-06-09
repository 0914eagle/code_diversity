
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
            
            # Check if the cell is already occupied by a platform
            if a[cell] != 0:
                # If the cell is occupied, return NO
                return "NO"
            
            # Assign the current platform to the cell
            a[cell] = i + 1
    
    # Loop through each cell in the river
    for i in range(1, n + 1):
        # Check if the cell is occupied by a platform
        if a[i] != 0:
            # If the cell is occupied, continue to the next cell
            continue
        
        # Check if the cell is within the maximum jump distance
        if i - jumps > d:
            # If the cell is not within the maximum jump distance, return NO
            return "NO"
        
        # Increment the number of jumps
        jumps += 1
    
    # If all cells are visited and no platform is occupied, return YES
    return "YES"

