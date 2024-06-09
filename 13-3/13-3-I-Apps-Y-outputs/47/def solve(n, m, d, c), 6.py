
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
            
            # Check if the cell number is within the range of the platform
            if cell_number <= platform_length:
                # Assign the platform index to the cell
                a[cell_number] = i + 1
    
    # Loop through each cell in the river
    for i in range(1, n + 1):
        # Check if the cell is not already assigned to a platform
        if a[i] == 0:
            # Check if the cell is within the range of the jump distance
            if i + d <= n + 1:
                # Assign the platform index to the cell
                a[i] = a[i + d]
                jumps_made += 1
    
    # Check if all cells are assigned to a platform
    if all(a[i] != 0 for i in range(1, n + 1)):
        return "YES\n" + " ".join(str(x) for x in a[1:])
    else:
        return "NO"

