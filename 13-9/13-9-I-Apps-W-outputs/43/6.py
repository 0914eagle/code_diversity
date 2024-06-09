
def solve_cube(k):
    # Check if the input is valid
    if k < 1 or k > 100:
        return -1
    
    # Initialize the cube with all white color
    cube = [[("w" for _ in range(k)) for _ in range(k)] for _ in range(k)]
    
    # Paint the first layer
    for i in range(k):
        for j in range(k):
            if i % 2 == 0:
                cube[i][j] = "b"
            else:
                cube[i][j] = "w"
    
    # Paint the other layers
    for i in range(1, k):
        for j in range(k):
            for k in range(k):
                if cube[i][j][k] == "w":
                    cube[i][j][k] = "b"
                else:
                    cube[i][j][k] = "w"
    
    # Return the cube
    return cube

