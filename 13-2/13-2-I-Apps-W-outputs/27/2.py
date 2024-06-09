
def f1(n, m):
    # Initialize the matrix with all cells set to white
    matrix = [['W' for _ in range(m)] for _ in range(n)]
    
    # Set the first row and column to black
    for i in range(n):
        matrix[i][0] = 'B'
    for j in range(m):
        matrix[0][j] = 'B'
    
    # Set the remaining cells to black or white based on the number of black neighbors
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i-1][j] == 'B' and matrix[i][j-1] == 'B':
                matrix[i][j] = 'B'
            else:
                matrix[i][j] = 'W'
    
    return matrix

