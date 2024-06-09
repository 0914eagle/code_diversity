
def solve_cube(k):
    # Check if the input is valid
    if k < 1 or k > 100:
        return -1
    
    # Initialize the cube with all white color
    cube = [[0] * k for _ in range(k)]
    
    # Iterate through each layer of the cube
    for layer in range(k):
        # Iterate through each row of the layer
        for row in range(k):
            # Iterate through each column of the row
            for col in range(k):
                # Check if the current cell is white
                if cube[layer][row][col] == 0:
                    # Check if the current cell has exactly 2 white neighbors
                    neighbors = 0
                    for i in range(max(0, layer-1), min(k, layer+2)):
                        for j in range(max(0, row-1), min(k, row+2)):
                            for k in range(max(0, col-1), min(k, col+2)):
                                if i != layer or j != row or k != col:
                                    neighbors += cube[i][j][k]
                    if neighbors != 2:
                        return -1
    
    # Print the cube
    for layer in cube:
        for row in layer:
            print("".join(["w" if cell == 0 else "b" for cell in row]))
    
    return 0

