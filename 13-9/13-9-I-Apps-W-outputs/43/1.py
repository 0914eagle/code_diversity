
def solve_cube(k):
    # Initialize a 3D array to store the painting of the cube
    cube = [[[None] * k for _ in range(k)] for _ in range(k)]

    # Iterate through each layer of the cube
    for layer in range(k):
        # Iterate through each row of the layer
        for row in range(k):
            # Iterate through each column of the row
            for col in range(k):
                # If the current cell is not painted, paint it with the opposite color of the neighbors
                if cube[layer][row][col] is None:
                    # Count the number of black neighbors
                    black_neighbors = 0
                    for i in range(max(0, layer-1), min(k, layer+2)):
                        for j in range(max(0, row-1), min(k, row+2)):
                            for k in range(max(0, col-1), min(k, col+2)):
                                if i != layer or j != row or k != col:
                                    if cube[i][j][k] == "b":
                                        black_neighbors += 1

                    # If the current cell has 2 black neighbors, paint it black
                    if black_neighbors == 2:
                        cube[layer][row][col] = "b"
                    # Otherwise, paint it white
                    else:
                        cube[layer][row][col] = "w"

    # Print the painting of the cube
    for layer in cube:
        for row in layer:
            print("".join(row))

    return cube

