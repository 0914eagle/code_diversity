
def count_valid_colorings(n, a):
    # Initialize the number of valid colorings to 0
    valid_colorings = 0
    
    # Loop through each row of the grid
    for i in range(1, n+1):
        # If the row is odd, there are n hexagons in the row
        if i % 2 == 1:
            num_hexagons = n
        # If the row is even, there are n-1 hexagons in the row
        else:
            num_hexagons = n-1
        
        # Loop through each hexagon in the row
        for j in range(1, num_hexagons+1):
            # If the current hexagon is not colored, skip it
            if a[i-1][j-1] == -1:
                continue
            
            # If the current hexagon is colored, check if it is part of a valid loop
            valid_loop = False
            
            # Loop through each neighboring hexagon
            for k in range(1, num_hexagons+1):
                # If the neighboring hexagon is not colored, skip it
                if a[i-1][k-1] == -1:
                    continue
                
                # If the neighboring hexagon is colored and is part of a valid loop, set valid_loop to True
                if a[i-1][j-1] == a[i-1][k-1]:
                    valid_loop = True
                    break
            
            # If the current hexagon is not part of a valid loop, set valid_colorings to 0 and break out of the loop
            if not valid_loop:
                valid_colorings = 0
                break
    
    # Return the number of valid colorings
    return valid_colorings

