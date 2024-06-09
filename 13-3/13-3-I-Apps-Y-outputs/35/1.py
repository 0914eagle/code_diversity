
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
            
            # Check if the cell is not already occupied by a platform
            if a[cell] == 0:
                # Occupy the cell with the current platform number
                a[cell] = i + 1
                
                # Increment the number of jumps
                jumps += 1
                
                # Check if the maximum number of jumps has been reached
                if jumps == d:
                    # Return the array a
                    return a
    
    # If the maximum number of jumps has not been reached, return NO
    return "NO"

