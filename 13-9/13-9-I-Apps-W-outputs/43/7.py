
def paint_cube(k):
    # Check if the input is valid
    if k < 1 or k > 100:
        return "-1"
    
    # Initialize the cube with alternating colors
    cube = [[i % 2 for i in range(k)] for _ in range(k)]
    
    # Check if the cube is valid
    for i in range(k):
        for j in range(k):
            if cube[i][j] == 0 and (i > 0 and cube[i-1][j] == 1 or i < k-1 and cube[i+1][j] == 1 or j > 0 and cube[i][j-1] == 1 or j < k-1 and cube[i][j+1] == 1):
                return "-1"
    
    # Return the painted cube
    return "\n".join("".join("w" if cube[i][j] == 0 else "b" for j in range(k)) for i in range(k))

