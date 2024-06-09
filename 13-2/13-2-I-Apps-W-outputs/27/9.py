
def f1(n, m):
    # Initialize the matrix with all cells white
    matrix = [['W' for _ in range(m)] for _ in range(n)]
    
    # Flip the color of the first cell to black
    matrix[0][0] = 'B'
    
    # Flip the color of the cells in the first row and column
    for i in range(1, n):
        matrix[i][0] = 'B' if matrix[i - 1][0] == 'W' else 'W'
    for j in range(1, m):
        matrix[0][j] = 'B' if matrix[0][j - 1] == 'W' else 'W'
    
    # Flip the color of the cells in the remaining rows and columns
    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = 'B' if matrix[i - 1][j] == 'W' and matrix[i][j - 1] == 'W' else 'W'
    
    return matrix

