
def solve_cube(k):
    # Check if the input is valid
    if k < 1 or k > 100:
        return -1
    
    # Initialize the cube with all units as white
    cube = [[("w" for _ in range(k)) for _ in range(k)] for _ in range(k)]
    
    # Iterate through each layer of the cube
    for layer in range(k):
        # Iterate through each row of the layer
        for row in range(k):
            # Iterate through each column of the row
            for col in range(k):
                # Check if the current unit is white
                if cube[layer][row][col] == "w":
                    # Check if the unit has exactly 2 neighboring units of the same color
                    num_neighbors = 0
                    for neighbor in [(layer, row-1, col), (layer, row+1, col), (layer-1, row, col), (layer+1, row, col), (layer, row, col-1), (layer, row, col+1)]:
                        if 0 <= neighbor[0] < k and 0 <= neighbor[1] < k and 0 <= neighbor[2] < k and cube[neighbor[0]][neighbor[1]][neighbor[2]] == "w":
                            num_neighbors += 1
                    
                    # If the unit has exactly 2 neighboring units of the same color, make it black
                    if num_neighbors == 2:
                        cube[layer][row][col] = "b"
    
    # Return the painted cube
    return cube

