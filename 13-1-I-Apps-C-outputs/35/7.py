
def count_valid_colorings(n, a):
    # Initialize the number of valid colorings to 0
    num_valid_colorings = 0
    
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
            
            # If the current hexagon is colored, check if it forms a valid loop
            valid_loop = True
            
            # Loop through each neighbor of the current hexagon
            for k in range(1, num_hexagons+1):
                # If the neighbor is not colored, skip it
                if a[i-1][k-1] == -1:
                    continue
                
                # If the neighbor is colored and is not the current hexagon, check if it forms a valid loop
                if k != j and a[i-1][k-1] != a[i-1][j-1]:
                    valid_loop = False
                    break
            
            # If the current hexagon forms a valid loop, increment the number of valid colorings
            if valid_loop:
                num_valid_colorings += 1
    
    # Return the number of valid colorings
    return num_valid_colorings

