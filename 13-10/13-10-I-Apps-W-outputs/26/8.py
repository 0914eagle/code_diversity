
def get_penalty(matrix_size, k):
    # Initialize the penalty to 0
    penalty = 0
    
    # Initialize the matrix with empty cells
    matrix = [["." for _ in range(matrix_size[1])] for _ in range(matrix_size[0])]
    
    # Place the candies in the matrix
    for i in range(k):
        # Choose a random row and column for the candy
        row = random.randint(0, matrix_size[0] - 1)
        col = random.randint(0, matrix_size[1] - 1)
        
        # Check if the cell is already occupied
        if matrix[row][col] == ".":
            # Add the penalty for the path
            penalty += 1
            # Place the candy in the cell
            matrix[row][col] = "C"
        else:
            # If the cell is already occupied, return -1
            return -1
    
    # Return the penalty
    return penalty

def get_paths(matrix_size, k):
    # Initialize the matrix with empty cells
    matrix = [["." for _ in range(matrix_size[1])] for _ in range(matrix_size[0])]
    
    # Place the candies in the matrix
    for i in range(k):
        # Choose a random row and column for the candy
        row = random.randint(0, matrix_size[0] - 1)
        col = random.randint(0, matrix_size[1] - 1)
        
        # Check if the cell is already occupied
        if matrix[row][col] == ".":
            # Place the candy in the cell
            matrix[row][col] = "C"
        else:
            # If the cell is already occupied, return an empty list
            return []
    
    # Initialize the paths
    paths = []
    
    # For each candy
    for i in range(k):
        # Get the row and column of the candy
        row = None
        col = None
        for r in range(matrix_size[0]):
            for c in range(matrix_size[1]):
                if matrix[r][c] == "C":
                    row = r
                    col = c
                    break
        
        # Find the path for the candy
        path = []
        for r in range(matrix_size[0]):
            for c in range(matrix_size[1]):
                if matrix[r][c] == ".":
                    path.append((r, c))
        
        # Add the path to the list of paths
        paths.append(path)
    
    # Return the list of paths
    return paths

if __name__ == '__main__':
    matrix_size = [4, 4]
    k = 4
    penalty = get_penalty(matrix_size, k)
    print(penalty)
    paths = get_paths(matrix_size, k)
    for path in paths:
        print(" ".join(str(cell) for cell in path))

