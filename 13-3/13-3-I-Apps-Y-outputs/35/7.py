
def solve(n, m, d, c):
    # Initialize the array a as all zeros
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
            
            # If the cell is not the last cell in the platform, set the cell number in the array a
            if j < length - 1:
                a[cell] = i + 1
            
            # If the cell is the last cell in the platform, set the cell number in the array a and increment the number of jumps
            else:
                a[cell] = i + 1
                jumps += 1
    
    # If the number of jumps is greater than or equal to d, return YES and the array a
    if jumps >= d:
        return "YES\n" + " ".join(map(str, a[1:]))
    
    # Otherwise, return NO
    else:
        return "NO"

