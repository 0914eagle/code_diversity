
def solve_cube(k):
    # Check if k is valid
    if k < 1 or k > 100:
        return "-1"
    
    # Initialize the cube with all units as white
    cube = [[0] * k for _ in range(k)]
    
    # Loop through each layer of the cube
    for layer in range(k):
        # Loop through each unit in the layer
        for row in range(k):
            for col in range(k):
                # Check if the unit is on the boundary of the cube
                if layer == 0 or layer == k-1 or row == 0 or row == k-1 or col == 0 or col == k-1:
                    # If it is on the boundary, paint it black
                    cube[layer][row][col] = 1
                else:
                    # If it is not on the boundary, paint it white
                    cube[layer][row][col] = 0
    
    # Return the painted cube
    return cube

