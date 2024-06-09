
def count_valid_colorings(n, grid):
    # Initialize a dictionary to store the number of valid colorings for each row
    valid_colorings = {i: 0 for i in range(1, n+1)}
    
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
            if grid[i][j] == -1:
                continue
            
            # If the current hexagon is colored, check if it forms a valid loop
            valid_loop = True
            
            # Loop through each neighboring hexagon
            for k in range(1, num_hexagons+1):
                # If the neighboring hexagon is not colored, skip it
                if grid[i][k] == -1:
                    continue
                
                # If the neighboring hexagon is colored and is not the current hexagon, check if it forms a valid loop
                if grid[i][k] != grid[i][j] and grid[i][k] != 6-grid[i][j]:
                    valid_loop = False
                    break
            
            # If the current hexagon forms a valid loop, increment the number of valid colorings for the row
            if valid_loop:
                valid_colorings[i] += 1
    
    # Return the sum of the number of valid colorings for all rows
    return sum(valid_colorings.values())

