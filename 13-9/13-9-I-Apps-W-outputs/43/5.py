
def solve_cube(k):
    # Check if the input is valid
    if k < 1 or k > 100:
        return "-1"
    
    # Initialize the cube with all white units
    cube = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            cube[i][j] = "w"
    
    # Iterate through each layer of the cube
    for i in range(k):
        # Check if the current layer is valid
        if not is_valid_layer(cube, i, k):
            return "-1"
    
    # Return the final cube configuration
    return "\n".join("".join(row) for row in cube)

def is_valid_layer(cube, i, k):
    # Check if the current layer has at least two black units
    if cube[i].count("b") < 2:
        return False
    
    # Check if the current layer has at least two white units
    if cube[i].count("w") < 2:
        return False
    
    # Check if the current layer has only black or white units
    if not all(unit in ("b", "w") for unit in cube[i]):
        return False
    
    # Check if the current layer has at least two neighboring units of the same color
    for j in range(k):
        if cube[i][j] == "b" and not has_two_neighbors(cube, i, j, "b"):
            return False
        if cube[i][j] == "w" and not has_two_neighbors(cube, i, j, "w"):
            return False
    
    return True

def has_two_neighbors(cube, i, j, color):
    # Check if the current unit has at least two neighboring units of the same color
    return (i > 0 and cube[i - 1][j] == color) or (i < len(cube) - 1 and cube[i + 1][j] == color) or (j > 0 and cube[i][j - 1] == color) or (j < len(cube[0]) - 1 and cube[i][j + 1] == color)

