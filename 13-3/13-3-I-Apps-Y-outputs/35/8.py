
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
            
            # Check if the cell is the last cell in the platform
            if j == platform_length - 1:
                # If it is, increment the number of jumps made
                jumps_made += 1
                
                # Check if the maximum number of jumps has been reached
                if jumps_made == d:
                    # If it has, return YES
                    return "YES"
                    
    # If the code reaches this point, it means that all platforms have been placed
    # and the maximum number of jumps has not been reached
    return "NO"

