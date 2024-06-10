
def get_min_penalty(n, m, k):
    # Initialize a matrix to store the paths
    matrix = [[0] * m for _ in range(n)]
    
    # Initialize a list to store the paths
    paths = []
    
    # Loop through each candy
    for i in range(k):
        # Find the next path for the candy
        path = find_path(matrix, n, m)
        
        # Add the path to the list of paths
        paths.append(path)
        
        # Update the matrix with the path
        update_matrix(matrix, path)
    
    # Calculate the minimum penalty
    penalty = calculate_penalty(paths)
    
    return penalty

def find_path(matrix, n, m):
    # Initialize a list to store the path
    path = []
    
    # Loop through each cell in the matrix
    for i in range(n):
        for j in range(m):
            # If the cell is empty
            if matrix[i][j] == 0:
                # Add the cell to the path
                path.append((i, j))
                
                # Update the matrix
                matrix[i][j] = 1
                
                # Return the path
                return path
    
    # If no path is found, return an empty list
    return []

def update_matrix(matrix, path):
    # Loop through each cell in the path
    for i, j in path:
        # Update the matrix
        matrix[i][j] = 1

def calculate_penalty(paths):
    # Initialize the penalty to 0
    penalty = 0
    
    # Loop through each path
    for path in paths:
        # Calculate the length of the path
        length = len(path)
        
        # Add the length to the penalty
        penalty += length
    
    # Return the penalty
    return penalty

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    print(get_min_penalty(n, m, k))

