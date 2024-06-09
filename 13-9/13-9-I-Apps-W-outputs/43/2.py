
def solve_cube(k):
    if k > 100 or k < 1:
        return -1
    
    # Initialize the cube with all white cubes
    cube = [[0] * k for _ in range(k)]
    
    # Iterate through each layer of the cube
    for layer in range(k):
        # Iterate through each row of the layer
        for row in range(k):
            # Iterate through each column of the row
            for col in range(k):
                # If the cube is in the first or last row, make it black
                if layer in [0, k-1] or row in [0, k-1] or col in [0, k-1]:
                    cube[layer][row][col] = 1
                # If the cube is in the second or second-to-last row, make it white
                else:
                    cube[layer][row][col] = 0
    
    # Return the cube
    return cube

